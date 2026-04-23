#Defining variables
window = False
door = False
investigate = False
hasphoto = False
r = True
returnnum = 0

#Title n stuff
print("INTROSPECTIVE")
print()

#Intro exposition

def intro():
    print()
    print("You wake up on a bed, staring at the ceiling of an unfamiliar room.")
    print("Laying there for a moment, you try and remember how you ended up here.")
    print("...nothing, no matter how long you think, you can't remember anything.")
    print("You sit up and glance around for a moment, noticing a window close on your left, and a door off to the right.")
    print()
    print("What do you do?")
    print()
    print("- Get up")
    print("- Lie back down")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "get up":
        getup()
    elif  choice == "lie back down":
        liedown()
    else:
      print("I don't understand")
      intro()


#The many different decisions and diologues that can occur
def getup():
    global window
    global door
    global investigate
    print()
    print("You stand up from the bed.")
    print("As you do, you feel a faint bit of regret.")
    print("You hadn't noticed it before, but the bed was quite comfortable,")
    print("and in it's absence, you feel... cold, and out of place.")
    print()
    print("What do you do?")
    print()
    print("- Open the window")
    print("- Open the door")
    print("- Look at the room")
    print("- Go back to bed")


    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "open the window":
        window = True
        windowR1()
    elif  choice == "open the door":
        door = True
        doorR1()
    elif  choice == "look at the room":
        investigate = True
        investigateR1()
    elif  choice == "go back to bed":
        backtobedR1()
    else:
      print("I don't understand")
      getup()


def liedown():
    print()
    print("You lie back down.")
    print("The bed is confortable.")
    print("You feel relaxed, and... tired.")
    print("Your eyes begin to close")
    print("As your head falls to the right, you see her face, one last time.")
    print("Your eyes shut.")
    print("You do not wake.")
    print("You didn't keep your promise")
    print()
    print("End")


def backtobedR1():
    print()
    print("You get back into bed.")
    print("The relief is instant, and yet, you're still cold.")
    print("You feel relaxed, and... tired.")
    print("Your eyes begin to close")
    if hasphoto == False:
        print("As your head falls to the right, you see her face, one last time.")
        print("Your eyes shut.")
        print("You do not wake.")
        print("You didn't keep your promise")
        print()
        print("End")
    if hasphoto == True:
        print("As your head falls to the right, you see... nothing.")
        print("Your eyes shut.")
        print("You open them.")
        print("You see the photo of the two young women on the table beside you.")
        print("You finally recognise yourself.")
    

def doorR1():
    print()
    print("WIP")
    roomreturn()
    

def windowR1():
    print()
    print("As you go to open the window, you notice that despite the")
    print("light streaming into the room, the outside is dark and unrecognizable.")
    print("It's faint, but you can barely make out distorded figures, standing there, eerily still.")
    print("Fear slowly engulfs you as you stare into the darkness.")
    print()
    print("What do you do?")
    print()
    print("- Open the window")
    print("- Return")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "open the window":
        windowR2()
    elif  choice == "return":
        roomreturn()
    else:
      print("I don't understand")
      windowR1()


def windowR2():
    print()
    print("Your hands shake as you grasp the bottom.")
    print("You freeze just before lifting up.")
    print("Should you really do this?")
    print()
    print("- Open the window")
    print("- Return")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "open the window":
        windowR3()
    elif  choice == "return":
        roomreturn()
    else:
      print("I don't understand")
      windowR2()

