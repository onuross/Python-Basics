maxScore = -1
try:
    euroVisionFile = open("metalEurovision.txt", "r")
    countryName = euroVisionFile.readline()
    while countryName != "":
        singerName = euroVisionFile.readline()
        songTitle = euroVisionFile.readline()
        print(countryName, singerName, songTitle)
        score = int(input("Enter Your Score For This Singer:"))
        while score < 0:
            score = int(input("Enter Your Score Again For This Singer:"))
        if score > maxScore:
            maxScore = score
            maxScoreCountryName = countryName
            maxScoreSingerName = singerName
            maxScoreSongTitle = songTitle
        countryName = euroVisionFile.readline()
    euroVisionFile.close()
except IOError:
    print("File Could Not Be Opened!")
except ValueError:
    print("Incorrect Numeric Data Entry!")
except:
    print("An Error Occured!")
else:
    print("The Winner :")
    print(maxScore, maxScoreCountryName, maxScoreSingerName)
