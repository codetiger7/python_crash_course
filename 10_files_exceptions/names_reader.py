

def file_reader(fileName):
    try:
        with open(fileName) as file:
            for line in file:
                print(line)
    except FileNotFoundError:
        #print("\nFile " + fileName + " is not in same folder as program\n")
        pass