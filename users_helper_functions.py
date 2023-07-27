from hashlib import sha256


def sha256_hash(password):
    encoded_password = password.encode()
    password_hash = sha256(encoded_password)
    hexdigested_hash = password_hash.hexdigest()
    return hexdigested_hash

