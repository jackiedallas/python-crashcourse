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
        First Name: {self.first_name.title()}
        Last Name: {self.last_name.title()}
        Age: {self.age}
        Gender: {self.gender.title()}
        Username: {self.user_name}
        E-Mail Address: {self.email}
        """).strip())

    def greet_user(self):
        """Print a personalized greeting to user."""
        print(f"Hello {self.first_name.title()} {self.last_name.title()}!")
        print(f"We setup your profile with the username '{self.user_name}'.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        print("Resetting login attempts.")
        self.login_attempts = 0

    def show_login_attempts(self):
        print(f"Login Attempts: {self.login_attempts}")
