import tkinter as tk
from person import Person


class BmiApp(tk.Frame):
    """UI class for BMI calculation"""
    __BG_LIGHT = "#A0A0A0"
    __BG_DARK = "#707070"

    def __init__(self, master=None):
        """Constructor"""
        super().__init__(master)
        self.root = master
        self.pack(fill="both", expand=True)
        self.person = Person(name="Unknown")
        # predefined widgets
        self.frm_name = None
        self.frm_height = None
        self.frm_weight = None
        self.lbl_name = None
        self.lbl_height = None
        self.lbl_weight = None
        self.lbl_bmi = None
        self.lbl_status_bar = None
        self.inp_name = None
        self.inp_height = None
        self.inp_weight = None
        self.btn_calculate = None
        # validate commands
        self.validate_float = (self.register(self.check_input), '%P')
        # create the real widgets
        self.__create_widgets()
        # set the root info
        self.root.title('Calculate BMI')
        self.root.update()
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height() + 100)

    def __create_widgets(self):
        """Place all visual components on the screen"""
        # ---------- Name frame ----------
        self.frm_name = tk.Frame(self, borderwidth=6, bg=self.__class__.__BG_DARK)
        self.frm_name.pack(side="top", fill="x")

        # Label for name
        self.lbl_name = tk.Label(self.frm_name,
                                 text="Give your name: ",
                                 width=20,
                                 anchor=tk.E
                                 )
        self.lbl_name.pack(side="left")

        # Input for name
        self.inp_name = tk.Entry(self.frm_name,
                                 highlightthickness=1,
                                 highlightcolor='yellow', )
        self.inp_name.insert(0, self.person.name)
        self.inp_name.pack(side="left", fill="x", expand=True, padx=10)

        # ---------- Length frame ----------
        self.frm_height = tk.Frame(self, borderwidth=6, bg=self.__class__.__BG_DARK)
        self.frm_height.pack(side="top", fill="x")

        # Label for length
        self.lbl_height = tk.Label(self.frm_height,
                                   text="Length in m: ",
                                   width=20,
                                   anchor=tk.E
                                   )
        self.lbl_height.pack(side="left")

        # Input for length
        self.inp_height = tk.Entry(self.frm_height,
                                   highlightthickness=1,
                                   highlightcolor='yellow',
                                   validate='key',
                                   validatecommand=self.validate_float)
        self.inp_height.pack(side="left", fill="x", expand=True, padx=10)

        # ---------- Weight frame ----------
        self.frm_weight = tk.Frame(self, borderwidth=6, bg=self.__class__.__BG_DARK)
        self.frm_weight.pack(side="top", fill="x")

        # Label for weight
        self.lbl_weight = tk.Label(self.frm_weight,
                                   text="Weight given in kg: ",
                                   width=20,
                                   anchor=tk.E
                                   )
        self.lbl_weight.pack(side="left")

        # Input for weight
        self.inp_weight = tk.Entry(self.frm_weight,
                                   highlightthickness=1,
                                   highlightcolor='yellow',
                                   validate='key',
                                   validatecommand=self.validate_float)
        self.inp_weight.pack(side="left", fill="x", expand=True, padx=10)

        # --------- Text ----------
        self.lbl_bmi = tk.Label(self)
        self.lbl_bmi.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        # --------- Status bar ---------
        self.lbl_status_bar = tk.Label(self, text="Status: OK", bg="#FFFFFF", bd=2, relief=tk.SUNKEN, anchor=tk.W)
        self.lbl_status_bar.pack(side="bottom", fill="x")

        # --------- Button ----------
        self.btn_calculate = tk.Button(self,
                                       text="Calculate BMI",
                                       bg=self.__class__.__BG_DARK,
                                       command=self.show_bmi,
                                       )
        self.btn_calculate.pack(side="bottom", fill="x", padx=10, pady=2)

    def show_bmi(self):
        """Calculate and show bmi info """
        self.person.name = self.inp_name.get()
        try:
            self.person.height = float(self.inp_height.get())
            self.person.weight = float(self.inp_weight.get())
        except ValueError as err:
            self.lbl_status_bar["text"] = f"Status: ERROR --> {err}"
            self.lbl_status_bar["bg"] = "#FF0000"
        else:
            self.lbl_bmi["text"] = self.person.print_bmi_string()
            self.lbl_status_bar["text"] = "Status: OK"
            self.lbl_status_bar["bg"] = "#FFFFFF"

    @staticmethod
    def check_input(is_allowed_text):
        """Check inputfield if it is emty or a float"""
        try:
            if not is_allowed_text or float(is_allowed_text):
                return True
        except ValueError:
            return False
