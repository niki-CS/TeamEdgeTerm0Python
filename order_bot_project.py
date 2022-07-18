# -------------------------------------------- 

	# You've just learned about variables, conditionals, functions, and user input. 
	# You've also created a basic calculator in a previous project.
	
	# Now imagine you are going out to eat.
	# Are you at a restaurant for a meal? Are you grabbing boba? Or are you just going to an ice cream parlor?
	# At the end of the meal, you get the bill. 

	# How do you think restaurants automate that math?

					# Let's try it!

# -------------------------------------------- 

# Scenario Parameters: 

	# When you eat out, you have the option to order one or multiple items.
	# What kind of items are available to order? There's usually a menu.
	# Allow your user to order a drink, meal, and dessert.

	# At the end of the order, the receipt comes and you have to calculate the total cost:
	# Don't forget the tax and tip!

# After this program finishes running, it should output a receipt with:
    #1. the items you ordered and their cost 
	#2. a total for your order before tax
	#3. a total for your order after tax
	#4. the amount of your tip 
	#5. the total including tax and tip

# -------------------------------------------- 


# -------------------------------------------- 

# Part 1:
# Let's start by creating the variables we'll need to keep track of the user's order
# as well as TAX and tip

# Remember: Your user should be able to order at least 3 items (a drink, meal, and dessert item). 

# --------------------------------------------
tax_rate = 0.08875


# -------------------------------------------- 

# Part 2:
# Next, let's display the menu. Include the food item name and it's cost. 

# Write a function that will display the menu:
# - Print each item available and it's cost. You should have at least 3 items available (a drink, meal, and dessert item). 

# --------------------------------------------

print("      MENU \n   _ _ _ _ _ \n")
print("Drinks:\n1. Milkshake    $3.00\n2.Coke    $2.00\n3. Sprite    $2.50")
print("\nMeals:\n1. Hamburger w/ Fries    $7.00\n2. Chicken & Waffles    $6.00\n3. Caesars Salad    $5.50")
print("\nDesserts:\n1. Vanilla Cake    $4.00\n2. Flan    $4.00\n3. Chocolate Sundae    $5.00")
print("\nHello and welcome to Niki's Diner!")

# -------------------------------------------- 

# Part 3:
# Let's take the order. What did the user order? What does it cost?

# Write a function that will take the order:
# - Prompt the user to enter a drink, dessert, and meal (Bonus: give them the option to not order an item)
# - Return the cost 

# Remember! Functions are meant to be reusable, so write a function that will work when called repeatedly!

# --------------------------------------------

global orderDrink 
global orderMeal
global orderDessert
global subtotal

# -------------------------------------------- 

# Part 4:
# Now that you have the costs of everything ordered, let's calculate the cost of the order(including tip and tax).

# Write a function that will calculate the cost of the order, including:
# - Cost of all ordered items
# - Tax (Look up the sales tax of your city)
# - Tip (Give the user the option to enter how much they want to tip)

# Remember! Functions are meant to be reusable, so write a function that will work when called for each person!

# -------------------------------------------- 

def foodBot():

	orderDrink = int(input("What would you like to drink? (Choose 1, 2, or 3. Choose 4 if you do not want a drink.):"))
	orderMeal = int(input("\nNow, what would you like to eat? (Choose 1, 2, or 3. Choose 4 if you do not want a meal.):"))
	orderDessert = int(input("\nLastly, what would you like to drink? (Choose 1, 2, or 3. Choose 4 if you do not want a dessert.):"))

	if orderDrink == 1:
		drink = 3.00 
	elif orderDrink == 2:
		drink = 2.00 
	elif orderDrink == 3:
		drink = 2.50 
	elif orderDrink == 4:
		drink = 0
	else:
		print("You have not selected a valid value. Please try again!")

	if orderMeal == 1:
		meal = 7.00 
	elif orderMeal == 2:
		meal = 6.00 
	elif orderMeal == 3:
		meal = 5.50 
	elif orderMeal == 4:
		meal = 0
	else:
		print("You have not selected a valid value. Please try again!")

	if orderDessert == 1:
		dessert = 4.00 
	elif orderDessert == 2:
		dessert = 4.00
	elif orderDessert == 3:
		dessert = 5.00 
	elif orderDessert == 4:
		dessert = 0
	else:
		print("You have not selected a valid value. Please try again!")

	subtotal = drink + meal + dessert
	tax = subtotal+tax_rate
	tax = round(tax, 2)
	subtotal = round(subtotal, 2)
	print(f"\nYou total with tax is: {tax}")

	tipInput = input("What would you like to tip? (10%, 15%, 20%, 22%):")
	if tipInput == "10%": 
		tip = subtotal*.10
	elif tipInput == "15%": 
		tip = subtotal*.15
	elif tipInput == "20%": 
		tip = subtotal*.20
	elif tipInput == "22%":
		tip = subtotal*.22

	if orderDrink == 1:
		selection1 = "Milkshake"
	elif orderDrink == 2:
		selection1 = "Coke" 
	elif orderDrink == 3:
		selection1 = "Sprite" 
	elif orderDrink == 4:
		selection1 = "No drink"
	
	if orderMeal == 1:
		selection2 = "Hamburger w/ Fries" 
	elif orderMeal == 2:
		selection2 = "Chicken & Waffles" 
	elif orderMeal == 3:
		selection2 = "Caesars Salad" 
	elif orderMeal == 4:
		selection2 = "No meal"
	
	if orderDessert == 1:
		selection3 = "Vanilla Cake"
	elif orderDessert == 2:
		selection3 = "Flan"
	elif orderDessert == 3:
		selection3 = "Chocolate Sundae" 
	elif orderDessert == 4:
		selection3 = "No dessert"

	tip = round(tip, 2)
	total = tax+tip	
	print("\nThank you for dining at Niki's Diner! Here is your receipt:\n")
	print(f"{selection1} - {drink}\n{selection2} - {meal}\n{selection3} - {dessert}\n")
	print(f"Subtotal: {subtotal}\nTax: {tax_rate}\nTip: {tip}\nTotal: {total}\n")
	print("Hope you come back soon!")

foodBot()

# -------------------------------------------- 

# Part 5:
# Let's print out a receipt.

# Write a function that will take the values of the order and total cost and print it out in an appealing way.

# The receipt should include:
# - Cost of each item
# - Tax for the order
# - Tip for the order
# - Total cost for the order

# -------------------------------------------- 
# -------------------------------------------- 

# Part 6: Food Order Bot

# Call all of your functions to get your food order bot up and running!

# --------------------------------------------
# -------------------------------------------- 

# Part 7: Upchallenges!

# How many of these upchallenges can you implement?

# - Make sure the user is only entering valid values. If they enter an invalid value, prompt them to re-enter. 
# - The displayed prices should only have two decimal places.
# - Implement a rewards system (stamp cards, buy one get one, etc)

# --------------------------------------------