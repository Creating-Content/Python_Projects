import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# BMI Categories
BMI_CATEGORIES = {
    (0, 18.5): 'Underweight',
    (18.5, 24.9): 'Normal weight',
    (25, 29.9): 'Overweight',
    (30, float('inf')): 'Obesity'
}

class BMI_Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("BMI Calculator")

        self.label_weight = tk.Label(master, text="Enter Weight (kg):")
        self.label_weight.grid(row=0, column=0)
        self.entry_weight = tk.Entry(master)
        self.entry_weight.grid(row=0, column=1)

        self.label_height = tk.Label(master, text="Enter Height (cm):")
        self.label_height.grid(row=1, column=0)
        self.entry_height = tk.Entry(master)
        self.entry_height.grid(row=1, column=1)

        self.button_calculate = tk.Button(master, text="Calculate BMI", command=self.calculate_bmi)
        self.button_calculate.grid(row=2, columnspan=2)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=3, columnspan=2)

        self.history = []

    def calculate_bmi(self):
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get()) / 100  # convert height to meters
            bmi = weight / (height ** 2)

            for key in BMI_CATEGORIES:
                if key[0] < bmi <= key[1]:
                    category = BMI_CATEGORIES[key]
                    break

            self.result_label.config(text=f"BMI: {bmi:.2f}, Category: {category}")
            self.history.append((weight, height, bmi, category))

        except ValueError:
            messagebox.showerror("Error", "Please enter valid weight and height.")

    def plot_history(self):
        weights = [record[0] for record in self.history]
        heights = [record[1] for record in self.history]
        bmis = [record[2] for record in self.history]

        plt.figure(figsize=(10, 5))
        plt.plot(weights, bmis, marker='o', linestyle='-', color='b')
        plt.xlabel('Weight (kg)')
        plt.ylabel('BMI')
        plt.title('BMI Trend Analysis')
        plt.grid(True)
        plt.show()

def main():
    root = tk.Tk()
    app = BMI_Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
