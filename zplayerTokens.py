import csv


def createCard(name, cost, text,  image, first, second, third, fourth, countX, countY):
    code = ""
    code += "\\token{" + str(countX%9) + "*\squarewidth}{" + str(countY) + "*\squareheight}"
    if text != "":
        code += "{" + text + "}"
    code += "{"  + first + "}{" + second + "}{" + third + "}{" + name + "}"
    code += "\n"
    return code

def processCards(fileName = "players.csv"):
    countX = 9
    countY = 0
    f = open("players.txt", "w")
    with open(fileName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name of card']
            cost = row['cost']
            cardType = row['type']
            image = row['Image'].lower()
            text = row['description']
            first = row['icon1']
            second = row['icon2']
            third = row['icon3']
            fourth = row['icon4']
            if cardType == "":
                continue
            if cardType != "Player":
                continue
            if row['Card Status'] == "":
                continue
            else:
                card = createCard(name, cost, text,  image, first, second, third, fourth, countX, countY)
            number = row['supply'] #this line and the next are the ones i changed
            f.write(card*int(number))
            countX+=1
            if countX%9 == 0:
                countY+=1
    return

processCards()
