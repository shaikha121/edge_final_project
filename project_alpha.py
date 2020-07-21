from random import randint
import random

class Amount():
    def __init__(self):
        self.result = 2000000

    def subtract(self,x):
        self.result =  self.result - int(x)

    def get_result(self):
        return self.result


print("Hello there,\n")

human_name = ""

person_name = input("What is your name? " + human_name)

Name = person_name

print()

print ("Hello " +person_name+ "\n")

answer = input("Do you want to play? (yes/no): ")

if answer.lower().strip() == "yes":
    print()
    print("Great you will not regret this.... I hope.\n")
    print("Ok then let's get started.\n")
    print("Oh I almost forgot, before we start you will need to choose your crew. \n")

else:
    print()
    print("No...wait...please I promise it will be fun. ")
    exit()

crew = input("please insert 3 names seperated by a comma: ")
print()
user_crew = crew.split(",")
print("crew names:\n")
for name in user_crew:
    print(name)

print()

print("You and your crew have decided to rob the LCL bank in France. Attempting to steal 2,000,000 euros in the process. \n")

print("You finally arrive to your destination.\n")
random_crew = random.choice(user_crew)

print("You appoint, "+str(random_crew)+" to keep watch incase any of the hostages attempt to escape or call for help. \n")

print("After a while one of your members, "+str(random_crew)+" ,informs you that the 2,000,000 euros have been retrevied.\n")

print("However, just before you are able to get away you hear a voice.\n")

print('Cop: "We have you surrounded, give use the money and your leader and we will let you go!"\n ')

print("what will you do? sacrifice yourself for the team or escape? \n")
answer = input("Type:sacrifice or escape. \n ")

if answer.lower().strip() == "sacrifice":
    print()
    print("You chose to sacrifice yourself.\n")
    print("You walk out with your hands above your head.\n")
    print("You give yourself up to the police,saving your team in the process. \n")
    print("You spent the rest of your life rotting away in jail. \n")
    print("GAME OVER \n")
    print("Total Money: \n")
    print(int(0))
    exit()

elif answer.lower().strip() == "escape":
    random_crew1 = random.choice(user_crew)
    print()
    print("You choose to escape.\n")
    print("While you and your team are attempting to escape,one of your team members, "+str(random_crew1)+" ,is suddenly shot in the leg, preventing them from continuing.\n" )
    print ("You have one option: save them or leave them.\n")
    print("Type: save or leave below. \n")
    answer = input("So what will it be? ")
    print()

    if answer.lower().strip() == "save":
        user_crew.remove(random_crew1)
        print("You go back and attempt to save them.\n")
        print("You manage to help them up to their feet, providing your shoulder for support.\n")
        print("Before you can make it to the back exit you hear a BANG!!! \n")
        print("....")
        print("....")
        print("....\n")
        print("You turn around finding your team mate laying on the ground motionless;two bullet wounds on their back. \n ")
        print("You look back up finding officers rushing towards you with their guns aiming staright at you. \n")
        print("Having had no time to grief you grab the straped bag containing some of the money from their shoulder and place it on yours.Causing some of the money to spill from the bag. \n")
        print("Having no time to retrieve it you do the only thing you can think of, you run, trying to make it back to your remaining crew members waiting for you by the get away car out back. \n")

A = Amount()
A.subtract(random.randrange(10000,500000))
print("Money Now: \n")
print(A.get_result())
print()
print()
print("You get meet your remaining members near the getaway car out the back.\n")
print("You can choose to be the driver or keep the plice at bay. \n")
print("what will it be?  \n")
answer = input("Type: drive or distract. \n")


