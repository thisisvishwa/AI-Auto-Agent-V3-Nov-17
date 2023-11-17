```python
import os
from web3 import Web3
from solc import compile_source

palm_api_key = os.getenv("palm_api_key")

def deployContract(contract_source_code, contract_name):
    # Compile the contract
    compiled_sol = compile_source(contract_source_code)
    contract_interface = compiled_sol['<stdin>:' + contract_name]

    # Connect to Palm network
    w3 = Web3(Web3.HTTPProvider('https://palm-testnet.infura.io/v3/' + palm_api_key))

    # Set the default account to use
    w3.eth.defaultAccount = w3.eth.accounts[0]

    # Create a contract in Ethereum
    Contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

    # Submit the transaction that deploys the contract
    tx_hash = Contract.constructor().transact()

    # Wait for the transaction to be mined, and get the transaction receipt
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    # Create the contract instance with the newly-deployed address
    contract_instance = w3.eth.contract(
        address=tx_receipt['contractAddress'],
        abi=contract_interface['abi'],
    )

    return contract_instance
```