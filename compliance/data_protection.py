```python
import os
from cryptography.fernet import Fernet

# Load the secret key
secret_key = os.getenv('SECRET_KEY')
cipher_suite = Fernet(secret_key)

def encryptData(data):
    """
    Function to encrypt user data
    """
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

def decryptData(encrypted_data):
    """
    Function to decrypt user data
    """
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data

def protectUserData(user_data):
    """
    Function to protect user data by encrypting it
    """
    encrypted_user_data = {key: encryptData(value) for key, value in user_data.items()}
    return encrypted_user_data

def retrieveUserData(encrypted_user_data):
    """
    Function to retrieve user data by decrypting it
    """
    user_data = {key: decryptData(value) for key, value in encrypted_user_data.items()}
    return user_data
```