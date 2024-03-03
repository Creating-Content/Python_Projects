import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.password_var = tk.StringVar()
        self.length_var = tk.IntVar(value=12)
        self.include_upper_var = tk.BooleanVar()
        self.include_lower_var = tk.BooleanVar()
        self.include_digits_var = tk.BooleanVar()
        self.include_symbols_var = tk.BooleanVar()

        self.create_widgets()

    def create_widgets(self):
        # Password Label and Entry
        ttk.Label(self.root, text="Generated Password:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.password_var, state="readonly").grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        # Length Label and Entry
        ttk.Label(self.root, text="Length:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        length_entry = ttk.Entry(self.root, textvariable=self.length_var)
        length_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        length_entry.bind('<FocusOut>', self.validate_length)

        # Checkboxes for character types
        ttk.Checkbutton(self.root, text="Include Uppercase", variable=self.include_upper_var).grid(row=2, column=0, sticky="w", padx=10, pady=5)
        ttk.Checkbutton(self.root, text="Include Lowercase", variable=self.include_lower_var).grid(row=3, column=0, sticky="w", padx=10, pady=5)
        ttk.Checkbutton(self.root, text="Include Digits", variable=self.include_digits_var).grid(row=4, column=0, sticky="w", padx=10, pady=5)
        ttk.Checkbutton(self.root, text="Include Symbols", variable=self.include_symbols_var).grid(row=5, column=0, sticky="w", padx=10, pady=5)

        # Generate Button
        ttk.Button(self.root, text="Generate Password", command=self.generate_password).grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        # Copy Button
        ttk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard).grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    def validate_length(self, event):
        try:
            length = int(self.length_var.get())
            if length <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Length must be a positive integer.")
            self.length_var.set(12)

    def generate_password(self):
        length = self.length_var.get()

        character_set = ""
        if self.include_upper_var.get():
            character_set += string.ascii_uppercase
        if self.include_lower_var.get():
            character_set += string.ascii_lowercase
        if self.include_digits_var.get():
            character_set += string.digits
        if self.include_symbols_var.get():
            character_set += string.punctuation

        if not character_set:
            messagebox.showerror("Error", "Please select at least one character type.")
            return

        password = ''.join(random.choice(character_set) for _ in range(length))
        self.password_var.set(password)

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard.")
        else:
            messagebox.showerror("Error", "No password generated yet.")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
