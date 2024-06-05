import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import pickle

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("400x300")

        
        self.weight_label = tk.Label(root, text="Weight (kg):")
        self.weight_label.pack()
        self.weight_entry = tk.Entry(root, width=20)
        self.weight_entry.pack()

        self.height_label = tk.Label(root, text="Height (m):")
        self.height_label.pack()
        self.height_entry = tk.Entry(root, width=20)
        self.height_entry.pack()

       
        self.calculate_button = tk.Button(root, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.pack()

       
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
 
       
        self.graph_button = tk.Button(root, text="View Historical Data", command=self.view_historical_data)
        self.graph_button.pack()

       
        self.user_data = {}

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())

            if weight <= 0 or height <= 0:
                messagebox.showerror("Error", "Invalid input. Please enter positive values.")
                return

            bmi = weight / (height ** 2)
            bmi_category = self.get_bmi_category(bmi)

            self.result_label.config(text=f"BMI: {bmi:.2f} ({bmi_category})")

           
            username = "default"  
            if username not in self.user_data:
                self.user_data[username] = []
            self.user_data[username].append((weight, height, bmi))

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def view_historical_data(self):
        username = "default" 
        if username not in self.user_data:
            messagebox.showerror("Error", "No historical data available.")
            return

        weights, heights, bmis = zip(*self.user_data[username])

        plt.plot(bmis)
        plt.xlabel("Measurement #")
        plt.ylabel("BMI")
        plt.title("BMI Trend")
        plt.show()

    def save_data(self):
        with open("user_data.pkl", "wb") as f:
            pickle.dump(self.user_data, f)

    def load_data(self):
        try:
            with open("user_data.pkl", "rb") as f:
                self.user_data = pickle.load(f)
        except FileNotFoundError:
            pass

    def run(self):
        self.load_data()
        self.root.mainloop()
        self.save_data()

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    app.run()