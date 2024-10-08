import json
from pathlib import Path

path = Path('numero_favorito.json')
contents = path.read_text()
num_fav = json.loads(contents)

print(f"Seu número favorito é {num_fav}")