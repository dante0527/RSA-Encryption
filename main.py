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

# Decryption alphabet
alphabet_d = {n: c for c, n in alphabet_e.items()}

# Euclidian Algorithm: Find GCD of two numbers
def gcd(a, b):
    if (b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)


# Generate encryption keys, e, and d
def prepare_rsa(p, q):

    # Part of public key
    N = p * q

    # Part of private key
    N0 = (p-1) * (q-1)

    # Part of public key
    # Find e: first integer relatively prime to N0
    for i in range(2, N0):
        if gcd(i, N0) == 1:
            e = i
            break
    
    # Part of private key
    # Find d: multiplicative inverse of e % N0
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


# Encrypt message from input file
def encrypt_message(message):

    # Messages
    plaintext = message.lower().split()
    encrypted = []

    # Exncrypt message
    for word in plaintext:

        # Split word into characters
        chars = split(word)

        # Create list of encrypted characters
        encrypted_chars = [encrypt(alphabet_e[char]) for char in chars]

        # Add encrypted word to list
        encrypted_word = " ".join(encrypted_chars)
        encrypted.append(encrypted_word)

    # Join encrypted words with space characters
    encrypted  = f" {encrypt(alphabet_e[' '])} ".join(encrypted)

    return encrypted


# Decrypt message from numbers to letters
def decrypt_message(message):

    # Messages
    encrypted = message.split()
    decrypted = []
    plaintext = []

    # Decrypt
    for char in encrypted:
        decrypted.append(decrypt(char))

    # Decipher message
    for char in decrypted:
        plaintext.append(alphabet_d[char])
    
    plaintext = "".join(plaintext)

    return plaintext

# Option Menu
def options():
    print("Options:\n\
        1 - Encrypt message from file\n\
        2 - Decrypt message from file\n\
        3 - Encrypt message in terminal\n\
        4 - Decrypt message in terminal\n")

# Get prime numbers
p = int(input("Enter the first prime number: "))
q = int(input("Enter the second prime number: "))

print()

# Generate values for encryption / decryption
N, e, d = prepare_rsa(p, q)

# User interface
while True:

    # Show options
    options()

    # Get selection from user
    selection = input()

    # Encrypt message from file
    if selection == "1":

        # Read plaintext input
        with open("input.txt", "r") as fin:
            message = fin.read()

        # Write encrypted message
        with open("encrypted.txt", "w") as fout:
            fout.write(encrypt_message(message))
        
        # Success message
        print("File encrypted!\n")

    # Decrypt message from file
    elif selection == "2":

        # Read plaintext input
        with open("input.txt", "r") as fin:
            message = fin.read()

        # Write encrypted message
        with open("decrypted.txt", "w") as fout:
            fout.write(decrypt_message(message))
        
        # Success message
        print("File decrypted!\n")

    # Encrypt message in terminal
    elif selection == "3":
        
        # Get message from user
        message = input("Enter message to encrypt:\n")

        # Print encrypted message
        print(f"\nEncrypted message:\n{encrypt_message(message)}\n")

    # Decrypt message in terminal
    elif selection == "4":

        # Get encrypted message from user
        message = input("Enter message to decrypt:\n")

        # Print decrypted message
        print(f"\nDecrypted message:\n{decrypt_message(message)}\n")

    # Input validation
    else:
        print("Invalid choice\n")

    # Option to exit
    exit = input("Make another selection?\n\
        'Y' to continue\n\
        any other key to exit\n").upper()

    print()

    # Make another selection
    if exit == "Y":
        continue
    
    # Exit
    else:
        break
