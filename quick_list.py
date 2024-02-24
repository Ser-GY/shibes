import json
import subprocess

tx_hashes = [
    "991b6d88202da4fc0a13c05d3a6a04e6328b495a72659d9d14b0f0f5c7b4c9e5",
    # Add more transaction hashes here
]

with open('doge_output.txt', 'w') as output_file:
    for tx_hash in tx_hashes:
        cmd = f"/root/dogecoin-1.14.6/bin/dogecoin-cli getrawtransaction {tx_hash} true"
        raw_transaction = subprocess.check_output(cmd, shell=True).decode("utf-8").strip()
        
        try:
            transaction_data = json.loads(raw_transaction)
            block_height = transaction_data.get('blk', 'Block Height not found')
            output_file.write(f"Transaction Hash: {tx_hash}, Block Height: {block_height}\n")
        except json.JSONDecodeError:
            output_file.write(f"Transaction Hash: {tx_hash}, Error: Unable to decode transaction data\n")
