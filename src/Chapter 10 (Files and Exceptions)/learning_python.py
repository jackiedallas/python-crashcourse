from pathlib import Path

path = Path('../text_files/learning_python.txt')
contents = path.read_text()

print(contents)

contents = contents.replace('Python', 'JavaScript')
# lines = contents.splitlines()

for line in contents.splitlines():
    # print(line)
    # line.replace('Python', 'Java')
    print(line)
