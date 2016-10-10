
def addition_program():
    add = True
    print("Enter q to quit")
    while(add):
        print()
        first = input("Enter first number: ")
        if first == 'q':
            break
        second = input("Enter second number: ")
        if second == 'q':
            break
        try:
            answer = float(first) + float(second)
        except ValueError:
            print("Please enter numbers not text for addition calculation")
        else:
            print(str(answer) + " = " + str(first) + " + " + str(second))



