
def count_word(filename, word):
    """Count the approximate number of a word in a file."""
    count = 0

    try:
        with open(filename) as f_obj:
            contents = f_obj.readlines()

    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        for line in contents:
            count += line.lower().count(word)

    print("The word " + word + " is found " + str(count) + " times in the given text")


