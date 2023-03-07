vastuseid_kokku = 20
#Punktisumma arvutamine
#all questions below are meant for ITA!!!!
question_1 = "Kas selle erialaga saab olulise eelise õpigute jätkamiseks kõrgkoolis ja võib spetsialiseeruda IT valdkonna profiks?    (JAH/EI)"
question_2 = "Milline eriala on eriliselt kiiresti kasvav ja maailma tulevik?     (TARKVARAARENDJA/VEEBIHALDUR)"
question_3 = "Tegu on globaalse kasvava ettevõtlusvaldkonnaga, kus heade spetsialistide järele on pidevalt suur nõudlus, mistõttu tarkvaraarendaja leiab hõlpsasti tööd ka väljaspool Eestit.      (ÕIGE/VALE)"
question_4 = "Tarkvaraarendajad saavad töötada vähestes valdkondades.    (ÕIGE/VALE)"
question_5 = "Eesti IT-sektoris on palgatase keskmisest kõrgem ning tarkvaraarendaja töötasu alumine määr võib ületada Eesti keskmise töötasu. (ÕIGE/VALE)"

row1 = 100
row2 = 200
row3 = 300
row4 = 400
row5 = 500
score = 0
print(question_1)
ans = input("Vastus: ")
if ans.lower() == "jah":
    score += row1
    vastuseid_kokku -= 1
else:
    score -= row1 / 2
    vastuseid_kokku -= 1
print(f"Punkti summa on nüüd: {score}")
print(f"{vastuseid_kokku} vastust on alles.")
print(question_2)
ans = input("Vastus: ")
if ans.lower() == "tarkvaraarendaja":
    score += row2
    vastuseid_kokku -= 1
else:
    score -= row2 / 2
    vastuseid_kokku -= 1
print(f"Punkti summa on nüüd: {score}")
print(f"{vastuseid_kokku} vastust on nüüd alles")
print(question_3)
ans = input("Vastus: ")
if ans.lower() == "õige":
    score += row3
    vastuseid_kokku -= 1
else:
    score -= row3 / 2
    vastuseid_kokku -= 1
print(f"Punkti summa on nüüd: {score}")
print(f"{vastuseid_kokku} vastust on nüüd alles")
print(question_4)
ans = input("Vastus: ")
if ans.lower() == "vale":
    score += row4
    vastuseid_kokku -= 1
else:
    score -= row4 / 2
    vastuseid_kokku -= 1
print(f"Punkti summa on nüüd: {score}")
print(f"{vastuseid_kokku} vastust on nüüd alles")
print(question_5)
ans = input("Vastus: ")
if ans.lower() == "õige":
    score += row5
    vastuseid_kokku -= 1
else:
    score -= row5 / 2
    vastuseid_kokku -= 1
print(f"Punkti summa on nüüd: {score}")
print(f"{vastuseid_kokku} vastust on nüüd alles")
