```python
import os
from web3 import Web3
from eth_account import Account

# Get the Palm API key from environment variables
palm_api_key = os.getenv("palm_api_key")

# Connect to the Palm network
w3 = Web3(Web3.HTTPProvider("https://rpc.palm.io"))

def setupWallet():
    # Generate a new account
    account = Account.create()

    # Store the private key in a secure manner
    private_key = account.privateKey
    with open("private_key.txt", "w") as file:
        file.write(private_key)

    # Get the public address of the account
    public_address = account.address

    # Return the public address for further use
    return public_address
```