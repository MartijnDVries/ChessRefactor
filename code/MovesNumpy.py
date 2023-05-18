from config import *
from CheckForChecksNumpy import CheckForChecksNumpy
from SquareTableNumpy import SquareTableNumpy
from Singleton import Singleton
from GetSquaresNumpy import GetSquaresNumpy
import ujson

class LegalMovesNumpy(metaclass=Singleton):
    def __init__(self):
        self.check = CheckForChecksNumpy()
        self.table = SquareTableNumpy()
        self.get = GetSquaresNumpy()
        self.white_kingcastle_rights = True
        self.white_queencastle_rights = True
        self.black_kingcastle_rights = True
        self.black_queencastle_rights = True
        self.moves = []
        
    def is_legal(self, move, piece_name):
        print("move in is legal", move)
        if move in self.moves:
            self.set_last_move(piece_name, move)
            if piece_name == "KING" or piece_name == "ROOK":
                old_square = move[:2]
                self.set_castling_rights(old_square, piece_name)
            return True

    def set_last_move(self, piece_name, move):
        self.last_move = {'piece': piece_name, 'move': move}

    def set_castling_rights(self, old_square, piece_name):
        if piece_name == "ROOK":
            if old_square == 'h1':
                self.white_kingcastle_rights = False
            if old_square == 'a1':
                self.white_kingcastle_rights = False
            if old_square == 'h8':
                self.black_kingcastle_rights = False
            if old_square == 'a8':
                self.black_queencastle_rights = False
        elif piece_name == "KING":
            if old_square == 'e1':
                self.white_kingcastle_rights = False
                self.white_queencastle_rights = False
            if old_square == 'e8':
                self.black_kingcastle_rights = False
                self.black_queencastle_rights = False
        
    
    def add_move(self, table, piece_square, square, own_color):
        table_copy = self.table.copyTable(table)

        self.table.setMove(piece_square, square, table_copy)
        if not(self.check.is_in_check(own_color, table_copy)):
            # return f"{piece_square}:{square}"
            return f"{self.test_for_squares_names(piece_square)}:{self.test_for_squares_names(square)}"
        return None
    
    def test_for_squares_names(self, square):
        return self.table.getSquareFromIndex(square)

    def moves_list(self, table, own_color):
        moves_list = []

        # En passant moves
        moves_list.extend(self.check_en_passant(table, own_color))

        # Castling
        moves_list.extend(self.check_castling(table, own_color))

        for square_index, square in enumerate(table):

            if not self.table.hasColorOnSquare(square, own_color):
                continue

            if self.table.hasPieceOnSquare(square, "ROOK"):
                for dir in ["right", "left"]:
                    squares = list(self.get.horizontal_squares_from(square_index, dir))
                    moves_list.extend(self.piece_moves(table, square_index, squares, own_color))
                for dir in ["up", "down"]:
                    squares = list(self.get.vertical_squares_from(square_index, dir))
                    moves_list.extend(self.piece_moves(table, square_index, squares, own_color))

            elif self.table.hasPieceOnSquare(square, "PAWN"):
                squares = self.get.pawn_move_squares_from(square_index, own_color)
                moves_list.extend(self.pawn_moves(table, square_index, squares, own_color))
                squares = self.get.pawn_capture_squares_from(square_index, own_color)
                moves_list.extend(self.pawn_captures(table, square_index, squares, own_color))

            elif self.table.hasPieceOnSquare(square, "BISHOP"):
                for dir in ["right_up", "right_down", "left_up", "left_down"]:
                    squares = list(self.get.diagonal_squares_from(square_index, dir))
                    moves_list.extend(self.piece_moves(table, square_index, squares, own_color))

            elif self.table.hasPieceOnSquare(square, "KNIGHT"):
                squares = self.get.knight_squares_from(square_index)
                moves_list.extend(self.knight_moves(table, square_index, squares, own_color))

            elif self.table.hasPieceOnSquare(square, "QUEEN"):
                for dir in ["right_up", "right_down", "left_up", "left_down"]:
                    squares = list(self.get.diagonal_squares_from(square_index, dir))
                    moves_list.extend(self.piece_moves(table, square_index, squares, own_color))
                for dir in ["right", "left"]:
                    squares = list(self.get.horizontal_squares_from(square_index, dir))
                    moves_list.extend(self.piece_moves(table, square_index, squares, own_color))
                for dir in ["up", "down"]:
                    squares = list(self.get.vertical_squares_from(square_index, dir))
                    moves_list.extend(self.piece_moves(table, square_index, squares, own_color))

            elif self.table.hasPieceOnSquare(square, "KING"):
                squares = self.get.king_squares(square_index)
                moves_list.extend(self.king_moves(table, square_index, squares, own_color))
       
        self.moves = filter_none(moves_list)

    def piece_moves(self, table, piece_square, squares, own_color):
        moves = []
        enemy_color = get_enemy_color(own_color)
        for square in squares:
            if self.table.hasColor(square, own_color, table):
                return moves
            if self.table.hasColor(square, enemy_color, table):
                moves.append(self.add_move(table, piece_square, square, own_color))
                return moves
            elif not self.table.hasPiece(square, table=table):
                moves.append(self.add_move(table, piece_square, square, own_color))
        return moves
    
    def king_moves(self, table, king_square, squares, own_color):
        moves = []
        enemy_color = get_enemy_color(own_color)
        for square in squares:
            if self.table.hasColor(square, own_color, table):
                continue
            if self.table.hasColor(square, enemy_color, table):
                moves.append(self.add_move(table, king_square, square, own_color))
            if not self.table.hasPiece(square, table=table):
                moves.append(self.add_move(table, king_square, square, own_color))
        return moves
    
    def knight_moves(self, table, piece_square, squares, own_color):
        moves = []
        enemy_color = get_enemy_color(own_color)
        for square in squares:
            if self.table.hasColor(square, own_color, table):
                continue
            if self.table.hasColor(square, enemy_color, table):
                moves.append(self.add_move(table, piece_square, square, own_color))
            if not self.table.hasPiece(square, table=table):
                moves.append(self.add_move(table, piece_square, square, own_color))
        return moves
                                
    def pawn_moves(self, table, pawn_square, squares, own_color):
        moves = []
        for square in squares:
            if self.table.hasPiece(square, table=table):
                return moves
            else:
                moves.append(self.add_move(table, pawn_square, square, own_color))
        return moves


    def pawn_captures(self, table, pawn_square, squares, own_color):
        moves = []
        enemy_color = get_enemy_color(own_color)
        for square in squares:
            if self.table.hasColor(square, enemy_color, table):
                moves.append(self.add_move(table, pawn_square, square, own_color))
        return moves
        
                
    def check_en_passant(self, table, own_color):
        moves = []
        enemy_color = get_enemy_color(own_color)

        # If no last move is set
        if not hasattr(self, 'last_move'):
            return moves
        
        # If last move is not pawn
        if not self.last_move['piece'] == "PAWN":
            return moves
        
        # If last move is not pawn two forward
        old_row = int(self.last_move['move'][1])
        new_row = int(self.last_move['move'][4])
        row_differnce = abs(new_row - old_row)
        if row_differnce != 2:
            return moves
        
        # If last move is not enemy pawn
        last_enemy_square = self.last_move['move'][3:]
        last_enemy_square_index = self.table.getSquareIndex(last_enemy_square)

        
         # if our pawn is next to the enemy pawn and the capture square is empty
        if last_enemy_square_index - LEFT:
            left_square = last_enemy_square_index - LEFT
        if last_enemy_square_index + RIGHT:
            right_square = last_enemy_square_index + RIGHT


        if own_color == 'WHITE':
            capture_square = last_enemy_square_index + UP
        else:
            capture_square = last_enemy_square_index - DOWN

        if self.table.hasPiece(left_square, "PAWN", table)\
              and self.table.hasColor(left_square, own_color, table)\
              and not self.table.hasPiece(capture_square, table=table):
            table_copy = self.table.copyTable(table)
            self.table.setEnpassantMove(last_enemy_square_index, left_square, capture_square, table_copy)
            if not self.check.is_in_check(own_color, table_copy):
                # move = f"{left_square}:{capture_square}"
                move = f"{self.test_for_squares_names(left_square)}:{self.test_for_squares_names(capture_square)}"
                moves.append(move)
  

        if self.table.hasPiece(right_square, "PAWN", table)\
              and self.table.hasColor(right_square, own_color, table)\
              and not self.table.hasPiece(capture_square, table=table):
            table_copy = self.table.copyTable(table)
            self.table.setEnpassantMove(last_enemy_square_index, right_square, capture_square, table_copy)
            if not self.check.is_in_check(own_color, table_copy):
                # move = f"{right_square}:{capture_square}"
                move = f"{self.test_for_squares_names(right_square)}:{self.test_for_squares_names(capture_square)}"
                moves.append(move)

      
        return moves

    def check_castling(self, table, own_color):
        moves = []
        if self.check.is_in_check(own_color, table):
            return moves
        if own_color == "WHITE":
            if self.white_kingcastle_rights:
                if not self.table.hasPiece(F1) and not self.table.hasPiece(G1):
                    moves.append("O-O")
            if self.white_queencastle_rights:
                if not self.table.hasPiece(D1) and not self.table.hasPiece(C1) and not self.table.hasPiece(B1):
                    moves.append("O-O-O")
        elif own_color == "BLACK":
            if self.black_kingcastle_rights:
                if not self.table.hasPiece(F8) and not self.table.hasPiece(G8):
                    moves.append("O-O")
            if self.black_queencastle_rights:
                if not self.table.hasPiece(D8) and not self.table.hasPiece(C8) and not self.table.hasPiece(B8):
                    moves.append("O-O-O")
        return moves
        
            
        
    
                    
if __name__ == "__main__":
    l = LegalMovesNumpy()
    s = SquareTableNumpy()
    s_list = s.getTable()
    
    s.setMove(D2, D5)
    s.setMove(E7, E5)
    l.set_last_move('PAWN', 'e7:e5')
    l.moves_list(s_list, 'WHITE')

    print(l.moves)

    