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
from PIL import Image
from time import sleep as sleep



root = tk.Tk()
root.title("Tic Tac Toe - Launcher")
root.iconbitmap("img\XO.ico")
root.resizable(0,0)
file="img\loading.gif"

info = Image.open(file)

frames = info.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None
def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = root.after(50,lambda :animation(count))

def stop_animation():
    root.after_cancel(anim)
    sleep(3)
    root.destroy()
    sleep(1)
    import launchcode

gif_label = tk.Label(root,image="")
gif_label.pack()

start = tk.Button(root,text="Get everything setup", width=30, height=10,command=lambda :animation(count))
start.pack()

stop = tk.Button(root,text="Run app",width=10, height=10,command=stop_animation)
stop.pack()

root.mainloop()