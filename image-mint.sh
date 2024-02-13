#!/bin/bash

#check that 2 arguments are passed in otherwise exit
if [ "$#" -ne 2 ]; then
    echo "Illegal number of parameters"
    echo "Usage: image-mint.sh <target_address> <file_name>"
    exit 1
fi

target_address=$1
file_name=$2

#mint started
node . mint "$target_address" "$file_name"

#minter goes to sleep to prevent spam, re-runs command if need to retry
: sleep
sleep 360 #sleep for 6 minutes
node . wallet sync

#pending file check
filenames=('pending-txs.json')

for filename in ${filenames[@]}; do
    if [ -f $filename ]; then
        goto "sleep"
    else
        echo "$filename does not exist. Mint finished"
    fi
done