def windowR3():
    print()
    print("You open the window.")
    print("Overwhealming fear paralyzes your body as the darkness drags you outside.")
    print("You hit the ground tumbling for a moment before landing on your back.")
    print("The figures slowly surround you as you lay there, unable to move.")
    print("Your eyes dart between them as what seems like oens pass in those few moments.")
    print("One by one, slowly begin to smile, then laugh.")
    print("It pierces your ears like nails, and pain erupts in your head.")
    print()
    print("- It hurts")
    #Taking input
    choice = input("> ").lower()
    print()
    print("You scream")
    print()
    print("- It hurts")
    #Taking input
    choice = input("> ").lower()
    print()
    print("You scream")
    print()
    print("- It hurts")
    #Taking input
    choice = input("> ").lower()
    print()
    print("You scream")
    print()
    print("- It hurts")
    #Taking input
    choice = input("> ").lower()
    print()
    print("You scream")
    print()
    print("- It hurts")
    #Taking input
    choice = input("> ").lower()
    print()
    print("You scream")
    print()
    print("- It hurts")
    #Taking input
    choice = input("> ").lower()
    print()
    print("You scream")
    print()
    print("...your throat becomes ragged from your screams.")
    print("You feel your body weaken.")
    print("Your eyes begin close the figures fade from your sight.")
    print("As your head falls to the right, you see her face, one last time.")
    print("Your eyes shut.")
    print("You do not wake.")
    print("You didn't keep your promise")
    print()
    print("End")



def investigateR1():
    print()
    print("You take a longer look around the room.")
    print("Even so, nothing in particular stands out to you.")
    print("It's sparsely furnished, with a small bedside table on the right, a dresser, and a standing mirror.")
    print()
    print("What do you do?")
    print()
    print("- Look at the furniture")
    print("- Return")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "look at the furniture":
        investigateR2()
    elif  choice == "return":
        roomreturn()
    else:
      print("I don't understand")
      investigateR1()



def investigateR2():
    print()
    print("Which piece of furniture should you look at first?")
    print()
    #print("- The trunk")
    print("- The dresser")
    print("- The mirror")
    print("- Return")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "the trunk":
        trunkR1()
    elif  choice == "the dresser":
        dresserR1()
    elif  choice == "the mirror":
        mirrorR1()
    elif  choice == "return":
        roomreturn()
    elif  choice == "the table":
        bedsidetableR1()
    elif  choice == "the small table":
        bedsidetableR1()
    elif  choice == "small bedside table":
        bedsidetableR1()
    elif  choice == "small table":
        bedsidetableR1()
    else:
      print("I don't understand")
      investigateR2()


def trunkR1():
    print()
    print("WIP")


def dresserR1():
    print()
    print("WIP")


def mirrorR1():
    print()
    print("You take a closer look at the mirror.")
    print("It's tall ")


def bedsidetableR1():
    print()
    print("You'd fogotten about the table for a moment there. Strange.")
    print("Looking closer, you find nothing of note except for a")
    print("small and uniteresting framed photograh.")
    print()
    print("What do you do?")
    print()
    print("- Return")
    print("- Look at the photo")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "look at the photo":
        bedsidetableR2()
    elif  choice == "return":
        roomreturn()
    else:
      print("I don't understand")
      bedsidetableR1()


def bedsidetableR2():
    print()
    print("You shouldn't look at the photo.")
    print()
    print("What do you do?")
    print()
    print("- Return")
    print("- Return")
    print("- Look at the photo")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "look at the photo":
        bedsidetableR3()
    elif  choice == "return":
        roomreturn()
    else:
      print("I don't understand")
      bedsidetableR2()


def bedsidetableR3():
    print()
    print("Don't. It's too late now.")
    print()
    print("What do you do?")
    print()
    print("- Return")
    print("- Return")
    print("- Return")
    print("- Look at the photo")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "look at the photo":
        bedsidetableR4()
    elif  choice == "return":
        roomreturn()
    else:
      print("I don't understand")
      bedsidetableR3()


def bedsidetableR4():
    print()
    print("...")
    print()
    print("- Return")
    print("- ̶L̶o̶o̶k̶ ̶a̶t̶ ̶t̶h̶e̶ ̶p̶h̶o̶t̶o̶")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "look at the photo":
        bedsidetableR5()
    elif  choice == "return":
        roomreturn()
    else:
      print("I don't understand")
      bedsidetableR4()


