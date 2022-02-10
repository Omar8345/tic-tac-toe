# Tic Tac Toe game made using Tkinter and Python
# Original repository: (https://github.com/Omar8345/tic-tac-toe)
# Made by : Omar Mostafa
# Date: 10/02/2022
# Version: 1.0
# Description: This is the local player Tic Tac Toe game
# Open source project under MIT lisence

##### CODING STARTS HERE #####

# Import the tkinter module
from tkinter import *
from tkinter import messagebox

# Import sleep from time module
import time
from time import sleep as sleep
from pyparsing import null_debug_action

try:
    # Create a tkitner window
    window = Tk()

    # Window specifications
    window.title("Tic Tac Toe")
    window.resizable(0, 0)
    window.configure(background="white")
    window.iconbitmap("img\XO.ico")

    # Create 9 buttons
    b1 = Button(window, text=" ", font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(b1))
    b2 = Button(window, text=" ", font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(b2))
    b3 = Button(window, text=" ", font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(b3))
    b4 = Button(window, text=" ", font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(b4))
    b5 = Button(window, text=" ", font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(b5))
    b6 = Button(window, text=" ", font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(b6))
    b7 = Button(window, text=" ", font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(b7))
    b8 = Button(window, text=" ", font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(b8))
    b9 = Button(window, text=" ", font='Times 20 bold', bg='white', fg='black', height=4, width=8, command=lambda: btnClick(b9))

    # store buttons in a list
    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

    # Place the buttons on the window
    b1.grid(row=1, column=0)
    b2.grid(row=1, column=1)
    b3.grid(row=1, column=2)
    b4.grid(row=2, column=0)
    b5.grid(row=2, column=1)
    b6.grid(row=2, column=2)
    b7.grid(row=3, column=0)
    b8.grid(row=3, column=1)
    b9.grid(row=3, column=2)
    
    # Button text turn X or O
    turn = "X"
    
    # Create btn_click function
    def btnClick(button_id):
        global turn
        # Each time a button is clicked, the next button text will change
        # The button text will be the O then X and so on
        if turn == "X":
            button_id.configure(text="X", bg="red", fg="white")
            # make button disabled
            button_id.configure(state=DISABLED)
            turn = "O"
        elif turn == "O":
            button_id.configure(text="O", bg="blue", fg="white")
            button_id.configure(state=DISABLED)
            turn = "X"
        
        # Check for the winner
        def checkforwinner():
            # If first row is X
            if (b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X"):
                # Show messagebox
                messagebox.showinfo("Winner", "X is the winner")
                # Make all buttons disabled
                for i in range(9):
                    buttons[i].configure(state=DISABLED)
            # If first row is O
            elif (b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O"):
                # Show alert box
                messagebox.showinfo("Winner", "O is the winner")
                # Make all buttons disabled
                for i in range(9):
                    buttons[i].configure(state=DISABLED)
            # If second row is X
            elif (b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X"):
                # Show alert box
                messagebox.showinfo("Winner", "X is the winner")
                # Make all buttons disabled
                for i in range(9):
                    buttons[i].configure(state=DISABLED)
            # If second row is O
            elif (b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O"):
                # Show alert box
                messagebox.showinfo("Winner", "O is the winner")
                # Make all buttons disabled
                for i in range(9):
                    buttons[i].configure(state=DISABLED)
            # If third row is X
            elif (b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X"):
                # Show alert box
                messagebox.showinfo("Winner", "X is the winner")
                # Make all buttons disabled
                for i in range(9):
                    buttons[i].configure(state=DISABLED)
            # If third row is O
            elif (b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O"):
                # Show alert box
                messagebox.showinfo("Winner", "O is the winner")
                # Make all buttons disabled
                for i in range(9):
                    buttons[i].configure(state=DISABLED)
            # If first column is X
            elif (b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X"):
                # Show alert box
                messagebox.showinfo("Winner", "X is the winner")
                # Make all buttons disabled
                for i in range(9):
                    buttons[i].configure(state=DISABLED)
            # If first column is O
            elif (b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O"):
                # Show alert box
                messagebox.showinfo("Winner", "O is the winner")
                # Make all buttons disabled
                for i in range(9):
                    buttons[i].configure(state=DISABLED)
            # If second column is X
            elif (b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X"):
                # Show alert box
                messagebox.showinfo("Winner", "X is the winner")
                # Make all buttons disabled
                for i in range(9):
                    buttons[i].configure(state=DISABLED)
            # If second column is O
            elif (b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O"):
                # Show alert box
                messagebox.showinfo("Winner", "O is the winner")
                # Make all buttons disabled
                for i in range(9):
                    buttons[i].configure(state=DISABLED)
            # If third column is X
            elif (b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X"):
                # Show alert box
                messagebox.showinfo("Winner", "X is the winner")
                # Make all buttons disabled
                for i in range(9):
                    buttons[i].configure(state=DISABLED)
            # If third column is O
            elif (b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O"):
                # Show alert box
                messagebox.showinfo("Winner", "O is the winner")
                # Make all buttons disabled
                for i in range(9):
                    buttons[i].configure(state=DISABLED)
            # If first diagonal is X
            elif (b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X"):
                # Show alert box
                messagebox.showinfo("Winner", "X is the winner")
                # Make all buttons disabled
                for i in range(9):
                    buttons[i].configure(state=DISABLED)
            # If first diagonal is O
            elif (b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O"):
                # Show alert box
                messagebox.showinfo("Winner", "O is the winner")
                # Make all buttons disabled
                for i in range(9):
                    buttons[i].configure(state=DISABLED)
            # If second diagonal is X
            elif (b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X"):
                # Show alert box
                messagebox.showinfo("Winner", "X is the winner")
                # Make all buttons disabled
                for i in range(9):
                    buttons[i].configure(state=DISABLED)
            # If second diagonal is O
            elif (b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O"):
                # Show alert box
                messagebox.showinfo("Winner", "O is the winner")
                # Make all buttons disabled
                for i in range(9):
                    buttons[i].configure(state=DISABLED)
            # If all buttons in the buttons list are disabled
            elif (b1["state"] == DISABLED and b2["state"] == DISABLED and b3["state"] == DISABLED and b4["state"] == DISABLED and b5["state"] == DISABLED and b6["state"] == DISABLED and b7["state"] == DISABLED and b8["state"] == DISABLED and b9["state"] == DISABLED):
                # Show alert box
                messagebox.showinfo("Draw", "The game is a draw")
            else:
                None
        checkforwinner()




except:
    print("ERROR")

# Run the game
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