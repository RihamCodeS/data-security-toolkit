import random
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fact_check(statement: str) -> bool:
    """
    Simulates a fact-checking mechanism.
    Args:
        statement (str): The statement to verify.
    Returns:
        bool: Randomly returns True (verified) or False (unverified).
    """
    logging.info(f"Fact-checking statement: '{statement}'")
    result = random.choice([True, False])
    logging.info(f"Fact-check result: {'Verified' if result else 'Unverified'}")
    return result

if __name__ == "__main__":
    fact_check("The Earth orbits the Sun.")
