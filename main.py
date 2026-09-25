from modules.hash import hash_file, verify_integrity 
from modules.encryption import aes_ed, rsa_ed
from modules.password import check_strength, hash_password, verify_password
from getpass import getpass

def menu():
    print("\nSelect operation: ")
    print("1. Hash file")
    print("2. Check file integrity")
    print("3. AES encrypt/decrypt")
    print("4. RSA encrypt/decrypt")
    print("5. Password manager")
    print("0. Exit")

run = True

print(
"""
Initiating Cryptography Toolkit v1.0...

\nWelcome, Agent! Your mission, should you choose to accept it:
- Analyze and hash files to detect tampering
- Encrypt and decrypt messages with AES and RSA
- Securely manage passwords and assess their strength

All systems online. Data protection protocols active.
Prepare to enter the world of digital secrecy!"""
)

while run:
    menu()
    choice = input("Enter choice (0-5): ")

    if choice == "0":
        run = False
        break
    
    elif choice == "1":
        file_path = input("Enter file path: ")
        print("\nSHA Hash of file is: ", hash_file(file_path))

    elif choice == "2":
        file_path1 = input("Enter path of file 1: ")
        file_path2 = input("Enter path of file 2: ")
        print(verify_integrity(file_path1, file_path2))

    elif choice == "3":
        message = input("Enter message to encrypt: ").encode()
        key, ciphertext, plaintext = aes_ed(message)
        print("AES Key: ", key)
        print("AES Ciphertext: ", ciphertext)
        print("AES Plaintext: ", plaintext)

    elif choice == "4":
        message = input("Enter message to encrypt: ").encode()
        ciphertext, plaintext = rsa_ed(message)
        print("\nRSA message, encrypted with a public key: ", ciphertext)
        print("RSA message, decrypted with a private key: ", plaintext)

    elif choice == "5":
        while True:
            password1 = getpass("Enter a password to check strength: ")
            print(check_strength(password1))
            if check_strength(password1).startswith("Weak"):
                print("Please choose a stronger password.")
            else:
                break

        hashed_password = hash_password(password1)
        print("Hashed password:", hashed_password)

        attempt = getpass("Re-enter the password to verify: ")
        print(verify_password(attempt, hashed_password))

    else:
        print("Invalid choice.")

    input("\nPress Enter to restart...")

print("Agent, you are exiting your cryptography toolkit. Stay sharp and secure out there!")