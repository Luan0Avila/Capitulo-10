from pathlib import Path

path = Path('guest_book.txt')
while True:
    username = input("Por favor digite seu nome: ")
    if username == 'q':
        break
    else:
        new_user = path.read_text()
        new_user += username + '\n'
        path.write_text(new_user)