if answer.lower().strip() == "drive":
    print()
    print("You get into the drivers seat, and start maneuvering between cars on the highway in an attempt to lose the police.\n")
    print("Suddenly the back windows break , due to the constant bullets being shot.\n" )
    print("This causes more money to be sucked up from the open duffel bags and fall onto the highway. \n")
    A.subtract(random.randrange(10000,500000))
    print("Money Now: \n")
    print(A.get_result())
    print()
    print("Before the start of the mission you and your team decided on two escape options (boat/helicopter) just to be safe. \n")
    print ("which one will you choose?  \n")
    answer = input("Type: boat or helicopter \n")

if answer.lower().strip() == "distract" :
    print("You take up the mantel of firing at the police from the sunroof.\n")
    print("Not realizing that doing this exposes most of your upper body you are shot on your shoulder, the same shoulder that the duffel bag is strapped too. \n")
    print("This causes the duffel bag to fall from your shoulder to the highway below.\n")
    A.subtract(random.randrange(500000,800000))
    print("Money Now: \n")
    print(A.get_result())
    print()
    print("Not wanting to risk getting shot again you re-enter the car. \n")
    print("before the start of the mission you and your team dicided on two escape options (boat/helicopter) just to be safe. \n")
    print ("which one will you choose?  \n")
    answer = input("Type: boat or helicopter \n")

if answer.lower().strip() == "boat":
    print()
    print("You and your team choose to escape using the boat. \n")
    print("You get to the docks and unload all the remaining cash on the boat. \n")
    print("You and your team escape before the cops show up .\n")
    print("MISSION COMPLETE \n")
    print("Total Money: \n")
    print(A.get_result())
    exit()

elif answer.lower().strip() == "helicopter" :
    print()
    print("You and your team choose to escape using the helicopter. \n")
    print("You arrive to the loction and unload the cash. \n")
    print("Before the cops show up you and your crew are able to escape. \n")
    print("MISSION COMPLETE \n")
    print("Total Money: \n")
    print(A.get_result())
    exit()

if answer.lower().strip() == "leave":
    print()
    print("Deciding not to risk it you leave your crew member.\n")
    print("The officers arrest "+str(random_crew1)+ "." )
    user_crew.remove(random_crew1)
    print("You then see the officers rushing towards you with their guns aiming staright at you. \n")
    print("You grab the straped bag containing some of the money off of the floor and place it on yours.Causing some of the money to spill from the bag. \n")
    print("Having no time to retrieve it, you do the only thing you can think of, you run, trying to make it back to your remaining crew members waiting for you by the get away car out back. \n")
    A.subtract(random.randrange(10000,500000))
    print("Money Now: \n")
    print(A.get_result())
    print()
    print()
    print("You get meet your remaining members near the getaway car out the back.\n")
    print("You can choose to be the driver or keep the plice at bay. \n")
    print("what will it be?  \n")
    answer = input("Type: drive or distract. \n")

    if answer.lower().strip() == "drive":
        print()
        print("You get into the drivers seat, and start maneuvering between cars on the highway in an attempt to lose the police.\n")
        print("Suddenly the back windows break , due to the constant bullets being shot.\n" )
        print("This causes more money to be sucked up from the open duffel bags and fall onto the highway. \n")
        A.subtract(random.randrange(10000,500000))
        print("Money Now: \n")
        print(A.get_result())
        print()
        print("before the start of the mission you and your team dicided on two escape options (boat/helicopter) just to be safe. \n")
        print ("which one will you choose?  \n")
        answer = input("Type: boat or helicopter \n")

    if answer.lower().strip() == "boat":
        print("You and your team choose to escape using the boat. \n")
        print("You get to the docks and unload all the remaining cash on the boat. \n")
        print("You and your team escape before the cops show up .\n")
        print("MISSION COMPLETE \n")
        print("Total Money: \n")
        print(A.get_result())
        exit()

    elif answer.lower().strip() == "helicopter" :
        print("You and your team choose to escape using the helicopter. \n")
        print("You arrive to the loction and unload the cash. \n")
        print("Before the cops show up you and your crew are able to escape. \n")
        print("MISSION COMPLETE \n")
        print("Total Money: \n")
        print(A.get_result())
        exit()