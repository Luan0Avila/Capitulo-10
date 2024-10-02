from pathlib import Path

path = Path('guest.txt')
username = input("Por favor digite seu nome: ")

path.write_text(username)
