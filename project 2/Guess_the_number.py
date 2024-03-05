import random

num = input("Enter the number :")

if num.isdigit():
    num = int(num)

    if num <=0:
        print('Please type a number lager than 0 next time ')
        quit()
else:
    print('print type a number nect time ')
    quit()

random_number = random.randint(0,num)

guesses = 0

while True:
    guesses +=1
    user_guesses = input("Make a guess :") 
    if user_guesses.isdigit():
        user_guesses =int(user_guesses)
    else:
        print("Please type a number next time :")
        continue
    if user_guesses == random_number:
        print("You got it ")
        break
    elif user_guesses >random_number:
        print("you are above the number !")
    else:
        print("You are belove the number !")
print("You got it in ",guesses ," guesses")
    