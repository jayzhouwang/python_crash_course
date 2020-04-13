"""adfasd"""

import user_class1


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(self.privileges)


class Admin(user_class1.User):
    """A special kind of user"""

    def __init__(self, first_name, last_name, location, favorite_language):
        super().__init__(first_name, last_name, location, favorite_language)
        self.privileges = Privileges()
