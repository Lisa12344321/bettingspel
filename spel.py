import tkinter as tk
import random

def spin_row():
    symbols = ["🍿","🍰","🍔"]
    results = []

    for symbol in range(3):
        results.append(random.choice(symbols))
    
    the_row["text"] = results

    return results

def bet():

    global money

    while money > 0:
    
        entry_text = int(bet_entry.get())
        if entry_text > money or entry_text < 0:
            print("nej")

        
        bet_label["text"] = f"Din bet: {entry_text} kr"
        bet_entry["state"] = "disabled"
        
        money = money-entry_text
        money_label["text"] = f"Pengar: {money} kr"
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

    


bet_label = tk.Label(root, text=" ")
bet_label.grid(row=1, column=0)

bet_button = tk.Button(root, text="Betta", command=lambda: bet())
bet_button.grid(row=0, column=1, sticky=tk.E)



the_row = tk.Label(root, text ="", font=20)
the_row.grid(row=2, column=0)


spin = tk.Button(root, text="SPIN", font=20, command=lambda: spin_row())
spin.grid(row=3, column=0)






root.mainloop()