import random

class Situation:
    def __init__(self, name, intro, question, option_1, option_2):
        self.name = name
        self.intro = intro
        self.question = question
        self.option_1 = option_1
        self.option_2 = option_2

    def __repr__(self):
         return (self.name)

    def choice(self):
        global active
        print(self.intro)
        if not self.question:
            return ""
        user_input = input(self.question)
        if user_input in self.option_1:
            if len(self.option_1[user_input]) == 1:
                return self.option_1[user_input][0]
            else:
                risk = random.randint(0, 1)
                return self.option_1[user_input][risk]

        elif user_input in self.option_2:
            if len(self.option_2[user_input]) == 1:
                return self.option_2[user_input][0]
            else:
                risk = random.randint(0, 2)
                return self.option_2[user_input][risk]

        if user_input == "quit":
                print("Try again soon!")
                active = False

        else:
            return self


ending_2 = Situation("OUTSIDE", "YOU WIN! You go outside of the closet and you look out the window in the living room.. You see a tree with a hole that seems like there is a light on the other side. You quickly run outside, go through the hole, and.. Youre home!!", "", "", "")

death_8 = Situation("HOME", "GAME OVER! You lost track of time and sat down to close your eyes out of exhaustion and dehydration and soon die.", "", "", "")

stay_still2 = Situation("CLOSET", "Good choice! The Demagorgan was still nearby so it is best to wait!", "How long do you want to wait for? (5 mins or 15 mins): ", {"5 mins":[ending_2]}, {"15 mins": [death_8]})

death_6 = Situation("LIVING ROOM", "You were in the direct eyesight from the Demagorgan and once he saw you he killed you.. GAME OVER.", "", "", "")

death_4 = Situation("MIKES HOUSE", "GAME OVER. You go to your long time friends Mike's home. This place was always the hang out house for your friend group so the familiarity makes you happy to get home but hat feeligng is soon erased by exhaustion. You soon fall asleep where the Demagorgan finds you and kills you.", "", "", "")

death_5 = Situation("WOODS", "GAME OVER. You stand no chance against this monster and you ultimately pissed him off which led to your early death..","", "", "")

ending_3 = Situation("WOODS", "YOU WIN!Demagorgans hate fire which allows you to successfully and easily defeat the Demagorgan.. You quickly look around after you defeated your enemy and in the distance you see a tree with a hole that seems like there is a light on the other side. You quickly run, go through the hole, and.. you're home!!", "", "", "")

ending_4 = Situation("WOODS", "YOU WIN! You hit the Demagorgan critically in the heart with your gun immediately killing them.. You quickly look around after you defeated your enemy and in the distance you see a tree with a hole that seems like there is a light on the other side. You quickly run, go through the hole, and.. you're home!!", "", "", "")

fight = Situation("WOODS", "While running around looking for something useful you hear footsteps that do not sound human...You're being chased!! You hide behind a large tree but your heavy breathing gives away your location and the Demagorgan soon finds you... BUT you're not dead yet! You're being dragged to what you can assume is it's lair..", "Now is your time to use your weapon! But, keep in mind that this is a risky fight that could lead to your death...(use flamethrower OR use gun): ", {"use flamethrower": [death_5, ending_3]}, {"use gun": [death_5, ending_4]})

now_outside = Situation("OUTSIDE","There was nothing else that was useful so you head outside but you hear a loud sound coming from seemingly behind you.","QUICK YOU NEED TO RUN! Where do you want to go? (mikes house OR woods): ", {"mikes house": [death_4]}, {"woods": [fight]})

armory_room = Situation("ARMORY ROOM", "You enter the armory room and see three possible weapons. The backpack to the left of the weapons can only fit one weapon. Your options are a flamethrower or a gun.", "Which weapon do you choose? (flamethrower or gun): ", {"flamethrower": [now_outside]}, {"gun": [now_outside]})

police_station = Situation("POLICE STATION", "You enter the police and it is empty but full of the filth from the Upside Down. To your left there's an armory room.","Do you want to enter the armory room? (yes OR no): ", {"yes": [armory_room]}, {"no": [death_8]})

look_around = Situation("OUTSIDE", "It is stormy outside and you miss the fake safety of your 'home'. You look around and remember that Mike's house is to the left while the police station is to the right", "Where do you want to go? (mikes house OR police station): ", {"mikes house": [death_4]}, {"police station": [police_station]})

closet = Situation("CLOSET", "You successfully hid from the Demagorgan..", "Do you want to stay inside the closet for a while or go outside now? (go outside OR stay inside): ", {"go outside": [look_around]}, {"stay inside": [stay_still2]})

death_7 = Situation("TABLE", "You were in the direct eyesight from the Demagorgan and once he saw you he killed you.. GAME OVER.", "", "", "")

house_2 = Situation("HOME", "You alerted the demagorgan!! You reach your home but you must quickly hide..","Do you want to hide under the coffee table or the closet? (table OR closet): ", {"table": [death_7]}, {"closet": [closet]})

call = Situation("HOME", "The phone starts to crackle and you can barely hear each other.. INCREASED URGENCY. Your mom starts to worry on the other side since she knows you are on the phone but she can't hear you well.'STAY SAFE AND HIDE WE WILL TRY OUR BEST TO GET YOU OUT' Will's mom says faintly. You start to get anxious of your hiding place since you have been here for what seems like an eternity..", "Do you want to hide somewhere else or stay? (hide OR stay): ", {"hide": [house_2]}, {"stay": [death_8]})

