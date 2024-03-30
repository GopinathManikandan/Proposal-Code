import tkinter as tk
import random
def show_popup():
    popup = tk.Toplevel(root)
    popup.title("Popup")
    label = tk.Label(popup, text=("Thanks for Accepting My Love !!"),font=("","15",""))
    label.pack(padx=50, pady=50)
def move_button(event):
    x = random.randint(0, 550)
    y = random.randint(0, 550)
    no_button.place(x=x, y=y)
root = tk.Tk()
root.title("Funny Luv")
root.geometry("1800x980")
root.config(bg="pink")
question_label = tk.Label(root, text="I Love You!....\n\n Do you like me?",font=(""","18","""))
question_label.pack(pady=57)
yes_button = tk.Button(root, text="Yes", font=("","14",""), command=show_popup)
yes_button.pack()
no_button = tk.Button(root, text="No",font=("","14",""))
no_button.pack()
no_button.bind("<Enter>", move_button)
