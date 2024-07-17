#1. Tip, tax, and total
# Write a program that calculates the total amount of a meal purchased at a restaurant. The program should ask the user to enter the charge for the food, and then calculate the amount of an 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.
def calculate_total():
    #user input
    charge_food = float(input("Enter the charge for food: $"))

    #calculate tip
    tip_amount = 0.18 * charge_food

    #calculate sales tax
    tax_amount = 0.07 * charge_food

    #calculate total
    total_cost = charge_food + tip_amount + tax_amount

    print(f"Cost of food: ${charge_food:.2f}")
    print(f"tip amount (18%): ${tip_amount:.2f}")
    print(f"sales tax amount(7%): ${tax_amount:.2f}")
    print(f"total amount: ${total_cost:.2f}")

calculate_total()

#2. Sales Prediction
# A company has determined that its annual profit is typically 23 percent of total sales. Write a program that asks the user to enter the projected amount of total sales, and then displays the profit that will be made from that amount.
def annual_profit():
    projected_amount = float(input('Enter the projected amount of total sales: '))

    profit = 0.23 * projected_amount

    print(f"Annual profit: ${profit:.2f}")

annual_profit()

#3. Miles-per-Gallon
# A car’s miles-per-gallon (MPG) can be calculated with the following formula:
# MPG = Miles driven Gallons of gas used
# Write a program that asks the user for the number of miles driven and the gallons of gas used. It should calculate the car’s MPG and display the result.
gas_used = int(input('Enter ther number of gallons used: '))
miles_driven = int(input('Enter the number of miles driven: '))

mpg =  miles_driven / gas_used
print('Your car gets', mpg , 'miles per gallon')



#4. Total Purchase
# A customer in a store is purchasing five items. Write a program that asks for the price of each item, and then displays the subtotal of the sale, the amount of sales tax, and the total. Assume the sales tax is 7 percent.
def customer1():
#cost of item
    item1 = float(input('price of item 1: '))
    item2 = float(input('price of item 2: '))
    item3 = float(input('price of item 3: '))
    item4 = float(input('price of item 4: '))
    item5 = float(input('price of item 5: '))

#total_cost
    cost_items = item1 + item2 + item3 + item4 + item5
#calcuate cost of food plus tax
    tax_amount = 0.07 * cost_items
#calculate total
    total = cost_items + tax_amount

    print(f"all items: ${cost_items:.2f}")
    print(f"sales tax amount(7%): ${tax_amount:.2f}")
    print(f"total amount: ${total:.2f}")
    
customer1()
