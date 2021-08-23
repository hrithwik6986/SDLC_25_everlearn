
import KBC
import hang_man
import ticTacToe
import snakegame
import time


def displayScreen():
    print('''

    _____          __  __ ______ __________  _   _ ______
    / ____|   /\   |  \/  |  ____|___  / __ \| \ | |  ____|
  | |  __   /  \  | \  / | |__     / / |  | |  \| | |__
  | | |_ | / /\ \ | |\/| |  __|   / /| |  | | . ` |  __|
  | |__| |/ ____ \| |  | | |____ / /_| |__| | |\  | |____
    \_____/_/    \_\_|  |_|______/_____\____/|_| \_|______|



  ''')

    print(''' What do you want to play today ?


  ''')

    print("1. HangMan    2.Quiz  3. Snake Game  4.tic_tac_toe 5.Quit")


while True:
    displayScreen()
    try:

        choice = int(input("Enter your choice: "))
        if choice == 1:
            hang_man.gamePlay()
        elif choice == 2:
            KBC.gamePlay()

        elif choice == 3:

            snakegame.gamePlay()
        elif choice == 4:

            ticTacToe.gamePlay()
        elif choice == 5:
            print("Thank you for Trying out GameZone")
            break
        else:
            print("Choose the right option")

    except:
        print("Enter a valid choice")

    time.sleep(2)
quit()
