import tkinter as tk
import os
import json

img = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..\img')
game_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..\data')
if not os.path.exists(game_data):
    os.makedirs(game_data)
bg = "#fffbf0"
n_bg = "#4cc7ff"
colors_difficult = ["#b3ff72", "#ffc160", "#cb1446", n_bg]
settings_difficult = [
    [9,9,10],
    [16,16,40],
    [30,16,99]
]

class HomePage(tk.Frame):
    def __init__(self, parent, controller, title):
        super().__init__(parent)
        self.controller = controller
        self.title = title
        self.config(bg=bg)
        self.place(relx=0.5, rely=0.5, anchor="center")

        # Créer le contenu de la page
        label = tk.Label(self, text="Démineur", font=("Arial Bold", 26), bg=bg)
        label.pack(expand=True)

        # Image et texte en fonction du niveau
        self.image_difficult = tk.Label(self)
        self.image_difficult.pack(expand=True)
        self.images_difficult = [
            tk.PhotoImage(file=os.path.join(img, "emoji_ange.png")),
            tk.PhotoImage(file=os.path.join(img, "emoji_confus.png")),
            tk.PhotoImage(file=os.path.join(img, "emoji_diable.png")),
            tk.PhotoImage(file=os.path.join(img, "emoji_question.png"))
        ]
        self.image_difficult.config(image=self.images_difficult[0], bg=bg)
        self.textes_difficult = [
            "Débutant", "Intermédiaire", "Avancé", "Personnalisé"
        ]
        self.label_difficult = tk.Label(self, text=self.textes_difficult[0], font=("Arial Bold", 20),
                                        bg=bg, fg=colors_difficult[0])
        self.label_difficult.pack(expand=True)

        # Curseur à quatre valeurs
        self.slider = tk.Scale(self, from_=0, to=3, resolution=1, orient="horizontal", showvalue=0,
                               length=150, highlightthickness=0, troughcolor="white", bg=colors_difficult[0])
        self.slider.pack(expand=True)

        # Création d'un cadre pour contenir le tableau
        self.setting_frame = tk.Frame(self, bg=bg)
        self.setting_frame.pack(expand=True)

        self.width_frame = tk.Frame(self.setting_frame, bg=bg)
        self.width_frame.pack(fill="x")
        self.width_label = tk.Label(self.width_frame, text="Largeur :", bg=bg, width=10, height=2)
        self.width_label.pack(side="left", padx=2, pady=2)
        self.width_value = tk.StringVar(self)
        self.width_value.set(settings_difficult[0][0])
        self.width_spinbox = tk.Spinbox(self.width_frame, from_=5, to=100, width=5, 
                                        textvariable=self.width_value,
                                        command=self.save_setting)
        self.width_spinbox.pack(side="left", padx=2, pady=2)

        self.length_frame = tk.Frame(self.setting_frame, bg=bg)
        self.length_frame.pack(fill="x")
        self.length_label = tk.Label(self.length_frame, text="Longueur :", bg=bg, width=10, height=2)
        self.length_label.pack(side="left", padx=2, pady=2)
        self.length_value = tk.StringVar(self)
        self.length_value.set(settings_difficult[0][1])
        self.length_spinbox = tk.Spinbox(self.length_frame, from_=5, to=100, width=5, 
                                         textvariable=self.length_value,
                                         command=self.save_setting)
        self.length_spinbox.pack(side="left", padx=2, pady=2)

        self.mine_frame = tk.Frame(self.setting_frame, bg=bg)
        self.mine_frame.pack(fill="x")
        self.mine_label = tk.Label(self.mine_frame, text="Mines :", bg=bg, width=10, height=2)
        self.mine_label.pack(side="left", padx=2, pady=2)
        self.mine_value = tk.StringVar(self)
        self.mine_value.set(settings_difficult[0][2])
        self.mine_spinbox = tk.Spinbox(self.mine_frame, from_=1, to=2000, width=5, 
                                       textvariable=self.mine_value,
                                       command=self.save_setting)
        self.mine_spinbox.pack(side="left", padx=2, pady=2)

        # Création du frame pour contenir les boutons
        self.button_frame = tk.Frame(self, bg=bg)
        self.button_frame.pack(expand=True)

        # Création des boutons
        self.statistic_img = tk.PhotoImage(file=os.path.join(img, "graphique.png")).subsample(2)
        self.btn_statistic = tk.Button(self.button_frame,
                                       image=self.statistic_img, bd=0,
                                       command=self.statistic, bg=bg)
        self.btn_statistic.pack(side="left", padx=10)

        self.btn_game = tk.Button(self.button_frame, text="Jouer", command=self.game)
        self.btn_game.config(width=10, height=2,
                             font=("Arial Bold", 12), relief=tk.RAISED,
                             fg="white", bg=colors_difficult[0])
        self.btn_game.pack(side="left", padx=10)

        self.setting_img = tk.PhotoImage(file=os.path.join(img, "engrenage.png")).subsample(2)
        self.btn_setting = tk.Button(self.button_frame,
                                     image=self.setting_img, bd=0,
                                     command=self.setting, bg=bg)
        self.btn_setting.pack(side="left", padx=10)

        # Lire les valeurs enregistrée du curseur depuis le fichier JSON
        self.load_difficult()
        # Lier l'événement "B1-Motion" (mouvement de souris) à la méthode save_difficult
        self.slider.bind("<Motion>", self.save_difficult)
        self.slider.bind("<ButtonRelease>", self.save_difficult)
        # Associer la touche "Espace" à l'événement de clic du bouton
        self.btn_game.focus_set()


    def load_setting(self):
        try:
            with open(os.path.join(game_data, "setting.json"), "r") as file:
                data = json.load(file)
                w = data.get("width")
                l = data.get("length")
                m = data.get("mines")
                if w is not None:
                    self.width_value.set(w)
                    self.width_spinbox.config(textvariable=self.width_value)
                if l is not None:
                    self.length_value.set(l)
                    self.length_spinbox.config(textvariable=self.length_value)
                if m is not None:
                    self.mine_value.set(m)
                    self.mine_spinbox.config(textvariable=self.mine_value)
        except FileNotFoundError:
            pass

    def update_difficult(self):
        value = self.slider.get()
        self.image_difficult.config(image=self.images_difficult[value])
        self.label_difficult.config(text=self.textes_difficult[value], fg=colors_difficult[value])
        self.slider.config(bg=colors_difficult[value])
        self.btn_game.config(bg=colors_difficult[value])
        if value==3:
            self.load_setting()
            self.width_spinbox.config(state="normal")
            self.length_spinbox.config(state="normal")
            self.mine_spinbox.config(state="normal")
        else:
            self.width_spinbox.config(state="disabled")
            self.length_spinbox.config(state="disabled")
            self.mine_spinbox.config(state="disabled")
            self.width_value.set(settings_difficult[value][0])
            self.width_spinbox.config(textvariable=self.width_value)
            self.length_value.set(settings_difficult[value][1])
            self.length_spinbox.config(textvariable=self.length_value)
            self.mine_value.set(settings_difficult[value][2])
            self.mine_spinbox.config(textvariable=self.mine_value)

    def load_difficult(self):
        try:
            with open(os.path.join(game_data, "difficult.json"), "r") as file:
                data = json.load(file)
                difficult = data.get("difficult")
                if difficult is not None:
                    self.slider.set(difficult)
                    self.update_difficult()
        except FileNotFoundError:
            pass

    def save_difficult(self,event):
        self.update_difficult()
        value = self.slider.get()
        data = {"difficult": value}
        with open(os.path.join(game_data, "difficult.json"), "w") as file:
            json.dump(data, file)

    def save_setting(self):
        difficult = self.slider.get()
        if difficult==3:
            w = self.width_spinbox.get()
            l = self.length_spinbox.get()
            m = self.mine_spinbox.get()
            max_mines = int(w)*int(l)//2
            self.mine_spinbox.config(to=max_mines)
            data = {"width": w,
                    "length": l,
                    "mines": m}
            with open(os.path.join(game_data, "setting.json"), "w") as file:
                json.dump(data, file)

    def game(self):
        self.controller.show_page("game")

    def statistic(self):
        self.controller.show_page("statistic")

    def setting(self):
        self.controller.show_page("setting")