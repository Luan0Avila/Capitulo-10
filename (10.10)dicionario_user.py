from pathlib import Path
import json

path = Path('userdata.json')
if path.exists():
    contents = path.read_text()
    userdata = json.loads(contents)
    username = userdata['name']
    age = userdata['age']
    country = userdata['country']
    print(f"Wllcome back, {username}\nI remenber your age: {age}\nAnd I remenber your country: {country}")

else:
    username = input('What is your name? ')
    age = input('What is your age? ')
    country = input('What is your country? ')
    userdata = {
        'name' : username,
        'age' : age,
        'country' : country
    }
    contents = json.dumps(userdata)
    path.write_text(contents)
    print(f"We'll remember you when you come back {username}!")