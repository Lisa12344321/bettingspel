from tkinter import *
import random

def spin_row():
    symbols = ["💸","💰","💎"]
    results = []

    for symbol in range(3):
        results.append(random.choice(symbols))
    
    the_row["text"] = results
    bet_entry["state"] = "normal"
    bet_button["state"] = "normal"
    spin["state"] = "disabled"

    global money
    global vinst
    #RESULTAT
    if results[0] == results[1] == results[2]:
        
        
        money = money + int(bet_entry.get())*vinst
        money_label["text"] = f"{money} $"
        win_label["text"] = f"Vinst! {str(bet_entry.get())} x {str(vinst)} \n + {int(bet_entry.get())*vinst} $"
        bet_entry.delete(0,END)

    else:
        entry_text = int(bet_entry.get())
        money = money-entry_text
        money_label["text"] = f"{money} $"
        win_label["text"] = f"Du vann inte \n - {bet_entry.get()} $"
        bet_entry.delete(0,END)
    
    

    return results

def bet():

    win_label["text"] = ""
    global money
    if money <= 0:
        bet_entry["state"] = "disabled"
        bet_button["state"] = "disabled"
        try_again_label["text"] = "Du har inga pengar kvar"

    while money > 0:
    
        
        bet_entry["state"] = "normal"
        entry_text = int(bet_entry.get())
        if entry_text <= money and entry_text > 0:
            try_again_label["text"] = ""
            the_row["text"] = ""
            bet_label["text"] = f"Din bet: {entry_text} $"
            bet_entry["state"] = "disabled"
            bet_button["state"] = "disabled"
            
            
            spin["state"] = "normal"
            break
        else:
            try_again_label["text"] = "Försök igen"
            break


root = Tk()
root.title("Spel")

frame = Frame(root)
frame.pack()

money = 1000
vinst = 4



money_label = Label(frame, text=f"{money} $")
money_label.grid(row=0, column=0)

bet_entry = Entry(frame)
bet_entry.grid(row=0, column=1)

try_again_label = Label(frame, text="")
try_again_label.grid(row=1, column=1)



bet_label = Label(frame, text=" ")
bet_label.grid(row=1, column=0)

bet_button = Button(frame, text="Betta", command=bet)
bet_button.grid(row=0, column=1, sticky=E)



the_row = Label(frame, text ="", font=20)
the_row.grid(row=2, column=0)


spin = Button(frame, text="SPIN", font=20, command=spin_row)
spin["state"] = "disabled"
spin.grid(row=3, column=0)

win_label = Label(frame, text="")
win_label.grid(row=2, column=1)




root.mainloop()