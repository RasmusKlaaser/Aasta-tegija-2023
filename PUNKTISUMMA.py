vastuseid_kokku = 20
#Punktisumma arvutamine
#1-st row is 100 points 2-nd row is 200 points, 3-rd is 300, 4-th is 400, 5th is 500 points.
question_1 = "Kas selle erialaga saab olulise eelise õpigute jätkamiseks kõrgkoolis ja võib spetsialiseeruda IT valdkonna profiks?    (JAH/EI)"
row1 = 100
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










