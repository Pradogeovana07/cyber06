#1. 1.	Write an if statement that checks if the variable a is equal to 1. If it is equal to 1, print a message saying, ‘a equals 1’, else print ‘a is not equal to 1’.
a = int(input('Enter a number:'))
if a == 1:
    print('a equals 1')
else:
    print('a is not equal to 1')

#2.2.	 Write an input statement that gets a value from the user that will be represented by variable B. You are requested to add an if-else statement to check If the variable B is less than 10. If the value from the user is less than 10 print, ‘Too small’. Else, it should print, ‘Perfect fit’.
b = int(input('Please enter a number: '))

if b < 10:
    print('too small')
else:
    print('perfect fit')

#3.	Write an if-else statement that asks the user to enter the speed at which he is driving. If the speed is less than 50 print ‘Speed in limit’, else print ‘Speed should be checked’.

speed = int(input('Enter your speed: '))

if speed > 50:
    print('speed in limit')
else:
    print('speed should be checked')

#4.	 Write a program that asks the user to enter their age.  The program should display a message indicating whether the person is an infant, a child, a teenager, or an adult. 
# Following are the guidelines:
# •	If the person is 1 year old or less, print he or she is an infant.
# •	If the person is older than 1 year, but younger than 13 years, print he or she is a child.
# •	If the person is at least 13 years old, but less than 20 years old, print he or she is a teenager.
# •	If the person is at least 20 years old, print he or she is an adult.

userAge = int(input('Enter your age: '))
if userAge <= 1:
    print('User is an infant')
if userAge > 1 and userAge < 13:
    print('user in a child')
if userAge > 13 and userAge < 20 :
    print('user is a teenager')
if userAge >= 20:
    print('user is an adult')
