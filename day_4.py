#day_4
day4 = open('day4.txt', 'r')

#Make a function
def calculatePoints(number):
    if number == 0:
        return 0
    return 2 ** (number - 1)

total = 0
lineNo = 0
#Iterating over lines in the text
for line in day4:
    lineNo += 1
    wins = 0
    points = 0
    #Splittng the card numbers with the actual values on the cards
    before, after = line.split(':')
    #Splitting the numbers based on the '|'
    left, right = after.split('|')
    #Strip whitespace to left and right. Splitting based on spaces.
    picks = left.strip().split(" ")
    answers = right.strip().split(" ")
    # print(picks)
    # print(answers)
    #Matching my numbers with winning numbers
    correctPicks = []
    for pick in picks:
        if pick == "":
            continue
        for answer in answers:
            if pick == answer:
                correctPicks.append(pick)
                wins = wins + 1
                break
                #print(wins)
    points = calculatePoints(wins)
    # points = 2 ** (wins -1)
    print("Line number: ", lineNo)
    print("Points for line", points)
    print("the correct picks", correctPicks)

    #Calculate total
    total = total + points
print(total)