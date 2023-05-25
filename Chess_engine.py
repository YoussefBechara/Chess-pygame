import re
import pygame
import time

class Chess:
    def __init__(self) -> None:
        self.board = [
            ['black_rook', 'black_knight', 'black_bishop', 'black_queen', 'black_king', 'black_bishop', 'black_knight',
             'black_rook'],
            ['black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn',
             'black_pawn'], ['_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_',
                                                       '_'],
            ['white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn',
             'white_pawn'],
            ['white_rook', 'white_knight', 'white_bishop', 'white_queen', 'white_king', 'white_bishop', 'white_knight',
             'white_rook']]
        
    def has_moved(self, before_row, before_col):
        if self.board[before_row][before_col] == 'white_pawn':
            if before_row == 6:
                return False
        if self.board[before_row][before_col] == 'black_pawn':
            if before_row == 1:
                return False
        if 'king' in self.board[before_row][before_col]:
            if ((before_row == (0 or 7)) and (before_col == 4)):
                return False
        if 'rook' in self.board[before_row][before_col]:
            if ((before_row == (0 or 7)) and (before_col == (0 or 7))):
                return False
        return True

    def is_available_move(self, before_row, before_col, after_row, after_col):
        pass_variable = 0  # variable created to ontinue the code with the except
        global col_available_move
        col_available_move = []
        global row_available_move
        row_available_move = []
        piece = self.board[before_row][before_col]
        if 'white' in piece:
            side = 'white'
        elif 'black' in piece:
            side = 'black'
        if 'pawn' in piece:  # PAWN
            if piece == 'black_pawn':
                if self.has_moved(before_row, before_col) is True:
                    try:
                        if self.board[before_row + 1][before_col] == '_':
                            row_available_move.append(before_row + 1)
                            col_available_move.append(before_col)
                    except:
                        pass_variable = 5
                else:  # here we dont do try and except cuz this means that pawn hasnt moved yet
                    if self.board[before_row + 1][before_col] == '_':
                        row_available_move.append(before_row + 1)
                        col_available_move.append(before_col)
                    if self.board[before_row + 2][before_col] == '_':
                        row_available_move.append(before_row + 2)
                        col_available_move.append(before_col)
                try:
                    if self.board[before_row + 1][before_col + 1] != '_':  # taking
                        row_available_move.append(before_row + 1)
                        col_available_move.append(before_col + 1)
                except:
                    pass_variable = 5
                try:
                    if self.board[before_row + 1][before_col - 1] != '_':
                        row_available_move.append(before_row + 1)
                        col_available_move.append(before_col - 1)
                except:
                    pass_variable = 5
            if piece == 'white_pawn':
                if self.has_moved(before_row, before_col) is True:
                    try:
                        if self.board[before_row - 1][before_col] == '_':
                            row_available_move.append(before_row - 1)
                            col_available_move.append(before_col)
                    except:
                        pass_variable = 5
                else:  # here we dont try except
                    if self.board[before_row - 1][before_col] == '_':
                        row_available_move.append(before_row - 1)
                        col_available_move.append(before_col)
                    if self.board[before_row - 2][before_col] == '_':
                        row_available_move.append(before_row - 2)
                        col_available_move.append(before_col)
                try:
                    if self.board[before_row - 1][before_col - 1] != '_':
                        row_available_move.append(before_row - 1)
                        col_available_move.append(before_col - 1)
                except:
                    pass_variable = 5
                try:
                    if self.board[before_row - 1][before_col + 1] != '_':
                        row_available_move.append(before_row - 1)
                        col_available_move.append(before_col + 1)
                except:
                    pass_variable = 1
        if 'king' in piece:  # KING
            for r in range(-1, 2):
                for c in range(-1, 2):
                    try:
                        if side not in self.board[before_row+r][before_col+c]:
                            col_available_move.append(before_col + c)
                            row_available_move.append(before_row + r)
                    except:
                        continue
            if self.has_moved(before_row,before_col) == False:
                if side == 'white':
                    if (self.board[7][7] == 'white_rook') and ((self.board[7][6] == '_')) and (self.board[7][5] == '_'):
                        white_short_castle = True
                        row_available_move.append(7)
                        col_available_move.append(6)
                    if (self.board[7][0] == 'white_rook') and ((self.board[7][1] == '_')) and (self.board[7][2] == '_') and (self.board[7][3] == '_'):
                        white_long_castle = True
                        row_available_move.append(7)
                        col_available_move.append(before_col-2)
        if 'rook' in piece:  # ROOK
            for r in range(1, 9):
                try:
                    if side in self.board[before_row+r][before_col]:
                        break
                    if (self.board[before_row + r][before_col] != '_') and (side not in self.board[before_row+r][before_col]):
                        row_available_move.append(before_row + r)
                        col_available_move.append(before_col)
                        break
                    if side not in self.board[before_row+r][before_col]:
                        row_available_move.append(before_row + r)
                        col_available_move.append(before_col)
                except:
                    pass_variable = 11
            for r in range(1, 9):
                try:
                    if side in self.board[before_row-r][before_col]:
                        break
                    if (self.board[before_row - r][before_col] != '_') and (side not in self.board[before_row-r][before_col]):
                        row_available_move.append(before_row - r)
                        col_available_move.append(before_col)
                        break
                    if side not in self.board[before_row-r][before_col]:
                        row_available_move.append(before_row - r)
                        col_available_move.append(before_col)
                except:
                    pass_variable = 1
            for c in range(1, 9):
                try:
                    if side in self.board[before_row][before_col + c]:
                        break
                    if (self.board[before_row][before_col + c] != '_') and (side not in self.board[before_row][before_col+c]):
                        col_available_move.append(before_col + c)
                        row_available_move.append(before_row)
                        break
                    if side not in self.board[before_row][before_col+c]:
                        col_available_move.append(before_col + c)
                        row_available_move.append(before_row)
                except:
                    pass_variable = 0
            for c in range(1, 9):
                try:
                    if side in self.board[before_row][before_col - c]:
                        break
                    if (self.board[before_row][before_col - c] != '_') and (side not in self.board[before_row][before_col-c]):
                        col_available_move.append(before_col - c)
                        row_available_move.append(before_row)
                        break
                    if side not in self.board[before_row][before_col-c]:
                        col_available_move.append(before_col - c)
                        row_available_move.append(before_row)
                except:
                    pass_variable = 1
        if 'bishop' in piece:  # BISHOP
            for r in range(-1, 2, 2):
                for c in range(-1, 2, 2):
                    try:
                        if side in self.board[before_row+r][before_col+c]:
                            continue
                        col_available_move.append(before_col + c)
                        row_available_move.append(before_row + r)
                    except:
                        pass_variable = 5
                    try:
                        if (c < 0) and (r < 0) and (self.board[before_row - 1][before_col - 1] == '_'):
                            for i in range(7):
                                if self.board[before_row + r - i][before_col + c - i] != '_':
                                    col_available_move.append(before_col + c - i)
                                    row_available_move.append(before_row + r - i)
                                    break
                                elif self.board[before_row + r - i][before_col + c - i] == '_':
                                    col_available_move.append(before_col + c - i)
                                    row_available_move.append(before_row + r - i)
                    except:
                        pass_variable = 5
                    try:
                        if (c < 0) and (r > 0) and (self.board[before_row + 1][before_col - 1] == '_'):
                            for i in range(7):
                                if self.board[before_row + r + i][before_col + c - i] != '_':
                                    col_available_move.append(before_col + c - i)
                                    row_available_move.append(before_row + r + i)
                                    break
                                elif self.board[before_row + r + i][before_col + c - i] == '_':
                                    col_available_move.append(before_col + c - i)
                                    row_available_move.append(before_row + r + i)
                    except:
                        pass_variable = 5
                    try:
                        if (c > 0) and (r > 0) and (self.board[before_row + 1][before_col + 1] == '_'):
                            for i in range(7):
                                if self.board[before_row + r + i][before_col + c + i] != '_':
                                    col_available_move.append(before_col + c + i)
                                    row_available_move.append(before_row + r + i)
                                    break
                                elif self.board[before_row + r + i][before_col + c + i] == '_':
                                    col_available_move.append(before_col + c + i)
                                    row_available_move.append(before_row + r + i)
                    except:
                        pass_variable = 5
                    try:
                        if (c > 0) and (r < 0) and (self.board[before_row - 1][before_col + 1] == '_'):
                            for i in range(7):
                                if self.board[before_row + r - i][before_col + c + i] != '_':
                                    col_available_move.append(before_col + c + i)
                                    row_available_move.append(before_row + r - i)
                                    break
                                elif self.board[before_row + r - i][before_col + c + i] == '_':
                                    col_available_move.append(before_col + c + i)
                                    row_available_move.append(before_row + r - i)
                    except:
                        pass_variable = 5
        if 'knight' in piece:  # KNIGHT
            try:
                if side not in self.board[before_row+1][before_col+2]:
                    col_available_move.append(before_col + 2)  # la right or left
                    row_available_move.append(before_row + 1)
            except:
                pass_variable = 2
            try:
                if side not in self.board[before_row-1][before_col+2]:
                    col_available_move.append(before_col + 2)
                    row_available_move.append(before_row - 1)
            except:
                pass_variable = 3
            try:
                if side not in self.board[before_row+1][before_col-2]:
                    col_available_move.append(before_col - 2)
                    row_available_move.append(before_row + 1)
            except:
                pass_variable = 4
            try:
                if side not in self.board[before_row-1][before_col-2]:
                    col_available_move.append(before_col - 2)
                    row_available_move.append(before_row - 1)
            except:
                pass_variable = 5
                # la fo2 w ta7et
            try:
                if side not in self.board[before_row+2][before_col+1]:
                    col_available_move.append(before_col + 1)
                    row_available_move.append(before_row + 2)
            except:
                pass_variable = 5
            try:
                if side not in self.board[before_row+2][before_col-1]:
                    col_available_move.append(before_col - 1)
                    row_available_move.append(before_row + 2)
            except:
                pass_variable = 5
            try:
                if side not in self.board[before_row-2][before_col+1]:
                    col_available_move.append(before_col + 1)
                    row_available_move.append(before_row - 2)
            except:
                pass_variable = 5
            try:
                if side not in self.board[before_row-2][before_col-1]:
                    col_available_move.append(before_col - 1)
                    row_available_move.append(before_row - 2)
            except:
                pass_variable = 5
        if 'queen' in piece:  # QUEEN IS COMBINATION ROOK AND BISHOP
            for r in range(1, 9):
                try:
                    if side in self.board[before_row+r][before_col]:
                        break
                    if (self.board[before_row + r][before_col] != '_') and (side not in self.board[before_row+r][before_col]):
                        row_available_move.append(before_row + r)
                        col_available_move.append(before_col)
                        break
                    if side not in self.board[before_row+r][before_col]:
                        row_available_move.append(before_row + r)
                        col_available_move.append(before_col)
                except:
                    pass_variable = 11
            for r in range(1, 9):
                try:
                    if side in self.board[before_row-r][before_col]:
                        break
                    if (self.board[before_row - r][before_col] != '_') and (side not in self.board[before_row-r][before_col]):
                        row_available_move.append(before_row - r)
                        col_available_move.append(before_col)
                        break
                    if side not in self.board[before_row-r][before_col]:
                        row_available_move.append(before_row - r)
                        col_available_move.append(before_col)
                except:
                    pass_variable = 1
            for c in range(1, 9):
                try:
                    if side in self.board[before_row][before_col + c]:
                        break
                    if (self.board[before_row][before_col + c] != '_') and (side not in self.board[before_row][before_col+c]):
                        col_available_move.append(before_col + c)
                        row_available_move.append(before_row)
                        break
                    if side not in self.board[before_row][before_col+c]:
                        col_available_move.append(before_col + c)
                        row_available_move.append(before_row)
                except:
                    pass_variable = 0
            for c in range(1, 9):
                try:
                    if side in self.board[before_row][before_col - c]:
                        break
                    if (self.board[before_row][before_col - c] != '_') and (side not in self.board[before_row][before_col-c]):
                        col_available_move.append(before_col - c)
                        row_available_move.append(before_row)
                        break
                    if side not in self.board[before_row][before_col-c]:
                        col_available_move.append(before_col - c)
                        row_available_move.append(before_row)
                except:
                    pass_variable = 1
            for r in range(-1, 2, 2):
                for c in range(-1, 2, 2):
                    try:
                        if side in self.board[before_row+r][before_col+c]:
                            continue
                        col_available_move.append(before_col + c)
                        row_available_move.append(before_row + r)
                    except:
                        pass_variable = 5
                    try:
                        if (c < 0) and (r < 0) and (self.board[before_row - 1][before_col - 1] == '_'):
                            for i in range(7):
                                if self.board[before_row + r - i][before_col + c - i] != '_':
                                    col_available_move.append(before_col + c - i)
                                    row_available_move.append(before_row + r - i)
                                    break
                                elif self.board[before_row + r - i][before_col + c - i] == '_':
                                    col_available_move.append(before_col + c - i)
                                    row_available_move.append(before_row + r - i)
                    except:
                        pass_variable = 5
                    try:
                        if (c < 0) and (r > 0) and (self.board[before_row + 1][before_col - 1] == '_'):
                            for i in range(7):
                                if self.board[before_row + r + i][before_col + c - i] != '_':
                                    col_available_move.append(before_col + c - i)
                                    row_available_move.append(before_row + r + i)
                                    break
                                elif self.board[before_row + r + i][before_col + c - i] == '_':
                                    col_available_move.append(before_col + c - i)
                                    row_available_move.append(before_row + r + i)
                    except:
                        pass_variable = 5
                    try:
                        if (c > 0) and (r > 0) and (self.board[before_row + 1][before_col + 1] == '_'):
                            for i in range(7):
                                if self.board[before_row + r + i][before_col + c + i] != '_':
                                    col_available_move.append(before_col + c + i)
                                    row_available_move.append(before_row + r + i)
                                    break
                                elif self.board[before_row + r + i][before_col + c + i] == '_':
                                    col_available_move.append(before_col + c + i)
                                    row_available_move.append(before_row + r + i)
                    except:
                        pass_variable = 5
                    try:
                        if (c > 0) and (r < 0) and (self.board[before_row - 1][before_col + 1] == '_'):
                            for i in range(7):
                                if self.board[before_row + r - i][before_col + c + i] != '_':
                                    col_available_move.append(before_col + c + i)
                                    row_available_move.append(before_row + r - i)
                                    break
                                elif self.board[before_row + r - i][before_col + c + i] == '_':
                                    col_available_move.append(before_col + c + i)
                                    row_available_move.append(before_row + r - i)
                    except:
                        pass_variable = 5
        available_moves = list(zip(row_available_move, col_available_move))
        if (after_row, after_col) in available_moves:
            return True
        return False
        
            
    def get_board(self):
        return self.board
    def check_turn(self, turn, mx, my, height):
        side = 'hi'
        if turn%2 ==0:
            side = 'white'
        else:
            side = 'black'
        if side in self.board[my//height][mx//height]:
            return True
        return False
    def check_win(self):
        is_white_king_dead = 0
        is_black_king_dead = 0
        for r in range(8):
            for c in range(8):
                if 'white_king' not in self.board[r][c]:
                    is_white_king_dead += 1
                if 'black_king' not in self.board[r][c]:
                    is_black_king_dead += 1
        if (is_black_king_dead == 64) or (is_white_king_dead == 64):
            quit()
    def check_if_move_happened(self, b1, b2):
        for r in range(8):
            for c in range(8):
                if b1[r][c] != b2[r][c]:
                    #print('hi')
                    return True
        return False
    
def pygamez():
        pieces_generated = False
        pygame.init()
        screen_x = 480
        screen_y = 480
        screen = pygame.display.set_mode((screen_x, screen_y))
        x, y, width, height = 0, 0,screen_x//8, screen_y//8
        run = True
        squares_generated = 0
        play = Chess()
        i = True
        k = 0
        turn = 0
        dot = pygame.image.load('red dot.png')
        dot_img = pygame.transform.scale(dot, (35, 35))
        board = play.get_board()

        def generate_squares(x, y):
            squares_generated = 0
            while squares_generated <= 64:
                    for i in range(8):
                        if i % 2 == 0:
                            pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))
                        else:
                            pygame.draw.rect(screen, (0, 255, 0), (x, y, width, height))
                        x += width
                        squares_generated += 1
                    x = 0
                    y += height
                    for i in range(8):
                        if i % 2 == 0:
                            pygame.draw.rect(screen, (0, 255, 0), (x, y, width, height))
                        else:
                            pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))
                        x += width
                        squares_generated += 1
                    y += height
                    x = 0
        def generate_pieces():
            for c in range(8):
                        for r in range(8): 
                            if board[c][r] == 'black_bishop':
                                bb = pygame.image.load('bb.png')
                                screen.blit(bb, (r*height,c*height))
                            if board[c][r] == 'white_bishop':
                                wb = pygame.image.load('wb.png')
                                screen.blit(wb, (r*height,c*height))
                            if board[c][r] == 'black_pawn':
                                bp = pygame.image.load('bp.png')
                                screen.blit(bp, (r*height,c*height))
                            if board[c][r] == 'white_pawn':
                                wp = pygame.image.load('wp.png')
                                screen.blit(wp, (r*height,c*height))
                            if board[c][r] == 'black_king':
                                bk = pygame.image.load('bk.png')
                                screen.blit(bk, (r*height,c*height))
                            if board[c][r] == 'white_king':
                                wk = pygame.image.load('wk.png')
                                screen.blit(wk, (r*height,c*height))
                            if board[c][r] == 'black_queen':
                                bq = pygame.image.load('bq.png')
                                screen.blit(bq, (r*height,c*height))
                            if board[c][r] == 'white_queen':
                                wq = pygame.image.load('wq.png')
                                screen.blit(wq, (r*height,c*height))
                            if board[c][r] == 'black_rook':
                                br = pygame.image.load('br.png')
                                screen.blit(br, (r*height,c*height))
                            if board[c][r] == 'white_rook':
                                wr = pygame.image.load('wr.png')
                                screen.blit(wr, (r*height,c*height))
                            if board[c][r] == 'white_knight':
                                wknight = pygame.image.load('wknight.png')
                                screen.blit(wknight, (r*height,c*height))
                            if board[c][r] == 'black_knight':
                                bknight = pygame.image.load('bknight.png')
                                screen.blit(bknight, (r*height,c*height))                    
        def refresh_board(xx, yy):
                screen.fill((0,0,0))
                generate_squares(xx, yy)
                generate_pieces()
        
        while run:
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            if squares_generated < 64:
                generate_squares(x, y)
                pieces_generated = False  
            if pieces_generated == False: #if board is generated
                    generate_pieces()
                    pieces_generated = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if k%2 != 0:
                        ax , ay = pygame.mouse.get_pos()
                        if play.is_available_move(my//height, mx//height, ay//height, ax//height) is True:
                            board[ay//height][ax//height] = board[my//height][mx//height]
                            board[my//height][mx//height] = '_'
                            turn += 1 #only if the move is made we increment turn
                        i = False
                        play.check_win()
                        
                    else: #checking av moves
                        mx, my = pygame.mouse.get_pos()
                        refresh_board(x, y)
                        
                        if play.check_turn(turn, mx, my, height) is True: #show dots
                            play.is_available_move(my//height, mx//height, 0, 0)
                            coords =list(zip(row_available_move,col_available_move))
                            for i in range(len(coords)):
                                    screen.blit(dot_img, (coords[i][1]*height + height//4, coords[i][0]*height + height//4))
                            i = False
                
                    
            if event.type == pygame.MOUSEBUTTONUP:
                while i is False:
                    k += 1
                    i = True    
            pygame.display.update()
pygamez()