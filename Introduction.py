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

    if roll_dice == "start".upper():
       possible_results = [1, 2, 3, 4, 5]
       result = random.choice(possible_results)
       print("Result of dice rolling is: " + str(result))
    else:
        print("Wrong input")

    if valik.lower() == "tarkvaraarendaja":
        question_1 = "QUESTION"
        question_2 = "Question"
        question_3 = "question"
        question_4 = "question"
        question_5 = "question"
    elif valik.lower() == "süsteemide spetsialist":
        question_1 = "dad"
        question_2 = "dad"
        question_3 = "dad"
        question_4 = "dad"
        question_5 = "dad"

    if result == 1:
        print(question_1)
    elif result == 2:
        print(question_2)
    elif result == 3:
        print(question_3)
    elif result == 4:
        print(question_4)
    elif result == 5:
        print(question_5)