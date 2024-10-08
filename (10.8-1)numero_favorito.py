import json
from pathlib import Path

num_fav = input('Digite seu número favorito: ')

path = Path('numero_favorito.json')
contents = json.dumps(num_fav)
path.write_text(contents)
