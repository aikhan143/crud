import json

def in_database(name):
    with open('db.json', 'r') as db:
        db_py = json.load(db)

        for user in db_py:
            if user['name'] == name:
                return True
        return False
        
def validate_password(password):
    if len(password) < 8:
        raise Exception('Password is too short')
    return True

def register(name, password):
    with open('db.json', 'r+') as db:
        db_py = json.load(db)

        if in_database(name):
            raise Exception('Username already exists')
        
        if validate_password(password):
            user = {'name': name, 'password': password}
            db_py.append(user)
            with open('db.json', 'w') as db_write:
                json.dump(db_py, db_write)
            return 'You have registered successfully'
            
    
def login(name, password):
    with open('db.json', 'r') as db:
        db_py = json.load(db)

        for user in db_py:
            if user['name'] == name:
                if user['password'] == password:
                    return 'You have logged in'
                else:
                    raise Exception('Incorrect password')
        else: 
                raise Exception('Incorrect login')
            
def change_password(name, new_password):
    with open('db.json', 'r+') as db:
        db_py = json.load(db)

        for user in db_py:
            if user['name'] == name:
                user['password'] = new_password
                with open('db.json', 'w') as db_write:
                    json.dump(db_py, db_write)
                return 'You have changed password'

def change_login(name, new_name):
    with open('db.json', 'r+') as db:
        db_py = json.load(db)

        if any(user['name'] == new_name for user in db_py):
            raise Exception('Username already exists')

        user_found = False

        for user in db_py:
            if user['name'] == name:
                user['name'] = new_name
                user_found = True

        if not user_found:
            raise Exception('There is no such username')

        with open('db.json', 'w') as db_write:
            json.dump(db_py, db_write)

    return 'You have changed login'

def delete_user(name, password):
    with open('db.json', 'r+') as db:
        db_py = json.load(db)

        user_found = False

        for user in db_py:
            if user['name'] == name and user['password'] == password:
                db_py.remove(user)
                user_found = True
                with open('db.json', 'w') as db_write:
                    json.dump(db_py, db_write)
                return 'You have deleted your account'
            
        if not user_found:
            raise Exception('Incorrect login or password')

print(register('test_user', '12345678'))
print(login('test_user', '12345678'))
print(change_password('test_user', 'new_password'))
print(change_login('test_user', 'aikhan'))
print(delete_user('aikhan', 'new_password'))