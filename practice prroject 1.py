print("Hello Gamer's Ready to play the game....")

print("Wellcome to Quiz game")

Playing =input("Do yo like to play Game ?...")
if Playing.lower() != 'yes':
    quit()

print("Lets start the game :")

count =0

Question1 = input("What A stand for?.. ")
if Question1 =='alpha':
    print("The answer is correct.")
    count += 1
else: print("The answer is incorrect.")

Question2 = input("What B stand for?.. ")
if Question2 =='bravo':
    print("The answer is correct.")
    count += 1
else: print("The answer is incorrect.")


Question3 = input("What C stand for?.. ")
if Question3 =='charlie':
    print("The answer is correct.")
    count += 1
else: print("The answer is incorrect.")

print("The total numer of answer correct was "+ str(count))

print ("The total percentage " + str((count / 3 )* 100) )