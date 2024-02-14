#!/bin/bash

# File containing NFT metadata, one per line
NFT_DATA_FILE="nft_data.txt"

# Dogecoin recipient address and the amount to send with each NFT transaction
recipientAddress="RecipientDogecoinAddress"
amountToSend=0.01 # Adjust as needed
fee=0.001 # Adjust based on current network conditions

# Check if dogecoin-cli and jq are available
if ! command -v dogecoin-cli &> /dev/null; then
    echo "dogecoin-cli could not be found. Please ensure Dogecoin Core is installed."
    exit 1
fi

if ! command -v jq &> /dev/null; then
    echo "jq could not be found, please install jq to parse JSON responses."
    exit 1
fi

# Function to send transaction with OP_RETURN containing NFT metadata
send_transaction() {
    local nftData="$1"
    local hexData=$(echo -n "$nftData" | xxd -p -c 200 | tr -d '\n')
    
    # Create the raw transaction with OP_RETURN and recipient output
    local rawTx=$(dogecoin-cli createrawtransaction "[]" "[{\"data\":\"$hexData\"}, {\"$recipientAddress\":$amountToSend}]")
    
    # Check for failure in raw transaction creation
    if [[ "$rawTx" == "" ]]; then
        echo "Failed to create raw transaction for NFT data: $nftData"
        return
    fi

    # Sign the raw transaction
    local signedTx=$(dogecoin-cli signrawtransactionwithwallet "$rawTx")
    local hexSignedTx=$(echo $signedTx | jq -r '.hex')
    
    # Check for failure in signing the transaction
    if [[ "$hexSignedTx" == "" || "$hexSignedTx" == "null" ]]; then
        echo "Failed to sign transaction for NFT data: $nftData"
        return
    fi

    # Broadcast the signed transaction
    local finalTx=$(dogecoin-cli sendrawtransaction "$hexSignedTx")
    
    # Check for failure in broadcasting the transaction
    if [[ "$finalTx" == "" ]]; then
        echo "Failed to send transaction for NFT data: $nftData"
        return
    fi

    echo "Transaction ID: $finalTx"
}

# Process each line in the NFT data file
while IFS= read -r line; do
    send_transaction "$line"
done < "$NFT_DATA_FILE"

echo "All NFT data from $NFT_DATA_FILE has been processed."
