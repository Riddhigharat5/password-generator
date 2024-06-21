import tkinter as tk
from tkinter import messagebox
import string
import random

# Function to generate a password
def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer")
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")
        return

    include_uppercase = var_uppercase.get()
    include_digits = var_digits.get()
    include_special = var_special.get()

    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "No character sets selected")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    entry_password.config(state=tk.NORMAL)
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)
    entry_password.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place the widgets
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(pady=10)

label_length = tk.Label(frame, text="Password Length:")
label_length.grid(row=0, column=0, padx=5, pady=5)

entry_length = tk.Entry(frame)
entry_length.insert(0, "12")  # Set default value to 12
entry_length.grid(row=0, column=1, padx=5, pady=5)

var_uppercase = tk.BooleanVar()
check_uppercase = tk.Checkbutton(frame, text="Include Uppercase", variable=var_uppercase)
check_uppercase.grid(row=1, columnspan=2, padx=5, pady=5)

var_digits = tk.BooleanVar()
check_digits = tk.Checkbutton(frame, text="Include Digits", variable=var_digits)
check_digits.grid(row=2, columnspan=2, padx=5, pady=5)

var_special = tk.BooleanVar()
check_special = tk.Checkbutton(frame, text="Include Special Characters", variable=var_special)
check_special.grid(row=3, columnspan=2, padx=5, pady=5)

button_generate = tk.Button(frame, text="Generate Password", command=generate_password)
button_generate.grid(row=4, columnspan=2, pady=10)

entry_password = tk.Entry(frame, width=30)
entry_password.grid(row=5, columnspan=2, padx=5, pady=5)
entry_password.config(state=tk.DISABLED)  # Initially disable the entry field

# Run the application
root.mainloop()