#1. Bug Collector A bug Collector collects bugs every day for five days. Write a program that keeps a running total of the number of bugs collected during the five days. The loop should ask for the number of bugs collected for each day, and when the loop is finished, the program should display the total number of bugs collected.

# totalBugs = 0
# days = int(input("how many days did you collect bugs for?"))
# for i in range(1, days + 1):
#     bugsCollected = int(input("Enter how many bugs were collected today: "))
#     totalBugs += bugsCollected
# print(f'You have collected a total of {totalBugs} bugs.')

#2. pennies for payWrite a program that calculates the amount of money a person would earn over a period of time if his or her salary is one penny the first day, two pennies the second day, and continues to double each day. The program should ask the user for the number of days. Display a table showing what the salary was for each day, and then show the total pay at the end of the period. The output should be displayed in a dollar amount, not the number of pennies.

# Function to calculate 2^(n-1)
def calculate_salary(n):
    return 2**(n - 1)

# Example usage:
n = (int(input('How many days did you work?')))  # Example day number
salary = calculate_salary(n)/100
print(f"The salary on day {n} is ${salary} dollars.")