def bedsidetableR5():
    print()
    print("You take a closer look at the photo.")
    print("In it, you see two young women standing next to each other, smiling.")
    print("They look happy.")
    print()
    print("What do you do?")
    print()
    print("Take the photo")
    print("Return")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "take the photo":
        bedsidetableR6()
    elif  choice == "return":
        roomreturn()
    else:
      print("I don't understand")
      bedsidetableR5()


def bedsidetableR6():
    global hasphoto
    print()
    print("You take the photo.")
    print("It feels almost... warm, in your hands.")
    print("You place it in your pocket, and the feeling fades.")
    hasphoto = True
    print()
    roomreturn()


def roomreturn():
    global returnnum
    global window
    global door
    global investigate
    print()
    print("You return back to the center of the room.")
    print(returnnum)
    if returnnum == 0:
        print("You feel cold, and wish you had just stayed in bed.")
    if returnnum == 1:
        print("You feel cold, and wish you had never woken up.")
    if returnnum == 2:
        print("You feel cold. Why keep trying?")
    if returnnum >= 3:
        print("You feel cold.")
    returnnum += 1
    print("What do you do?")
    print()
    if window == False:
        print("- Open the window")
    else:
        print("- Go back to bed")
    if door == False:
        print("- Open the door")
    else:
        print("- Go back to bed")
    if investigate == False:
        print("- Investigate the furniture")
    else:
        print("- Go back to bed")
    print("- Go back to bed")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "open the window":
        window = True
        windowR1()
    elif  choice == "open the door":
        door = True
        doorR1()
    elif  choice == "go back to bed":
        backtobedR1()
    elif  choice == "investigate the furniture":
        investigate = True
        investigateR1()
    else:
      print("I don't understand")
      roomreturn()


def retry():
    global r
    print()
    print()
    print("Do you want to play again?")
    print("Yes, or no.")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "yes":
        intro()
    if  choice == "no":
        print()
        r = False
        return r
    else:
      print("I don't understand")
      retry()


#Calling the intro function to start the game
intro()
while r == True:
    retry()
#Defining variables
window = False
door = False
investigate = False
hasphoto = False
r = True
returnnum = 0

#Title n stuff
print("INTROSPECTIVE")
print()

#Intro exposition

def intro():
    print()
    print("You wake up on a bed, staring at the ceiling of an unfamiliar room.")
    print("Laying there for a moment, you try and remember how you ended up here.")
    print("...nothing, no matter how long you think, you can't remember anything.")
    print("You sit up and glance around for a moment, noticing a window close on your left, and a door off to the right.")
    print()
    print("What do you do?")
    print()
    print("- Get up")
    print("- Lie back down")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "get up":
        getup()
    elif  choice == "lie back down":
        liedown()
    else:
      print("I don't understand")
      intro()


#The many different decisions and diologues that can occur
def getup():
    global window
    global door
    global investigate
    print()
    print("You stand up from the bed.")
    print("As you do, you feel a faint bit of regret.")
    print("You hadn't noticed it before, but the bed was quite comfortable,")
    print("and in it's absence, you feel... cold, and out of place.")
    print()
    print("What do you do?")
    print()
    print("- Open the window")
    print("- Open the door")
    print("- Look at the room")
    print("- Go back to bed")


    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "open the window":
        window = True
        windowR1()
    elif  choice == "open the door":
        door = True
        doorR1()
    elif  choice == "look at the room":
        investigate = True
        investigateR1()
    elif  choice == "go back to bed":
        backtobedR1()
    else:
      print("I don't understand")
      getup()


def liedown():
    print()
    print("You lie back down.")
    print("The bed is confortable.")
    print("You feel relaxed, and... tired.")
    print("Your eyes begin to close")
    print("As your head falls to the right, you see her face, one last time.")
    print("Your eyes shut.")
    print("You do not wake.")
    print("You didn't keep your promise")
    print()
    print("End")


