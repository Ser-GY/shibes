#!/bin/bash

#check that 2 arguments are passed in otherwise exit
if [ "$#" -ne 2 ]; then
    echo "Illegal number of parameters"
    echo "Usage: image-mint.sh <target_address> <file_name>"
    exit 1
fi

target_address=$1
file_name=$2

function goto
{
    label=$1
    cmd=$(sed -n "/^:[[:blank:]][[:blank:]]*${label}/{:a;n;p;ba};" $0 | 
          grep -v ':$')
    eval "$cmd"
    exit
}

#mint started
node . wallet sync
node . mint "$target_address" "$file_name"

retry=${1:-"retry"}
goto "$retry"

#minter goes to sleep to prevent spam, re-runs command if need to retry
: retry
sleep 300 #sleep for 5 minutes
node . wallet sync

#pending file check
filenames=('pending-txs.json')

for filename in ${filenames[@]}; do
    if [ -f $filename ]; then
        goto "$retry"
    else
        echo "$filename does not exist. Mint finished"
    fi
done
