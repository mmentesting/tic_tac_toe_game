from tkinter import *
from tkinter import messagebox
from random import choice

def user_move(i):
    global PLAYER, IMAGE
    buttons[i].config(text=PLAYER, image=IMAGE, state="disabled")
    if not is_winner(buttons):
        switch_player()
        if not two_players:
            window.after(500, comp_move)
    else:
        disable_buttons()

def comp_move():
    global PLAYER, IMAGE
    b = choice(buttons)
    if b.cget("state") != "disabled":
        b.config(text=PLAYER, image=IMAGE, state="disabled")
        if not is_winner(buttons):
            switch_player()
        else:
            disable_buttons()
    else:
        comp_move()

def switch_player():
    global PLAYER, IMAGE
    if PLAYER == "X":
        PLAYER = "O"
        IMAGE = o_img
    else:
        PLAYER = "X"
        IMAGE = x_img
    headline.config(text=f"{PLAYER} Turn")

def is_winner(button_list):
    for i in range(0, 9, 3):  # horizontal check
        if button_list[i].cget("text") == button_list[i + 1].cget("text") == button_list[i + 2].cget("text") != "":
            headline.config(text=f"{PLAYER} You Win!")
            return True
    for i in range(3):  # vertical check
        if button_list[i].cget("text") == button_list[i + 3].cget("text") == button_list[i + 6].cget("text") != "":
            headline.config(text=f"{PLAYER} You Win!")
            return True
    if button_list[0].cget("text") == button_list[4].cget("text") == button_list[8].cget("text") != "" \
            or button_list[2].cget("text") == button_list[4].cget("text") == button_list[6].cget("text") != "":
        headline.config(text=f"{PLAYER} You Win!")
        return True
    if all("disabled" in b.cget("state") for b in button_list):
        headline.config(text="It's a Draw")
        return True
    return False

def disable_buttons():
    for b in buttons:
        b.config(state="disabled")

def new_game():
    global PLAYER, IMAGE
    for b in buttons:
        PLAYER = "X"
        IMAGE = x_img
        b.config(text="", image=b_img, state="active")
        headline.config(text=f"{PLAYER} Turn")

window = Tk()
window.title("Tic Tac Toe")

menubar = Menu(window)
window.config(bg="crimson", menu=menubar)
menu = Menu(menubar, tearoff=0)
menu.add_command(label="New Game", command=new_game)
menubar.add_cascade(label="File", menu=menu)
window.eval("tk::PlaceWindow . center")

two_players = messagebox.askyesno("Tic Tac Toe", "Switch to 2 players?")

b_img = PhotoImage(file="images/b.png")
x_img = PhotoImage(file="images/x.png")
o_img = PhotoImage(file="images/o.png")
IMAGE = x_img
PLAYER = "X"

headline = Label(text="X Turn", font=("ariel", 24, "bold", "italic"), bg="crimson", fg="white", pady=5)
headline.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

button_positions = []
for row in range(1, 4):
    for col in range(3):
        button_positions.append((row, col))
buttons = []
for index in range(len(button_positions)):
    button = Button(text="", image=b_img, command=lambda i=index: user_move(i))
    button.grid(row=button_positions[index][0], column=button_positions[index][1], padx=5, pady=5)
    buttons.append(button)

if __name__ == "__main__":
    window.mainloop()
