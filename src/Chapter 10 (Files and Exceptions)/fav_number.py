from pathlib import Path
import json

def new_fav_number(file_path):
    """Prompt user for a new favorite number and save it at the file path."""
    path = Path(file_path)
    num = input("What is your favorite number? ")
    contents = json.dumps(num)
    path.write_text(contents)
    print(f"We'll save your favorite number til you get back!")

def get_fav_number(file_path):
    """Check if the file path exists and return the contents"""
    path = Path(file_path)
    if path.exists():
        contents = path.read_text()
        num = json.loads(contents)
        return num
        
def fav_number(file_path):
    """
    Use the functions defined above to recall a 
    favorite number or store a new one.
    """
    path = Path(file_path)
    number = get_fav_number(path)
    if number:
        print(f"I know your favorite number! It's {number}.")
    else:
        new_fav_number(path)

fav_number('../json/fav_number.json')   
    