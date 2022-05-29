import random
import time
Dice_Range = list(range(1,7))
Dice_State = True
while(Dice_State == True):
    state = input("Do You Want To Roll THe Dice Again(Y/n):")
    if state == "Y" or state == "y":
        print(f"The answer is {random.randrange(1,7)}")
    if state == "N" or state == "n":
        print("Closing THe dice Simulator Session...")
        time.sleep(2)
        print("Session Ended")
        break