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
    return account

def deployContract(contract_abi, contract_bytecode):
    # Get the account from wallet setup
    account = setupWallet()

    # Estimate the gas required to deploy the contract
    gas_estimate = w3.eth.estimateGas({
        "from": account.address,
        "data": contract_bytecode
    })

    # Build a transaction to deploy the contract
    transaction = {
        "from": account.address,
        "data": contract_bytecode,
        "gas": gas_estimate
    }

    # Sign the transaction
    signed_txn = w3.eth.account.signTransaction(transaction, account.privateKey)

    # Send the transaction
    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    # Wait for the transaction to be mined, and get the transaction receipt
    txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)

    # Create a contract instance with the newly deployed contract address
    contract = w3.eth.contract(
        address=txn_receipt['contractAddress'],
        abi=contract_abi
    )

    return contract

def handleTransaction(contract, function_name, *args):
    # Get the account from wallet setup
    account = setupWallet()

    # Estimate the gas required to execute the function
    gas_estimate = contract.functions[function_name](*args).estimateGas()

    # Build a transaction to execute the function
    transaction = contract.functions[function_name](*args).buildTransaction({
        "from": account.address,
        "gas": gas_estimate
    })

    # Sign the transaction
    signed_txn = w3.eth.account.signTransaction(transaction, account.privateKey)

    # Send the transaction
    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    # Wait for the transaction to be mined, and get the transaction receipt
    txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)

    return txn_receipt
```