from user import User


class Privileges:
    """A model of the privileges for an Administrator."""

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Print a list of privileges for admins."""
        print("Administrator Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Extending User class to an administrator."""
    def __init__(self, first_name, last_name, age, gender, user_name, email):
        """Initialize admin with default attributes."""
        super().__init__(first_name, last_name, age, gender, user_name, email)
        self.privileges = Privileges()


new_admin = Admin('steve', 'jobs', 45, 'male', 'stevie_j', 'stevie@apple.com')
new_admin.describe_user()
new_admin.privileges.show_privileges()
new_admin.greet_user()
new_admin.increment_login_attempts()
new_admin.show_login_attempts()
new_admin.reset_login_attempts()
new_admin.show_login_attempts()
