
soccer = {'name1', 'name2', 'name3'}
football = {'name4', 'name5', 'name6'}

print(f'Hello, this is this year\'s football lineup:')
for i in football:
    print(i)

print(f'And this is this year\'s soccer lineup:')
for i in soccer:
    print(i)

bothTeams = soccer.union(football)

print(f'This is this year\'s soccer AND football team memebers: {bothTeams}')

difInSoccer = soccer.difference(football)
print(difInSoccer)

difInFootball = football.difference(soccer)
print(difInFootball)

empty = set()
userInput = input('Enter you name:')
empty.add(userInput)
print(empty)

deleteUser = input('Enter your name to be removed from the list:')
empty.remove(deleteUser)
print("Your name has been removed")

def deleteAll():
    soccer.clear()
    football.clear()
    empty.clear()

    print(soccer)
    print(football)
    print(empty)
