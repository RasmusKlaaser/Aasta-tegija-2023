
#questions
question_1 = "tere?"

# Rolling a dice
import random
roll_dice = input("Write START to dice roll: ")

if roll_dice == "start" or "Start" or "START":
   posiblle_results = [1, 2]
   result = random.choice(posiblle_results)
   print("Result of dice rolling is : " + str(result))
else:
    return None

if roll_dice == 1:
    print(question_1)
d