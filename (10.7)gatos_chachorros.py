from pathlib import Path

path = Path('gatos.txt')
try:
    contents = path.read_text()
except FileNotFoundError:
    print('Desculpe, mas este arquivo não foi encontrado!')

print(contents)


path = Path('cachorros.txt')

try:
    contents = path.read_text()
except FileNotFoundError:
    print('Desculpe, mas este arquivo não foi encontrado!')

print(contents)
