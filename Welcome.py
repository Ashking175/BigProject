from time import sleep

BANNER = r"""
BBBB  III  GGGG     CCCC  AAA   SSSS  III N    N  OOO
B   B  I  G        C     A   A S       I  N N  N O   O 
BBBB   I  G  GG    C     AAAAA  SSSS   I  N  N N O   O
B   B  I  G   G    C     A   A      S  I  N   NN O   O
BBBB  III  GGGG     CCCC A   A  SSSS  III N    N  OOO
"""

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
        sleep(3)
        print("you stand infront of the casino")
        print("A small breeze hits you")
        print("it fills you with determination")
    else:
        print("You were forced inside by a angry bald man dressed as santa")

main()



