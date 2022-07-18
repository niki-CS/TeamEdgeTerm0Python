#********************************************************************
 #                                                                 
 #  Team Edge List Mini-project: THE SHOPPING LIST HELPER
 # 
 #  This project prompts users using input() to prompt users
 #  to add (or remove) items from a shopping list. It starts empty
 #  and each time the program is run it asks you to either add or 
 #  remove an item from the list. It also updates the user of its
 #  contents. The shopping list also checks to see if an item 
 #  is already present in the list and prevents you from adding it
 #  again, giving feedback along the way. 
 # 
 # ***************************************************************/

active = True

print("Welcome to Shopping List!")

welcome_message = "Hi! I'm your shopping assistant. Let me take your order. \nYou can type 'add milk' to add milk to your shopping list. \nor you can type 'remove milk' to remove it. \n"

print(welcome_message)

#-->Todo: declare a shopping_list list
shopping_list = []

def prompt_user():
    reply = input("What do you want to add or remove?  >>  ")
    if reply == "":
        print("I didn't understand that. Try typing add/remove followed by an item")
    return reply 

def check_answer(ans):
    split_input = ans.split(" ")
    ans = split_input[0]
    if ans == "add":
        add_item(split_input[1])
    if ans == "remove":
        remove_item(split_input[1])

def add_item(item):
    global shopping_list
    shopping_list.append(item)
    new_item_list = (",".join(item))
    print(str(item) + " added. The shopping list now has: " + str(shopping_list))
    

#this function can take in a string and store it in an array
    
def remove_item(item):
    global shopping_list
    shopping_list.remove(item)
    print(str(item) + " removed. The shopping list now has: " + str(shopping_list))
    if len(shopping_list) < 1:
        print("shopping list complete!")

while active:
    check_answer(prompt_user()) #this makes the program continously prompt and check response while the boolean 'active' returns True
