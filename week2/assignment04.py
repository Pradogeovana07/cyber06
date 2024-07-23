# # Chapter 5: Functions
# 1.	Write a function named computer() that prints your name.
def computer():
    name = "Geovana"
    print(name)
computer()

# 2.	Write a function named times_ten() the function should accept an argument from a user and display the product of its argument multiplied times 10.
def times_ten():
    x = int(input("Enter a number: "))
    print(x*10)
times_ten()

# 3.	Write a function named welcome() that asks the user to enter his or her name and displays it followed by a welcome message.
def welcome():
    name = input("Enter your name: ")
    print("Thank you for signing up", name)
welcome()

# 4.	Write a function named get_first_name() that asks the user to enter his or her first name and returns it.
def get_first_name():
    name = input("What is your name? ")
    print(name)
get_first_name()

# 5.	Write a function named area() that gets a number from a user and multiplies it by 15.
def area():
    number = int(input('Enter area: '))
    print(number * 15)
area()