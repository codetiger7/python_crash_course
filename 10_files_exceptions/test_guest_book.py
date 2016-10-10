
active = True
while(active):
    name = input("What is your name? (q to quit): ")
    if name != 'q':
        with open("guest_book.txt", "a") as file_object:
            file_object.write(name + '\n')
        print("Welcome " + name)
    else:
        active = False

