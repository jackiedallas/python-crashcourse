# create a list of users
banned_users = ['andrew', 'kaelyn', 'marisol', 'rosalia']

user = 'jackie'
user2 = 'kaelyn'

# use if statement to check if users are present in list
if user not in banned_users:
    print(f"{user.title()} is not banned.")

if user2 in banned_users:
    print(f"{user2} is banned.")
