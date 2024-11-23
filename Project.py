import random
import os
os.system("cls")

class DiceRoll:
    def __init__(self):
        Goal = random.randrange(1,12)
        Dices = 7

        print( " -- !!Dice Rolling!! -- ")
        print(f"        {Dices} Dices         \n")
        print(f"Target Number : {Goal}")

        while True:
            Rolls = int(input("How many dices? (1/2) : "))
            if Rolls == 1 and Dices >= 1:
                os.system("cls")
                print(f"!!Target Number : {Goal}!!\n")

                Dices = Dices - 1
                print(f"!{Dices} Dices left!\n")

                Result = random.randrange(1,6)
                print(f"# You Rolled : {Result}\n")
                if Result == Goal:
                    print("Winner!")
                    break
                elif Goal >= Result:
                    print(f"-- Loser! You were {Goal - Result} number(s) away --\n")
                elif Goal <= Result:
                    print(f"-- Loser! You were {Result - Goal} number(s) away --\n")

            elif Rolls == 2 and Dices >= 2:
                os.system("cls")
                print(f"!!Target Number : {Goal}!!\n")

                Dices = Dices - 2
                print(f"!{Dices} Dices left!\n")

                Result1 = random.randrange(1,6)
                Result2 = random.randrange(1,6)

                print(f"+  First Dice : {Result1}")
                print(f"++ Second Dice : {Result2}\n")

                Result = Result1 + Result2
                print(f"# You Rolled : {Result}\n")
                if Result == Goal:
                    print("Winner!")
                    break
                elif Goal >= Result:
                    print(f"-- Loser! You were {Goal - Result} number(s) away --\n")
                elif Goal <= Result:
                    print(f"-- Loser! You were {Result - Goal} number(s) away --\n")
         
            elif Dices == 0 :
                print("No Dices Available!")
                break

            elif Rolls >= 2:
                print("INVALID!")

def main():
    run = DiceRoll()

if __name__ == "__main__":
    main()
