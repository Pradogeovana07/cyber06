#1 Create a python program that will slice the following string and only provide the middle name. string = ‘Patty Lynn Smith’ (Use indexing to get the name)

name = ('Patty Lynn Smith')
print(name[5:10])

#2. Create a dictionary called phonebook and add 3 names and 3 phone numbers as key: value pairs. Print the dictionary.
phoneBook = {
    "john":"111-111-1111",
    "Susan": "222-222-2222",
    "Gwen": "333-333-3333"
    }
print(phoneBook)

# #3. Create a python program that adds another fruit to the already created list called fruits in question 1.
fruit = []

#4. In the string “Hippopotamus”, using the indexing techniques, print out index 6 and index 8 separately.
x = ('HIPPOPOTAMUS')
print(x[6])
print(x[8])

#5. Using python, create a list of fruits and store them in the variable fruits. Create another list of your top 3 musicians and store them in a variable called music.
fruits = ["apples","bananas","pears"]
musicians = ["artist1", "artist2", "artist3"]

# #6. Write a python program that will count the number of items in the list called fruits we just created.
print(len(fruits))

#7. Create an input statement that would request a string from a user. Using the string from the user, find the length of the string and print it out.
a = input('enter a sentence: ')
print(len(a))

#8. Create a dictionary with the keys : value pair of any items of your choosing. To create this dictionary the dict() built-in method should be used. Using a For loop, loop through the dictionary and print only the keys of the dictionary.

phoneBook = dict(john = "111-111-1111",Susan = "222-222-2222",Gwen= "333-333-3333")
print(phoneBook)

#9. Using a python program join the list called fruits with the list called music and print out the content of the new list.

fruits = ["apples","bananas","pears"]
musicians = ["artist1", "artist2", "artist3"]
music = fruits + musicians
print(music)

#10. Create two input statements that will get two names from a user then concatenate both names together and print them out.
firstName = input('Please enter your first name: ')
lastName = input('Please eneter your last name: ')
fullName = firstName + lastName
print(fullName)

