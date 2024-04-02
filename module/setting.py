import tkinter as tk
from tkinter import ttk

import module.management as mg
import module.text as tt

class SettingPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title = tt.setting_title
        self.config(bg=mg.bg)

        # Menu bar
        self.barre = tk.Frame(self, bg=mg.n_bg)
        self.barre.pack(side=tk.TOP, fill=tk.X)
        self.home_img = mg.img_home.subsample(2)
        self.btn_home = tk.Button(self.barre, image=self.home_img, bd=0, command=self.home, bg=mg.n_bg)
        self.btn_home.pack(side=tk.LEFT, padx=10, pady=5)
        self.game_img = mg.img_game.subsample(2)
        self.btn_game = tk.Button(self.barre, image=self.game_img, bd=0, command=self.game, bg=mg.n_bg)
        self.btn_game.pack(side=tk.LEFT, padx=10, pady=5)
        self.statistic_img = mg.img_graph.subsample(2)
        self.btn_statistic = tk.Button(self.barre, image=self.statistic_img, bd=0, command=self.statistic, bg=mg.n_bg)
        self.btn_statistic.pack(side=tk.LEFT, padx=10, pady=5)

        # Page content
        label = tk.Label(self, text=tt.setting_title, font=("Arial Bold", 26), bg=mg.bg)
        label.pack(pady=40)

        self.var = tk.StringVar(self)
        self.var.set(list(mg.language_possibility.keys())[0])
        combobox = ttk.Combobox(self, textvariable=self.var)
        combobox['values'] = list(mg.language_possibility.keys())
        combobox.pack(pady=40)

        self.btn_validate = tk.Button(self, text=tt.validate, command=self.validate)
        self.btn_validate.config(width=15, height=2, font=("Arial Bold", 12), relief=tk.RAISED,
                             fg="white", bg=mg.n_bg)
        self.btn_validate.pack(pady=80)


    def home(self):
        self.controller.show_page("home")

    def statistic(self):
        self.controller.show_page("statistic")

    def game(self):
        self.controller.show_page("game")

    def validate(self):
        self.controller.grab_set()
        self.confirm_window = tk.Toplevel(self)
        window_width = 400
        window_height = 100
        x = (self.winfo_screenwidth() - window_width) // 2
        y = (self.winfo_screenheight() - window_height - 100) // 2
        self.confirm_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.confirm_window.title(tt.confirm_title)
        self.confirm_window.protocol("WM_DELETE_WINDOW", self.return_main_window)
        label = tk.Label(self.confirm_window, text=tt.confirm_message[0], padx=20, pady=20)
        label.pack()
        self.button_frame = tk.Frame(self.confirm_window)
        self.button_frame.pack()
        btn_yes = tk.Button(self.button_frame, text=tt.confirm_message[1], width=5, height=1,
                            relief=tk.RAISED, command=self.update_app_language)
        btn_yes.pack(side=tk.LEFT, padx=10)
        btn_no = tk.Button(self.button_frame, text=tt.confirm_message[2], width=5, height=1,
                           relief=tk.RAISED, command=self.return_main_window)
        btn_no.pack(side=tk.LEFT, padx=10)

    def update_app_language(self):
        selected_language = mg.language_possibility[self.var.get()]
        mg.set_language(selected_language)
        tt.update_language(selected_language)
        self.return_main_window()
        self.controller.refresh_all_page()
        self.controller.show_page("home")
    
    def return_main_window(self):
        self.confirm_window.destroy()
        self.controller.grab_release()