#!/bin/bash

#check that 4 arguments are passed in otherwise exit
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
while [ $count -lt $max_count ]; do
    echo "Current count: $count"
    node . drc-20 mint "$target_address" "$token_name" "$mint_limit"
    remaining=$((max_count - count))
    echo "Counts left: $remaining"
    sleep 300  # Sleep for 3,5 minutes
    ((count++))
done
