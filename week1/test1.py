# #1 Write a Python statement that assigns the sum of 10 and 14 to the variable total.

total = 10 + 14
print(total)

# #2 Write an if-else statement that asks the user to enter their age. If their age is less than 50 print ‘You are getting there ‘, else print ‘You are healthy and aging gracefully’.

userAge = int(input('Please enter you age: '))

if userAge < 50:
    print('You are getting there')
else:
    print('You are healthy and aging gracefully')

# #3  customer in a store is purchasing five items. Write a program that asks for the price of each item, and then displays the subtotal of the sale, the amount of sales tax, and the total. Assume the sales tax is 7 percent.

item1 = float(input('Enter cost of item 1 $: '))
item2 = float(input('Enter cost of item 2 $: '))
item3 = float(input('Enter cost of item 3 $: '))
item4 = float(input('Enter cost of item 4 $: '))
item5 = float(input('Enter cost of item 5 $: '))

costForItems = item1 + item2 + item3 + item4 + item5
Tax = costForItems* 0.07
total = Tax + costForItems
print(total)

#4 Write an if statement that checks if the variable a is equal to 1. If it is equal to 1, print a message saying ‘a equals 1’, else print ‘a is not equal to 1’

a = int(input('Enter a number:'))
if a == 1:
    print('a equals 1')
else:
    print('a is not equal to 1')


#5 Write an if-else statement that asks the user to enter the speed at which he is driving. If the speed is more than 50 print ‘Speed in limit’, else print ‘Speed should be checked’.

speed = int(input('Enter your speed: '))

if speed > 50:
    print('speed in limit')
else:
    print('speed should be checked')


#6 The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles. The program should tell the user which rectangle has the greater area, or if the areas are the same.

lenght1 = int(input('Enter the length of the first rectangle: '))
width1 = int(input('Enter the width of the first rectangle: '))
area1 = lenght1 * width1
print(area1)

length2 = int(input('Enter the length of the second rectangle: '))
width2 = int(input('Enter the width of the second rectangle: '))
area2 = length2 * width2
print(area2)

if area1 > area2 :
    print('the first rectangle has greater area')

elif area1 == area2:
    print("areas are the same")
else:
    print('the second rectangle has a greater area')


#7 Using the input function, create a python code that asks for a user’s name and prints it out.
name = input('Enter you name: ')
print(name)

#8 Write an input statement that gets a value from the user that will be represented by variable B. You are requested to add an if-else statement to check If the variable B is less than 10. If the value from the user is less than 10 print, ‘Too small’. Else, it should print, ‘Perfect fit’.

b = int(input('Please enter a number: '))

if b < 10:
    print('too small')
else:
    print('perfect fit')

#9 A customer in a store is purchasing five items. Write a program that asks for the price of each item, and then displays the subtotal of the sale

item1 = float(input('Enter price of item 1: $'))
item2 = float(input('Enter price of item 2: $'))
item3 = float(input('Enter price of item 3: $'))
item4 = float(input('Enter price of item 4: $'))
item5 = float(input('Enter price of item 5: $'))

total = item1 + item2 + item3 + item4 + item5
print(total)


#10 Create a variable called Name and assign your name to it. Print the output of the variable
Name = ('Geovana')
print(Name)



