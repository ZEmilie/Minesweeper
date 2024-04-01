import tkinter as tk
import os

import module.management as mg

class SettingPage(tk.Frame):
    def __init__(self, parent, controller, title):
        super().__init__(parent)
        self.controller = controller
        self.title = title
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
        label = tk.Label(self, text="Bienvenue dans le jeu Démineur!", font=("Helvetica", 16))
        label.pack(pady=10)

    def home(self):
        self.controller.show_page("home")

    def statistic(self):
        self.controller.show_page("statistic")

    def game(self):
        self.controller.show_page("game")