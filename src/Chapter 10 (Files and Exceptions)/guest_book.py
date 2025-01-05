from pathlib import Path

content = []
file_path = Path('../text_files/guest_book.txt')
prompt = "\nWhat guest do you want to add (when you're done enter 'q'): "

while True:
    guest = input(prompt)
    if guest == 'q':
        break
    else:
        content.append(guest)

if not file_path.exists():
    with open(file_path, "x") as file:
        for guest in content:
            file.write(guest + "\n")
else:
    with open(file_path, "a") as file:
        for guest in content:
            file.write("\n" + guest)
        file.write("\n" + content)
