# Imports
import random
#import time
#import sys
from browser import document, html

# Accepted answers
case_answer = ['yes', 'yea', 'sure','ya']
case_close = ['no', 'nope', 'nah','na']

def gloves (g):
    if g > 1 and g <= 2:
        return("Bloodhound Gloves | Snakebite")
    elif g > 2 and g <= 3:
        return("Bloodhound Gloves | Charred")
    elif g > 3 and g <= 4:
        return("Bloodhound Gloves | Bronzed")
    elif g > 4 and g <= 5:
        return("Bloodhound Gloves | Guerrilla")
    elif g > 5 and g <= 6:
        return("Driver Gloves | Crimson Weave")
    elif g > 6 and g <= 7:
        return("Driver Gloves | Lunar Weave")
    elif g > 7 and g <= 8:
        return("Driver Gloves | Diamondback")
    elif g > 8 and g <= 9:
        return("Driver Gloves | Convoy")
    elif g > 9 and g <= 10:
        return("Hand Wraps | Leather")
    elif g > 10 and g <= 11:
        return("Hand Wraps | Slaughter")
    elif g > 11 and g <= 12:
        return("Hand Wraps | Badlands")
    elif g > 12 and g <= 13:
        return("Hand Wraps | Spruce DDPAT")
    elif g > 13 and g <= 14:
        return("Moto Gloves | Spearmint")
    elif g > 14 and g <= 15:
        return("Moto Gloves | Cool Mint")
    elif g > 15 and g <= 16:
        return("Moto Gloves | Boom!")
    elif g > 16 and g <= 17:
        return("Moto Gloves | Eclipse")
    elif g > 17 and g <= 18:
        return("Specialist Gloves | Crimson Kimono")
    elif g > 18 and g <= 19:
        return("Specialist Gloves | Emerald Web")
    elif g > 19 and g <= 20:
        return("Specialist Gloves | Foundation")
    elif g > 20 and g <= 21:
        return("Specialist Gloves | Forest DDPAT")
    elif g > 21 and g <= 22:
        return("Sport Gloves | Pandora's Box")
    elif g > 22 and g <= 23:
        return("Sport Gloves | Superconductor")
    elif g > 23 and g <= 24:
        return("Sport Gloves | Hedge Maze")
    else:
        return("Sport Gloves | Arid")

def stattrak(z):
    if z <= 1:
        return ("Stattrak")
    else:
        return ('')

def roll(x,g):
    if x <= 1:
        return(gloves())
    elif x > 1 and x <= 3:
        return("AWP | Oni Taiji")
    elif x > 3 and x <= 5:
        return("Five-SeveN | Hyper Beast")
    elif x > 5 and x <= 9:
        return("M4A4 | Hellfire")
    elif x > 9 and x <= 13:
        return("Galil AR | Sugar Rush")
    elif x > 13 and x <= 17:
        return("Dual Berettas | Cobra Strike")
    elif x > 17 and x <= 21:
        return("AK-47 | Orbit MK01")
    elif x > 21 and x <= 25:
        return("SSG 08 | Death's Head")
    elif x > 25 and x <= 29:
        return("P90 | Death Grip")
    elif x > 29 and x <= 33:
        return("P2000 | Woodsman")
    elif x > 33 and x <= 37:
        return("P250 | Red Rock")
    elif x > 37 and x <= 46:
        return("USP-S | Blueprint")
    elif x > 46 and x <= 55:
        return("M4A1-S | Briefing")
    elif x > 55 and x <= 64:
        return("Tec-9 | Cut Out")
    elif x > 64 and x <= 73:
        return("UMP-45 | Metal Flowers")
    elif x > 73 and x <= 82:
        return("FAMAS | Macabre")
    elif x > 82 and x <= 91:
        return("MAG-7 | Hard Water")
    else:
        return("MAC-10 | Aloha")


def wear(y):
    print("")
    if y <=1:
        return("(Factory New)")
    elif y <=2:
        return("(Minimal Wear)")
    elif y <=3:
        return("(Field Tested)")
    elif y <=4:
        return("(Well-Worn)")
    else:
        return("(Battle-Scarred)")

def everything():
        # Create random numbers
        x = random.randint(1, 100)
        y = random.randint(1,5)
        z = random.randint(1,4)
        g = random.randint(1,25)
        print ("Unboxing...")
        # time.sleep(1)
        if x == 1:
           print ("You've Unboxed: " + roll(x,g) + " " + wear(y))
        else:
            print ("You've Unboxed: " + stattrak(z) + " " + roll() + " " + wear())
        print("")


def start():
    print ("Welcome, Would You Like to Open a Case?")
    answer_one = str(input("Welcome, Would You Like to Open a Case?"))
    if answer_one in case_answer:
        everything()
    elif answer_one in case_close:
        print ("GoodBye, Come Back Soon!")
        # time.sleep(1)
        # sys.exit()
    else:
        print ("Sorry, I didn't Understand What You Meant")
        print()
        # time.sleep(1)
        start()

# Prints out text
def print(*args):
    # Add a new line
    document["output"] <= html.BR()

    # No space for first text piece
    first = True
    for arg in args:
        if first:
            first = False
        else:
            document["output"] <= " "
        document["output"] <= arg

# Print out the integer results
print (z, x, y)

# Bind click listener to button
document['test'].bind('click', start)