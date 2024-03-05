print("Welcome to my computer quize !")

playing =input("Do you want to play ? ")

print(playing)


if playing != "yes":
    quit()

print ("Okay ! lets play : )")
score =0

answer = input("What does CPU stand for ? ")
if answer.lower() == "central processing unit":
    print("Correct !")
    score += 1
else: 
    print("incorrect")


question2 = input("What is I stand for :")
if question2 == "india":
    print("Thats correct")
    score += 1
else:
    print("Incorrect")


Question3 = input("what is K means: ")
if Question3 == "kilo":
    print("Thats correct !")
    score += 1
else:
    print("Its incorrect")


Question4 = input("what A stand for :")
if Question4 == "alpha":
    print("Its correct") 
    score += 1 
else:print("its wrong") 

print("Your score was :"+ str(score))