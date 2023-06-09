from config import *
from CheckForChecks import CheckForChecks
from SquareTable import SquareTable
from Singleton import Singleton
from GetSquares import GetSquares
import ujson

class LegalMoves(metaclass=Singleton):
    def __init__(self):
        self.check = CheckForChecks()
        self.table = SquareTable()
        self.get = GetSquares()
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
        
        
    def copy(self, table):
        return ujson.loads(ujson.dumps(table))
    
    def add_move(self, table, piece_square, square, own_color):
        table_copy = self.copy(table)
        self.table.setMove(piece_square, square, table_copy)
        if not(self.check.is_in_check(own_color, table_copy)):
            return f"{piece_square}:{square}"
        return None

    def moves_list(self, table, own_color):
        moves_list = []

        # En passant moves
        moves_list.extend(self.check_en_passant(table, own_color))

        # Castling
        moves_list.extend(self.check_castling(table, own_color))

        for square in table:
            
            
            if not self.table.hasColor(square, own_color, table) or not self.table.hasPiece(square, table=table):
                continue

            if self.table.hasPiece(square, "ROOK", table):
                for dir in ["right", "left"]:
                    squares = self.get.horizontal_squares_from(square, dir)
                    moves_list.extend(self.piece_moves(table, square, squares, own_color))
                for dir in ["up", "down"]:
                    squares = self.get.vertical_squares_from(square, dir)
                    moves_list.extend(self.piece_moves(table, square, squares, own_color))

            elif self.table.hasPiece(square, "PAWN", table):
                squares = self.get.pawn_move_squares_from(square, own_color)
                moves_list.extend(self.pawn_moves(table, square, squares, own_color))
                squares = self.get.pawn_capture_squares_from(square, own_color)
                moves_list.extend(self.pawn_captures(table, square, squares, own_color))

            elif self.table.hasPiece(square, "BISHOP", table):
                for dir in ["right_up", "right_down", "left_up", "left_down"]:
                    squares = self.get.diagonal_squares_from(square, dir)
                    moves_list.extend(self.piece_moves(table, square, squares, own_color))

            elif self.table.hasPiece(square, "KNIGHT", table):
                squares = self.get.knight_squares_from(square)
                moves_list.extend(self.knight_moves(table, square, squares, own_color))

            elif self.table.hasPiece(square, "QUEEN", table):
                for dir in ["right_up", "right_down", "left_up", "left_down"]:
                    squares = self.get.diagonal_squares_from(square, dir)
                    moves_list.extend(self.piece_moves(table, square, squares, own_color))
                for dir in ["right", "left"]:
                    squares = self.get.horizontal_squares_from(square, dir)
                    moves_list.extend(self.piece_moves(table, square, squares, own_color))
                for dir in ["up", "down"]:
                    squares = self.get.vertical_squares_from(square, dir)
                    moves_list.extend(self.piece_moves(table, square, squares, own_color))

            elif self.table.hasPiece(square, "KING", table):
                squares = self.get.king_squares(square)
                moves_list.extend(self.king_moves(table, square, squares, own_color))
       
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
            elif not self.table.hasPiece(square, table):
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
        new_square = self.last_move['move'][3:]
        if not self.table.hasColor(new_square, enemy_color, table):
            return moves
        
         # if our pawn is next to the enemy pawn and the capture square is empty
        left_square = self.get.getNewSquare(new_square, 1, 0)
        right_square = self.get.getNewSquare(new_square, -1, 0)

        if new_row == 5:
            capture_square = self.get.getNewSquare(new_square, 0, 1)
        else:
            capture_square = self.get.getNewSquare(new_square, 0, -1)
        try:
            if self.table.hasPiece(left_square, "PAWN", table)\
                and self.table.hasColor(left_square, own_color, table)\
                and not self.table.hasPiece(capture_square, table=table):
                table_copy = self.copy(table)
                self.table.setEnpassantMove(new_square, left_square, capture_square, table_copy)
                if not self.check.is_in_check(own_color, table_copy):
                    move = f"{left_square}:{capture_square}"
                    moves.append(move)
        except KeyError:
            pass

        try:
            if self.table.hasPiece(right_square, "PAWN", table)\
                and self.table.hasColor(right_square, own_color, table)\
                and not self.table.hasPiece(capture_square, table=table):
                table_copy = self.copy(table)
                self.table.setEnpassantMove(new_square, right_square, capture_square, table_copy)
                if not self.check.is_in_check(own_color, table_copy):
                    move = f"{right_square}:{capture_square}"
                    moves.append(move)
        except KeyError:
            pass
      
        return moves

    def check_castling(self, table, own_color):
        moves = []
        if self.check.is_in_check(own_color, table):
            return moves
        if own_color == "WHITE":
            if self.white_kingcastle_rights:
                if not self.table.hasPiece('f1') and not self.table.hasPiece('g1'):
                    moves.append("O-O")
            if self.white_queencastle_rights:
                if not self.table.hasPiece('d1') and not self.table.hasPiece('c1') and not self.table.hasPiece('b1'):
                    moves.append("O-O-O")
        elif own_color == "BLACK":
            if self.black_kingcastle_rights:
                if not self.table.hasPiece('f8') and not self.table.hasPiece('g8'):
                    moves.append("O-O")
            if self.black_queencastle_rights:
                if not self.table.hasPiece('d8') and not self.table.hasPiece('c8') and not self.table.hasPiece('b8'):
                    moves.append("O-O-O")
        return moves
        
            
        
    
                    
if __name__ == "__main__":
    l = LegalMoves()
    s = SquareTable()
    s_list = s.getTable()

    
    print(l.moves_list(s_list, 'WHITE'))
    print(l.moves)

    