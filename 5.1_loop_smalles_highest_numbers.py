# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is
# entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number,
# catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10,
# and 4 and match the output below.

# defining a method for handling the search
def high_small_numbers():
    smallest = None
    largest =  None
    sets = []
    while True:
        try:
            # The input field
            number = input("Enter a number: ")
            # Checking the input is the exit word or a number if not converts it to integer
            if number == "done":
                break
            else:
                number = int(number)
        except:
            # If the input invalid it prints out an error message
            print("Invalid input")
            continue

        # Append the entered input to the sets list if it's a number.
        sets.append(number)

    # looking for the largest numbers
    for num in sets:
        # if the initial value is none, assigns the first number to the variable called largest
        if largest is None :
            largest = num
        elif num > largest:
            largest = num

    # looking for the smallest number
    for num in sets:
        # if the initial value is none, assigns the first number to the variable called smallest
        if smallest is None :
            smallest = num
        elif num < smallest:
            smallest = num

    # printing the result in the end when all numbers were found.
    print("Maximum is", largest)
    print("Minimum is", smallest)

# if this is the main scope, it runs the method
if __name__ == "__main__":
    high_small_numbers()