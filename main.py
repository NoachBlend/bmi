# --------- import ---------
import tkinter as tk
from bmiapp import BmiApp

# --------- main program ---------
if __name__ == '__main__':
    root = tk.Tk()
    bmi_app = BmiApp(root)
    bmi_app.mainloop()
