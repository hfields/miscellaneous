import random
debug = False

def main():
    """ Randomly generates teams out of a given list of players. Will make teams even
    if possible """
    # Find number of teams and number of players (cannot be more players than teams)
    while (True):
        numteams = get_int("How many teams? ")
        numplayers = get_int("How many players? ")
        if numteams > numplayers:
            print("More teams than players. Try again, dickhead.\n")
            continue
        else:
            break
    players = []
    for i in range(numplayers):
        s = "Who is player " + str(i + 1) + "? "
        players += [str(input(s))]
    teams = []
    for i in range(numteams):
        teams += [[]]
    currentteam = 0
    for i in range(numplayers):
        p = random.choice(players)
        teams[currentteam] += [p]
        players.remove(p)
        if currentteam == numteams - 1:
            currentteam = 0
        else:
            currentteam += 1
    for i in range(numteams):
        print("Team " + str(i + 1) + ":\n")
        for player in teams[i]:
            print(player)
        print("\n")  
    return

def get_int(s):
    """ Returns an integer casting of user input (displays the string s 
    to the user. Validates input to make sure that a non-negative integer
    is input."""
    while(True):
        try:
            r = int(input(s))
        except:
            print("Don't be a bitch. Pick a non-negative integer.\n")
            continue
        if r < 0:
            print("Don't be a bitch. Pick a non-negative integer.\n")
            continue
        else:
            return r

if __name__ == "__main__" and debug == False:
    main()

