from tkinter import *
import random, string
import pyperclip

# ---- Setup Window ----
root = Tk()
root.geometry("500x400")
root.resizable(0, 0)
root.title("🔥 Password Generator")
root.config(bg="#2c3e50")

# ---- Header ----
Label(root, text='🔐 PASSWORD GENERATOR', font=('Helvetica', 18, 'bold'), bg="#2c3e50", fg="white").pack(pady=10)
Label(root, text='Built with Python 🐍', font=('Helvetica', 10), bg="#2c3e50", fg="white").pack(side=BOTTOM, pady=10)

# ---- Frame for Body ----
frame = Frame(root, bg="#34495e")
frame.pack(pady=20, padx=20)

# ---- Password Length Input ----
Label(frame, text='Password Length:', font=('Helvetica', 12), bg="#34495e", fg="white").grid(row=0, column=0, pady=10, padx=10)
pass_len = IntVar(value=12)
Spinbox(frame, from_=8, to_=32, textvariable=pass_len, width=5, font=('Helvetica', 12)).grid(row=0, column=1, pady=10)

# ---- Password Output ----
pass_str = StringVar()
Entry(frame, textvariable=pass_str, font=('Helvetica', 14), width=30, bd=2).grid(row=1, column=0, columnspan=2, pady=10)

# ---- Functions ----
def Generator():
    length = pass_len.get()
    password = []

    if length >= 4:
        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]
        password += random.choices(string.ascii_letters + string.digits + string.punctuation, k=length - 4)
        random.shuffle(password)
    else:
        password = random.choices(string.ascii_letters + string.digits + string.punctuation, k=length)

    pass_str.set(''.join(password))

def Copy_password():
    pyperclip.copy(pass_str.get())

# ---- Buttons ----
Button(frame, text='Generate 🔁', command=Generator, bg="#27ae60", fg="white", font=('Helvetica', 12, 'bold'), width=20).grid(row=2, column=0, columnspan=2, pady=10)
Button(frame, text='Copy 📋', command=Copy_password, bg="#2980b9", fg="white", font=('Helvetica', 12, 'bold'), width=20).grid(row=3, column=0, columnspan=2, pady=5)

# ---- Run App ----
root.mainloop()
