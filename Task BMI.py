import tkinter as tk
from tkinter import messagebox

# ---------- BMI Calculation Function ----------
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        # Determine BMI status
        if bmi < 18.5:
            status = "Underweight"
        elif bmi < 24.9:
            status = "Normal"
        elif bmi < 29.9:
            status = "Overweight"
        else:
            status = "Obese"

        result_label.config(text=f"BMI: {bmi}")
        status_label.config(text=f"Status: {status}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

# ---------- Main Window ----------
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("350x300")
window.resizable(False, False)

# ---------- Heading ----------
title_label = tk.Label(
    window,
    text="BMI Calculator",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=10)

# ---------- Weight Input ----------
weight_label = tk.Label(window, text="Enter Weight (kg)")
weight_label.pack()
weight_entry = tk.Entry(window, width=20)
weight_entry.pack(pady=5)

# ---------- Height Input ----------
height_label = tk.Label(window, text="Enter Height (meters)")
height_label.pack()
height_entry = tk.Entry(window, width=20)
height_entry.pack(pady=5)

# ---------- Calculate Button ----------
calculate_button = tk.Button(
    window,
    text="Calculate BMI",
    font=("Arial", 10, "bold"),
    bg="#4CAF50",
    fg="white",
    command=calculate_bmi
)
calculate_button.pack(pady=15)

# ---------- Result Display ----------
result_label = tk.Label(window, text="BMI: --", font=("Arial", 12))
result_label.pack(pady=5)

status_label = tk.Label(window, text="Status: --", font=("Arial", 12))
status_label.pack(pady=5)

# ---------- Run Window ----------
window.mainloop()