# Matthew McLaughlin 34026707
# points.py

class LinePoints:
    '''
    class is used for determining the points needed to draw a nxn grid on
    a canvas of w, width and h, height
    '''
    
    def __init__(self, board_rows, board_columns, window_width, window_height):
        self._rows = board_rows
        self._columns = board_columns
        self._window_width = window_width
        self._window_height = window_height
        self._x1_pixel = 20
        self._y1_pixel = 20
        
        self._x_edge = window_width - self._x1_pixel
        self._y_floor = window_height - self._y1_pixel
        
        
    def grid_floor(self):
        return self._y_floor

    def grid_edge(self):
        return self._x_edge

    def _grid_width(self):
        return self._x_edge - self._x1_pixel
    
    def _grid_height(self):
        return self._y_floor - self._y1_pixel
    
   
    def get_column_cords(self)-> [()]:
        '''
        Return a list of tuples cointaining line cordinates for columns in
        an nxn grid in the format [(x1,y1,x2,y2)]
        '''
        x = self._x1_pixel
        columns = self._columns
        delta_x = self._grid_width() / columns
        y = self._y1_pixel
        
        y2 = self._y_floor
        
        cord_list = []
        
        for i in range(columns + 1):
            cord_list.append((x, y, x, y2))
            x = x + delta_x
        return cord_list

    def get_row_cords(self)-> [()]:
        '''
        Return a list of tuples containing line cordinates for columns
        in an nxn gri in the format [(x1,y1,x2,y2)]
        '''
        x = self._x1_pixel
        x2 = self._x_edge
        y = self._y1_pixel
        rows = self._rows 
        delta_y = self._grid_height() / rows
        cord_list = []

        for i in range(rows + 1):
            cord_list.append((x, y, x2, y))
            y = y + delta_y
        return cord_list


    def get_column_bounds(self)->[['x1,x2']]:
        '''
        Given a list of tuples containing column cordinates
        give me the boundaries for each column
        '''
        columns= self.get_column_cords()
        column_boundaries = []
        for i in range(len(columns)-1):
            sub_list = []
            sub_list.append(columns[i][0])
            sub_list.append(columns[i+1][0])
            column_boundaries.append(sub_list)

        return column_boundaries

    def get_row_bounds(self)->[['y1,y2']]:
        '''
        Given a list of tuples containing column cordiantes
        give me the boundaries for each row in the following format
        [x1, x2, y1, y2]
        '''
        rows = self.get_row_cords()
        row_boundaries = []
        for i in range(len(rows)-1):
            sub_list = []
            sub_list.append(rows[i][1])
            sub_list.append(rows[i+1][1])
                                
            row_boundaries.append(sub_list)

        return row_boundaries


    def get_cells(self)->[[('x1,y1,x2,y2')]]:
        '''
        Create a two d list that contains tuples which are cordinates
        of all the spots in the grid. The item returned back is essentially
        a game board
        '''
        column_bounds = self.get_column_bounds()
        row_bounds = self.get_row_bounds()
        board = []
        for i in range(len(column_bounds)):
            sublist = []
            for j in range(len(row_bounds)):
                sublist.append((column_bounds[i][0], row_bounds[j][0],
                                column_bounds[i][1], row_bounds[j][1]))
            board.append(sublist)

        return board
        
        
                
    
            
            
            
            
            
        
        
 
        

    
                             
                             
        
        
            
        









    

    



##    def get_column_pixel_cords(self):
##        x = self._starting_pixel
##        self._window_width/self._board_columns
##        l = []
##        for i in range(self._board_columns + 1):
##            l.append((x, self._starting_pixel, x, self._window_height - self._starting_pixel))
##            x += (self._window_width-self._starting_pixel)/(self._board_columns+1)
##
##        return l
##
##    def get_row_pixel_cords(self):
##        y = self._starting_pixel
##        l = []
##        for i in range(self._board_rows + 1):
##            l.append((self._starting_pixel, y, self._window_width - self._starting_pixel, y))
##            y += ((self._window_height-self._starting_pixel)/(self._board_rows + 1))
##                  
##                  
##        
##        return l

