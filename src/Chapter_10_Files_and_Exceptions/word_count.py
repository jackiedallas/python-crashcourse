from pathlib import Path

def count_words(path):
    """
    Count the approximate number of words in a file.
    """
    
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print(f"Sorry, the file {path} does not exist.")
        pass
    else:
        # count the approximate number of words in the file
        words = contents.split()
        num_words = len(words)
        print(f"The file path {path} has about {num_words} words.")

path = Path('../text_files/joe.txt')
count_words(path)
count_words(Path('../text_files/guest_book.txt'))
count_words(Path('../text_files/pi_million_digits.txt'))