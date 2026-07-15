import string
from getpass import getpass

print("=" * 60)
print("      ADVANCED PASSWORD STRENGTH CHECKER")
print("=" * 60)

# Password input (hidden)
password = getpass("Enter Password: ")
confirm_password = getpass("Confirm Password: ")

if password != confirm_password:
    print("\nERROR: Passwords do not match!")
    exit()

if len(password) == 0:
    print("\nERROR: Password cannot be empty!")
    exit()

# Common weak passwords
common_passwords = {
    "password", "123456", "12345678",
    "qwerty", "admin", "welcome",
    "password123", "letmein"
}

# Character checks
length = len(password)

has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_symbol = any(c in string.punctuation for c in password)

# Repeated character detection
unique_chars = len(set(password))
repeated_chars = unique_chars < (length / 2)

# Sequential pattern detection
sequences = [
    "123456", "234567", "345678",
    "abcdef", "bcdefg",
    "qwerty", "asdfgh", "zxcvbn"
]

password_lower = password.lower()

sequential_pattern = False

for seq in sequences:
    if seq in password_lower:
        sequential_pattern = True
        break

# Entropy Score
score = 0

if length >= 8:
    score += 2

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_symbol:
    score += 1

# Penalties
if repeated_chars:
    score -= 1

if sequential_pattern:
    score -= 1

# Common password check
common_password = password_lower in common_passwords

print("\n" + "=" * 60)
print("PASSWORD SECURITY REPORT")
print("=" * 60)

print(f"Length                : {length}")
print(f"Uppercase Letters     : {has_upper}")
print(f"Lowercase Letters     : {has_lower}")
print(f"Numbers               : {has_digit}")
print(f"Special Symbols       : {has_symbol}")
print(f"Repeated Characters   : {repeated_chars}")
print(f"Sequential Pattern    : {sequential_pattern}")

print("\nSECURITY POLICY CHECK")

if length >= 8:
    print("✓ Length Requirement Passed")
else:
    print("✗ Length Requirement Failed")

if has_upper:
    print("✓ Uppercase Requirement Passed")
else:
    print("✗ Uppercase Requirement Failed")

if has_digit:
    print("✓ Number Requirement Passed")
else:
    print("✗ Number Requirement Failed")

if has_symbol:
    print("✓ Symbol Requirement Passed")
else:
    print("✗ Symbol Requirement Failed")

# Final classification
if common_password:
    strength = "WEAK"
    print("\n⚠ Common Password Detected!")
else:
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

print("\nPASSWORD STRENGTH :", strength)

print("\nRECOMMENDATIONS")

if length < 8:
    print("- Use at least 8 characters.")

if not has_upper:
    print("- Add uppercase letters.")

if not has_lower:
    print("- Add lowercase letters.")

if not has_digit:
    print("- Add numbers.")

if not has_symbol:
    print("- Add special characters (@, #, $, %, &, etc.).")

if repeated_chars:
    print("- Avoid repeating the same characters too often.")

if sequential_pattern:
    print("- Avoid predictable sequences like 123456 or qwerty.")

if common_password:
    print("- Do not use commonly known passwords.")

if strength == "STRONG":
    print("- Excellent! Your password follows strong security practices.")

print("\nValidation Completed Successfully.")