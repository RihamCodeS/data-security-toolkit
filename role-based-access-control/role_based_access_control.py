import logging
from functools import wraps

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

users = {
    "admin": {"roles": ["read", "write", "delete"]},
    "user": {"roles": ["read"]},
}

def check_permission(role_required: str):
    """
    Decorator to check if a user has the required role to access a function.
    Args:
        role_required (str): The role required to execute the function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(user: str, *args, **kwargs):
            if role_required in users.get(user, {}).get("roles", []):
                logging.info(f"Access granted to {user} for role: {role_required}")
                return func(user, *args, **kwargs)
            else:
                logging.error(f"Access denied for {user}. Missing role: {role_required}")
                return None
        return wrapper
    return decorator

@check_permission("read")
def read_data(user: str):
    logging.info(f"{user} is reading data.")

@check_permission("write")
def write_data(user: str):
    logging.info(f"{user} is writing data.")

if __name__ == "__main__":
    read_data("admin")  # Access granted
    write_data("user")  # Access denied
