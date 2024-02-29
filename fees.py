import os
from dotenv import load_dotenv
import requests
import json

# Load environment variables from the .env file
load_dotenv()

NODE_RPC_URL = os.getenv("NODE_RPC_URL")
NODE_RPC_USER = os.getenv("NODE_RPC_USER")
NODE_RPC_PASS = os.getenv("NODE_RPC_PASS")

# Configure the HTTP request header
headers = {
    'content-type': 'application/json',
}

# Prepare the request payload to get the fee estimate
payload = json.dumps({
    "jsonrpc": "1.0",
    "id": "curltest",
    "method": "estimatesmartfee",
    "params": [1]  # Assuming information for the next block is desired
})

# Make the RPC request
response = requests.post(NODE_RPC_URL, auth=(NODE_RPC_USER, NODE_RPC_PASS), headers=headers, data=payload)

# Check if the request was successful and print the fee estimate
if response.status_code == 200:
    result = response.json()
    doge_fee_rate = result['result']['feerate'] if 'feerate' in result['result'] else 'Not available'
    
    # Convert DOGE to Satoshis
    satoshi_fee_rate = float(doge_fee_rate) * 10**8
    
    print(f"Estimated fee for the next block: {doge_fee_rate} DOGE per KB")
    print(f"Equivalent in Satoshis per KB: {satoshi_fee_rate} sats per KB")
else:
    print("Error calling estimatesmartfee:", response.text)
