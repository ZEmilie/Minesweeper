import tkinter as tk
import os
import json

bg = "#fffbf0"
n_bg = "#4cc7ff"
bg_board = "grey"
colors_difficult = ["#b3ff72", "#ffc160", "#cb1446", n_bg]

img = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..\img')
img_difficult = []
img_game = None
img_graph = None
img_home = None
img_setting = None
img_bomb = None
img_flag = None
img_bang = None
def init_img():
    global img_difficult
    global img_game
    global img_graph
    global img_home
    global img_setting
    global img_bomb
    global img_flag
    global img_bang
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

game_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..\data')
if not os.path.exists(game_data):
    os.makedirs(game_data)

wlm_difficult = [[9,9,10], [16,16,40], [30,16,99]]

def set_difficult(value):
    data = {"difficult": value}
    with open(os.path.join(game_data, "difficult.json"), "w") as file:
        json.dump(data, file)

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

def set_wlm(w,l,m):
    data = {"width": w, "length": l, "mines": m}
    with open(os.path.join(game_data, "wlm.json"), "w") as file:
        json.dump(data, file)

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