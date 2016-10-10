import json


def store_favourite_number():
    f_number = input("What is your favourite number? ")
    filename = "stored_number.json"
    with open(filename, 'w') as f_obj:
        json.dump(f_number,f_obj)


def retrieve_favourite_number():
    filename = 'stored_number.json'
    try:
        with open(filename) as f_obj:
            fav_num = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return fav_num


def favourite_number_prog():
    number = retrieve_favourite_number()
    if number:
        print("I know your favourite number! It's " + number + ".")
    else:
        store_favourite_number()


favourite_number_prog()