def backtobedR1():
    print()
    print("You get back into bed.")
    print("The relief is instant, and yet, you're still cold.")
    print("You feel relaxed, and... tired.")
    print("Your eyes begin to close")
    if hasphoto == False:
        print("As your head falls to the right, you see her face, one last time.")
        print("Your eyes shut.")
        print("You do not wake.")
        print("You didn't keep your promise")
        print()
        print("End")
    if hasphoto == True:
        print("As your head falls to the right, you see... nothing.")
        print("Your eyes shut.")
        print("You open them.")
        print("You see the photo of the two young women on the table beside you.")
        print("You finally recognise yourself.")
    

def doorR1():
    print()
    print("WIP")
    roomreturn()
    

def windowR1():
    print()
    print("As you go to open the window, you notice that despite the")
    print("light streaming into the room, the outside is dark and unrecognizable.")
    print("It's faint, but you can barely make out distorded figures, standing there, eerily still.")
    print("Fear slowly engulfs you as you stare into the darkness.")
    print()
    print("What do you do?")
    print()
    print("- Open the window")
    print("- Return")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "open the window":
        windowR2()
    elif  choice == "return":
        roomreturn()
    else:
      print("I don't understand")
      windowR1()


def windowR2():
    print()
    print("Your hands shake as you grasp the bottom.")
    print("You freeze just before lifting up.")
    print("Should you really do this?")
    print()
    print("- Open the window")
    print("- Return")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "open the window":
        windowR3()
    elif  choice == "return":
        roomreturn()
    else:
      print("I don't understand")
      windowR2()

def windowR3():
    print()
    print("You open the window.")
    print("Overwhealming fear paralyzes your body as the darkness drags you outside.")
    print("You hit the ground tumbling for a moment before landing on your back.")
    print("The figures slowly surround you as you lay there, unable to move.")
    print("Your eyes dart between them as what seems like oens pass in those few moments.")
    print("One by one, slowly begin to smile, then laugh.")
    print("It pierces your ears like nails, and pain erupts in your head.")
    print("It hurts")
    #Taking input
    choice = input("> ").lower()
    print()
    print("You scream")
    print()
    print("It hurts")
    #Taking input
    choice = input("> ").lower()
    print()
    print("You scream")
    print()
    print("It hurts")
    #Taking input
    choice = input("> ").lower()
    print()
    print("You scream")
    print()
    print("It hurts")
    #Taking input
    choice = input("> ").lower()
    print()
    print("You scream")
    print()
    print("It hurts")
    #Taking input
    choice = input("> ").lower()
    print()
    print("You scream")
    print()
    print("It hurts")
    #Taking input
    choice = input("> ").lower()
    print()
    print("You scream")
    print()
    print("...your throat becomes ragged from your wails.")
    print("You feel your body weaken.")
    print("Your eyes begin close the figures fade from your sight.")
    print("As your head falls to the right, you see her face, one last time.")
    print("Your eyes shut.")
    print("You do not wake.")
    print("You didn't keep your promise")
    print()
    print("End")



def investigateR1():
    print()
    print("You take a longer look around the room.")
    print("Even so, nothing in particular stands out to you.")
    print("It's sparsely furnished, with a small bedside table on the right, a dresser, and a standing mirror.")
    print()
    print("What do you do?")
    print()
    print("- Look at the furniture")
    print("- Return")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "look at the furniture":
        investigateR2()
    elif  choice == "return":
        roomreturn()
    else:
      print("I don't understand")
      investigateR1()



def investigateR2():
    print()
    print("Which piece of furniture should you look at first?")
    print()
    #print("- The trunk")
    print("- The dresser")
    print("- The mirror")
    print("- Return")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "the trunk":
        trunkR1()
    elif  choice == "the dresser":
        dresserR1()
    elif  choice == "the mirror":
        mirrorR1()
    elif  choice == "return":
        roomreturn()
    elif  choice == "the table":
        bedsidetableR1()
    elif  choice == "the small table":
        bedsidetableR1()
    elif  choice == "small bedside table":
        bedsidetableR1()
    elif  choice == "small table":
        bedsidetableR1()
    else:
      print("I don't understand")
      investigateR2()


