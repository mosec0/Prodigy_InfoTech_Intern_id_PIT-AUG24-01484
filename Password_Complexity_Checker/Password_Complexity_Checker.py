import re

def password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[\W_]', password) is not None

    # Evaluate password strength
    strength = 0
    feedback = []

    if length_criteria:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if uppercase_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if lowercase_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if digit_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one digit.")

    if special_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Determine strength level
    if strength == 5:
        feedback.insert(0, "Password strength: Very Strong")
    elif strength == 4:
        feedback.insert(0, "Password strength: Strong")
    elif strength == 3:
        feedback.insert(0, "Password strength: Medium")
    else:
        feedback.insert(0, "Password strength: Weak")

    return "\n".join(feedback)

def main():
    print("Password Complexity Checker")
    password = input("Enter a password to check its strength: ")
    feedback = password_strength(password)
    print(feedback)

if __name__ == "__main__":
    main()
