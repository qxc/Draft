import csv

def createCard(name, cardType, cost, text,  image, first, second, third, fourth, tier):
    code = "\\begin{tikzpicture} \n\cardbackground{" +cardType  +"} \n" #"\\"+ cardType + "} \n"
    code += "\cardtitle{" + name+ "} \n"
    code += "\cardborder{} \n"
    code += "\cardcost{" + cost + "} \n"
    if text != "":
        code += "\cardcontent{" + text + "} \n"
    code += "\cardimage{" + image + "} \n"
    code += "\\first{"
    if first == "":
        code += "notVision}"
    else:
        code +=first + "}"
    code += "\n\second{"
    if second == "":
        code += "notVision}"
    else:
        code +=second + "}"
    code += "\n\\third{"
    if third == "":
        code += "notVision}"
    else:
        code +=third + "}"
    code += "\n\\fourth{"
    if fourth == "":
        code += "notVision}"
    else:
        code +=fourth + "}\n"

    code += " \cardtier{" + tier + "} \n"
    code += "\end{tikzpicture}\n\hspace{-4mm}\n"
    return code

def createObj(name, cardType, cost, text, image):
    code = "\\begin{tikzpicture} \n\cardbackground{" + cardType + "} \n"
    code += "\cardtitle{" + name+ "} \n"
    code += "\cardborder{} \n"
    code += "\cardcontent{" + text + "} \n"
    code += "\cardimage{" + image + "} \n"
    if cost != "":
        code += "\cardvp{" + str(cost) + "} \n"
    code += "\end{tikzpicture}\n\hspace{-4mm}\n"
    return code

def processCards(fileName = "cardList.csv"):
    f = open("cards.txt", "w")
    with open(fileName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name of card']
            cost = row['cost']
            cardType = row['type'].lower()
            image = row['Image'].lower()
            text = row['description']
            first = row['icon1']
            second = row['icon2']
            third = row['icon3']
            fourth = row['icon4']
            tier  = row['tier']
            if cardType == "":
                continue
            if row['Card Status'] == "":
                continue
            if cardType == "location" or cardType =="arena" or cardType == "team comp":
                card = createObj(name, cardType, cost, text, image)
            else:
                card = createCard(name, cardType, cost, text,  image, first, second, third, fourth, tier)
            number = row['supply'] #this line and the next are the ones i changed
            f.write(card*int(number))
    return

processCards()
