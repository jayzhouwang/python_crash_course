# usernames = ['admin', 'jack', 'tom', 'jerry', 'william']
usernames = []
username = 'admin'
if usernames:   
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    elif username in usernames:
        print(f"Hello {username.title()}, thank you to logging in again.")
else:
    print("We need to find some users.")