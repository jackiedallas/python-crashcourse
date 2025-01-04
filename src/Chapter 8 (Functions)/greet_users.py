from faker import Faker  # type: ignore

fake = Faker()


def greet_users(names):
    """print a simple greeting to each user in the list"""
    for name in names:
        message = f"Hello, {name.title()}!"
        print(message)


usernames = [fake.first_name().lower() for _ in range(10)]
greet_users(usernames)
