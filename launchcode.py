# Tic Tac Toe Game (Launcher)
# Original repository: (https://github.com/Omar8345/tic-tac-toe)
# Author: Omar Mostafa
# Date: 08/02/2022
# Version: 1.0
# Description: Tic Tac Toe Game made using Python Tkitner (Open Source)
#             This game is a simple game that can be played with two players
#             and can be played with a computer.

##### CODING STARTS HERE #####

import tkinter as tk
import tkinter.ttk as ttk
from time import sleep as sleep
 
 
try:
    def run():
        root = tk.Tk()
        root.title("Tic Tac Toe - Launcher")
        root.geometry("400x400")
        root.iconbitmap("img\XO.ico")
 
        class Button:
 
            row = 0
            def __init__(self, text, func, image=""):
                image = tk.PhotoImage(file=image)
                tk.Grid.rowconfigure(root, Button.row, weight=1)
                tk.Grid.columnconfigure(root, 0, weight=1)
 
                self.button = tk.Button(
                    root,
                    text=text,
                    image=image,
                    compound = tk.LEFT,
                    command=func)
                # self.button.pack()
                self.button.grid(sticky="nswe")
                self.button.image = image
                Button.row += 1
 
            def open(text):
                os.startfile(text)
 
 
        data = [
            ["PC - PLAY VS PC", lambda: pc(), "img\icon90.png"],
            ["LOCAL - PLAY VS FRIEND LOCALLY", lambda: local(), "img\icon90.png"],
        ]

        def pc():
            import pc

        def local():
            import local
 
        for d in data:
            b = Button(*d)
 
        root.mainloop()
except:
    None

if __name__ == "__main__":
    run()
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
    run()