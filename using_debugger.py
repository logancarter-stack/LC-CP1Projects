# LC 1 Ravager Snack Bar 
import random

pirate_name = input("What's your name, pirate? ")
snack_name = input("What snack do you want? ")

price = random.randint(2, 8)  # random price in credits
quantity = int(input("How many would you like? "))

total = price * quantity
total_new = int(total)#made total an interger
discounted_total = total_new -2 * 0.10

tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)

print("Hello, " + pirate_name + "! Here's your order summary:")
print("Snack: " + snack_name)#runtime error fixed : change snackName to snack_name
print("Price per snack: " + str(price) + " credits")
print("Total before tax: "  + str(discounted_total))# printed the same thing as above now it print what is was meant to 
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits")# syntax error fixed : no parenthesse to parenthesses