from pathlib import Path
import json


def get_stored_userdata(path):

    if path.exists():
        contents = path.read_text()
        userdata = json.loads(contents)
        username = userdata['name']
        age = userdata['age']
        country = userdata['country']
        return userdata
    else:
        return None
    



def greet_user():
    path = Path('userdata2.json')
    userdata = get_stored_userdata(path)
    if userdata:
        print(f"Wellcome back, {userdata['name']}\nI remenber your age: {userdata['age']}\nAnd I remenber your country: {userdata['country']}")
        confirmation = input(f'Is this user information correct? (y/n)\n{userdata['name']}, {userdata['age']},  {userdata['country']} ')
        if confirmation.lower() == 'n':
            get_new_userdata()
    else:
        get_new_userdata()


def get_new_userdata():
   path = Path('userdata2.json')
   username = input('What is your name? ')
   age = input('What is your age? ')
   country = input('What is your country? ')
   userdata = {
       'name': username,
       'age': age,
       'country': country
   }
   contents = json.dumps(userdata)
   path.write_text(contents)
   print(f"We'll remember you when you come back {username}!")

greet_user()
