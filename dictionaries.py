#############################################################################
 #                                                                  
 #  Team Edge dictionaries: Dictionaries CHALLENGES 
 # 
 #  For this activity, you will be building a dictionary and with properties
 #  and methods. You will access the properties, set new values, and use
 #  the methods to change your dictionary state. What dictionary? Ask your coach.
 # 
 #  1. DEFINE: Make a dictionary and set its properties, printing changes in between.
 #  2. MODIFY: Add 2 new properties and assing values. Change existing values,
 #     including adding or updating values inside lists
 #  3. METHODS: Now its time to make some methods tha can make a change
 #     to your values, like a boolean, or they can print something about
 #     the dictionary. Nothing fancy, unless you fancy it.
 #  4. LITERALLY: Use string literals to put it all together in one statement.
 # 
 # #########################################################################/

print("------------------- CHALLENGE 1 : DEFINE    -------------------")

#Below is a simple example of a dictionary implementaion. 
#-->TODO: Add at least 3 comments to the dictionary below to demonstrate you understand its usage

dictionary = {
    "name": "box",
    "is_empty": True
}
#working with the dictionary:
dictionary["length"] = 12
dictionary["width"] = 8
dictionary["contents"] = ["doll", "toy car", "clothes"]
print(f"{dictionary['name']} is {dictionary['length']} {dictionary['width']}")
dictionary["contents"].append("shoes")
print(f"{dictionary['name']} has {dictionary['contents']}")
print(dictionary)

#-->TODO: Declare a new dictionary and set at least 4 properties to it including: string, boolean, number, list

##################################  MY dictionary ########################### #/
book = {
    "name": "Six of Crows",
    "genre": "Fantasy",
    "release": 2015,
    "characters": ["Kaz", "Inej", "Jesper", "Wylan", "Nina"],
    "tv_show": True
}

########################################################################## #/
print("------------------- CHALLENGE 2 : MODIFY   -------------------")

#-->TODO: Print your dictionary you created above
#print(book)

#-->TODO: Update the dictionary you just created  by adding new properties and values, including list elements, in this section.
book["characters"].append("Matthias")
book["series"] = ["Shadow and Bone", "Crooked Kingdom", "Rule of Wolves"]

#-->TODO: Print your dictionary again and observe changes
print(book)

print("------------------- CHALLENGE 3 : METHODS   -------------------")

#-->TODO: Make a method that will update your dictionary value. It should take in a dictionary and return it modified.
book.pop("tv_show")
get_main = {"characters": "Kaz"}.get("characters")
#-->TODO: Call the method.
print(book)

print("------------------- CHALLENGE 4 : LITERALLY   -------------------") 
#-->TODO: Put it all together using a string literal to tell the story of your dictionary!
print(f"My favorite book is called {book['name']}. It is in the {book['genre']} genre and it was released in {book['release']}. The main characters in this book are {book['characters']} with the book mainly centering on {get_main}. Some other books in this universe are {book['series']}.")