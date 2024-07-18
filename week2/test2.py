# 1. Using a For Loop, write a program that loops through and prints your first name.
# hint: for i in "Myblog":
#               print (i, '?')



#2. Using a For Loop, write a program that loops through the name ANONYMOUS and prints

# for i in "ANONYMOUS":
#     print(i)


#3. Using a while loop, create an infinite loop. (Remember to stop the program after you run it for a few seconds)

# i = 6
# while i == 6:
#   print(i)

# #4. Write a function named area that accepts the base and perpendicular of a right-angled triangle as two arguments and returns the area of that triangle.
# a = float(input('What is the first side?'))
# b = float(input('What is the second side?'))
# area = a*b/2
# print(area)


# #5. Write a function named times_ten. The function should accept an argument and display the product of its argument multiplied times 10.
# x = float(input('Enter a number: '))
# print(x * 10)


#6. Write a function named welcome() that asks the user to enter his or her name and displays it followed by a welcome message.
def welcome():
    x = (input('What is your name?'))
    print(f'welcome {x}!')
welcome()

#7. Write a program that gets input from the user and writes that input into a file that you will call ‘friends.txt’.

f = open('friends.txt')
f.write(input('Enter your email address: '))
print(f.read())

#8. Write a program that will read ‘ip.txt’ as soon as the boss executes it.
print(f.read('ip.txt'))

#9. Write a program that will write 3 IP Addresses (192.168.2.3, 10.0.0.1, 192.168.44.3) into a file named ‘ip.txt’. The boss needs them!! 

f = open('addresses.txt','w')

f.write('192.168.2.3, ')
f.write('10.0.01, ')
f.write('192.168.44.3')

f = open("addresses.txt", "r")
print(f.read())

#10. Write a program that will write THREE NAMES into a text file names ‘philosophers.txt’.

f = open('philosophers.txt','w')

f.write('name1')
f.write('name2 ')
f.write('name3')

f = open("philosophers.txt", "r")
print(f.read())