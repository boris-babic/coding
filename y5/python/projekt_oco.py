from tkinter import ttk, messagebox
import tkinter as tk
from datetime import datetime



def display_selection():
    # Get the selected value.
    mesiac = combo_mesiace_od.get()
    rok = combo_rok_od.get()
    pocet_dni = days_in_month(mesiac, rok)
    print(mesiac, rok, pocet_dni, month_to_number(mesiac))

main_window = tk.Tk()
main_window.config(width=500, height=300)
main_window.title("selector")

combo_mesiace_od = ttk.Combobox(
    state="readonly",
    values=["január", "február", "marec", "apríl", "máj", "jún", "júl", "august", "september", "október", "november", "december"]

)
combo_rok_od = ttk.Combobox(
    state="readonly",
    values=[str(x) for x in range(2024, 2050)]#roky
)
combo_mesiace_od.place(x=100, y=50)
combo_rok_od.place(x=250, y= 50)

label_od = tk.Label(main_window, text="od datumu")
label_od.place(x=25, y=50)
button = ttk.Button(text="Hotovo", command=display_selection)
button.place(x=50, y=200)


def is_leap_year(year):
    if int(year) % 400 == 0:
        return True
    elif int(year) % 100 == 0:
        return False
    elif int(year) % 4 == 0:
        return True
    else:
        return False

def days_in_month(month_name, year):
    mesiace = {
        "január": 31,
        "február": 28,
        "marec": 31,
        "apríl": 30,
        "máj": 31,
        "jún": 30,
        "júl": 31,
        "august": 31,
        "september": 30,
        "október": 31,
        "november": 30,
        "december": 31
    }
    month_name_lower = month_name.lower()
    if month_name_lower == "február" and is_leap_year(year):
        return 29
    elif month_name_lower in mesiace:
        return mesiace[month_name_lower]
    else:
        return "Neplatný mesiac"

def month_to_number(month_name):
    mesiace = {
        "január": 1,
        "február": 2,
        "marec": 3,
        "apríl": 4,
        "máj": 5,
        "jún": 6,
        "júl": 7,
        "august": 8,
        "september": 9,
        "október": 10,
        "november": 11,
        "december": 12
    }
    # Convert month name to lowercase to make it case-insensitive
    month_name_lower = month_name.lower()
    # Check if the provided month exists in the dictionary
    if month_name_lower in mesiace:
        return mesiace[month_name_lower]
    else:
        return "Neplatný mesiac"
    

main_window.mainloop()