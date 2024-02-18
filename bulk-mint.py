import sys
import subprocess
import time

def run_command(command):
    # Execute a shell command and capture its output
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # Print the output from the command
    print("Output from command:")
    print(result.stdout)

    # If there is an error, print the error message
    if result.stderr:
        print("Error in command:")
        print(result.stderr)

    return result

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 6:
        print("Usage: python script.py <address> <ticker> <amount> <interval_seconds> <num_loops>")
        sys.exit(1)

    # Extract command-line arguments
    address = sys.argv[1]
    ticker = sys.argv[2]
    amount = sys.argv[3]
    interval_seconds = int(sys.argv[4])
    num_loops = int(sys.argv[5])

    # Loop for the specified number of times
    for _ in range(num_loops):
        # Construct the command to mint tokens
        mint_command = f"node . drc-20 mint {address} {ticker} {amount}"

        # Run the minting command
        result_mint = run_command(mint_command)

        # Wait for the specified interval before the next iteration
        time.sleep(interval_seconds)

if __name__ == "__main__":
    main()
