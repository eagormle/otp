import random
import string


def generate_key(plaintext):
    """Generate a random key based on the length of the plaintext."""
    return ''.join(random.choices(string.ascii_uppercase, k=len(plaintext)))


def encrypt(plaintext, key):
    """Encrypt the plaintext using the provided key."""
    return ''.join(chr((ord(char) + ord(key[i % len(key)])) % 26 + 65) for i, char in enumerate(plaintext))


def decrypt(ciphertext, key):
    """Decrypt the ciphertext using the provided key."""
    return ''.join(chr((ord(char) - ord(key[i % len(key)])) % 26 + 65) for i, char in enumerate(ciphertext))


def main():
    plaintext = input("Enter plaintext: ").upper()
    key = generate_key(plaintext)
    ciphertext = encrypt(plaintext, key)

    print(f"Plaintext: {plaintext}")
    print(f"Key: {key}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted Text: {decrypt(ciphertext, key)}")


if __name__ == "__main__":
    main()