def trunkR1():
    print()
    print("WIP")


def dresserR1():
    print()
    print("WIP")


def mirrorR1():
    print()
    print("You take a closer look at the mirror.")
    print("It's tall ")


def bedsidetableR1():
    print()
    print("You'd fogotten about the table for a moment there. Strange.")
    print("Looking closer, you find nothing of note except for a")
    print("small and uniteresting framed photograh.")
    print()
    print("What do you do?")
    print()
    print("- Return")
    print("- Look at the photo")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "look at the photo":
        bedsidetableR2()
    elif  choice == "return":
        roomreturn()
    else:
      print("I don't understand")
      bedsidetableR1()


def bedsidetableR2():
    print()
    print("You shouldn't look at the photo.")
    print()
    print("What do you do?")
    print()
    print("- Return")
    print("- Return")
    print("- Look at the photo")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "look at the photo":
        bedsidetableR3()
    elif  choice == "return":
        roomreturn()
    else:
      print("I don't understand")
      bedsidetableR2()


def bedsidetableR3():
    print()
    print("Don't. It's too late now.")
    print()
    print("What do you do?")
    print()
    print("- Return")
    print("- Return")
    print("- Return")
    print("- Look at the photo")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "look at the photo":
        bedsidetableR4()
    elif  choice == "return":
        roomreturn()
    else:
      print("I don't understand")
      bedsidetableR3()


def bedsidetableR4():
    print()
    print("...")
    print()
    print("- Return")
    print("- ̶L̶o̶o̶k̶ ̶a̶t̶ ̶t̶h̶e̶ ̶p̶h̶o̶t̶o̶")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "look at the photo":
        bedsidetableR5()
    elif  choice == "return":
        roomreturn()
    else:
      print("I don't understand")
      bedsidetableR4()


def bedsidetableR5():
    print()
    print("You take a closer look at the photo.")
    print("In it, you see two young women standing next to each other, smiling.")
    print("They look happy.")
    print()
    print("What do you do?")
    print()
    print("Take the photo")
    print("Return")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "take the photo":
        bedsidetableR6()
    elif  choice == "return":
        roomreturn()
    else:
      print("I don't understand")
      bedsidetableR5()


def bedsidetableR6():
    global hasphoto
    print()
    print("You take the photo.")
    print("It feels almost... warm, in your hands.")
    print("You place it in your pocket, and the feeling fades.")
    hasphoto = True
    print()
    roomreturn()


def roomreturn():
    global returnnum
    global window
    global door
    global investigate
    print()
    print("You return back to the center of the room.")
    print(returnnum)
    if returnnum == 0:
        print("You feel cold, and wish you had just stayed in bed.")
    if returnnum == 1:
        print("You feel cold, and wish you had never woken up.")
    if returnnum == 2:
        print("You feel cold. Why keep trying?")
    if returnnum >= 3:
        print("You feel cold.")
    returnnum += 1
    print("What do you do?")
    print()
    if window == False:
        print("- Open the window")
    else:
        print("- Go back to bed")
    if door == False:
        print("- Open the door")
    else:
        print("- Go back to bed")
    if investigate == False:
        print("- Investigate the furniture")
    else:
        print("- Go back to bed")
    print("- Go back to bed")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "open the window":
        window = True
        windowR1()
    elif  choice == "open the door":
        door = True
        doorR1()
    elif  choice == "go back to bed":
        backtobedR1()
    elif  choice == "investigate the furniture":
        investigate = True
        investigateR1()
    else:
      print("I don't understand")
      roomreturn()


def retry():
    global r
    print()
    print()
    print("Do you want to play again?")
    print("Yes, or no.")

    #Taking input
    choice = input("> ").lower()
    #Deciding direction
    if  choice == "yes":
        intro()
    if  choice == "no":
        print()
        r = False
        return r
    else:
      print("I don't understand")
      retry()


#Calling the intro function to start the game
intro()
while r == True:
    retry()
