# Matthew McLaughlin 34026707
# othello_model.py

'''
This module contains functions and classes needed for the rules of an
othello game
'''

import points

EMPTY = 0
WHITE = 'W'
BLACK = 'B'


class InvalidMoveError(Exception):
    def __init__(self, value):
        self.value = value
        
    
class OthelloState:
    def __init__(self, columns, rows, turn, upper_left):
        '''Intializes an Othello game given a number of rows adn columns
        '''
        self._state = self._create_grid(rows, columns)
        self._rows = rows
        self._columns = columns
        self._turn = turn
        self._upperleft = upper_left

        
    def state(self):
        '''Returns the current game state
        '''
        return self._state

    def turn(self):
        '''return the player letter whos turn it is, W or B'''
        return self._turn

    def switch(self):
        '''Switch turn from B to W or W to B'''
        if self._turn == WHITE:
            self._turn = BLACK
        else:
            self._turn = WHITE

    def start(self):
        '''Update game state so white or black is in the middle
           upper left most portion of the grid
        '''
        upper_left = (int(self._columns/2)-1), int((self._rows/2)-1)
        lower_right = (int(self._columns/2), int(self._rows/2))

        upper_right = (int(self._columns/2), int((self._rows/2)-1))
        lower_left = (int((self._columns/2)-1), int(self._rows/2))
        
        if self._upperleft == WHITE:
           self._state[upper_left[0]][upper_left[1]] = WHITE
           self._state[lower_right[0]][lower_right[1]] = WHITE
           self._state[upper_right[0]][upper_right[1]]= BLACK
           self._state[lower_left[0]][lower_left[1]] = BLACK
        else:
            self._state[upper_left[0]][upper_left[1]] = BLACK
            self._state[lower_right[0]][lower_right[1]] = BLACK
            self._state[upper_right[0]][upper_right[1]]= WHITE
            self._state[lower_left[0]][lower_left[1]] = WHITE


    def flip(self, list_of_tuples):
        if self._turn == WHITE:
            for lst in list_of_tuples:
                for t in lst:
                    self._state[t[0]][t[1]] = 'W'
        else:
            for lst in list_of_tuples:
                for t in lst:
                    self._state[t[0]][t[1]] = 'B'

                    
    def check(self, column, row):
        '''Checks in every direction if a proposed move is valid.
           returns a list containing tuples of positions to flip
           if the move is valid. And an empty list otherwise'''
        
        if column > self._columns:
            try:
                raise InvalidMoveError('INVALID')
            except InvalidMoveError as e:
                    return e.value
        elif row > self._rows:
            try:
                raise InvalidMoveError('INVALID')
            except InvalidMoveError as e:
                    return e.value
                
        positions_to_flip = []
        # right, left, down, up, down-l, down-r, up-l, up-rv (rspectively) 
        directions = [(0,1), (0, -1), (1,0), (-1,0), (1, -1), (1,1), (-1, -1), (-1, 1)]
        rows = list(range(self._rows))
        columns = list(range(self._columns))
        for d in directions:
            sublist = []
            trans_col, trans_row = d

            trans_col += column
            trans_row += row

            if self._space_is_empty(column, row):
                while True:
                    if trans_row not in rows:
                        sublist = []
                        break

                    elif trans_col not in columns:
                        sublist = []
                        break
                    
                    elif self._state[trans_col][trans_row] == 0:
                        sublist = []
                        break
                    
                    elif self._state[trans_col][trans_row] == self._turn:
                        break
                    
                    else:
                        sublist.append((trans_col, trans_row))
                        trans_col += d[0]
                        trans_row += d[1]

                if sublist!= []:
                    sublist.insert(0, (column, row))
                    positions_to_flip.append(sublist)

    
            else:
                try:
                    raise InvalidMoveError('INVALID')
                except InvalidMoveError as e:
                    return e.value                       
                        
        #Returns INVALID if the move results in no pieces being flipped
        b = False
        for x in positions_to_flip:
            if x!=[]:
                b = True

        if b == False:
            try:
                raise InvalidMoveError('INVALID')
            except InvalidMoveError as e:
                    return e.value
        else:
            return positions_to_flip
                                         
    def _space_is_empty(self, column, row):
        '''Returns true if space is empty false otherwise'''
        return not bool(self._state[column][row])

    def move(self, column, row):
        '''Update game state with the specified move'''
        if self._turn == WHITE:
            self._state[column][row] = WHITE
        else:
            self._state[column][row] = BLACK

    def is_board_full(self):
        '''Returns true if the board is full false otherwise'''
        v = True
        for l in self._state:
            if 0 in l:
                v = False
        return v
    
    def has_move(self):
        '''Checks for every position on the board if
           a player has a move such that at least 1 tile
           can be flipped. Returns true if list contains
           at least one element false otherwise'''
        b = False
        moves = []
        cordinates = self._get_cordinates()
        for tup in cordinates:
            col, row = tup
            moves.append(self.check(col,row))
        for x in moves:
            if x!="INVALID":
                b=True

        return b

    def winner_is(self, win_type):
        '''
        Given a win type, checks who the winner is
        and determines if there is a tie or a winner,
        if there is a tie returns 0
        otherwise returns color of player
        '''
        white_score, black_score = self.score()

        if win_type == '>':
            if white_score > black_score:
                return WHITE
            elif white_score == black_score:
                    return EMPTY
            else:
                return BLACK
        else:
            if white_score < black_score:
                return WHITE
            elif black_score == white_score:
                return EMPTY
            else:
                return BLACK
    
    def score(self):
        '''returns the current score for of the game, white, black'''

        white_score = 0
        black_score = 0
        for i in range(len(self._state)):
            for j in range(len(self._state[i])):
                if self._state[i][j] == WHITE:
                    white_score+=1
                elif self._state[i][j] == BLACK:
                    black_score+=1
        return white_score, black_score
    
    def _get_cordinates(self):
        '''returns a list of tuples that contain cordinate pairs
           of every location on the board'''
        cordinates = []
        for i in range(len(self._state)):
            for j in range(len(self._state[i])):
                cordinates.append((i,j))
        return cordinates
    
    def _create_grid(self, rows:int, columns:int):
        '''Given a number of rows and columns create a grid.
           col specifies number of sublist containers
           row specifies number of 0s inside col
           *Input must be numbers between 4-16 inclusive
        '''
        grid = []
        for c in range(columns):
            grid.append([])
            for r in range(rows):
                grid[c].append(0)
                       
        return grid



