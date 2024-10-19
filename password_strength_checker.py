import re

# Common passwords list (usually this would be a much larger list or from a file)
common_passwords = [
    "password", "123456", "123456789", "12345678", "12345",
    "1234567", "1234567890", "qwerty", "abc123", "password1"
]

def check_password_strength(password):
    # Check length
    length_criteria = len(password) >= 12
    
    # Check for lowercase, uppercase, digits, and special characters
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[@$!%*?&#]', password) is not None
    
    # Check if password is common
    common_password_criteria = password.lower() not in common_passwords

    # Collect all criteria
    criteria = {
        "Length (>= 12 characters)": length_criteria,
        "Lowercase letter": lowercase_criteria,
        "Uppercase letter": uppercase_criteria,
        "Digit": digit_criteria,
        "Special character (@$!%*?&#)": special_char_criteria,
        "Not a common password": common_password_criteria
    }
    
    # Determine overall strength
    if all(criteria.values()):
        strength = "Strong"
    elif length_criteria and sum(criteria.values()) >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    return strength, criteria

def suggest_improvements(criteria):
    suggestions = []
    if not criteria["Length (>= 12 characters)"]:
        suggestions.append("Increase the length to at least 12 characters.")
    if not criteria["Lowercase letter"]:
        suggestions.append("Include at least one lowercase letter.")
    if not criteria["Uppercase letter"]:
        suggestions.append("Include at least one uppercase letter.")
    if not criteria["Digit"]:
        suggestions.append("Include at least one digit.")
    if not criteria["Special character (@$!%*?&#)"]:
        suggestions.append("Include at least one special character (@$!%*?&#).")
    if not criteria["Not a common password"]:
        suggestions.append("Avoid common passwords or easily guessable passwords.")
    
    return suggestions

def main():
    password = input("Enter a password to check its strength: ")
    strength, criteria = check_password_strength(password)
    
    print(f"Password Strength: {strength}")
    print("Criteria Met:")
    for criterion, met in criteria.items():
        print(f"  {criterion}: {'Yes' if met else 'No'}")
    
    if strength != "Strong":
        print("\nSuggestions to improve your password:")
        for suggestion in suggest_improvements(criteria):
            print(f"  - {suggestion}")

if __name__ == "__main__":
    main()
