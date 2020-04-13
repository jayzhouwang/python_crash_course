class User:
    """ A class to model user"""

    def __init__(self, first_name, last_name, location, favourite_language):
        """Initializea all attribute"""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.favorite_language = favourite_language
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the users's information"""
        print("User info:")
        print(f"-name: {self.first_name.title()} {self.last_name.title()}")
        print(f"-location: {self.location.title()}")
        print(f"-favorite language: {self.favorite_language.title()}")

    def greet_user(self):
        """Print a personalized greeting to the user"""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self):
        """Add 1 to login_attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0"""
        self.login_attempts = 0


user = User('jack', 'wang', 'changshu', 'python')

user.increment_login_attempts()
print(user.login_attempts)
user.increment_login_attempts()
print(user.login_attempts)
user.increment_login_attempts()
print(user.login_attempts)

user.reset_login_attempts()
print(user.login_attempts)
