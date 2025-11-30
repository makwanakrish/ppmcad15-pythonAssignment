# This script checks how strong a password is.
# It makes sure the password meets all the required security rules.

import string

def check_password_strength(password):
    """
    Function to check the password against all four rules.
    It returns True if strong, or False if weak.
    """
    # RULE 1: Check if the password is at least 8 characters long.
    is_long_enough = len(password) >= 8

    # RULE 2: Check for uppercase and lowercase letters.
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_both_cases = has_uppercase and has_lowercase

    # RULE 3: Check for at least one number (digit 0-9).
    has_digit = any(char.isdigit() for char in password)

    # RULE 4: Check for at least one special character.
    # We list all the special characters we allow.
    special_characters = "!@#$%^&*()-_+=[]{}|;:',.<>?/~`"
    has_special_char = any(char in special_characters for char in password)

    # The password is STRONG if ALL four rules are TRUE.
    is_strong = (
        is_long_enough and
        has_both_cases and
        has_digit and
        has_special_char
    )

    return is_strong

# --- Main part of the script ---

if __name__ == "__main__":
    # Ask the user to input a password.
    user_password = input("Please enter your password to check its strength: ")

    # Call the function to check the password.
    is_valid = check_password_strength(user_password)

    # Give feedback to the user based on the result.
    if is_valid:
        print("\n*** RESULT: STRONG PASSWORD! ***")
        print("This password meets all the security requirements.")
    else:
        print("\n*** RESULT: WEAK PASSWORD! ***")
        print("Please make it stronger by following these rules:")
        print("- Be at least 8 characters long.")
        print("- Use both UPPERCASE (A, B) and lowercase (a, b) letters.")
        print("- Use at least one NUMBER (1, 2, 3).")
        print("- Use at least one SPECIAL CHARACTER (!, @, #, $).")