import random

print("Hello there,\n")

human_name = ""

person_name = input("What is your name? " + human_name)

print()

print (" Hello " + person_name+ "\n")

answer = input("Do you want to play? (yes/no): ")

if answer.lower().strip() == "yes":
    print()

    print("Great you will not regret this.... I hope.\n")

    print("Ok then let's get started.\n")

    print("Oh I almost forgot, before we start you will need to choose your crew. \n")
    crew = input("please insert 3 names seperated by a comma: ")

    print()

    user_crew = crew.split(",")

    print("crew names:\n")

    for name in user_crew:
        print(name)
print()

print("You and your crew have decided to rob the LCL bank in France. Attempting to steal 2,000,000 euros in the process. \n")

print("You finally arrive to your destination.\n")
random_crew = random.choices(user_crew)

print("You appoint" +str(random_crew)+ "to keep watch in case any of the hostages attempt to escape or call for help \n")

print("After a while one of your members +str(random_crew)+ informs you that the 2,000,000 euros have been retrevied.\n")

print("However just before you are able to get away you hear a voice.\n")

print('Cop: "We have you surrounded, give use the money and your leader and we will let you go!"\n ')

answer = input("what will you do? sacrifice yourself for the team or escape? \n ")


