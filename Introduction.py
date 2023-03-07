import random

# Introduction

otsus = 1
valik = input("Palun vali eriala: (tarkvaraarendaja) või (süsteemide spetsialist): ")
if valik.lower() == "tarkvaraarendaja":
    print("Olete valinud tarkvaraarendaja")
elif valik.lower() == "süsteemide spetsialist":
    print("Olete valinud süsteemide spetsialisti")
else:
    otsus = 0
    print("Vale sisestus")

# Rolling a dice

result = 0
if otsus == 1:
    roll_dice = input("Write (START) to dice roll: ")

    if roll_dice == "START":
       possible_results = [1, 2, 3, 4, 5]
       result = random.choice(possible_results)
       print("Result of dice rolling is: " + str(result))
    else:
        print("Wrong input")
#Making sure that u can write both ways

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

#ALL THE QUESTIONS BELOW ARE FOR ITS!!!
question_1_2 = "Kas IT-süsteemide spetsialist saab tööle IT-süsteemide spetsialistina või klienditoespetsialistina?    (SPETSIALIST/KLIENDITUGI)"
question_2_2 = "Kas tegu on ettevõttevaldkonnaga, kus spetsialistie järele on väike nõudlus?    (JAH/EI)"
question_3_2 = "Kas IT-spetsialist haldab arvutivõrke, telefoniteenuseid ja vajadusel ehitab müüri?      (JAH/EI)"
question_4_2 = "Mida tähendab lühend IT?   (FILM/INFO-TEADUS/INFO-TEHNOLOOGIA)"
question_5_2 = "Milliseid võtmeoskusi on vaja edukaks IT-spetsialisti karjääriks?  (ERINEVATE ARVUTIKEELTE TUNDMINE/INVESTEERIMINE/LOOGILINE MÕTLEMINE)"

print(question_1_2)
ans = input("Vastus: ")
if ans.lower() == "spetsialist":
    score += row1
    vastuseid_kokku -= 1
else:
    score -= row1 / 2
    vastuseid_kokku -= 1
print(f"Punkti summa on nüüd: {score}")
print(f"{vastuseid_kokku} vastust on nüüd alles")
print(question_2_2)
ans = input("Vastus: ")
if ans.lower() == "ei":
    score += row2
    vastuseid_kokku -= 1
else:
    score -= row2 / 2
    vastuseid_kokku -= 1
print(f"Punkti summa on nüüd: {score}")
print(f"{vastuseid_kokku} vastust on nüüd alles")
print(question_3_2)
ans = input("Vastus: ")
if ans.lower() == "ei":
    score += row3
    vastuseid_kokku -= 1
else:
    score -= row3 / 2
    vastuseid_kokku -= 1
print(f"Punkti summa on nüüd: {score}")
print(f"{vastuseid_kokku} vastust on nüüd alles")
print(question_4_2)
ans = input("Vastus: ")
if ans.lower() == "info-tehnoloogia":
    score += row4
    vastuseid_kokku -= 1
else:
    score -= row4 / 2
    vastuseid_kokku -= 1
print(f"Punkti summa on nüüd: {score}")
print(f"{vastuseid_kokku} vastust on nüüd alles")
print(question_5_2)
ans = input("Vastus: ")
if ans.lower() == "loogiline mõtlemine":
    score += row5
    vastuseid_kokku -= 1
else:
    score -= row5 / 2
    vastuseid_kokku -= 1
print(f"Punkti summa on nüüd: {score}")
print(f"{vastuseid_kokku} vastust on nüüd alles")

