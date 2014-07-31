print("OAK: Zzz... Hm? Wha...? You woke me up! What hour is it?")
def poketime():
    time = raw_input("Enter the hour of day:  ")
    if str(time).lower() == "12am":
        print ("OAK: WTF, it's the middle of the night!?  Kids these days smh.")
    elif str(time).lower() == "1am":
        print("OAK: WTF, it's the middle of the night!?  Kids these days smh.")
    elif str(time).lower() == "2am":
        print ("oAK: WTF, it's the middle of the night!?  Kids these days smh.")
    elif str(time).lower() == "3am":
        print ("OAK: WTF, it's the middle of the night!?  Kids these days smh.")
    elif str(time).lower() == "4am":
        print ("OAK: Holy hell it's early, why aren't you asleep?")
    elif str(time).lower() == "5am":
        print ("OAK: Holy hell it's early, why aren't you asleep?")
    elif str(time).lower() == "6am":
        print ("OAK: Holy hell it's early, why aren't you asleep?")
    elif str(time).lower() == "7am":
        print ("OAK: Holy hell it's early, why aren't you asleep?")
    elif str(time).lower() == "8am":
        print ("OAK: My alarm clock was just about to go off, could you nOT WAIT FIVE MINUTES?")
    elif str(time).lower() == "9am":
        
        print ("OAK: Hot damn, I overslept! wait...it's my day off!")
    elif str(time).lower() == "10am":
        print ("OAK: Hot damn, I overslept! wait...it's my day off!")
    elif str(time).lower() == "11am":
        print ("OAK: Hot damn, I overslept! wait...it's my day off!")
    elif str(time).lower() == "12pm":
        print ("OAK: Hot damn, I overslept! wait...it's my day off!")
    elif str(time).lower() == "1pm":
        print ("OAK: WHOA I SLEPT LATE! Must have hit the bottle a little hard last night amirite lol")
    elif str(time).lower() == "2pm":
        print ("OAK: WHOA I SLEPT LATE! Must have hit the bottle a little hard last night amirite lol")
    elif str(time).lower() == "3pm":
        print ("OAK: WHOA I SLEPT LATE! Must have hit the bottle a little hard last night amirite lol")
    elif str(time).lower() == "4pm":
        print ("OAK: WHOA I SLEPT LATE! Must have hit the bottle a little hard last night amirite lol")
    elif str(time).lower() == "5pm":
        print ("OAK: WHOA I SLEPT LATE! Must have hit the bottle a little hard last night amirite lol")
    elif str(time).lower() == "6pm":
        print ("OAK: I just got off work, can't I have a beer first?")
    elif str(time).lower() == "7pm":
        print ("OAK: I just got off work, can't I have a beer first?")
    elif str(time).lower() == "8pm":
        print ("OAK: I just got off work, can't I have a beer first?")
    elif str(time).lower() == "9pm":
        print ("OAK: Come on kid, I was just about to go to bed :(")
    elif str(time).lower() == "10pm":
        print ("OAK: Come on kid, I was just about to go to bed :(")
    elif str(time).lower() == "11pm":
        print ("OAK: Come on kid, I was just about to go to bed :(")
    else:
        print ("OAK: Speak up kid, I can't hear you! (example: 11am)")
        return poketime()
poketime()
raw_input("OAK: ....ahh whatever, I guess now's as good a time as any...")
raw_input("OAK: Welcom to the world of POKEMON! I'm Professor Oakafealus Plastermeecus, but my homies just call me OAK.")
raw_input("OAK: This world is inhabited by creatures that we call Pokemon. They live to serve us and our every need because science has allowed us to imprison them in machines for our own leisurely use!")
raw_input("OAK: Some people play with Pokemon and unnaturally keep them as pets.")
raw_input("OAK: Some use them to brutally beat other Pokemon to within inches of their lives!")
raw_input("OAK: We don't know everything about Pokemon yet.")
raw_input("OAK: There are still many mysteries to solve.  Did you know we've studied Pokemon for hundreds of years and never saw one lay an egg until a few years ago?")
raw_input("OAK: That's why I'm terrible at my job!")
raw_input("OAK: Now I know you've lived next door to me for ten years now buuuuuuut...")
def pokegender():
    gender = raw_input("r u a boy or a girl...?: ")
    if str(gender).lower() == "boy":
        raw_input("OAK: really?--I mean...okay.")
    elif str(gender).lower() == "girl":
        raw_input("OAK: oh...cuuuute...")
    else:
        print("OAK: I'm going to be honest, Pat, It's not obvious, just tell me. (Enter 'boy' or 'girl')")
        return pokegender()
