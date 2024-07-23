# 1.	Create a for loop that will loop and print all the characters in the string “Hippopotamus”.
x = 'Hippopotamus'
for i in x:
    print(i)

# 2.	In the string “Hippopotamus”, using the indexing techniques, print out index 6 and index 8 separately.
x = ('HIPPOPOTAMUS')
print(x[6])
print(x[8])


# 3.	Create an input statement that would request a string from a user. Using the string from the user, find the length of the string and print it out.
a = input('enter a sentence: ')
print(len(a))

# 4.	Create two input statements that will get two names from a user then concatenate both names together and print them out.
firstName = input('Please enter your first name: ')
lastName = input('Please eneter your last name: ')
fullName = firstName + lastName
print(fullName)


# 5.	Create a python program that will slice the following string and only provide the middle name. string = ‘Patty Lynn Smith’ (Use indexing to get the name)
name = ('Patty Lynn Smith')
print(name[5:10])