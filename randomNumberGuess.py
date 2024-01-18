import random
maxNumber=100
minNumber=1
randomNumber= random.randint(minNumber, maxNumber)
guess= int(input("\nGuess The Number: "))
x=1     #guess count
while randomNumber != guess: 
    if randomNumber <guess:
        print("\nDown")
    else:
        print("\nUp")
    guess= int(input("\nGuess The Number: "))
    x += 1         
print(f"\n\n\nCongratulations The Number is {randomNumber} \nYou Find it in {x} tries")


