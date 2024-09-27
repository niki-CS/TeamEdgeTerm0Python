import random

# -------------------------------------------- 

	# You've just learned about variables, conditionals.
	# Just from knowing those two topics, you can do so much!
	
	# Let's try to make a simple program that responds to the user.
	# We're going to recreate the Magic 8 Ball!!!
			
			# Never heard of it? That's ok!

					# You got this!

  # -------------------------------------------- 

	# How a Magic 8 Ball Works:

	# The user asks a question and vigoriously shakes the ball. 
	# Then the ball will respond with one of twenty responses, chosen at random. 

	# That's pretty simple right?

 # -------------------------------------------- 

	# Part 1: 
	# Print instructions on the screen and 
	# prompt the user to ask a question

  # --------------------------------------------

print("How a Magic 8 Ball works:\n") 
print("The user asks a question and vigoriously shakes the ball then the ball will respond with one of twenty responses.\n")
print("Pretty simple right?\n")
question = input("What is your question?: ")

# -------------------------------------------- 

	# Part 2: Next, we need to randomly select a response from 20 options.

	# Randomly select a number from 0 - 19
	# Use that to select from the following responses:
		# 0 - It is certain.
		# 1 - It is decidedly so.
		# 2 - Without a doubt.
		# 3 - Yes - definitely.
		# 4 - You may rely on it.
		# 5 - As I see it, yes.
		# 6 - Most likely.
		# 7 - Outlook good.
		# 8 - Yes.
		# 9 - Signs point to yes.
		# 10 - Reply hazy, try again.
		# 11 - Ask again later.
		# 12 - Better not tell you now.
		# 13 - Cannot predict now.
		# 14 - Concentrate and ask again.
		# 15 - Don't count on it.
		# 16 - My reply is no.
		# 17 - My sources say no.
		# 18 - Outlook not so good.
		# 19 - Very doubtful.

	# Look up random.rand_int to see how you can use it to select a random number.

  # -------------------------------------------- 

answer = random.randint(0, 20)

if answer == 0:
	print("It is certain.")
elif answer == 1:
	print("It is decidedly so.")
elif answer == 2:
	print("Without a doubt.")
elif answer == 3:
	print("Yes - definitely.")
elif answer == 4:
	print("You may rely on it.")
elif answer == 5:
	print("As I see it, yes.")
elif answer == 6:
	print("Most likely.")
elif answer == 7:
	print("Outlook good.")
elif answer == 8:
	print("Yes.")
elif answer == 9:
	print("Signs point to yes.")
elif answer == 10:
	print("Reply hazy, try again.")
elif answer == 11:
	print("Ask again later.")
elif answer == 12:
	print("Better not tell you now.")
elif answer == 13:
	print("Cannot predict now.")
elif answer == 14:
	print("Concentrate and ask again.")
elif answer == 15:
	print("Don't count on it.")
elif answer == 16:
	print("My reply is no.")
elif answer == 17:
	print("My sources say no.")
elif answer == 18:
	print("Outlook not so good.")
elif answer == 19:
	print("Very doubtful.")

# -------------------------------------------- 

	# Part 3: Customize it!

	# Select your own theme and use case and modify your code!
	
# -------------------------------------------- 

# horoscope = input("What is your horoscope? ")
# if horoscope == "Capricorn":
# 	print("You are tenacious, pragmatic, a stickler for rules, and ferocious ")
# elif horoscope == "Aquarius":
# 	print("You are assertive, creative, impulsive, and a loner")
# elif horoscope == "Pisces":
# 	print("You are adventurous, compassionate, anxious, and needy")
# elif horoscope == "Aries":
# 	print("You are confident, fiery, impatient, and honest.")
# elif horoscope == "Taurus":
# 	print("You are loyal, persistent, lazy, and bullheaded.")
# elif horoscope == "Gemini":
# 	print("You are intelligent ,sociable, superficial, and indecisive.")
# elif horoscope == "Cancer":
# 	print("You are charitable, loyal, blunt, and crabby.")
# elif horoscope == "Leo":
# 	print("You are proud, brave, arrogant, and competitive.")
# elif horoscope == "Virgo":
# 	print("You are diligent, organized, critical, and perfectionists.")
# elif horoscope == "Libra":
# 	print("You are clever, extroverted, social and vain.")
# elif horoscope == "Scorpio":
# 	print("You are magnetic, envious, and a thrill-seeker.")
# elif horoscope == "Sagittarius":
# 	print("You are indpendent, adventurous, blunt, and impatient.")







