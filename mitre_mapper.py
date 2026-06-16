from collections import defaultdict

attempts = defaultdict(int)

COMMON_PASSWORDS = {
    "admin", "123456", "password",
    "admin123", "root", "qwerty"
}

def map_attack(ip, username, password):
    attempts[ip] += 1

    if attempts[ip] >= 5:
        return "T1110.003 - Password Spraying"

    if password.lower() in COMMON_PASSWORDS:
        return "T1110 - Brute Force"

    if username.lower() in ["root", "admin", "administrator"]:
        return "T1078 - Valid Accounts"

    return "T1589 - Gather Victim Identity Information"
