# users_wrapper.py

users = [
    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
        }
    },
    # Outros usuários...
]

def list():
    return users

def create(name, username, email):
    new_id = max(user["id"] for user in users) + 1
    new_user = {
        "id": new_id,
        "name": name,
        "username": username,
        "email": email,
        "address": {},
        "phone": "",
        "website": "",
        "company": {}
    }
    users.append(new_user)
    return new_user

def read(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    return user

def update(user_id, name=None, username=None, email=None):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        if name:
            user['name'] = name
        if username:
            user['username'] = username
        if email:
            user['email'] = email
        return user
    else:
        return None

def delete(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return users
