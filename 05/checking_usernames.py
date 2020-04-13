current_users = ['admin', 'jack', 'tom', 'jerry', 'william']
new_users = ['Admin', 'tom', 'tesla', 'trump', 'elizabeth']
for username in new_users:
    if username.lower() in current_users:
        print("You need to enter a new username.")
    else:
        print(f"The username \"{username.title()}\" is available.")