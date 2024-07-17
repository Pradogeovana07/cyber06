# 1.	Using a For Loop, write a program that loops through and prints your first name. 


for i in "Myblog":
    print (i, 'Geovana')

#2. Using a For Loop, write a program that loops through the name ANONYMOUS and prints

for i in "ANONYMOUS":
    print(i)

#3. Using a For Loop write a program that loops through numbers in the range 1-5.

for i in range(1,6):
    print(i)

#4.	Using a while loop, write a program that asks for your name and if the input is wrong print ‘WRONG NAME’
def name_input():
    name = input('What is your name? ')

    i = name
    while (i == "Geovana"):
        print('CORRECT!')
        break
    else:
     print("WRONG NAME")
    
name_input()

#5.	Using a while loop, create an infinite loop. (Remember to stop the program after you run it for a few seconds) 

i = 6
while i == 6:
  print(i)
  