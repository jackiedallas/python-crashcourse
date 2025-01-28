"""
pets.py
@author: Jackie Johnson-Dallas
Created January 28th, 2025
This script will import the path library and read contents of a file
"""

from pathlib import Path

def read_file(path):
    try:
        inputPath = Path(path)
        contents = inputPath.read_text()
    except FileNotFoundError:
        # print(f"Sorry, the file path '{path}' does not exist....")
        pass
    else:
        print(contents)

read_file('../text_files/catss.txt')
read_file('../text_files/dogs.txt')
