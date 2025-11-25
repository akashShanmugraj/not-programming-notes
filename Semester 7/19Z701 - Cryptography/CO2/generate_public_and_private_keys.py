import hashlib
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

def derive_seed_from_passphrase(passphrase: str, salt: bytes) -> bytes:
    """
    Derive a 32-byte seed using PBKDF2-HMAC-SHA256.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,            # Ed25519 seed size
        salt=salt,
        iterations=200_000,
    )
    return kdf.derive(passphrase.encode("utf-8"))

def main():
    passphrase = input("Enter your secret passphrase: ")

    # Deterministic salt for demo (not secure)
    salt = b"fixed-salt-for-demo-only"

    seed = derive_seed_from_passphrase(passphrase, salt)

    private_key = Ed25519PrivateKey.from_private_bytes(seed)
    public_key = private_key.public_key()

    # Correct serialization
    private_hex = private_key.private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption()
    ).hex()

    public_hex = public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    ).hex()

    print("\n=== Generated Keys ===")
    print("Private Key (hex):", private_hex)
    print("Public Key  (hex):", public_hex)

if __name__ == "__main__":
    main()
