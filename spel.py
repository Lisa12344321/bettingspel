import tkinter as tk
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
    #RESULTAT
    if results[0] == results[1] == results[2]:
        print("jaaa")
        
        money = money + int(bet_entry.get())*2
        money_label["text"] = f"Pengar: {money} kr"
        win_label["text"] = f"Du vann! Din bet x2: {int(bet_entry.get())*2} kr"

    else:
        print("nej")
        win_label["text"] = "Du vann inte"
    
    

    return results

def bet():

    win_label["text"] = ""
    global money
    if money <= 0:
        bet_entry["state"] = "disabled"
        bet_button["state"] = "disabled"
        try_again_label["text"] = "Du har inga pengar kvar"
        print(":(")

    while money > 0:
    
        
        bet_entry["state"] = "normal"
        entry_text = int(bet_entry.get())
        if entry_text <= money and entry_text > 0:
            try_again_label["text"] = ""
            the_row["text"] = ""
            bet_label["text"] = f"Din bet: {entry_text} kr"
            bet_entry["state"] = "disabled"
            bet_button["state"] = "disabled"
            
            money = money-entry_text
            money_label["text"] = f"Pengar: {money} kr"
            spin["state"] = "normal"
            break
        else:
            try_again_label["text"] = "Försök igen"
            break
    




def pay():
    pass


root = tk.Tk()
root.title("Spel")

money = 100



money_label = tk.Label(root, text=f"Pengar: {money} kr")
money_label.grid(row=0, column=0)

bet_entry = tk.Entry(root)
bet_entry.grid(row=0, column=1)

try_again_label = tk.Label(root, text="")
try_again_label.grid(row=1, column=1)



bet_label = tk.Label(root, text=" ")
bet_label.grid(row=1, column=0)

bet_button = tk.Button(root, text="Betta", command=bet)
bet_button.grid(row=0, column=1, sticky=tk.E)



the_row = tk.Label(root, text ="", font=20)
the_row.grid(row=2, column=0)


spin = tk.Button(root, text="SPIN", font=20, command=spin_row)
spin["state"] = "disabled"
spin.grid(row=3, column=0)

win_label = tk.Label(root, text="")
win_label.grid(row=2, column=1)




root.mainloop()