pokegender()
player = raw_input("OAK: And....what was your name again?: ")
if str(player).lower() == "ash":
    raw_input("OAK: Wow, how original -__-")
else:
    raw_input("OAK: In my defense that's a real forgettable name...")
raw_input("OAK: ANYWAY...{}, are you ready? Your very own Pokemon Journey is about to unfold!".format(player))
raw_input("OAK: Even though you are only ten, you get to go out into the wild and live off of berries and nuts while using pokemon to terrorize weaker trainers into giving you money to buy food and rent!")
raw_input("OAK: But as long as you use your Pokemon as tools and don't let them get funny ideas about independance or freedom, You'll be just fine!")
raw_input("OAK: Your journey awaits, follow me to my lab!")
raw_input("You follow Professor Oak to his labrotory next door.  Inside are walls of machinery and books.  in the middle of the room is a table with three pokeballs sitting on top.")
raw_input("OAK: What are you doing here?")
raw_input("OAK: ...Oh, I told you to come didn't I?  Whatever, on this table are three pokemon to choose from! Charmander, Bulbasaur, and Squirtle!")
raw_input("OAK: When I was your age, I was a serious pokemon trainer, I've killed hundreds! But in my old age, I only have a few left. You can choose one if you wish.")
def sure(yes, no):
    sure = raw_input("Are you sure?: ")
    if str(sure).lower() == "yes":
        raw_input(yes)
        return 'yes'
    if str(sure).lower() == "no":
        raw_input(no)
        return 'no'
    else:
        raw_input("OAK: Huh? (Type 'yes' or 'no')")
        
        

def pokechoose():           
    final_choice = 'no'
    while final_choice != 'yes':
        choice = raw_input("Which Pokemon will you choose?"
                        "Choose between Charmander, Bulbasaur, or Squirtle: ")
        if str(choice).lower() == "charmander":
            char = raw_input("OAK: Are you sure?  don't come to me when it is ten feet tall and won't listen to you.")
            final_choice = sure("OAK: Alright...", "OAK: Wuss...")
##            if str(char).lower() == "yes":
##                raw_input("OAK: Alright...")
##                final_choice = 'yes'
##            elif str(char).lower() == "no":
##                raw_input("OAK: Wuss...")
##            else:
##                raw_input("OAK: huh? (type 'yes' or 'no')")
        elif str(choice).lower() == "squirtle":
            squirt = raw_input("OAK: Really?  you had the chance at a fire-breathing dragon and you choose a bubble turtle...")
            final_choice = sure("OAK: If you say so...", "OAK: Sure, okay...")
##                raw_input("OAK: Alright...")
##                final_choice = 'yes'
##            elif str(squirt).lower() == "no":
##                raw_input("OAK: sure, okay...")
##            else:
##                raw_input("OAK: huh? (type 'yes' or 'no')")
        elif str(choice).lower() == "bulbasaur":
            bulb = raw_input("OAK: BWAHAHA really?")
            final_choice = sure("OAK: you're picked on a lot at school aren't you?", "OAK: Okay, good, I'm glad you're joking.")
##            if str(bulb).lower() == "yes":
##                raw_input("OAK: You get picked on at school a lot don't you?")
##                final_choice = 'yes'
##            elif str(bulb).lower() == "no":
##                raw_input("OAK: okay, good, I'm glad you're joking.")
##            else:
##                raw_input("OAK: huh? (type 'yes' or 'no')")
        else:
            raw_input("OAK:  I don't have that Pokemon.")
    return choice
choice = pokechoose()
a = {}
a["s"] = 4
a["d"] = 2
a["hp"] = 25
b = {}
b["s"] = 3
b["d"] = 3
b["hp"] = 20
c = {}
c["s"] = 2
c["d"] = 4
c["hp"] = 30
d = {}
d["s"] = 3
d["d"] = 3
d["hp"] = 25
poke2 = 'Rattata'
x = ['tackle', 'tackle', 'growl', 'sword dance']
trp = d
raw_input("OAK: congradulations, you're a proud owner of a {}!".format(choice))
pokename = raw_input("OAK: Would you like to name your {}?: ".format(choice))
if str(pokename).lower() == "yes":
    poke1 = raw_input("Enter name: ")
    raw_input("OAK: {} is a weird name for a pokemon...".format(poke1))
elif str(pokename).lower() == "no":
    poke1 = choice
else:
    raw_input("too late, kid, I'm not waiting around for you to come up with a name.")
    poke1 = choice
if choice == "charmander":
    choice = a
elif choice == "bulbasaur":
    choice = b
elif choice == "squirtle":
    choice = c
