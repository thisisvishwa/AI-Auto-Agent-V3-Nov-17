```python
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware

# Connect to Palm testnet
w3 = Web3(Web3.HTTPProvider('https://palm-testnet.infura.io/v3/YOUR-PROJECT-ID'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Load the shared variable for Palm API key
with open('shared_variables.json') as f:
    data = json.load(f)
    palm_api_key = data['palm_api_key']

# Load the user's wallet
with open('wallet.json') as keyfile:
    encrypted_key = keyfile.read()
    private_key = w3.eth.account.decrypt(encrypted_key, 'the password')
    account = w3.eth.account.privateKeyToAccount(private_key)

# Function to handle transactions
def handleTransaction(receiver_address, amount):
    # Estimate the gas price
    gas_price = w3.eth.gas_price

    # Construct a raw transaction
    raw_transaction = {
        'to': receiver_address,
        'value': w3.toWei(amount, 'ether'),
        'gas': 21000,
        'gasPrice': gas_price,
        'nonce': w3.eth.getTransactionCount(account.address),
    }

    # Sign the transaction
    signed_transaction = w3.eth.account.signTransaction(raw_transaction, private_key)

    # Send the transaction
    transaction_hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)

    # Return the transaction hash
    return transaction_hash.hex()
```