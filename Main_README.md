# Doginals

A minter and protocol for inscriptions on Dogecoin. 

## ⚠️⚠️⚠️ Important ⚠️⚠️⚠️

Use this wallet for inscribing only! Always inscribe from this wallet to a different address, e.g. one you created with DogeLabs or Doggy Market. This wallet is not meant for storing funds or inscriptions.

## Prerequisites

This guide requires a bit of coding knowledge and running Ubuntu on your local machine or a rented one. To use this, you'll need to use your terminal to setup a Dogecoin node, clone this repo and install Node.js on your computer.

### Setup Dogceoin node

Follow the instructions here to setup and sync your Dogecoin node: (https://dogecoin.com/dogepedia/how-tos/operating-a-node/#linux-instructions)

How to check if your node is in sync with the network.
On your `dogecoin` install folder, type the command `dogecoin-cli getinfo`

Compare the "blocks" value to the current block height via a Dogecoin explorer like: https://sochain.com/DOGE



### Install NodeJS

Please head over to (https://github.com/nodesource/distributions#using-ubuntu) and follow the installation instructions.

Check if they are installed by running the following commands:
`node -v` and `npm -v`



### Setup Shibescriptions

#### Clone Doginal minter
On your Terminal, type the following commands:
```
cd
git clone https://github.com/Ser-GY/shibes.git
```
#### Setup minter

```
cd shibes
npm install
``` 

After all dependencies are solved, you can configure the environment:

#### Configure environment

Create a `.env` file with your node information. Set your own username/password.

```
NODE_RPC_URL=http://127.0.0.1:22555
NODE_RPC_USER=ape
NODE_RPC_PASS=zord
TESTNET=false
FEE_PER_KB=69000000
```
You can get the current fee per kb from [here](https://blockchair.com/).

Create a `dogecoin.conf` at `/root/.dogecoin` folder. Set your own username/password.

```
rpcuser=ape
rpcpassword=zord
rpcport=22555
server=1
listen=1
```

### Managing wallet balance

Generate a new `.wallet.json` file:

```
node . wallet new
```

Then send DOGE to the address displayed. Once sent, sync your wallet:

```
node . wallet sync
```

If you are minting a lot, you can split up your UTXOs:

```
node . wallet split <count>
```

When you are done minting, send the funds back:

```
node . wallet send <address> <optional amount>
```


### Minting Doginals

**Note**: Please use a fresh wallet to mint to with nothing else in it until proper wallet for doginals support comes. You can get a paper wallet [here](https://www.fujicoin.org/wallet_generator?currency=Dogecoin).

#### Inscribe a file
From file:

```
node . mint <address> <path>
```

From data:

```
node . mint <address> <content type> <hex data>
```

Examples:

```
node . mint DSV12KPb8m5b6YtfmqY89K6YqvdVwMYDPn dog.jpeg
```

```
node . mint DSV12KPb8m5b6YtfmqY89K6YqvdVwMYDPn "text/plain;charset=utf-8" 576f6f6621 
```



#### Incribing DRC-20

```
node . drc-20 mint <address> <ticker> <amount>
```

Examples: 

```
node . drc-20 mint DSV12KPb8m5b6YtfmqY89K6YqvdVwMYDPn dogi 1000
```


### Viewing Doginals

Start the server:

```
node . server
```

And open your browser to:

```
http://localhost:3000/tx/15f3b73df7e5c072becb1d84191843ba080734805addfccb650929719080f62e
```

### Additional Info

#### Protocol

The doginals protocol allows any size data to be inscribed onto subwoofers.

An inscription is defined as a series of push datas:

```
"ord"
OP_1
"text/plain;charset=utf-8"
OP_0
"Woof!"
```

For doginals, we introduce a couple extensions. First, content may spread across multiple parts:

```
"ord"
OP_2
"text/plain;charset=utf-8"
OP_1
"Woof and "
OP_0
"woof woof!"
```

This content here would be concatenated as "Woof and woof woof!". This allows up to ~1500 bytes of data per transaction.

Second, P2SH is used to encode inscriptions.

There are no restrictions on what P2SH scripts may do as long as the redeem scripts start with inscription push datas.

And third, inscriptions are allowed to chain across transactions:

Transaction 1:

```
"ord"
OP_2
"text/plain;charset=utf-8"
OP_1
"Woof and "
```

Transaction 2

```
OP_0
"woof woof!"
```

With the restriction that each inscription part after the first must start with a number separator, and number separators must count down to 0.

This allows indexers to know how much data remains.


### Troubleshooting

#### I'm getting ECONNREFUSED errors when minting

There's a problem with the node connection. Your `dogecoin.conf` file should look something like:

```
rpcuser=ape
rpcpassword=zord
rpcport=22555
server=1
```

Make sure `port` is not set to the same number as `rpcport`. Also make sure `rpcauth` is not set.

Your `.env file` should look like:

```
NODE_RPC_URL=http://127.0.0.1:22555
NODE_RPC_USER=ape
NODE_RPC_PASS=zord
TESTNET=false
```

#### I'm getting "insufficient priority" errors when minting

The miner fee is too low. You can increase it up by putting FEE_PER_KB=300000000 in your .env file or just wait it out. The default is 100000000 but spikes up when demand is high.

——Changing-Wallets———

Inside of /root/.dogecoin cp wallet.dat /root/saved_wallets/wallet02 cp wallet.dat /root/.dogecoin

Inside of /root/Doginals_pepe cd /root/Doginals_pepe cp .wallet.json /root/saved_wallets/wallet02 cp .wallet.json /root/Doginals_pepe

Inside of /root/saved_wallets

mkdir wallet03 nano wallet03.txt

Enter the address and save

Inside of /root/.dogecoin rm wallet.dat

Inside of /root/Doginals_pepe rm .wallet.json

Make new wallet: Be inside /root/Doginals_pepe cd Doginals_pepe

node . wallet new

———End———

—name— node . mint DFh6dtqDwqtz7xwfp4Js4hycMfP9oYG8HW "text/plain;charset=utf-8" 646269742e646f6765 ——

./dogecoin-cli getreceivedbyaddress DFh6dtqDwqtz7xwfp4Js4hycMfP9oYG8HW

———art mint——— node . mint DFh6dtqDwqtz7xwfp4Js4hycMfP9oYG8HW /root/node_runners/100.png ————end———-

node . drc-20 mint DFh6dtqDwqtz7xwfp4Js4hycMfP9oYG8HW shit 10

———bulk mints——— ./bulk-mint1.sh 20 DFh6dtqDwqtz7xwfp4Js4hycMfP9oYG8HW shit 10

./bulk-mint.sh 25 DFh6dtqDwqtz7xwfp4Js4hycMfP9oYG8HW shit 10 ————end————

cp .wallet.json /root/saved_wallets/wallet01
