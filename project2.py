from datetime import datetime

# ==========================================
# PROJECT 2 : BASIC ENCRYPTION & DECRYPTION
# DecodeLabs Cyber Security Internship
# ==========================================

print("=" * 60)
print("      BASIC ENCRYPTION & DECRYPTION SYSTEM")
print("=" * 60)

# ==========================================
# SECURITY INFORMATION
# ==========================================

print("\n[INFO] This project demonstrates:")
print("1. Data Confidentiality")
print("2. Caesar Cipher Encryption")
print("3. Caesar Cipher Decryption")
print("4. ASCII Character Manipulation")
print("5. Modulo Arithmetic")
print("6. Data Protection Concepts")


# ==========================================
# ENCRYPTION FUNCTION
# ==========================================

def encrypt(text, shift):

    encrypted_text = ""

    for char in text:

        # Uppercase Letters
        if char.isupper():

            ascii_value = ord(char)

            shifted = ((ascii_value - 65 + shift) % 26) + 65

            encrypted_text += chr(shifted)

        # Lowercase Letters
        elif char.islower():

            ascii_value = ord(char)

            shifted = ((ascii_value - 97 + shift) % 26) + 97

            encrypted_text += chr(shifted)

        # Numbers, Spaces, Symbols
        else:
            encrypted_text += char

    return encrypted_text


# ==========================================
# DECRYPTION FUNCTION
# ==========================================

def decrypt(text, shift):

    decrypted_text = ""

    for char in text:

        if char.isupper():

            ascii_value = ord(char)

            shifted = ((ascii_value - 65 - shift) % 26) + 65

            decrypted_text += chr(shifted)

        elif char.islower():

            ascii_value = ord(char)

            shifted = ((ascii_value - 97 - shift) % 26) + 97

            decrypted_text += chr(shifted)

        else:
            decrypted_text += char

    return decrypted_text


# ==========================================
# SECURITY STRENGTH CHECKER
# ==========================================

def security_strength(shift):

    if shift <= 3:
        return "LOW"

    elif shift <= 10:
        return "MEDIUM"

    else:
        return "HIGH"


# ==========================================
# LOGGING FUNCTION
# ==========================================

def save_log(operation, original, result, shift):

    with open("cipher_log.txt", "a") as file:

        file.write("\n")
        file.write("=" * 50 + "\n")
        file.write(f"Date & Time : {datetime.now()}\n")
        file.write(f"Operation   : {operation}\n")
        file.write(f"Shift Key   : {shift}\n")
        file.write(f"Input       : {original}\n")
        file.write(f"Output      : {result}\n")


# ==========================================
# BRUTE FORCE ATTACK DEMO
# ==========================================

def brute_force(cipher_text):

    print("\nPossible Keys:")

    for key in range(1, 26):

        possible = decrypt(cipher_text, key)

        print(f"Key {key:2} --> {possible}")


# ==========================================
# ASCII DEMONSTRATION
# ==========================================

def ascii_demo():

    print("\nASCII Demonstration")

    sample = "A"

    print("Character :", sample)
    print("ASCII Code:", ord(sample))
    print("Back To Character:", chr(ord(sample)))


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n")
    print("=" * 60)
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. ASCII Demonstration")
    print("4. Brute Force Attack Demo")
    print("5. Security Analysis")
    print("6. Exit")
    print("=" * 60)

    choice = input("Enter Your Choice: ")

    # ======================================
    # OPTION 1 : ENCRYPTION
    # ======================================

    if choice == "1":

        print("\nINPUT PHASE")

        plaintext = input("Enter Plain Text: ")

        try:
            shift = int(input("Enter Shift Key (1-25): "))

            if shift < 1 or shift > 25:
                print("Shift Key Must Be Between 1 And 25")
                continue

        except ValueError:
            print("Invalid Shift Key")
            continue

        print("\nPROCESS PHASE")

        ciphertext = encrypt(plaintext, shift)

        print("\nOUTPUT PHASE")

        print("Original Text  :", plaintext)
        print("Encrypted Text :", ciphertext)

        print("Security Level :", security_strength(shift))

        save_log("Encryption",
                 plaintext,
                 ciphertext,
                 shift)

    # ======================================
    # OPTION 2 : DECRYPTION
    # ======================================

    elif choice == "2":

        cipher = input("Enter Cipher Text: ")

        try:
            shift = int(input("Enter Shift Key: "))
        except ValueError:
            print("Invalid Shift Key")
            continue

        plain = decrypt(cipher, shift)

        print("\nDecrypted Text :", plain)

        save_log("Decryption",
                 cipher,
                 plain,
                 shift)

    # ======================================
    # OPTION 3 : ASCII
    # ======================================

    elif choice == "3":

        ascii_demo()

    # ======================================
    # OPTION 4 : BRUTE FORCE
    # ======================================

    elif choice == "4":

        cipher = input("Enter Cipher Text: ")

        brute_force(cipher)

    # ======================================
    # OPTION 5 : SECURITY ANALYSIS
    # ======================================

    elif choice == "5":

        print("\nSECURITY ANALYSIS")

        print("\nAdvantages:")
        print("- Easy To Implement")
        print("- Demonstrates Encryption Concepts")
        print("- Protects Data From Casual Viewing")

        print("\nLimitations:")
        print("- Only 25 Possible Keys")
        print("- Vulnerable To Brute Force Attacks")
        print("- Vulnerable To Frequency Analysis")

        print("\nModern Alternatives:")
        print("- AES")
        print("- RSA")
        print("- ECC")

    # ======================================
    # OPTION 6 : EXIT
    # ======================================

    elif choice == "6":

        print("\nThank You")
        print("Project Completed Successfully")
        break

    else:
        print("Invalid Choice")