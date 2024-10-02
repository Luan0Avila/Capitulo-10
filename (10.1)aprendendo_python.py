from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
print(contents)

string = ''
lines = contents.splitlines()
for line in lines:
    string += line

print (string)