raw_input("OAK: Great, you got a pokemon.  Now you and {} leave me alone.".format(poke1))
raw_input("???: NOT SO FAST!")
raw_input("OAK: Wha?  what's going on here!?")
raw_input("???: Prepare for trouble!")
raw_input("???: Make it double!")
raw_input("???: To protect the world from devastation!")
raw_input("???: To unite all people within our nation!")
raw_input("???: To denounce the evils of truth and love!")
raw_input("???: To extend our reach to the stars above!")
raw_input("JESSIE: Jessie!")
raw_input("JAMES: James!")
raw_input("JESSIE: Team Rocker, blast off at the speed of light!")
raw_input("JAMES: Surrender now or prepare to fight!")
raw_input("OAK: What is the meaning of this?  Why are you here?")
raw_input("JESSIE: We are taking over the world starting at this lab in this random town!")
raw_input("JAMES: Although we are adults and possibly far superior physically, we challenge YOU to a POKEMON BATTLE!")
raw_input("Jessie and James challenge you to a battle.")
def battle2():  
    if trp.values()[1] <= 0:
        raw_input("{} died! you won!".format(poke2))
        raw_input("{} unleashes a surprising Hyper Beam attack, sending the mourning Team Rocket rocketing into the sky!".format(poke1))
        raw_input("JESSIE & JAMES: LOOKS LIKE TEAM ROCKET'S BLASTING OFF AGAAAAAAAAAaaaaaaaaaaaaaiiiiiiiinnn....")
        raw_input("ting")
        raw_input("OAK: Congratulations, {}! you saved the world by beating a level 4 Rattata!".format(player))
        raw_input("You and {} venture off into the wonderful world of Pokemon! who knows what adventures awaits!".format(poke1))
        raw_input("THE END")
    else:
        import random
        if random.choice(x) == 'tackle':
            raw_input("{} used 'tackle!".format(poke2))
            choice['hp'] = choice.values()[1] - int((2*(trp.values()[0])/((choice.values()[2]))))
            if choice.values()[1] >= 1:
                raw_input("{} has {} hp left!".format(poke1, choice.values()[1]))
            else:
                raw_input("{} has 0 hp left!".format(poke1))
            battle1()
            return choice
        elif random.choice(x) == 'growl':
            raw_input("{} used growl! defense was lowered!".format(poke2))
            choice['d'] = choice.values()[2] - 1
            battle1()
            return choice
        else:
            raw_input("{} used sword dance! its strength grew!".format(poke2))
            trp['s'] = trp.values()[0] + 1
            battle1()
            return trp
    
    
    
    

def battle1():
    if choice.values()[1] <= 0:
        raw_input("{} died! you lost!".format(poke1))
        raw_input("JESSIE: Looks like your Pokemon is--")
        raw_input("JAMES: Poke-GONE!")
        raw_input("JESSIE & JAMES: HAHAHAHAHAHAHAHAHAHAHAHAHA!")
        raw_input("Team Rocket took over the world and all Pokemon are slaves because you and {} couldn't stope them.".format(poke1))
        raw_input("GAME OVER")
        
    else:
            
        attack = raw_input("TACKLE, GROWL or SWORD DANCE?: " )
        if str(attack).lower() == "tackle":
            raw_input("{} used tackle!".format(poke1))
            trp['hp'] = trp.values()[1] - int((2*(choice.values()[0])/((trp.values()[2]))))
            if trp.values()[1] >= 1:
                raw_input("{} has {} hp left!".format(poke2, trp.values()[1]))
            else:
                raw_input("{} has 0 hp left!".format(poke2))
            battle2()
            return trp
        elif str(attack).lower() == "growl":
            raw_input("{} used growl! {}'s defense was lowered!".format(poke1, poke2))
            trp['d'] = trp.values()[2] - 1
            battle2()
            return trp
        elif str(attack).lower() == "sword dance":
            raw_input("{} used sword dance! its strength grew!".format(poke1))
            choice['s'] = choice.values()[0] + 1
            battle2()
            return choice
        else:
            raw_input("Not a proper command.  Type 'tackle', 'growl', or 'sword dance'.: ")
            battle1()
        

def pokebattle():
    raw_input("{} Sent out {}!".format(player, poke1))
    raw_input("Team Rocket sent out {}!".format(poke2))
    choice1 = raw_input("BATTLE or RUN: ")
    if str(choice1).lower() == "run":
        raw_input("You have fled from battle!")
        raw_input("Team Rocket Conqured the world! Pokemon are slaves now because you and {} ran away. cowards!".format(poke1))
        raw_input("GAME OVER")
    elif str(choice1).lower() == "battle":
        battle1()
    else:
        raw_input("invalid input.  type 'battle' or 'run'")
        pokebattle()
pokebattle()
