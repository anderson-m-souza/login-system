import pyargon2
import secrets


def hash_password(password, salt):
    hex_encoded_hash = pyargon2.hash(password,
                                     salt,
                                     time_cost=2,
                                     memory_cost=19456,
                                     parallelism=1,
                                     variant='id')
    return hex_encoded_hash


def generate_salt():
    salt = secrets.token_hex()
    return salt

