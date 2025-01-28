from pathlib import Path

contents = "I love programming.\n"
contents += "I love learning new languages.\n"
contents += "I also love snowboarding.\n"

destination_path = Path('../text_files/programming.txt')
destination_path.write_text(contents)
