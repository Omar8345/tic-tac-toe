# Tic Tac Toe Game
# Author: Omar Mostafa
# Date: 08/02/2022
# Version: 1.0
# Description: Tic Tac Toe Game made using Python Tkitner (Open Source)
#             This game is a simple game that can be played with two players
#             and can be played with a computer.

# Importing the necessary libraries
import tkinter
import random
import time

# Tkinter
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.geometry("400x400")

# Window icon
window.iconbitmap("XO.ico")

# Game PC function
def game_pc():
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
        # check if button contains O
        if buttons['text'] == "O":
            None
        elif buttons['text'] == " ":
            buttons.config(text="X")
        elif buttons['text'] == "X":
            None
        else:
            None

        # check if 1st row is equal to X
        if b1['text'] == "X" and b2['text'] == "X" and b3['text'] == "X":
            print("X wins")
        # check if 2nd row is equal to X
        elif b4['text'] == "X" and b5['text'] == "X" and b6['text'] == "X":
            print("X wins")
        # check if 3rd row is equal to X
        elif b7['text'] == "X" and b8['text'] == "X" and b9['text'] == "X":
            print("X wins")
        # check if 1st column is equal to X
        elif b1['text'] == "X" and b4['text'] == "X" and b7['text'] == "X":
            print("X wins")
        # check if 2nd column is equal to X
        elif b2['text'] == "X" and b5['text'] == "X" and b8['text'] == "X":
            print("X wins")
        # check if 3rd column is equal to X
        elif b3['text'] == "X" and b6['text'] == "X" and b9['text'] == "X":
            print("X wins")
        # check if 1st diagonal is equal to X
        elif b1['text'] == "X" and b5['text'] == "X" and b9['text'] == "X":
            print("X wins")
        # check if 2nd diagonal is equal to X
        elif b3['text'] == "X" and b5['text'] == "X" and b7['text'] == "X":
            print("X wins")
        # check if 1st row is equal to O
        elif b1['text'] == "O" and b2['text'] == "O" and b3['text'] == "O":
            print("O wins")
        # check if 2nd row is equal to O
        elif b4['text'] == "O" and b5['text'] == "O" and b6['text'] == "O":
            print("O wins")
        # check if 3rd row is equal to O
        elif b7['text'] == "O" and b8['text'] == "O" and b9['text'] == "O":
            print("O wins")
        # check if 1st column is equal to O
        elif b1['text'] == "O" and b4['text'] == "O" and b7['text'] == "O":
            print("O wins")
        # check if 2nd column is equal to O
        elif b2['text'] == "O" and b5['text'] == "O" and b8['text'] == "O":
            print("O wins")
        # check if 3rd column is equal to O
        elif b3['text'] == "O" and b6['text'] == "O" and b9['text'] == "O":
            print("O wins")
        # check if 1st diagonal is equal to O
        elif b1['text'] == "O" and b5['text'] == "O" and b9['text'] == "O":
            print("O wins")
        # check if 2nd diagonal is equal to O
        elif b3['text'] == "O" and b5['text'] == "O" and b7['text'] == "O":
            print("O wins")   
        # check if all buttons are filled 
        elif buttons == "X" or buttons == "O":
            print("Draw")
        # fill any empty random button with O
        else:
            # create a list of empty buttons
            empty_buttons = []
            # check if button is empty
            for button in buttons:
                if button['text'] == " ":
                    empty_buttons.append(button)
            # choose a random button from the list of empty buttons
            r = random.choice(empty_buttons)
            # put O in the random button
            r.config(text="O")

        
    window.mainloop()
        






game_pc()