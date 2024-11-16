from faker import Faker  # type: ignore
fake = Faker()

# usernames = []
# usernames = [fake.first_name().lower() for _ in range(8)]
# usernames.insert(4, 'admin')
current_users = [fake.first_name().lower() for _ in range(10)]
new_users = current_users[5:]
new_users.append(fake.first_name().lower())
new_users.append(fake.first_name().lower())
new_users.append(fake.first_name().lower())
new_users.append(fake.first_name().lower())
new_users.append(fake.first_name().lower())

admin_message = 'Hello Admin, would you like to see a status report?'
empty_message = 'We need to find some users!'
print(current_users)
print(new_users)
if new_users:
    for user in new_users:
        if user in current_users:
            print(f"'{user}', this username already exists create a new one.")
        else:
            print(f"'{user}', this username is available.")
# if usernames:
#     for username in usernames:
#         if username == 'admin':
#             print(admin_message)
#         else:
#             print(f"Hello {username.title()}, thank you for logging in again!")
# else:
#     print(empty_message)
