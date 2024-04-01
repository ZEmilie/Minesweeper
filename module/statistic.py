import tkinter as tk
import os

import module.management as mg

class StatisticPage(tk.Frame):
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
        self.setting_img = mg.img_setting.subsample(2)
        self.btn_setting = tk.Button(self.barre, image=self.setting_img, bd=0, command=self.setting, bg=mg.n_bg)
        self.btn_setting.pack(side=tk.LEFT, padx=10, pady=5)

        # Page content
        self.frame_statistic = tk.Frame(self, bg=mg.bg)
        self.frame_statistic.pack(pady=20)

        self.images_difficult = mg.img_difficult
        self.textes_difficult = [
            "Débutant", "Intermédiaire", "Avancé"
        ]
        for i in range(3):
            image_level = tk.Label(self.frame_statistic, image=self.images_difficult[i],
                                   bg=mg.bg, width=250, height=150)
            image_level.grid(row=0, column=i, sticky="nsew")
            label_level = tk.Label(self.frame_statistic, text=self.textes_difficult[i],
                                   font=("Arial Bold", 20), bg=mg.bg, fg=mg.colors_difficult[i])
            label_level.grid(row=1, column=i, sticky="nsew", pady=20)
            best_time, n_win, n_lose = mg.get_statistic(i)
            label_win = tk.Label(self.frame_statistic, text=f"Partie gagnée : {n_win}",
                                   font=("Arial", 16), bg=mg.bg, fg=mg.colors_difficult[i])
            label_win.grid(row=2, column=i, sticky="nsew")
            label_lose = tk.Label(self.frame_statistic, text=f"Partie perdue : {n_lose}",
                                   font=("Arial", 16), bg=mg.bg, fg=mg.colors_difficult[i])
            label_lose.grid(row=3, column=i, sticky="nsew")
            label_time = tk.Label(self.frame_statistic, text=f"Meilleur temps : {best_time}",
                                   font=("Arial", 16), bg=mg.bg, fg=mg.colors_difficult[i])
            label_time.grid(row=4, column=i, sticky="nsew")


    def home(self):
        self.controller.show_page("home")

    def setting(self):
        self.controller.show_page("setting")

    def game(self):
        self.controller.show_page("game")