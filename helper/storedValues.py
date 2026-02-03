import json
from getpass import getpass
from pathlib import Path

SECRETS_FILE = Path("secrets.json") 

default_secrets = {
    "open_ai_key": "",
    "gmail_email": "",
    "gmail_app_password": "",
    "postgres_connection_string": ""
}

if not SECRETS_FILE.exists():
    with SECRETS_FILE.open("w") as f:
        json.dump(default_secrets, f, indent=4)
    print(f"{SECRETS_FILE} did not exist. Created file with empty values.")

def prompt_value(name: str) -> str:
    """Prompt the user for a value, input hidden for security."""
    prompt = f"Enter {name}: "
    return getpass(prompt)

def get_secret(name: str) -> str:
    """Retrieve a single secret by name from the secrets file."""
    with SECRETS_FILE.open("r") as f:
        secrets = json.load(f)
    
    if name not in secrets:
        raise KeyError(f"Secret '{name}' not found in {SECRETS_FILE}.")
    
    return secrets[name]
