usernames = ['admin', 'jack', 'tom', 'jerry','william']
username = 'admin'
if username == 'admin':
    print("Hello admin, would you like to see a status report?")
elif username in usernames:
    print(f"Hello {username.title()}, thank you to logging in again.")
