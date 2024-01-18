age= int(input("Enter Your Age:"))
lastAnnual= int(input("Enter Your Last Annual Fee:"))
rankRegular= int(input("Enter Your Team's Rank at The End of The Regular Season:"))
matchNumber= 26
if age==22:
    releaseFee=lastAnnual*2
elif age==23:
    releaseFee=lastAnnual
elif age==24:
    releaseFee=lastAnnual/2
else:
    releaseFee=0

if rankRegular<=8:
    matchPlayoff= int(input("Enter The Number of Games Your Team Played in The Playoff Season:"))
else:
    matchPlayoff=0
    
matchNumber= matchNumber + matchPlayoff
costPerGame= lastAnnual/matchNumber
if age>=22:
    print(f"Your Cost To Your Team Per Game Played= {costPerGame:.2f} \nYou Have The Right To Be Released, Your Release Fee = {releaseFee}")
else:
    print(f"Your Cost To Your Team Per Game Played= {costPerGame:.2f} \nYou Do Not Have The Right To Be Released")