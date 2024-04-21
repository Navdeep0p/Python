import random
import time

exersice = [
    "push-ups",
    "squats",
    "lunges",
    "crunches",
    "pull-ups"]


print("Hello! \n")

def main():
   while True:   
      output = random.choice(exersice);

      count = ["5", "10", "25", "30", "45", "50"]

      freq = random.choice(count)
      print("Randomizing exersises and reps")

      time.sleep(3)

      print(f"You need to do {output} - {freq} times. \n")

      refresh = input("Would you like to refresh the output? (n- NO / Enter -YES ):")

      if(refresh == "n"):
       break
            

main()           