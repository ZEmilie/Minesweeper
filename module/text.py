import os
import json

import module.management as mg


lg = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..\language')
game_title, setting_title, statistic_title, confirm_title = "", "", "", ""
game, new_game, validate = "", "", ""
game_win, game_lose, best_time = "", "", ""
time, mines = "", ""
texts_difficult, size, confirm_message = [], [], []

def init():
    update_language(mg.get_language())

def update_language(lg_selected):
    try:
        with open(os.path.join(lg, f"{lg_selected}.json"), "r", encoding="utf-8") as file:
            data = json.load(file)
            global game_title, setting_title, statistic_title, confirm_title, confirm_message
            global game, new_game, validate, game_win, game_lose, best_time
            global time, mines, texts_difficult, size
            game_title = data.get("game_title")
            setting_title = data.get("setting_title")
            statistic_title = data.get("statistic_title")
            confirm_title = data.get("confirm_title")
            confirm_message = data.get("confirm_message")
            game = data.get("game")
            new_game = data.get("new_game")
            validate = data.get("validate")
            game_win = data.get("game_win")
            game_lose = data.get("game_lose")
            best_time = data.get("best_time")
            time = data.get("time")
            mines = data.get("mines")
            texts_difficult = data.get("texts_difficult")
            size = data.get("size")
    except FileNotFoundError:
        update_language(mg.default_language)
