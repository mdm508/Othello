# Matthew McLaughlin 34026707

import tkinter as tk
import points
import othello_model

# The following constants are used for cordinating font sizes and colors and so on
FONT = ('Helvetica', 16)
BGROUND_COLOR = 'green'
LINE_WIDTH = 5
PLAYER_BLACK = 'Black'
PLAYER_WHITE = 'White'


EMPTY = othello_model.EMPTY
BLACK = othello_model.BLACK
WHITE = othello_model.WHITE


BACKGROUND_COLOR = 'green'
FONT = ('Helvetica', 16)
STICKY = tk.N + tk.S + tk.E + tk.W

class ConfigureGame():
    def __init__(self):
        '''
        Intializes a window for configuring how an othello game
        will be played
        '''
        self.dialog = tk.Toplevel()
        self.rows = 8
        self.columns = 8
        self.turn = 'B'
        self.UL = 'B'
        self.win_type = '>'


        # Row Label
        row_label = tk.Label(self.dialog, text = 'Rows', bg = BACKGROUND_COLOR,
                                   font = FONT, width = 10 )
        row_label.grid(row = 0, column = 0, sticky = STICKY)
        # Row Radio Box
        self._row_RB_var = tk.IntVar(value = 8)
        row_4_RB = tk.Radiobutton(self.dialog, text = '4',variable= self._row_RB_var, value = 4)
        row_4_RB.grid(row = 0, column = 1)
        row_6_RB = tk.Radiobutton(self.dialog, text = '6',variable= self._row_RB_var, value = 6)
        row_6_RB.grid(row = 0, column = 2)
        row_8_RB = tk.Radiobutton(self.dialog, text = '8',variable= self._row_RB_var, value = 8)
        row_8_RB.grid(row = 0, column = 3)
        row_10_RB = tk.Radiobutton(self.dialog, text = '10',variable= self._row_RB_var, value = 10)
        row_10_RB.grid(row = 0, column = 4)
        row_12_RB = tk.Radiobutton(self.dialog, text = '12',variable= self._row_RB_var, value = 12)
        row_12_RB.grid(row = 0, column = 5)
        row_14_RB = tk.Radiobutton(self.dialog, text = '14',variable= self._row_RB_var, value = 14)
        row_14_RB.grid(row = 0, column = 6)
        row_16_RB = tk.Radiobutton(self.dialog, text = '16',variable= self._row_RB_var, value = 16)
        row_16_RB.grid(row = 0, column = 7)
        

        # Column Label
        column_label = tk.Label(self.dialog, text = 'Columns',
                                      bg = BACKGROUND_COLOR, font = FONT, width = 10)
        column_label.grid(row = 1, column = 0, sticky = STICKY)
        # Column Radio Box
        self._col_RB_var = tk.IntVar(value = 8)
        col_4_RB = tk.Radiobutton(self.dialog, text = '4', variable = self._col_RB_var, value = 4)
        col_4_RB.grid(row = 1, column = 1)

        col_6_RB = tk.Radiobutton(self.dialog, text = '6', variable = self._col_RB_var, value = 6)
        col_6_RB.grid(row = 1, column = 2)

        col_8_RB = tk.Radiobutton(self.dialog, text = '8', variable = self._col_RB_var, value = 8)
        col_8_RB.grid(row = 1, column = 3)

        col_10_RB = tk.Radiobutton(self.dialog, text = '10', variable = self._col_RB_var, value = 10)
        col_10_RB.grid(row = 1, column = 4)

        col_12_RB = tk.Radiobutton(self.dialog, text = '12', variable = self._col_RB_var, value = 12)
        col_12_RB.grid(row = 1, column = 5)

        col_14_RB = tk.Radiobutton(self.dialog, text = '14', variable = self._col_RB_var, value = 14)
        col_14_RB.grid(row = 1, column = 6)

        col_16_RB = tk.Radiobutton(self.dialog, text = '16', variable = self._col_RB_var, value = 16)
        col_16_RB.grid(row = 1, column = 7)
        
        # Turn Label
        turn_label = tk.Label(self.dialog, text = 'Turn',
                                    bg = BACKGROUND_COLOR, font = FONT, width = 10)
        turn_label.grid(row = 2, column = 0, sticky = STICKY)

        # Turn Radio box
        self._turn_var = tk.StringVar(value = 'B')
        turn_black = tk.Radiobutton(self.dialog, text = 'Black', value = 'B', variable = self._turn_var)
        turn_black.grid(row = 2, column = 1)
        turn_white = tk.Radiobutton(self.dialog, text = 'White', value = 'W', variable = self._turn_var)
        turn_white.grid(row = 2, column = 2)
        

        # Upper Left Label
        upper_left_label = tk.Label(self.dialog, text = 'Up-Left', font = FONT,
                                          width = 10, bg = BACKGROUND_COLOR)
        upper_left_label.grid(row = 3, column = 0, sticky = STICKY)

        
        # Upper Left Radio box
        self._UL_var = tk.StringVar(value ='B')
        UL_black = tk.Radiobutton(self.dialog, text = 'Black', value = 'B', variable = self._UL_var)
        UL_black.grid(row = 3, column = 1)
        UL_white = tk.Radiobutton(self.dialog, text = 'White', value = 'W', variable = self._UL_var)
        UL_white.grid(row = 3, column = 2)
  

        # Win Type Label
        win_type_label = tk.Label(self.dialog, text = 'Win Type', font = FONT, width = 10,
                                        bg = BACKGROUND_COLOR)
        win_type_label.grid(row = 4, column = 0, sticky = STICKY)

        # Win Type Radio box
        self._win_type_var = tk.StringVar(value='>')
        high_win = tk.Radiobutton(self.dialog, text = 'High', value = '>', variable = self._win_type_var)
        high_win.grid(row = 4, column = 1)
        low_win = tk.Radiobutton(self.dialog, text = 'Low', value = '<', variable = self._win_type_var)
        low_win.grid(row=4, column = 2)
        
        # Button
        button = tk.Button(self.dialog, text = 'Submit', font = FONT,
                           command = self._button_pressed)
        button.grid(row = 8, column = 0, columnspan =2)
    
            
        self.dialog.rowconfigure(0, weight = 1)
        self.dialog.rowconfigure(1, weight = 1)
        self.dialog.rowconfigure(2, weight = 1)
        self.dialog.rowconfigure(3, weight = 1)
        self.dialog.rowconfigure(4, weight = 1)
        self.dialog.rowconfigure(5, weight = 1)
        self.dialog.rowconfigure(6, weight = 1)
        self.dialog.rowconfigure(6, weight = 1)
        self.dialog.rowconfigure(7, weight = 1)

        self.dialog.columnconfigure(0, weight = 1)
        self.dialog.columnconfigure(1, weight = 1)
        
                                      
    def _button_pressed(self):
        self.rows = self._row_RB_var.get()
        self.columns = self._col_RB_var.get()
        self.turn = self._turn_var.get()
        self.UL = self._UL_var.get()
        self.win_type = self._win_type_var.get()
        self.dialog.destroy()

    def show(self):
        self.dialog.grab_set()
        self.dialog.wait_window()

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def get_turn(self):
        return self.turn

    def get_UL(self):
        return self.UL

    def get_win_type(self):
        return self.win_type
        



    
   


