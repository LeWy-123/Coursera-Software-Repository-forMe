# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the
# score is between 0.0 and 1.0, print a grade using the following table: Score Grade >= 0.9 A >= 0.8 B >= 0.7 C >=
# 0.6 D < 0.6 F If the user enters a value out of range, print a suitable error message and exit. For the test,
# enter a score of 0.85.

def grading():
    try:
        grade = float(input("Enter your score: "))
    except:
        print("Please enter a valid score, should be between 0.0 and 1.0.")
        return None
    if grade > 1.0 or grade < 0.0:
        print("Your grade is out of range!")
        return None
    elif grade >= 0.9:
        print("A")
    elif grade >= 0.8:
        print("B")
    elif grade >= 0.7:
        print("C")
    elif grade >= 0.6:
        print("D")
    elif grade < 0.6:
        print("F")
    else:
        print("Invalid score")

if __name__ == "__main__":
    grading()

