import tkinter as tk
import os

from module.home import img, bg, settings_difficult, n_bg, game_data

class GamePage(tk.Frame):
    def __init__(self, parent, controller, title):
        super().__init__(parent)
        self.controller = controller
        self.title = title
        self.config(bg=bg)

        # Barre d'option
        self.barre = tk.Frame(self, bg=n_bg)
        self.barre.pack(side=tk.TOP, fill=tk.X)
        self.home_img = tk.PhotoImage(file=os.path.join(img, "home.png")).subsample(2)
        self.btn_home = tk.Button(self.barre, image=self.home_img, bd=0, command=self.home, bg=n_bg)
        self.btn_home.pack(side=tk.LEFT, padx=10, pady=5)
        self.setting_img = tk.PhotoImage(file=os.path.join(img, "engrenage.png")).subsample(2)
        self.btn_setting = tk.Button(self.barre, image=self.setting_img, bd=0, command=self.setting, bg=n_bg)
        self.btn_setting.pack(side=tk.LEFT, padx=10, pady=5)
        self.statistic_img = tk.PhotoImage(file=os.path.join(img, "graphique.png")).subsample(2)
        self.btn_statistic = tk.Button(self.barre, image=self.statistic_img, bd=0, command=self.statistic, bg=n_bg)
        self.btn_statistic.pack(side=tk.LEFT, padx=10, pady=5)

        # Contenu de la page du jeu
        

    def home(self):
        self.controller.show_page("home")

    def statistic(self):
        self.controller.show_page("statistic")

    def setting(self):
        self.controller.show_page("setting")