def takeInformationCalculateFansCount(teamFanNumber):
    cont = 'y'
    while cont == 'y' or cont == 'Y':
        team = input("Enter Name Of The Team:")
        if team in teamFanNumber:
            teamFanNumber[team] += 1
        else:
            teamFanNumber[team] = 1
        cont = input("Do You Want To Continue:")



def printFanNumber(teamFanNumber):
    for team in teamFanNumber:
        print(team, teamFanNumber[team])

def main():
    teamFanNumber = {}
    takeInformationCalculateFansCount(teamFanNumber)
    printFanNumber(teamFanNumber)

main()