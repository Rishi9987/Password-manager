from cryptography.fernet import Fernet
import json
import os

KEY_FILE = "key.key"
DATA_FILE = "data.json"

# -----------------------------
# KEY GENERATION & LOADING
# -----------------------------

def write_key():
    """Generate a new encryption key and save it to a file."""
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

def load_key():
    """Load the encryption key from the file."""
    if not os.path.exists(KEY_FILE):
        write_key()
    return open(KEY_FILE, "rb").read()

# -----------------------------
# ENCRYPTION & DECRYPTION
# -----------------------------
def encrypt_password(password):
    """Encrypt a password using Fernet symmetric encryption."""
    key = load_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(password.encode())
    return encrypted.decode()

def decrypt_password(encrypted_password):
    """Decrypt a password previously encrypted."""
    key = load_key()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_password.encode())
    return decrypted.decode()

# -----------------------------
# FILE HANDLING FUNCTIONS
# -----------------------------

def save_password(service, username, password):
    """Save encrypted password to JSON file."""
    encrypted = encrypt_password(password)
    data = {}
    
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {}

    data[service] = {
        "username": username,
        "password": encrypted
    }

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def get_password(service):
    """Retrieve and decrypt password for a given service."""
    if not os.path.exists(DATA_FILE):
        return None, None

    with open(DATA_FILE, "r") as file:
        data = json.load(file)

    if service in data:
        username = data[service]["username"]
        password = decrypt_password(data[service]["password"])
        return username, password
    else:
        return None, None
