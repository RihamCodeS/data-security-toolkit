import hashlib
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_hash(data: bytes) -> str:
    """
    Calculates the SHA-256 hash of the given data.
    Args:
        data (bytes): The data to hash.
    Returns:
        str: The hexadecimal representation of the hash.
    """
    return hashlib.sha256(data).hexdigest()

def verify_hash(data: bytes, original_hash: str) -> bool:
    """
    Verifies that the hash of the given data matches the original hash.
    Args:
        data (bytes): The data to verify.
        original_hash (str): The original hash to compare against.
    Returns:
        bool: True if the hashes match, False otherwise.
    """
    return calculate_hash(data) == original_hash

def integrity_demo():
    """
    Demonstrates data integrity verification using hashes.
    """
    data = b"Sample data for hashing."
    original_hash = calculate_hash(data)
    logging.info(f"Original Hash: {original_hash}")

    if verify_hash(data, original_hash):
        logging.info("Hash verification successful.")
    else:
        logging.error("Hash verification failed.")

if __name__ == "__main__":
    integrity_demo()
