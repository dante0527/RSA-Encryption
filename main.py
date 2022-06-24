from alphabet import *

# Prime numbers
p = 3
q = 11

# Public keys
N = p * q
e = 3

# Private keys
d = 7


def encrypt(char):
    return str((int(char) ** e) % N).zfill(2)


def decrypt(char):
    return str((int(char) ** d) % N).zfill(2)


def split(word):
    return [char for char in word]


def encrypt_message():
    # Messages
    plaintext = []
    encrypted = []

    # Read plaintext message
    with open("input.txt", "r") as fin:
        message = fin.read()
        plaintext = message.lower().split()

    # Encrypt message
    for word in plaintext:
        # Split word into characters
        chars = split(word)

        # Create list of encrypted characters
        encrypted_chars = [encrypt(alphabet_e[char]) for char in chars]

        # Add encrypted word to list
        encrypted_word = " ".join(encrypted_chars)
        encrypted.append(encrypted_word)

    # Join encrypted words with space characters
    encrypted = " 32 ".join(encrypted)

    # Write encrypted message
    with open("encrypted.txt", "w") as fout:
        fout.write(encrypted)
    
    return encrypted


def decrypt_message():
    # Messages
    encrypted = []
    decrypted = []
    plaintext = []

    # Read encrypted message
    with open("input.txt", "r") as fin:
        message = fin.read()
        encrypted = message.split()

    # Decrypt message
    for char in encrypted:
        decrypted.append(decrypt(char))

    # Decipher message
    for char in decrypted:
        plaintext.append(alphabet_d[char])

    plaintext = "".join(plaintext)

    # Write encrypted message
    with open("decrypted.txt", "w") as fout:
        fout.write(plaintext)

    return plaintext

encrypt_message()
#decrypt_message()