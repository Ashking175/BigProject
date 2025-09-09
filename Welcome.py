import random
from time import sleep
from TheGreatOutdoors import the_great_outdoors
BANNER = r"""
BBBB  III  GGGG     CCCC  AAA   SSSS  III N    N  OOO
B   B  I  G        C     A   A S       I  N N  N O   O 
BBBB   I  G  GG    C     AAAAA  SSSS   I  N  N N O   O
B   B  I  G   G    C     A   A      S  I  N   NN O   O
BBBB  III  GGGG     CCCC A   A  SSSS  III N    N  OOO
"""

num = random.randint(1, 3)
agree_list = ["y", "sure", "yes", "oui", "idk", "yeah", "yea", "yh", "ofc", "defo"]
disagree_list = ["n", "nah", "no", "non", "know", "nay", "never", "henri", "nope", "np", "ni", "mo", " o"]
reputation = 0

def main():
    global reputation
    print("")
    print("                  WELCOME TO THE")
    print(BANNER)
    user_enter = input("Would you like to enter? ").lower()
    if user_enter in agree_list:
        print("This action WILL have consequences")
        reputation -= 1
    elif user_enter in disagree_list:
        print("hmmm")
        sleep(1)
        print("you stand in front of the casino")
        sleep(1)
        print("A small breeze hits you")
        sleep(1)
        print("it fills you with determination")
        sleep(2)
        the_great_outdoors()
    else:
        print("You were forced inside by a angry bald man dressed as santa")

main()



