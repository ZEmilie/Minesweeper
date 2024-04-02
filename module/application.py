import tkinter as tk

from module.setting import SettingPage
from module.game import GamePage
from module.statistic import StatisticPage
from module.home import HomePage
import module.text as tt

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        tt.init()
        self.title(tt.game_title)
        window_width = 800
        window_height = 575
        x = (self.winfo_screenwidth() - window_width) // 2
        y = (self.winfo_screenheight() - window_height - 100) // 2
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Create a frame to display the content of different pages
        self.container = tk.Frame(self)
        self.container.pack(expand=True, fill="both")

        # Configure the options for centring the frame in the main window
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Dictionary for storing instances of different pages
        self.pages = {}
        self.pages["home"] = HomePage(self.container, self)
        self.pages["setting"] = SettingPage(self.container, self)
        self.pages["game"] = GamePage(self.container, self)
        self.pages["statistic"] = StatisticPage(self.container, self)

        # Display home page at startup
        self.show_page("home")

        self.protocol("WM_DELETE_WINDOW", self.stop_app)

    def show_page(self, page_name):
        if page_name=="statistic":
            self.refresh_statistic_page()
        # Hide all pages
        for page in self.pages.values():
            page.grid_remove()
        # Display the requested page
        self.pages[page_name].grid(row=0, column=0, sticky="nsew")
        # Change the title of the main window
        self.title(self.pages[page_name].title)

    def refresh_all_page(self):
        self.refresh_home_page()
        self.refresh_setting_page()
        self.refresh_game_page()
        self.refresh_statistic_page()

    def refresh_home_page(self):
        self.pages["home"].destroy()
        self.pages["home"] = HomePage(self.container, self)

    def refresh_setting_page(self):
        self.pages["setting"].destroy()
        self.pages["setting"] = SettingPage(self.container, self)
    
    def refresh_game_page(self):
        self.pages["game"].destroy()
        self.pages["game"] = GamePage(self.container, self)

    def refresh_statistic_page(self):
        self.pages["statistic"].destroy()
        self.pages["statistic"] = StatisticPage(self.container, self)
    
    def stop_app(self):
        self.destroy()