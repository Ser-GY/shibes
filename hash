#!/usr/bin/env python3
import subprocess
import json

# List of transaction hashes
transaction_hashes = [
    "991b6d88202da4fc0a13c05d3a6a04e6328b495a72659d9d14b0f0f5c7b4c9e5"
]

dogecoin_cli = "/root/dogecoin-1.14.6/bin/dogecoin-cli"

# Function to get block hash for a transaction hash
def get_block_hash(tx_hash):
    cmd = [dogecoin_cli, 'gettransaction', tx_hash]
    result = http://subprocess.run(cmd, capture_output=True, text=True)
    if result.stdout:
        tx_info = json.loads(result.stdout)
        # Assuming you're looking for the block hash where the transaction was included
        block_hash = tx_info.get('blockhash', None)
        return block_hash
    else:
        return None

# Print block hashes to doge_output.txt
with open("doge_output.txt", "a") as file:
    for tx_hash in transaction_hashes:
        block_hash = get_block_hash(tx_hash)
        if block_hash:
            file.write(f"Transaction Hash: {tx_hash}, Block Hash: {block_hash}\n")
        else:
            file.write(f"Transaction Hash: {tx_hash}, Block Hash not found\n")

print("Script executed successfully.")
