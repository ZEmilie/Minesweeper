import tkinter as tk

from module.setting import SettingPage
from module.game import GamePage
from module.statistic import StatisticPage
from module.home import HomePage

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Démineur")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 400
        window_height = 450
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height - 100) // 2
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Créer un cadre pour afficher le contenu des différentes pages
        self.container = tk.Frame(self)
        self.container.pack(expand=True, fill="both")

        # Configurer les options pour centrer le cadre dans la fenêtre principale
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Dictionnaire pour stocker les instances des différentes pages
        self.pages = {}
        self.pages["home"] = HomePage(self.container, self, "Démineur")
        self.pages["setting"] = SettingPage(self.container, self, "Paramètres")
        self.pages["game"] = GamePage(self.container, self, "Démineur")
        self.pages["statistic"] = StatisticPage(self.container, self, "Statistiques")

        # Afficher la page d'accueil au démarrage
        self.show_page("home")

        self.protocol("WM_DELETE_WINDOW", self.stop_app)

    def show_page(self, page_name):
        # Masquer toutes les pages
        for page in self.pages.values():
            page.grid_remove()

        # Afficher la page demandée
        self.pages[page_name].grid(row=0, column=0, sticky="nsew")
        
        # Changer le titre de la fenêtre principale
        self.title(self.pages[page_name].title)
    
    def stop_app(self):
        self.destroy()