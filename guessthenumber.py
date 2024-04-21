import random
import string



def main():
 while True:   
    numbers = string.digits
    no1 = random.choice(numbers)
    no2 = random.choice(numbers)

    rand = ( no1 + no2 )
    
    user = input("Guess a number: ")
    if user.isdigit():
        user = int(user)
        if 0 <= user <= 100:
             if (rand == user):
              print(f"\n You gussed it right.!! no. is {rand}. \n")
             elif(rand != user):
              print(f"\n Wrong guess.. the no. is {rand}. Better luck next time. \n")    
        else:
            print("\n please select a number between 0-100.\n")
    else:
        print("\n Please enter a number.\n")     
    
    quit = input("hit 'enter' to play again (or) 'q' to Quit.")

    if(quit == "q"):
       print("Better luck nex time. ")
       break



main()