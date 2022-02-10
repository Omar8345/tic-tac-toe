# Tic Tac Toe Game
# Original repository: (https://github.com/Omar8345/tic-tac-toe)
# Author: Omar Mostafa
# Date: 08/02/2022
# Version: 1.0
# Description: Tic Tac Toe Game made using Python Tkitner (Open Source)
#             This game is a simple game that can be played with two players
#             and can be played with a computer.

##### CODING STARTS HERE #####

# Importing the necessary libraries
from itertools import tee
import tkinter
import random
import time
from tkinter import messagebox
from numpy import empty
from time import sleep as sleep

try:
    # Tkinter
    window = tkinter.Tk()
    window.title("Tic Tac Toe")
    window.resizable(0, 0) # It makes everything needed to fit the window! WoW!

    # Window icon
    window.iconbitmap("img\XO.ico")

    # Tkinter game buttons
    # create 9 tkinter buttons
    b1 = tkinter.Button(window, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: btn_click(b1))
    b1.grid(row=1, column=0)

    b2 = tkinter.Button(window, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: btn_click(b2))
    b2.grid(row=1, column=1)
    b3 = tkinter.Button(window, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: btn_click(b3))
    b3.grid(row=1, column=2)
    b4 = tkinter.Button(window, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: btn_click(b4))
    b4.grid(row=2, column=0)
    b5 = tkinter.Button(window, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: btn_click(b5))
    b5.grid(row=2, column=1)
    b6 = tkinter.Button(window, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: btn_click(b6))
    b6.grid(row=2, column=2)
    b7 = tkinter.Button(window, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: btn_click(b7))
    b7.grid(row=3, column=0)
    b8 = tkinter.Button(window, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: btn_click(b8))
    b8.grid(row=3, column=1)
    b9 = tkinter.Button(window, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: btn_click(b9))
    b9.grid(row=3, column=2)

    # create a list to store the buttons
    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

    # create a list to store the values of the buttons
    values = []


    # when button clicked, it puts X in the button
    def btn_click(buttons):
        # make clicked button disabled
        buttons.config(state=tkinter.DISABLED)

        # check if button contains O
        if buttons['text'] == "O":
            None
        elif buttons['text'] == " ":
            buttons.config(text="X")
            buttons.config(bg="red")
        elif buttons['text'] == "X":
            None
        else:
            None

        # check if 1st row is equal to X
        if b1['text'] == "X" and b2['text'] == "X" and b3['text'] == "X":
            print("X wins")
            tkinter.messagebox.showinfo("Winner", "X wins")
            # stop the game
            window.destroy()
        # check if 2nd row is equal to X
        elif b4['text'] == "X" and b5['text'] == "X" and b6['text'] == "X":
            print("X wins")
            tkinter.messagebox.showinfo("Winner", "X wins")
            # stop the game
            window.destroy()
        # check if 3rd row is equal to X
        elif b7['text'] == "X" and b8['text'] == "X" and b9['text'] == "X":
            print("X wins")
            tkinter.messagebox.showinfo("Winner", "X wins")
            # stop the game
            window.destroy()
        # check if 1st column is equal to X
        elif b1['text'] == "X" and b4['text'] == "X" and b7['text'] == "X":
            print("X wins")
            tkinter.messagebox.showinfo("Winner", "X wins")
            # stop the game
            window.destroy()
        # check if 2nd column is equal to X
        elif b2['text'] == "X" and b5['text'] == "X" and b8['text'] == "X":
            print("X wins")
            tkinter.messagebox.showinfo("Winner", "X wins")
            # stop the game
            window.destroy()
        # check if 3rd column is equal to X
        elif b3['text'] == "X" and b6['text'] == "X" and b9['text'] == "X":
            print("X wins")
            tkinter.messagebox.showinfo("Winner", "X wins")
            # stop the game
            window.destroy()
        # check if 1st diagonal is equal to X
        elif b1['text'] == "X" and b5['text'] == "X" and b9['text'] == "X":
            print("X wins")
            tkinter.messagebox.showinfo("Winner", "X wins")
            # stop the game
            window.destroy()
        # check if 2nd diagonal is equal to X
        elif b3['text'] == "X" and b5['text'] == "X" and b7['text'] == "X":
            print("X wins")
            tkinter.messagebox.showinfo("Winner", "X wins")
            # stop the game
            window.destroy()

        else:
            emptybuttons = []
            if b1['text'] == " ":
                emptybuttons.append(b1)
            if b2['text'] == " ":
                emptybuttons.append(b2)
            if b3['text'] == " ":
                emptybuttons.append(b3)
            if ['text'] == " ":
                emptybuttons.append(b4)
            if b5 == " ":
                emptybuttons.append(b5)
            if b6['text'] == " ":
                emptybuttons.append(b6)
            if b7['text'] == " ":
                emptybuttons.append(b7)
            if b8['text'] == " ":
                emptybuttons.append(b8)
            if b9['text'] == " ":
                emptybuttons.append(b9)
            # randomly select a button from the list
            import random
            random_button = random.choice(emptybuttons)
            # change button text to O
            random_button.config(text="O")
            # make button disabled
            random_button.config(state=tkinter.DISABLED)
            # make O blue
            random_button.config(bg="blue")
            # clear the list
            emptybuttons.clear()
            # check if 1st row is equal to O
        if b1['text'] == "O" and b2['text'] == "O" and b3['text'] == "O":
            print("O wins")
            # alert
            tkinter.messagebox.showinfo("Winner", "O wins")
            # stop the game
            window.destroy()
        # check if 2nd row is equal to O
        elif b4['text'] == "O" and b5['text'] == "O" and b6['text'] == "O":
            print("O wins")
            tkinter.messagebox.showinfo("Winner", "O wins")
            # stop the game
            window.destroy()
        # check if 3rd row is equal to O
        elif b7['text'] == "O" and b8['text'] == "O" and b9['text'] == "O":
            print("O wins")
            tkinter.messagebox.showinfo("Winner", "O wins")
            # stop the game
            window.destroy()
        # check if 1st column is equal to O
        elif b1['text'] == "O" and b4['text'] == "O" and b7['text'] == "O":
            print("O wins")
            tkinter.messagebox.showinfo("Winner", "O wins")
            # stop the game
            window.destroy()
        # check if 2nd column is equal to O
        elif b2['text'] == "O" and b5['text'] == "O" and b8['text'] == "O":
            print("O wins")
            tkinter.messagebox.showinfo("Winner", "O wins")
            # stop the game
            window.destroy()
        # check if 3rd column is equal to O
        elif b3['text'] == "O" and b6['text'] == "O" and b9['text'] == "O":
            print("O wins")
            tkinter.messagebox.showinfo("Winner", "O wins")
            # stop the game
            window.destroy()
        # check if 1st diagonal is equal to O
        elif b1['text'] == "O" and b5['text'] == "O" and b9['text'] == "O":
            print("O wins")
            tkinter.messagebox.showinfo("Winner", "O wins")
            # stop the game
            window.destroy()
        # check if 2nd diagonal is equal to O
        elif b3['text'] == "O" and b5['text'] == "O" and b7['text'] == "O":
            print("O wins")
            tkinter.messagebox.showinfo("Winner", "O wins")
            # stop the game
            window.destroy()
        # check if all buttons are filled
        elif buttons == "X" or buttons == "O":
            print("Draw")
            tkinter.messagebox.showinfo("Winner", "Draw, Game Over!")
            # stop the game
            window.destroy()
except:
    None

def run_game():
    window.mainloop()


if __name__ == "__main__":
    run_game()
else:
    print("If you run the game using the launcher.py or launcher.exe.")
    sleep(1)
    print('Ignore this message, thank you.')
    print('------------------------------------------------------')
    print("Error: This is a module and not a script.")
    sleep(2)
    print("Please run this module as a script.")
    sleep(2)
    print("If you actually did run it as a script, please report this bug.")
    sleep(2)
    print("Raise an issue on GitHub. More details:")
    sleep(2)
    print("__name__ != __main__")
    sleep(2)
    print(" __name__ does not equal __main__ and this was made to prevent errors.")
    sleep(2)
    print("If you are a developer and you are seeing this message, please report this bug and (if possible, more details).")
    sleep(2)
    print("If you are not a developer and you are seeing this message, please report the details gaven above.")
    sleep(2)
    print("Thank you.")
    sleep(2)
    print("Omar Mostafa")
    sleep(2)
    print("Hope you in good health. Stay safe.")
    sleep(1)