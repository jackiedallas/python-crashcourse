from pathlib import Path
import json

def new_user_info(file_path):
    """Write new dictionary to file path."""
    path = Path(file_path)
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    age = input("How old are you? ")
    user_info = {
        'First Name': str(first_name), 
        'Last Name': str(last_name), 
        'Age': int(age)
        }
    print(user_info)
    json_string = json.dumps(user_info, indent=4)
    path.write_text(json_string)
    print("We have saved your information!")

def get_user_info(file_path):
    path = Path(file_path)
    if path.exists():
        content = path.read_text()
        user_info = json.loads(content)
        print(user_info)
    else:
        new_user_info(file_path)

get_user_info('../json/user4_dictionary.json')
