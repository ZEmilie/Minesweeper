import tkinter as tk

import module.management as mg
import module.calculate as calculate
import module.text as tt

class GamePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title = tt.game_title
        self.config(bg=mg.bg)
        self.w, self.l, self.m = mg.get_wlm_final()

        # Menu bar
        self.barre = tk.Frame(self, bg=mg.n_bg)
        self.barre.pack(side=tk.TOP, fill=tk.X)
        self.home_img = mg.img_home.subsample(2)
        self.btn_home = tk.Button(self.barre, image=self.home_img, bd=0, command=self.home, bg=mg.n_bg)
        self.btn_home.pack(side=tk.LEFT, padx=10, pady=5)
        self.setting_img = mg.img_setting.subsample(2)
        self.btn_setting = tk.Button(self.barre, image=self.setting_img, bd=0, command=self.setting, bg=mg.n_bg)
        self.btn_setting.pack(side=tk.LEFT, padx=10, pady=5)
        self.statistic_img = mg.img_graph.subsample(2)
        self.btn_statistic = tk.Button(self.barre, image=self.statistic_img, bd=0, command=self.statistic, bg=mg.n_bg)
        self.btn_statistic.pack(side=tk.LEFT, padx=10, pady=5)

        # Page content
        self.top_frame = tk.Frame(self, bg=mg.bg_board)
        self.top_frame.pack(pady=10)
        self.time_elapsed = 0
        self.mines_count = self.m
        self.empty_count = self.w*self.l-self.m
        self.time_label = tk.Label(self.top_frame, text=f"{tt.time}: {self.time_elapsed} s",
                                   bg=mg.bg, relief=tk.RAISED, width=10, height=2)
        self.time_label.pack(side=tk.LEFT, padx=10, pady=5)
        self.update_time()
        self.mines_label = tk.Label(self.top_frame, text=f"{tt.mines}: {self.mines_count}",
                                    bg=mg.bg, relief=tk.RAISED, width=10, height=2)
        self.mines_label.pack(side=tk.RIGHT, padx=10, pady=5)

        self.bomb_img = mg.img_bomb.subsample(4)
        self.flag_img = mg.img_flag.subsample(4)
        self.bang_img = mg.img_bang.subsample(4)
        self.create_game_board()
        self.btn_game = tk.Button(self, text=tt.new_game, command=self.new_game)
        self.btn_game.config(width=15, height=2, font=("Arial Bold", 12), relief=tk.RAISED,
                             fg="white", bg=mg.n_bg)
        self.btn_game.pack(pady=20)


    def update_time(self):
        self.time_elapsed += 1
        self.time_label.config(text=f"{tt.time}: {self.time_elapsed} s")
        self.time_update_id = self.after(1000, self.update_time)

    def create_game_board(self):
        self.game_board = tk.Frame(self, bg="white", width=300, height=300)
        self.game_board.pack()
        self.cells = []
        for i in range(self.l):
            row_cells = []
            for j in range(self.w):
                cell = tk.Label(self.game_board, bg=mg.bg_board, relief=tk.RAISED, width=2, height=1)
                cell.grid(row=i, column=j, padx=1, pady=1)
                cell.bind("<Button-1>", lambda event, row=i, column=j: self.left_click(row,column))
                cell.bind("<Button-3>", lambda event, row=i, column=j: self.right_click(row,column))
                row_cells.append(cell)
            self.cells.append(row_cells)
        self.matrix_mines = calculate.mines_position(self.w,self.l,self.m)

    def game_over(self):
        if self.time_update_id:
            self.after_cancel(self.time_update_id)
        for i in range(self.l):
            for j in range(self.w):
                cell = self.cells[i][j]
                color = cell.cget('bg')
                elmt = self.matrix_mines[i][j]
                if color==mg.bg_board and elmt==9:
                    cell.config(bg=mg.bg, image=self.bomb_img, relief=tk.FLAT, width=15, height=15)
                cell.unbind("<Button-1>")
                cell.unbind("<Button-3>")
        self.btn_game.config(bg=mg.colors_difficult[2])
        self.top_frame.config(bg=mg.colors_difficult[2])
        mg.set_statistic(self.time_elapsed,False)

    def game_win(self):
        if self.time_update_id:
            self.after_cancel(self.time_update_id)
        for i in range(self.l):
            for j in range(self.w):
                cell = self.cells[i][j]
                color = cell.cget('bg')
                elmt = self.matrix_mines[i][j]
                if color==mg.bg_board and elmt==9:
                    cell.config(bg=mg.bg, image=self.bomb_img, relief=tk.FLAT, width=15, height=15)
                cell.unbind("<Button-1>")
                cell.unbind("<Button-3>")
        self.btn_game.config(bg=mg.colors_difficult[0])
        self.top_frame.config(bg=mg.colors_difficult[0])
        mg.set_statistic(self.time_elapsed,True)

    def update_empty_count(self):
        self.empty_count += -1
        if self.empty_count==0:
            self.game_win()

    def sum_flag_neighbour(self, row, column):
        s = 0
        # row-1
        if row-1>=0:
            if column-1>=0:
                if str(self.cells[row-1][column-1].cget('image'))==str(self.flag_img):

                    s+=1
            if str(self.cells[row-1][column].cget('image'))==str(self.flag_img):
                s+=1
            if column+1<self.w:
                if str(self.cells[row-1][column+1].cget('image'))==str(self.flag_img):
                    s+=1
        # row
        if column-1>=0:
            if str(self.cells[row][column-1].cget('image'))==str(self.flag_img):
                s+=1
        if column+1<self.w:
            if str(self.cells[row][column+1].cget('image'))==str(self.flag_img):
                s+=1
        # row+1
        if row+1<self.l:
            if column-1>=0:
                if str(self.cells[row+1][column-1].cget('image'))==str(self.flag_img):
                    s+=1
            if str(self.cells[row+1][column].cget('image'))==str(self.flag_img):
                s+=1
            if column+1<self.w:
                if str(self.cells[row+1][column+1].cget('image'))==str(self.flag_img):
                    s+=1
        return s

    def drain_full_case(self, row, column):
        cell = self.cells[row][column]
        color = cell.cget('bg')
        if color==mg.bg_board:
            cell = self.game_board.grid_slaves(row=row, column=column)[0]
            if self.matrix_mines[row][column]==9:
                cell.config(bg=mg.bg, image=self.bang_img, relief=tk.FLAT, width=15, height=15)
                self.game_over()
            elif self.matrix_mines[row][column]==0:
                cell.config(bg=mg.bg, relief=tk.FLAT)
                self.update_empty_count()
                # row-1
                if row-1>=0:
                    if column-1>=0:
                        self.drain_full_case(row-1,column-1)
                    self.drain_full_case(row-1,column)
                    if column+1<self.w:
                        self.drain_full_case(row-1,column+1)
                # row
                if column-1>=0:
                    self.drain_full_case(row,column-1)
                if column+1<self.w:
                    self.drain_full_case(row,column+1)
                # row+1
                if row+1<self.l:
                    if column-1>=0:
                        self.drain_full_case(row+1,column-1)
                    self.drain_full_case(row+1,column)
                    if column+1<self.w:
                        self.drain_full_case(row+1,column+1)
                self.drain_full_case(row,column)
            else:
                nb = self.matrix_mines[row][column]
                cell.config(text=nb, fg=mg.colors_number[nb],
                            bg=mg.bg, relief=tk.FLAT)
                self.update_empty_count()

    def left_click(self, row, column):
        cell = self.cells[row][column]
        color = cell.cget('bg')
        t = cell.cget('text')
        if color==mg.bg_board:
            self.drain_full_case(row,column)
        elif t!='':
            s = self.sum_flag_neighbour(row,column)
            if s==t:
                # row-1
                if row-1>=0:
                    if column-1>=0:
                        self.drain_full_case(row-1,column-1)
                    self.drain_full_case(row-1,column)
                    if column+1<self.w:
                        self.drain_full_case(row-1,column+1)
                # row
                if column-1>=0:
                    self.drain_full_case(row,column-1)
                if column+1<self.w:
                    self.drain_full_case(row,column+1)
                # row+1
                if row+1<self.l:
                    if column-1>=0:
                        self.drain_full_case(row+1,column-1)
                    self.drain_full_case(row+1,column)
                    if column+1<self.w:
                        self.drain_full_case(row+1,column+1)

    def right_click(self, row, column):
        cell = self.cells[row][column]
        color = cell.cget('bg')
        w = cell.cget('width')
        if color==mg.bg_board:
            cell = self.game_board.grid_slaves(row=row, column=column)[0]
            cell.config(bg=mg.bg, image=self.flag_img, relief=tk.FLAT, width=15, height=15)
            self.mines_count += -1
            self.mines_label.config(text=f"{tt.mines}: {self.mines_count}")
        elif w==15:
            cell = self.game_board.grid_slaves(row=row, column=column)[0]
            cell.config(image='', bg=mg.bg_board, relief=tk.RAISED, width=2, height=1)
            self.mines_count += 1
            self.mines_label.config(text=f"{tt.mines}: {self.mines_count}")

    def home(self):
        self.controller.show_page("home")

    def statistic(self):
        self.controller.show_page("statistic")

    def setting(self):
        self.controller.show_page("setting")

    def new_game(self):
        self.controller.refresh_game_page()
        self.controller.show_page("game")