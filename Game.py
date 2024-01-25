from random import randint
random_Number = randint(1,10)
life = 3
unusual = ""
print("\nYou have only",life,"chance for play this game.\n")


while(life > 0):
    guess_Number = int(input("Guess a Number for this Game : "))
    if(guess_Number is random_Number):
        print("\n",unusual.center(40),"Congratulations!🎉\n",unusual.center(45),"You Won.\n\n")
        break
    elif(life == 1):
        print("\nrandom_Number was :",random_Number)
        print(unusual.center(41),"You losed.\n",unusual.center(27),"You have no life for play this game.\n",unusual.center(40),"Try again.\n\n",unusual.center(33),"Better Luck Next Time!",'\n')
        break
    elif(guess_Number > 10):
        print('\n',unusual.center(43),"You lose.\n",unusual.center(14),"Cause of you are trying to give number above of 10 (for guess_Number)\n\n")
        break
    elif(guess_Number < 1):
        print('\n',unusual.center(42),"You lose.\n",unusual.center(17),"Cause of you are trying to take below of 1 (for guess_Number)\n\n")
        break
    elif(guess_Number < random_Number):
        print("\nHint! Please write big number (for guess_Number)")
        print("You have only",life - 1,"chance for play this game.\n")
        life -= 1
    elif(guess_Number > random_Number):
        print("\nHint! Please write small number (for guess_Number)")
        print("You have only",life - 1,"chance for play this game.\n")
        life -= 1