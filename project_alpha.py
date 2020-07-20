from random import randint
import random

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
    print("No...wait...please I promise it will be fun ")
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

print("You appoint, "+str(random_crew)+" to keep watch in case any of the hostages attempt to escape or call for help \n")

print("After a while one of your members, "+str(random_crew)+" ,informs you that the 2,000,000 euros have been retrevied.\n")

print("However, just before you are able to get away you hear a voice.\n")

print('Cop: "We have you surrounded, give use the money and your leader and we will let you go!"\n ')

print("what will you do? sacrifice yourself for the team or escape? \n")
answer = input("Type sacrifice or escape: ")

if answer.lower().strip() == "sacrifice":
    print()
    print("You chose to sacrifice yourself.\n")
    print("You walk out with your hands above your head.\n")
    print("You give yourself up to the police,saving your team in the process. \n")
    print("You spent the rest of your life rotting away in jail \n")
    print("GAME OVER")
    exit()

elif answer.lower().strip() == "escape":
    random_crew1 = random.choice(user_crew)
    print("You choose to escape.\n")
    print("While you and your team are attempting to escape \n")
    print("One of your team members, "+str(random_crew1)+" ,is suddenly shot in the leg, enabling them to continue.\n" )
    print ("You have one option: save them or leave them.\n")
    print("Type save or leave below: \n")
    answer = input("So what will it be? ")
    print()
# add def so that money can be tracked
    if answer.lower().strip() == "save":
        print("You go back and attempt to save them.\n")
        print("You manage to help them up to their feet, providing your shoulder for support.\n")
        print("Before you can make it to the back exit you hear a BANG!!! \n")
        print()
        print("....")
        print("....")
        print("..../n")
        print("You turn around finding your team mate laying on the ground motionless; two bullet wounds on his back. \n ")
        print("You look back up finding officers rushing towards you with their guns aiming staright at you. \n")
        print("Having had no time to grief you grab the straped bag containing some of the money from his shoulder and place it on yours.Causing some of the money to spill from the bag. \n")
        print("Having no time to retrieve it do the only thing you can think of, you run, trying to make it back to your remaining crew members waiting for you by the get away car out back. \n")