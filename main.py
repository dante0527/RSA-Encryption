# Encryption alphabet
alphabet_e = {'a': '01',
            'b': '02',
            'c': '03',
            'd': '04',
            'e': '05',
            'f': '06',
            'g': '07',
            'h': '08',
            'i': '09',
            'j': '10',
            'k': '11',
            'l': '12',
            'm': '13',
            'n': '14',
            'o': '15',
            'p': '16',
            'q': '17',
            'r': '18',
            's': '19',
            't': '20',
            'u': '21',
            'v': '22',
            'w': '23',
            'x': '24',
            'y': '25',
            'z': '26',
            ' ': '32'}

# Decryption Alphabet
alphabet_d = {n: c for c, n in alphabet_e.items()}

# Euclidian Algorithm: Find GCD of two numbers
def gcd(a, b):
    if (b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)


# Generate public encryption keys, e, and d
def prepare_rsa(p, q):

    # Public keys
    N = p * q
    N0 = (p-1)*(q-1)

    # Find e: first integer relatively prime to N0
    for i in range(2, N0):
        if gcd(i, N0) == 1:
            e = i
            break
        else:
            continue

    # Find d: inverse of e % N0
    for i in range(0, N0):
        if ((e * i) % N0) == 1:
            d = i
            break
    
    return N, e, d


# Encrypt character
def encrypt(char):
    return str((int(char) ** e) % N).zfill(2)


# Decrypt character
def decrypt(char):
    return str((int(char) ** d) % N).zfill(2)


# Split word into characters
def split(word):
    return [char for char in word]


# Encrypt message from letters to numbers
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

    # Write encrypted message to file
    with open("encrypted.txt", "w") as fout:
        fout.write(encrypted)
    
    return encrypted


# Decrypt message from numbers to letters
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


# Select prime numbers
N, e, d = prepare_rsa(3, 11)

# Encrypt or decrypt message
#encrypt_message()
#decrypt_message()
