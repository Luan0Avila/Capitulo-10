import json
from pathlib import Path


path = Path('num_favorito.json')
if path.exists():
    contents = path.read_text()
    num_fav = json.loads(contents)
    print(f"Seu número favorito é {num_fav}")

else:
    num_fav = input('Digite seu número favorito: ')
    contents = json.dumps(num_fav)
    path.write_text(contents)

