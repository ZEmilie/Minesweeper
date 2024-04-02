import tkinter as tk
import os
import json

# Color
bg = "#fffbf0"
n_bg = "#4cc7ff"
bg_board = "grey"
colors_difficult = ["#b3ff72", "#ffc160", "#cb1446", n_bg]

# Image
img = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..\img')
img_difficult, img_bomb, img_flag, img_bang = [], None, None, None
img_game, img_graph, img_home, img_setting = None, None, None, None
def init_img():
    global img_difficult, img_bomb, img_flag, img_bang
    global img_game, img_graph, img_home, img_setting
    img_difficult = [tk.PhotoImage(file=os.path.join(img, "emoji_ange.png")),
                     tk.PhotoImage(file=os.path.join(img, "emoji_confus.png")),
                     tk.PhotoImage(file=os.path.join(img, "emoji_diable.png")),
                     tk.PhotoImage(file=os.path.join(img, "emoji_question.png"))]
    img_game = tk.PhotoImage(file=os.path.join(img, "game.png"))
    img_graph = tk.PhotoImage(file=os.path.join(img, "graphique.png"))
    img_home = tk.PhotoImage(file=os.path.join(img, "home.png"))
    img_setting = tk.PhotoImage(file=os.path.join(img, "engrenage.png"))
    img_bomb = tk.PhotoImage(file=os.path.join(img, "bombe.png"))
    img_flag = tk.PhotoImage(file=os.path.join(img, "drapeau.png"))
    img_bang = tk.PhotoImage(file=os.path.join(img, "bang.png"))

# Data
game_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..\data')
if not os.path.exists(game_data):
    os.makedirs(game_data)

# Data Language
language_possibility = {
    "English": "english",
    "Français": "french"
}
default_language = list(language_possibility.values())[0]
def get_language():
    try:
        with open(os.path.join(game_data, "language.json"), "r") as file:
            data = json.load(file)
            language = data.get("language")
            if language is not None:
                return language
            else:
                return default_language
    except FileNotFoundError:
        return default_language
def set_language(value):
    data = {"language": value}
    with open(os.path.join(game_data, "language.json"), "w") as file:
        json.dump(data, file)

# Data Difficult
def get_difficult():
    try:
        with open(os.path.join(game_data, "difficult.json"), "r") as file:
            data = json.load(file)
            difficult = data.get("difficult")
            if difficult is not None:
                return difficult
            else:
                return 0
    except FileNotFoundError:
        return 0
def set_difficult(value):
    data = {"difficult": value}
    with open(os.path.join(game_data, "difficult.json"), "w") as file:
        json.dump(data, file)

# Data Option Difficult
difficult_name = ["easy", "medium", "hard"]
wlm_difficult = [[9,9,10], [16,16,40], [30,16,99]]
def get_wlm():
    try:
        with open(os.path.join(game_data, "wlm.json"), "r") as file:
            data = json.load(file)
            w = data.get("width")
            l = data.get("length")
            m = data.get("mines")
            return w,l,m
    except FileNotFoundError:
        return wlm_difficult[0]
def set_wlm(w,l,m):
    data = {"width": w, "length": l, "mines": m}
    with open(os.path.join(game_data, "wlm.json"), "w") as file:
        json.dump(data, file)
def get_wlm_final():
    value = get_difficult()
    if value==3:
        w,l,m = get_wlm()
        w = int(w)
        l = int(l)
        m = int(m)
    else:
        w,l,m = wlm_difficult[value]
    return w,l,m

# Data Statistic
def get_statistic(level):
    if level!=3:
        try:
            with open(os.path.join(game_data, f"{difficult_name[level]}.json"), "r") as file:
                data = json.load(file)
                best_time = data.get("time")
                n_win = data.get("win")
                n_lose = data.get("lose")
                return best_time, n_win, n_lose
        except FileNotFoundError:
            return None, 0, 0
def set_statistic(time,win):
    level = get_difficult()
    if level!=3:
        best_time, n_win, n_lose = get_statistic(level)
        if win:
            n_win = int(n_win)+1
            if best_time is None or int(best_time)>time:
                best_time = time
        else:
            n_lose = int(n_lose)+1
        data = {"time": best_time, "win": n_win, "lose": n_lose}
        with open(os.path.join(game_data, f"{difficult_name[level]}.json"), "w") as file:
            json.dump(data, file)