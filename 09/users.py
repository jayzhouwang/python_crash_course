class User:
    """ A class to model user"""

    def __init__(self, first_name, last_name, location, favourite_language):
        """Initializea all attribute"""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.favorite_language = favourite_language

    def describe_user(self):
        """Print a summary of the users's information"""
        print("User info:")
        print(f"-name: {self.first_name.title()} {self.last_name.title()}")
        print(f"-location: {self.location.title()}")
        print(f"-favorite language: {self.favorite_language.title()}")
    
    def greet_user(self):
        """Print a personalized greeting to the user"""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

user1 = User('jack', 'wang', 'changshu', 'python')
user1.describe_user()
user1.greet_user()
