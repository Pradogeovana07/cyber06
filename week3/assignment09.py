
#1 Create a set and save it under variable new. Using the for loop, loop through and print all the values in the set.

new = {1 , 2, 3, 4, 5}
for i in new :
    print (i)

#2 Create an empty set and assign it to variable empty. Using the add method, add 5 different types of data to the set, and using a for loop, loop through and print all the values in the set.

empty = set()
empty.add('data1')
empty.add('data2')
empty.add('data3')
empty.add('data4')
empty.add('data5')

for i in empty:
    print(i)

#3.	Using the ‘in’ and ‘not in’ operators, get a user to provide a value that you will check if it’s available in the set. If the value is in the set, print a message indicating that it is in the set and if not print an error message.
x = input('Enter a value: ')
if x in empty:
    print('Already in the set!')
elif 'x' not in empty:
    print('Error, that value is not in the set') 
    
#4 4.	Using the remove method, remove two values from the set we made in question 1.

empty.remove('data3')
empty.remove('data4')
print(empty)


#5.	Create two sets and assign them to a variable of your choosing. Using the union operator, join the two sets together and print them out.

fruits = {'apple','banana','orange'}
veggies = {'carrot', 'cucumber, squash'}

new = fruits.union(veggies)

print(new)