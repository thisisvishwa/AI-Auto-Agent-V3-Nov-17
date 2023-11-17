```python
from cryptography.fernet import Fernet

def generate_key():
    """
    Generate a key for encryption and decryption
    """
    return Fernet.generate_key()

def encrypt_data(data, key):
    """
    Encrypt the data with the provided key
    """
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data, key):
    """
    Decrypt the data with the provided key
    """
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

def encryptData(data):
    """
    Function to encrypt data
    """
    key = generate_key()
    encrypted_data = encrypt_data(data, key)
    return encrypted_data, key

def decryptData(encrypted_data, key):
    """
    Function to decrypt data
    """
    decrypted_data = decrypt_data(encrypted_data, key)
    return decrypted_data
```