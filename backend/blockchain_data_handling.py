```python
import requests
from schemas import TransactionSchema

def handleBlockchainData(transaction_data):
    # Validate the incoming data
    errors = TransactionSchema().validate(transaction_data)
    if errors:
        raise ValueError(f"Invalid transaction data: {errors}")

    # Extract the transaction details
    transaction_id = transaction_data['id']
    sender = transaction_data['sender']
    recipient = transaction_data['recipient']
    amount = transaction_data['amount']

    # Log the transaction details
    print(f"Transaction ID: {transaction_id}")
    print(f"Sender: {sender}")
    print(f"Recipient: {recipient}")
    print(f"Amount: {amount}")

    # Send the transaction data to the Palm API
    response = requests.post(
        "https://api.palm.io/transactions",
        headers={"Authorization": f"Bearer {palm_api_key}"},
        json=transaction_data,
    )

    # Handle the response
    if response.status_code != 200:
        raise Exception(f"Failed to handle transaction: {response.text}")

    # Return the transaction ID
    return transaction_id
```