class OthelloApp():
    def __init__(self):
        self._root_window = tk.Tk()
        
        # Info about game  board
        self.rows = 8
        self.columns = 8
        self.turn = 'B'
        self.UL = 'B'
        self.win_type = '>'
        # Intialize othell game state
        self._state = othello_model.OthelloState(self.rows, self.columns, self.turn, self.UL)
        
        self._state.start()
        self._white_score, self._black_score = self._state.score()
        self._turn = self._state.turn()

        



        
        # CANVAS
        self._canvas = tk.Canvas(
            self._root_window, width = 400, height = 400,
            bg = BGROUND_COLOR)

        self._canvas.grid(row=1, column=0, padx=10,
                          sticky = tk.N + tk.S + tk.E + tk.W)
        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._handle_game_logic)


        # START BUTTON
        self._start_button = tk.Button(self._root_window, bg = BACKGROUND_COLOR, text='Full Rules Othello', font = FONT)
        self._start_button.grid(row=1, column = 0, sticky = tk.N +tk.S + tk.E + tk.W)
        self._start_button.bind('<Button-1>', self._dialog_pop_up)
        
        

        # SCOREBOARD
        self._frame = tk.Frame(self._root_window, padx=15)
        self._frame.grid(row = 0, column = 1, rowspan=4)
        ## Black Score
        black_score_label = tk.Label(self._frame, text = 'Black', font = FONT)
        black_score_label.grid(row = 0, column = 0, sticky=tk.S)
        self._black_score_var = tk.StringVar(value = str(self._black_score))
        self._black_score_number = tk.Label(self._frame, textvariable = self._black_score_var, font = FONT)
        self._black_score_number.grid(row = 0, column = 1)
        
        ## White Score
        white_score_label = tk.Label(self._frame, text = 'White', font = FONT)
        white_score_label.grid(row = 1, column = 0, sticky=tk.N)
        self._white_score_var = tk.StringVar(value = str(self._white_score))
        self._white_score_number = tk.Label(self._frame, textvariable = self._white_score_var, font = FONT)
        self._white_score_number.grid(row = 1, column = 1)

        # TURN TRACKER AND WINNER DISPLAY
        turn = self._whos_turn()
        self._turn_label_var = tk.StringVar(value=turn )
        self._turn_label = tk.Label(self._root_window, font=FONT, textvariable = self._turn_label_var, padx=15)
        self._turn_label.grid(row = 0, column = 0, sticky = tk.W)

        
        # CONFIGURE
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

        

    def _dialog_pop_up(self, event):
        dialog = ConfigureGame()
        dialog.show()
        
        self.rows = dialog.get_rows()
        self.columns = dialog.get_columns()
        self.turn = dialog.get_turn()
        self.UL = dialog.get_UL()
        self._state = self._state = othello_model.OthelloState(self.columns,self.rows, self.turn, self.UL)
        self._state.start()
        self._on_canvas_resized(event)
        self._start_button.destroy()
        self._update_turn_label()
        self.win_type = dialog.get_win_type()
        


        
    def state(self):
        return self._state
    
    def start(self):

        self._root_window.mainloop()

    def _on_canvas_clicked(self,event):
        cordinate_pair = (event.x, event.y)
        window_width = self._canvas.winfo_width()
        window_height = self._canvas.winfo_height()

        indexes = othello_model.OthelloLayout().where_am_i(self.rows,self.columns,window_width, window_height, cordinate_pair)
        return indexes
    

    def _on_canvas_resized(self, event):
        self._canvas.delete(tk.ALL)
        
        self._draw_grid(event)



    def _draw_grid(self, event):
        
        window_width = self._canvas.winfo_width()
        window_height = self._canvas.winfo_height()

        
        for x1, y1, x2, y2 in points.LinePoints(self.rows, self.columns, window_width, window_height).get_column_cords():
            self._canvas.create_line(x1, y1, x2, y2,width=LINE_WIDTH)

        for x1, y1, x2, y2 in points.LinePoints(self.rows, self.columns, window_width, window_height).get_row_cords():
            self._canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH)

        self._draw_ovals()

        

    def _draw_ovals(self):
        '''
        draw a circle in the grid for every color in self._state
        for the given color
        '''
        
        window_width = self._canvas.winfo_width()
        window_height = self._canvas.winfo_height()
        
        cells = points.LinePoints(self.rows, self.columns, window_width, window_height).get_cells()
        for tup in othello_model.OthelloLayout().ovals_to_draw(self._state.state(), self.rows, self.columns, window_width, window_height):
            turn, column_index, row_index = tup
            if turn == WHITE:
                x1, y1, x2, y2 = cells[column_index][row_index]
                self._canvas.create_oval(x1, y1, x2, y2, fill = PLAYER_WHITE)
            else:
                x1, y1, x2, y2 = cells[column_index][row_index]
                self._canvas.create_oval(x1, y1, x2, y2, fill = PLAYER_BLACK)

    def _whos_turn(self):
        '''
        Return WHITE's or BLACK'S MOVE
        '''
        self._turn = self._state.turn()
        if self._turn == BLACK:
            return "BLACK'S MOVE"
        else:
            return "WHITE'S MOVE"
    
    def _update_turn_label(self)-> str:
        '''
        Return a string of whose turn it is, BLACK'S MOVE or WHITES MOVE
        '''
        self._turn = self._state.turn()
        if self._turn == BLACK:
            self._turn_label_var.set("BLACK'S MOVE")
        else:
            self._turn_label_var.set("WHITE'S MOVE")
    

    def _update_score(self)-> None:
        '''
        Update the score on the tkinter window. Optionally, it returns the score as well
        '''
        
        self._white_score, self._black_score = self._state.score()
        self._black_score_var.set(self._black_score)
        self._white_score_var.set(self._white_score)
        return self._white_score, self._black_score


    def _game_over(self)->None:
        '''
        Replace turn_label with 'WINNER PLAYER'
        '''
        winner = self._state.winner_is(self.win_type)
        if winner == WHITE:
            self._turn_label_var.set("WHITE WINS")
        elif winner == BLACK:
            self._turn_label_var.set("BLACK WINS")
        else:
            self._turn_label_var.set("Looks like we have ourselves a tie")

    def _handle_game_logic(self, event):
        '''
        This function handles the progression of the game. It knows
        when the game is over and whos turn it is
        '''
 
        if self._state.has_move():
            try:
                move = self._on_canvas_clicked(event)
                column_index, row_index = move
                position_to_flip = self._state.check(column_index, row_index)
            except:
                pass 
            else:
                if position_to_flip != 'INVALID':
                    self._state.flip(position_to_flip)
                    self._draw_ovals()
                    self._state.switch()
                    self._update_score()
                    self._update_turn_label()
                    if self._state.is_board_full():
                        self._game_over()
                    
        else:
            self._state.switch()
            if not self._state.has_move():
                self._game_over()
            else:
                self._update_score()
                self._update_turn_label()
                if self._state.is_board_full():
                    self._game_over()
    
        
    


if __name__ == "__main__":
    game = OthelloApp().start()
    # These are default values needed to get a game state
