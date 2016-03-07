import csv

def createCard(name, cardType, cost, text,  image, vision, push, roam):
    code = "\\begin{tikzpicture} \n\cardbackground{" +cardType  +"} \n" #"\\"+ cardType + "} \n"
    code += "\cardtitle{" + name+ "} \n"
    code += "\cardborder{} \n"
    code += "\cardcontent{" + text + "} \n"
    code += "\cardimage{" + image + "} \n"
    code += "\cardprice{" + str(cost) + "\\vp} \n"
    code += "\stance{" + image + "} \n"
    code += "\\attributes{"
    if vision != "x":
        code += "not"
    code += "Vision}{"
    if push != "x":
        code += "not"
    code += "Push}{"
    #if glob != "x":
    #    code += "not"
    #code += "GlobalPresence}{"
    if roam != "x":
        code += "not"
    code += "Roam} \n"
    #if version != "":
     #   code += "\sync{" + version + "} \n"
    code += "\end{tikzpicture}\n\hspace{-4mm}\n"
    return code

def createObj(name, cost, text, image):
    code = "\\begin{tikzpicture} \n\cardbackground{Objective} \n"
    code += "\cardtitle{" + name+ "} \n"
    code += "\cardborder{} \n"
    code += "\cardcontent{" + text + "} \n"
    code += "\cardimage{" + image + "} \n"
    code += "\cardprice{" + str(cost) + "} \n"
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
            image = row['Ranged/Melee']
            text = row['description']
            vision = row['Vision']
            push = row['Push']
            #glob = row['Global Presence']
            roam = row['Roam']
            if cardType == "":
                continue
            if row['Card Status'] == "":
                continue
            if cardType == "objective":
                card = createObj(name, cost, text, image)
            else:
                card = createCard(name, cardType, cost, text,  image, vision, push, roam)
            number = row['supply'] #this line and the next are the ones i changed
            f.write(card*int(number))
    return

processCards()