class OthelloLayout:
    '''
    This class contains tools for mapping the othello game state
    to an Othello application
    '''
    def __init__(self):
        self._nothing = 0
    

    def ovals_to_draw(self,game_state,rows, columns, window_width, window_height)-> ('B col_i, row_i'):
        '''
        Returns a tuple containing a turn, a column index, and a row index
        '''
        cells = points.LinePoints(rows, columns, window_width, window_height).get_cells()
        indexes = []
        for i in range(len(game_state)):
            for j in range(len(game_state[i])):
                if game_state[i][j] == WHITE:
                    indexes.append((WHITE,i,j))
                elif game_state[i][j] == BLACK:
                    indexes.append((BLACK,i,j))
        return indexes

    def where_am_i(self,rows, columns, window_width, window_height, cordinate_pair: '(x1, y1)')-> ('column_index, row_index'):
        '''
        Given a cordinate pair from a mouse click, this function will tell you
        where if anywhere, your click was on the grid. If the click was not within
        the grid then the function returns None
        '''
        x, y = cordinate_pair
        l = points.LinePoints(rows,columns, window_width, window_height)
        for i in range(len(l.get_cells())):
            for j in range(len(l.get_cells()[i])):
                x1, y1, x2, y2 = l.get_cells()[i][j]
                if x1<=x<=x2 and y1<=y<=y2:
                    return (i,j)
        
        
    
        
    

    
        
        
        
        
        
        
    





        