write = Situation("HOME", "They can't see what you write.. it's the Upside Down!", "Do you want to call mom or quit game? (call OR quit): ", {"call": [call]}, "quit")

house_1 = Situation("HOME","You are now home. You feel a bit safer in the familiarity of your house, even though it is covered with dust and goo of the Upside Down. Now, your next mission is to see if you can communicate with anyone back in the normal Hawkins.","Do you want to try and call your house or communicate through writing on the wall with black paint? (call OR write): ", {"call": [call]}, {"write": [write]})

death_1 = Situation("WOODS", "You try to run and you alert the demagorgan of where you are. You are too far from your wooden house at this point and have no here to hide. The demagorgan finds and you die.\nNow just shutting down...", "","", "")

death_2 = Situation("WOODEN HOUSE","GAME OVER. You flicker the light twice by turning the light bulb until it turns off and back to its original place so the light turns back on twice. URGENCY DECREASED. Your mom thinks you are safe so your friends and family start to take their time to save you. Little do they know, there's no drinkable water in the Upside Down.. You soon die because of waiting too long.", "","", "")

death_3 = Situation("WOODEN HOUSE", "GAME OVER. You hear footsteps that soon mulitply and sound like a herd of unknown beings coming towards your house.. You die due to a Demagorgan invasion to your hiding spot..", "", "", "")

ending_1 = Situation("DEMAGORGAN LAIR", "YOU WIN! You are taken to the Demagorgans lair where you are soon hooked up to weird slimy vines.. You slowly lose consciousness.. BUT YOU SEE A LIGHT! Its your mom and Hopper!! You're saved.", "", "", "")

look_woods = Situation("WOODS", "While running around looking for something useful you hear footsteps that do not sound human...You're being chased!! You hide behind a large tree but your heavy breathing gives away your location and the Demagorgan soon finds you... BUT you're not dead yet! You're being dragged to what you can assume is it's lair..\n", "You can use the little energy you have to risk it and fight back or stay still.. (fight back OR stay still): ", {"fight back": [death_5]}, {"stay still": [ending_1]})

leave_home = Situation("WOODS","After you get out you soon turn back and see your wooden house explode as the Demagorgan and its army invade it.. Good move! Now you must move quick..","Do you want to look around the WOODS or look for a new hiding spot? (woods OR new spot): ", {"woods": [look_woods]}, {"new spot":[death_4]})

no_mom = Situation("WOODEN HOUSE", "You flicker the light once by turning the light bulb until it turns off and back to its original place so the light turns back on. URGENCY INCREASED. This makes Will's mom worry more and increases their urgency in wanting to get you out of here. 'STAY SAFE AND HIDE WE WILL TRY OUR BEST TO GET YOU OUT' Will's mom says. You start to get anxious of your hiding place since you have been here for what seems like an eternity..","Do you want to leave the WOODEN HOUSE or stay? (leave OR stay): ", {"leave":[leave_home]}, {"stay": [death_3]})

hang = Situation("WOODEN HOUSE", "You have decided to listen to Elevens advice and hang in there in the wooden house. You start to lose hope when suddenly you see the lightbulb in the room flickering. You slowly stand and go near the light and hear a small voice. It's your mom! Shes communicating through the lights??..'WILL! ARE YOU OKAY? FLICKER ONCE FOR YES, TWICE FOR NO'","What do you want to respond? (yes OR no): ", {"yes": [death_2]}, {"no": [no_mom]})

wooden_house = Situation("WOODEN HOUSE", "You go to the wooden house and lay down silently on the sleeping bag in the corner.. after what seems like hours you feel a hand resting on yours. It's Eleven, your friend with location tracking visiting you in a hologram like form. She tells you to hang in there, to not move, and that they are close to finding you... But, after seemingly hours pass in your wooden house, you start to get restless.", "Do you run or hang in there? (run OR hang): ", {"run": [death_1]}, {"hang": [hang]})

bike = Situation("WOODS", "You reach the woods and look around.","You remember that your wooden play house is to the right .. but should you try to run as far as you can and see what you find instead? (wooden house OR run): ", {"wooden house": [wooden_house]}, {"run": [death_1]}, )

introduction = Situation("WELCOME", "                                      W\u0332E\u0332L\u0332C\u0332O\u0332M\u0332E\u0332 \u0332t\u0332o\u0332 \u0332t\u0332h\u0332e\u0332 \u0332U\u0332P\u0332S\u0332I\u0332D\u0332E\u0332 \u0332D\u0332O\u0332W\u0332N\u0332.\u0332\nYou are playing the role of WILL BYERS and your family and friends are trying to rescue you.\nYou landed in THE UPSIDE DOWN, a place that is identical to your home Hawkins but is full of monsters lurking, while biking home one dark night alone. \nYou were chased by a monster called the demogorgon into this place and now you desperately want to get out. You will have two options for each situation and one will likely lead to death while the other will lead to success so CHOOSE WISELY. If you want to end the game, input 'quit'.\nYou stand in the middle of a nightmare version of your childhood town and you don't know what to do. You see your bike on the ground in front of you but you also know that the woods are a 7 minute distance from your house. You also see your house in the distance...", "Should you take a risk and run home or take your bike to the woods? (home OR bike): ", {"home": [house_1, house_2]}, {"bike": [bike]})

active = True
location = introduction

while active:
    location = location.choice()
    print("\n",location)
    if location == "":
        active = False
        print("Now shutting down... The UPSIDE DOWN will miss you")