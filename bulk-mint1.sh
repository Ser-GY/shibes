if [ "$#" -ne 4 ]; then
echo "Illegal number of parameters"
    echo "Usage: bulk-mint.sh <max_count> <target_address> <token_name> <mint_limit>"
    exit 1
fi

count=0
max_count=$1
target_address=$2
token_name=$3
mint_limit=$4

# Initialize an array to store minting details
minting_operations=()

while [ $count -lt $max_count ]; do
    echo "Current count: $count"
    
    # Add minting details to the array
    minting_operations+=("node . drc-20 mint \"$target_address\" \"$token_name\" \"$mint_limit\"")

    ((count++))
done

# Execute all minting operations in a single transaction
for operation in "${minting_operations[@]}"; do
    eval "$operation"
done

