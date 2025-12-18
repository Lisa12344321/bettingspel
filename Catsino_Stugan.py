from tkinter import *
import random
from tkinter import messagebox

def spin_row():

    

    symbols = [katt_1,katt_2,katt_3]
    results = []

    for symbol in range(3):
        results.append(random.choice(symbols))
    
    
    the_row.config(image=results[0])
    the_row2.config(image=results[1])
    the_row3.config(image=results[2])
    bet_entry["state"] = "normal"
    bet_button["state"] = "normal"
    spin["state"] = "disabled"

    global money
    global vinst
    #RESULTAT
    if results[0] == results[1] == results[2]:
        
        if results[0] == katt_1:
            money = money + int(bet_entry.get())*vinst
            money_label["text"] = f"{money} $"
            win_label["text"] = f"Vinst! {str(bet_entry.get())} x {str(vinst)} \n + {int(bet_entry.get())*vinst} $"
            bet_entry.delete(0,END)
        
        elif results[0] == katt_2:
            money = money + int(bet_entry.get())*vinst*2
            money_label["text"] = f"{money} $"
            win_label["text"] = f"Vinst! {str(bet_entry.get())} x {str(vinst*2)} \n + {int(bet_entry.get())*vinst*2} $"
            bet_entry.delete(0,END)

        else:
            money = money + int(bet_entry.get())*vinst*4
            money_label["text"] = f"{money} $"
            win_label["text"] = f"Vinst! {str(bet_entry.get())} x {str(vinst*4)} \n + {int(bet_entry.get())*vinst*4} $"
            bet_entry.delete(0,END)

    else:
        entry_text = int(bet_entry.get())
        money = money-entry_text
        money_label["text"] = f"{money} $"
        win_label["text"] = f"Du vann inte \n - {str(bet_entry.get())} $"
        bet_entry.delete(0,END)
    
    

    return results

def bet(event):

    win_label["text"] = ""
    global money
    if money <= 0:
        bet_entry["state"] = "disabled"
        bet_button["state"] = "disabled"
        try_again_label["text"] = "Du har inga pengar kvar"

        if messagebox.askyesno(message="Spela igen?"):
            money = 1000
            money_label["text"] = f"{money} $"
            bet_entry.delete(0,END)
            bet_entry["state"] = "normal"
            bet_button["state"] = "normal"
            try_again_label["text"] = ""
            bet_label["text"] = ""
            
        else:
            root.destroy()

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
root.title("Catsino Stugan")
root.geometry("1920x1080")

icon = PhotoImage(file="ikon-pengar.png")
root.iconphoto(True, icon)

root.config(bg="#000000")

frame = Frame(root, bg="#000000")
frame.pack()

money = 1000
vinst = 3

katt_1 = PhotoImage(file="katt1-edit.png")
katt_2 = PhotoImage(file="åke-edit.png")
katt_3 = PhotoImage(file="herman-edit.png")

logga = PhotoImage(file="catsino-logga.png")
logga_label = Label(frame, image=logga, bg="#000000")
logga_label.grid(row=0, column=0, columnspan=2, pady= 20)


money_label = Label(frame, text=f"{money} $", font=20, fg="#00FF00", bg="#000000")
money_label.grid(row=1, column=0)

bet_entry = Entry(frame, font=20, fg="#00FF00", bg="#262626")
bet_entry.grid(row=1, column=1, padx=20, pady=30)

try_again_label = Label(frame, text="", font=20, fg="#00FF00", bg="#000000")
try_again_label.grid(row=2, column=1)



bet_label = Label(frame, text="", font=20, fg="#00FF00", bg="#000000")
bet_label.grid(row=2, column=0)

bet_button = Button(frame, text="Betta", command=bet, font=20, fg="#00FF00", bg="#000000")
root.bind("<Return>", bet)
bet_button.bind("<Button-1>", bet)

bet_button.grid(row=1, column=1, sticky=E)

#---------------------------------------------

the_row = Label(frame, font=20, bg="#000000")
the_row.grid(row=4, column=0, columnspan=2, pady=10, sticky=W)

the_row2 = Label(frame, font=20, bg="#000000")
the_row2.grid(row=4, column=0, columnspan=2, pady=10)

the_row3 = Label(frame, font=20, bg="#000000")
the_row3.grid(row=4, column=0, columnspan=2, pady=10, sticky=E)

#------------------------------------------------

spin = Button(frame, text="SPIN", font=20, command=spin_row, bg= "#00FF00")
spin["state"] = "disabled"
spin.grid(row=5, column=0, columnspan=2, pady=20)


win_label = Label(frame, text="", font=20, fg="#00FF00", bg="#000000")
win_label.grid(row=3, column=0, columnspan=2)




root.mainloop()