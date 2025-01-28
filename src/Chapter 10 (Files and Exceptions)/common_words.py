from pathlib import Path

def common_words(path, word):
    try:
        file_path = Path(path)
        contents = file_path.read_text(encoding='utf-8')
        word_to_lower = word.lower()
        word_count = contents.lower().count(word_to_lower)
    except FileNotFoundError:
        print(f"File not found..")
    else:
        print(f"The word '{word}' appears {word_count} times in the '{path}'.")

common_words('../text_files/moby_dick.txt', 'the ')
common_words('../text_files/r_and_j.txt', 'madman')

    