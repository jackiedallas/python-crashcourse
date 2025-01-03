import textwrap


class User:
    """Class to create a user."""

    def __init__(self, first_name, last_name, age, gender, user_name, email):
        """Initialize user with first and last name."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.user_name = user_name
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        """Print a message describing the user."""
        print(textwrap.dedent(f"""
        First Name: {self.first_name}
        Last Name: {self.last_name}
        Age: {self.age}
        Gender: {self.gender}
        Username: {self.user_name}
        E-Mail Address: {self.email}
        """).strip())

    def greet_user(self):
        """Print a personalized greeting to user."""
        print(f"Hello {self.first_name} {self.last_name}!")
        print(f"We setup your profile with the username '{self.user_name}'.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        print("Resetting login attempts.")
        self.login_attempts = 0

    def show_login_attempts(self):
        print(f"Login Attempts: {self.login_attempts}")


my_user = User(
    'Jackie',
    'Dallas',
    32,
    'Male',
    'jackieray24',
    'jdallas@gmail.com'
    )

my_user.describe_user()
my_user.greet_user()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.show_login_attempts()
# print(my_user.login_attempts)
my_user.reset_login_attempts()
# print(my_user.login_attempts)
my_user.show_login_attempts()
