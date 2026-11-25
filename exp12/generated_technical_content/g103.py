def check_password(password):
    checks = {
        "Minimum 8 characters": len(password) >= 8,
        "Uppercase": any(c.isupper() for c in password),
        "Lowercase": any(c.islower() for c in password),
        "Digit": any(c.isdigit() for c in password),
        "Special character": any(not c.isalnum() for c in password)
    }
    for rule, passed in checks.items():
        print(rule, ":", "Pass" if passed else "Fail")
    return all(checks.values())
