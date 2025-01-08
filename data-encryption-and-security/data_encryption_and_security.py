import os
import json
import hashlib
import logging
from cryptography.fernet import Fernet

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_encryption_key():
    """
    Generates an encryption key and saves it to a file.
    Run this function only once, and store the key securely.
    """
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)
    logging.info("Encryption key generated and saved to 'encryption_key.key'.")

def load_encryption_key():
    """
    Loads the encryption key from the file.
    Returns:
        Fernet: An instance of the Fernet encryption handler.
    """
    try:
        with open("encryption_key.key", "rb") as key_file:
            return Fernet(key_file.read())
    except FileNotFoundError:
        logging.error("Encryption key file not found. Generate the key first.")
        return None

def encrypt_data(data: bytes, fernet: Fernet) -> bytes:
    """Encrypts data using the provided Fernet instance."""
    return fernet.encrypt(data)

def decrypt_data(data: bytes, fernet: Fernet) -> bytes:
    """Decrypts data using the provided Fernet instance."""
    return fernet.decrypt(data)

def validate_data(data: dict, schema: dict) -> bool:
    """
    Validates a dataset against a defined schema.
    Args:
        data (dict): The data to validate.
        schema (dict): A dictionary defining expected keys and their types.
    Returns:
        bool: True if the data matches the schema, False otherwise.
    """
    try:
        for key, value_type in schema.items():
            if key not in data or not isinstance(data[key], value_type):
                raise ValueError(f"Invalid or missing key: '{key}', expected type: {value_type}")
        logging.info("Data validation successful.")
        return True
    except Exception as e:
        logging.error(f"Data validation failed: {e}")
        return False

def dataset_security_demo():
    """
    Demonstrates encryption, decryption, and validation of a dataset.
    """
    if not os.path.exists("encryption_key.key"):
        generate_encryption_key()

    fernet = load_encryption_key()
    if not fernet:
        return

    # Sample data and schema
    sample_data = {"name": "John Doe", "age": 30, "email": "john@example.com"}
    schema = {"name": str, "age": int, "email": str}

    if validate_data(sample_data, schema):
        encrypted = encrypt_data(json.dumps(sample_data).encode(), fernet)
        logging.info(f"Encrypted Data: {encrypted}")

        decrypted = decrypt_data(encrypted, fernet)
        logging.info(f"Decrypted Data: {decrypted.decode()}")

if __name__ == "__main__":
    dataset_security_demo()
