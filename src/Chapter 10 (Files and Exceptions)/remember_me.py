from pathlib import Path
import json

def get_store_username(file_path):
    """Get stored username if available."""
    path = Path(file_path)
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else: 
        return None

def get_new_username(file_path):
    """Get a new username."""
    path = Path(file_path)
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username
    
def greet_user(file_path):
    """Greet the user by name."""
    path = Path(file_path)
    username = get_store_username(file_path)
    if username:
        print(f"Welcome Back, {username}!")
    else:
        username = get_new_username(file_path)
        print(f"We'll remember you when you come back, {username}!")

greet_user('../json/username.json')
