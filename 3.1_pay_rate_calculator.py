# 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly
# rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a
# rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and
# float() to convert the string to a number. Do not worry about error checking the user input - assume the user types
# numbers properly.

def pay_rate():
    salary = 0
    try:
        hrs = float(input("Enter Hours: "))
        try:
            rate = float(input("Enter Rate: "))
        except:
            print("Please enter a valid number.")
            return None
    except:
        print("Please enter a valid number.")
        return None

    if hrs > 40:
        salary = 40 * rate
        overtime = hrs - 40
        salary = salary + overtime * (rate * 1.5)
    else:
        salary = hrs * rate

    print(f"{salary}")

if __name__ == "__main__":
    pay_rate()