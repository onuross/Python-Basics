def main():
    grades = []
    takeGrades(grades)
    statistics(grades)

def takeGrades(grades):
    another = 'y'
    while another in ['y','Y']:
        aGrade = int(input("Enter Student's Grade:"))
        grades.append(aGrade)
        another = input("Is There Another Student?:")

def statistics(grades):
    stdCount = len(grades)
    classGpa = sum(grades)/stdCount
    squareOfDiffTotal = 0
    gradesAboveGpaCount = 0
    for index in range(stdCount):
        squareOfDiffTotal += (grades[index] - classGpa)**2
        if grades[index] > classGpa:
            gradesAboveGpaCount += 1
    print(classGpa)
    try:
        stdDev = (squareOfDiffTotal / (stdCount-1))**0.5
    except ZeroDivisionError:
        print("Standart Deviation Can Not Be Calculated For One Student!")
    else:
        print(stdDev)

    print(gradesAboveGpaCount,gradesAboveGpaCount*100/stdCount)
    print(max(grades))
    print(min(grades))


main()


