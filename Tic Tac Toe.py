from tkinter import *  
from tkinter import messagebox
import random

Player1 = random.choice(["O","X"])  # pilih pemain awal acak
stop_game = False

def clicked(r,c):
    global Player1

    if Player1 == "O" and states[r][c] == 0 and not stop_game:
        b[r][c].configure(text="O", fg="#00ffff")  # Neon cyan
        states[r][c] = 'O'
        Player1 = 'X'
        status_label.config(text="Giliran: PLAYER 2", fg="#ff9933")

    elif Player1 == 'X' and states[r][c] == 0 and not stop_game:
        b[r][c].configure(text="X", fg="#ff9933")  # Neon orange
        states[r][c] = "X"
        Player1 = "O"
        status_label.config(text="Giliran: PLAYER 1", fg="#00ffff")

    check_if_win()

def check_if_win():
    global stop_game

    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] != 0:
            highlight_winner([(i,0),(i,1),(i,2)])
            stop_game = True
            messagebox.showinfo("Winner", states[i][0] + " Menang!")
            return

        elif states[0][i] == states[1][i] == states[2][i] != 0:
            highlight_winner([(0,i),(1,i),(2,i)])
            stop_game = True
            messagebox.showinfo("Winner", states[0][i] + " Menang!")
            return

    if states[0][0] == states[1][1] == states[2][2] != 0:
        highlight_winner([(0,0),(1,1),(2,2)])
        stop_game = True
        messagebox.showinfo("Winner", states[0][0] + " Menang!")
        return

    if states[0][2] == states[1][1] == states[2][0] != 0:
        highlight_winner([(0,2),(1,1),(2,0)])
        stop_game = True
        messagebox.showinfo("Winner", states[0][2] + " Menang!")
        return

    if all(states[i][j] != 0 for i in range(3) for j in range(3)):
        stop_game = True
        messagebox.showinfo("Tie", "Permainan Seri!")

def highlight_winner(coords):
    for r,c in coords:
        b[r][c].configure(bg="#ffcc00")  # Neon gold highlight

def reset_game():
    global Player1, stop_game, states
    Player1 = random.choice(["O", "X"])
    stop_game = False
    states = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            b[i][j].configure(text="", bg="#1a1a1a")
    if Player1 == "O":
        status_label.config(text="Giliran: PLAYER 1", fg="#00ffff")
    else:
        status_label.config(text="Giliran: PLAYER 2", fg="#ff9933")

# Design window
root = Tk()
root.title("Tic Tac Toe")  
root.resizable(0,0)
root.configure(bg="#000000")  # Black background

# Label atas: O vs X
title_label = Label(root, text="O    vs    X", font=("Helvetica", 20, "bold"), fg="#ffffff", bg="#000000")
title_label.grid(row=0, column=0, columnspan=3, pady=(10,0))

# Label bawah: PLAYER1 vs PLAYER2
role_label = Label(root, text="PLAYER 1        PLAYER 2", font=("Helvetica", 12, "bold"), fg="#00ffff", bg="#000000")
role_label.grid(row=1, column=0, columnspan=3)

# Button grid
b = [[0,0,0],[0,0,0],[0,0,0]]
states = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    for j in range(3): 
        b[i][j] = Button(
            height=4, width=8, 
            font=("Helvetica","20","bold"), 
            bg="#1a1a1a",  # dark tile
            fg="#ffffff",
            activebackground="#333333",
            command=lambda r=i, c=j: clicked(r,c))
        b[i][j].grid(row=i+2, column=j, padx=2, pady=2)

# Status giliran
if Player1 == "O":
    status_text = "Giliran: PLAYER 1"
    status_color = "#00ffff"
else:
    status_text = "Giliran: PLAYER 2"
    status_color = "#ff9933"

status_label = Label(root, text=status_text, font=("Helvetica","15","bold"),
                     fg=status_color, bg="#000000")
status_label.grid(row=5, column=0, columnspan=3)


# Tombol reset
reset_btn = Button(root, text="Reset Game", font=("Helvetica","12","bold"), command=reset_game, bg="#00cc66", fg="white")
reset_btn.grid(row=6, column=0, columnspan=3, pady=10)

root.mainloop()
