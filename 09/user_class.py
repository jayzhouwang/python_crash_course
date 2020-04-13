"""A class that represent a user"""


class User:
    """ A class to model user"""

    def __init__(self, first_name, last_name, location, favorite_language):
        """Initializea all attribute"""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.favorite_language = favorite_language

    def describe_user(self):
        """Print a summary of the users's information"""
        print("User info:")
        print(f"-name: {self.first_name.title()} {self.last_name.title()}")
        print(f"-location: {self.location.title()}")
        print(f"-favorite language: {self.favorite_language.title()}")

    def greet_user(self):
        """Print a personalized greeting to the user"""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(self.privileges)


class Admin(User):
    """A special kind of user"""

    def __init__(self, first_name, last_name, location, favorite_language):
        super().__init__(first_name, last_name, location, favorite_language)
        self.privileges = Privileges()
