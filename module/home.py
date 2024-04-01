import tkinter as tk

import module.management as mg
from module.game import GamePage

class HomePage(tk.Frame):
    def __init__(self, parent, controller, title):
        super().__init__(parent)
        self.controller = controller
        self.title = title
        self.config(bg=mg.bg)
        self.place(relx=0.5, rely=0.5, anchor="center")
        mg.init_img()

        # Page content
        label = tk.Label(self, text="Démineur", font=("Arial Bold", 26), bg=mg.bg)
        label.pack(expand=True)

        # Image and text according to level
        self.image_difficult = tk.Label(self)
        self.image_difficult.pack(expand=True)
        self.images_difficult = mg.img_difficult
        self.image_difficult.config(image=self.images_difficult[0], bg=mg.bg)
        self.textes_difficult = [
            "Débutant", "Intermédiaire", "Avancé", "Personnalisé"
        ]
        self.label_difficult = tk.Label(self, text=self.textes_difficult[0], font=("Arial Bold", 20),
                                        bg=mg.bg, fg=mg.colors_difficult[0])
        self.label_difficult.pack(expand=True)

        # Four-value slider
        self.slider = tk.Scale(self, from_=0, to=3, resolution=1, orient="horizontal", showvalue=0,
                               length=150, highlightthickness=0, troughcolor="white", bg=mg.colors_difficult[0],
                               command=self.save_difficult)
        self.slider.pack(expand=True)

        # Width, Length, Mines
        self.setting_frame = tk.Frame(self, bg=mg.bg)
        self.setting_frame.pack(expand=True)

        self.width_frame = tk.Frame(self.setting_frame, bg=mg.bg)
        self.width_frame.pack(fill="x")
        self.width_label = tk.Label(self.width_frame, text="Largeur :", bg=mg.bg, width=10, height=2)
        self.width_label.pack(side="left", padx=2, pady=2)
        self.width_value = tk.StringVar(self)
        self.width_value.set(mg.wlm_difficult[0][0])
        self.width_spinbox = tk.Spinbox(self.width_frame, from_=5, to=40, width=5, 
                                        textvariable=self.width_value,
                                        command=self.save_setting)
        self.width_spinbox.pack(side="left", padx=2, pady=2)

        self.length_frame = tk.Frame(self.setting_frame, bg=mg.bg)
        self.length_frame.pack(fill="x")
        self.length_label = tk.Label(self.length_frame, text="Longueur :", bg=mg.bg, width=10, height=2)
        self.length_label.pack(side="left", padx=2, pady=2)
        self.length_value = tk.StringVar(self)
        self.length_value.set(mg.wlm_difficult[0][1])
        self.length_spinbox = tk.Spinbox(self.length_frame, from_=5, to=20, width=5, 
                                         textvariable=self.length_value,
                                         command=self.save_setting)
        self.length_spinbox.pack(side="left", padx=2, pady=2)

        self.mine_frame = tk.Frame(self.setting_frame, bg=mg.bg)
        self.mine_frame.pack(fill="x")
        self.mine_label = tk.Label(self.mine_frame, text="Mines :", bg=mg.bg, width=10, height=2)
        self.mine_label.pack(side="left", padx=2, pady=2)
        self.mine_value = tk.StringVar(self)
        self.mine_value.set(mg.wlm_difficult[0][2])
        self.mine_spinbox = tk.Spinbox(self.mine_frame, from_=1, to=250, width=5, 
                                       textvariable=self.mine_value,
                                       command=self.save_setting)
        self.mine_spinbox.pack(side="left", padx=2, pady=2)

        # Button Frame
        self.button_frame = tk.Frame(self, bg=mg.bg)
        self.button_frame.pack(expand=True)

        self.statistic_img = mg.img_graph.subsample(2)
        self.btn_statistic = tk.Button(self.button_frame,
                                       image=self.statistic_img, bd=0,
                                       command=self.statistic, bg=mg.bg)
        self.btn_statistic.pack(side="left", padx=10)

        self.btn_game = tk.Button(self.button_frame, text="Jouer", command=self.game)
        self.btn_game.config(width=10, height=2,
                             font=("Arial Bold", 12), relief=tk.RAISED,
                             fg="white", bg=mg.colors_difficult[0])
        self.btn_game.pack(side="left", padx=10)

        self.setting_img = mg.img_setting.subsample(2)
        self.btn_setting = tk.Button(self.button_frame,
                                     image=self.setting_img, bd=0,
                                     command=self.setting, bg=mg.bg)
        self.btn_setting.pack(side="left", padx=10)

        # Read recorded cursor values from JSON file
        self.load_difficult()

        # Link the "Space" key to the button click event
        self.btn_game.focus_set()
        self.bind("<Return>", self.start_game_enter)


    def load_setting(self):
        w,l,m = mg.get_wlm()
        if w is not None:
            self.width_value.set(w)
            self.width_spinbox.config(textvariable=self.width_value)
        if l is not None:
            self.length_value.set(l)
            self.length_spinbox.config(textvariable=self.length_value)
        if m is not None:
            self.mine_value.set(m)
            self.mine_spinbox.config(textvariable=self.mine_value)

    def update_difficult(self):
        value = self.slider.get()
        self.image_difficult.config(image=self.images_difficult[value])
        self.label_difficult.config(text=self.textes_difficult[value], fg=mg.colors_difficult[value])
        self.slider.config(bg=mg.colors_difficult[value])
        self.btn_game.config(bg=mg.colors_difficult[value])
        if value==3:
            self.load_setting()
            self.width_spinbox.config(state="normal")
            self.length_spinbox.config(state="normal")
            self.mine_spinbox.config(state="normal")
        else:
            self.width_spinbox.config(state="disabled")
            self.length_spinbox.config(state="disabled")
            self.mine_spinbox.config(state="disabled")
            self.width_value.set(mg.wlm_difficult[value][0])
            self.width_spinbox.config(textvariable=self.width_value)
            self.length_value.set(mg.wlm_difficult[value][1])
            self.length_spinbox.config(textvariable=self.length_value)
            self.mine_value.set(mg.wlm_difficult[value][2])
            self.mine_spinbox.config(textvariable=self.mine_value)

    def load_difficult(self):
        difficult = mg.get_difficult()
        self.slider.set(difficult)
        self.update_difficult()

    def save_difficult(self,event):
        self.update_difficult()
        value = self.slider.get()
        mg.set_difficult(value)

    def save_setting(self):
        difficult = self.slider.get()
        if difficult==3:
            w = self.width_spinbox.get()
            l = self.length_spinbox.get()
            m = self.mine_spinbox.get()
            max_mines = int(w)*int(l)//2
            self.mine_spinbox.config(to=max_mines)
            mg.set_wlm(w,l,m)

    def game(self):
        self.controller.refresh_game_page()
        self.controller.show_page("game")

    def statistic(self):
        self.controller.show_page("statistic")

    def setting(self):
        self.controller.show_page("setting")

    def start_game_enter(self, event):
        self.game()