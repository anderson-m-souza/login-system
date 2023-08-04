import hashlib
import secrets


def hash_password(password, salt):
    salted_password = password
    encoded_password = salted_password.encode()
    password_hash = hashlib.sha256(encoded_password)
    hexdigested_hash = password_hash.hexdigest()
    return hexdigested_hash


def generate_salt():
    salt = secrets.token_hex()
    return salt

