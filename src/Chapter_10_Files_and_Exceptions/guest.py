from pathlib import Path

content = ''
file_path = Path('../text_files/guest.txt')
guest_user = input("What's your name? ")
content += guest_user.title()

if not file_path.exists():
    file_path.write_text(content)
else:
    with file_path.open(mode="a") as file:
        file.write("\n" + content)
