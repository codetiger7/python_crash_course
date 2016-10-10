import json


def get_stored_username():
    """Get stored username"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for new username"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def remember_user():
    username = get_new_username()
    print("We'll remember you when you come back, " + username + "!")


def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        verify = input("Are you " + username + " ? (y/n): ")
        if verify == "y":
            print("Welcome back, " + username + "!")
        else:
            remember_user()
    else:
        remember_user()


greet_user()



