from config import *
from CheckForChecks import CheckForChecks
from Position import Position
from Singleton import Singleton
from GetSquares import GetSquares
import ujson


class LegalMovesNumpy(metaclass=Singleton):
    def __init__(self):
        self.check = CheckForChecks()
        self.positionHandler = Position()
        self.get = GetSquares()
        self.white_kingcastle_rights = True
        self.white_queencastle_rights = True
        self.black_kingcastle_rights = True
        self.black_queencastle_rights = True
        self.castle_moves = {'O-O', 'O-O-O'}
        self.moves = []

    def is_legal(self, move, piece_name, color=None):
        if move in self.moves:
            self.set_last_move(piece_name, move)
            if piece_name == "KING" or piece_name == "ROOK":
                self.set_castling_rights(move, piece_name, color)
            return True

    def set_last_move(self, piece_name, move):
        self.last_move = {'piece': piece_name, 'move': move}

    def last_old_square(self):
        if self.last_move['move'] not in self.castle_moves:
            last_old_square = self.last_move['move'].split(':')
            return last_old_square[0]

    def last_new_square(self):
        if self.last_move['move'] not in self.castle_moves:
            last_old_square = self.last_move['move'].split(':')
            return last_old_square[1]

    def set_castling_rights(self, move, piece_name, color=None):
        if move in self.castle_moves:
            if move == 'O-O':
                if color == 'WHITE':
                    self.white_kingcastle_rights = False
                else:
                    self.black_kingcastle_rights = False
            elif move == 'O-O-O':
                if color == 'WHITE':
                    self.white_queencastle_rights = False
                else:
                    self.black_queencastle_rights = False
        elif piece_name == "ROOK":
            old_square = move.split(':')[0]
            if old_square == H1:
                self.white_kingcastle_rights = False
            if old_square == A1:
                self.white_kingcastle_rights = False
            if old_square == H8:
                self.black_kingcastle_rights = False
            if old_square == A8:
                self.black_queencastle_rights = False
        elif piece_name == "KING":
            if old_square == E1:
                self.white_kingcastle_rights = False
                self.white_queencastle_rights = False
            if old_square == E8:
                self.black_kingcastle_rights = False
                self.black_queencastle_rights = False

    def add_move(self, position, piece_square, square, own_color):
        table_copy = self.positionHandler.copyTable(position)

        self.positionHandler.setMove(piece_square, square, table_copy)
        if not (self.check.is_in_check(own_color, table_copy)):
            return f"{piece_square}:{square}"
            # return f"{self.test_for_squares_names(piece_square)}:{self.test_for_squares_names(square)}"
        return None

    def test_for_squares_names(self, square):
        return self.positionHandler.getSquareFromIndex(square)

    def moves_list(self, position, own_color):
        moves_list = []

        # En passant moves
        moves_list.extend(self.check_en_passant(position, own_color))

        # Castling
        moves_list.extend(self.check_castling(position, own_color))

        for square_index, square in enumerate(position):

            if not self.positionHandler.hasColorOnSquare(square, own_color):
                continue

            if self.positionHandler.hasPieceOnSquare(square, "ROOK"):
                for dir in ["right", "left"]:
                    squares = list(
                        self.get.horizontal_squares_from(square_index, dir))
                    moves_list.extend(self.piece_moves(
                        position, square_index, squares, own_color))
                for dir in ["up", "down"]:
                    squares = list(
                        self.get.vertical_squares_from(square_index, dir))
                    moves_list.extend(self.piece_moves(
                        position, square_index, squares, own_color))

            elif self.positionHandler.hasPieceOnSquare(square, "PAWN"):
                squares = self.get.pawn_move_squares_from(
                    square_index, own_color)
                moves_list.extend(self.pawn_moves(
                    position, square_index, squares, own_color))

            elif self.positionHandler.hasPieceOnSquare(square, "BISHOP"):
                for dir in ["right_up", "right_down", "left_up", "left_down"]:
                    squares = list(
                        self.get.diagonal_squares_from(square_index, dir))
                    moves_list.extend(self.piece_moves(
                        position, square_index, squares, own_color))

            elif self.positionHandler.hasPieceOnSquare(square, "KNIGHT"):
                squares = self.get.knight_squares_from(square_index)
                moves_list.extend(self.knight_moves(
                    position, square_index, squares, own_color))

            elif self.positionHandler.hasPieceOnSquare(square, "QUEEN"):
                for dir in ["right_up", "right_down", "left_up", "left_down"]:
                    squares = list(
                        self.get.diagonal_squares_from(square_index, dir))
                    moves_list.extend(self.piece_moves(
                        position, square_index, squares, own_color))
                for dir in ["right", "left"]:
                    squares = list(
                        self.get.horizontal_squares_from(square_index, dir))
                    moves_list.extend(self.piece_moves(
                        position, square_index, squares, own_color))
                for dir in ["up", "down"]:
                    squares = list(
                        self.get.vertical_squares_from(square_index, dir))
                    moves_list.extend(self.piece_moves(
                        position, square_index, squares, own_color))

            elif self.positionHandler.hasPieceOnSquare(square, "KING"):
                squares = self.get.king_squares(square_index)
                moves_list.extend(self.king_moves(
                    position, square_index, squares, own_color))

        self.moves = filter_none(moves_list)
        return self.moves

    def piece_moves(self, position, piece_square, squares, own_color):
        moves = []
        enemy_color = get_enemy_color(own_color)
        for square in squares:
            if self.positionHandler.hasColor(square, own_color, position):
                return moves
            if self.positionHandler.hasColor(square, enemy_color, position):
                moves.append(self.add_move(
                    position, piece_square, square, own_color))
                return moves
            elif not self.positionHandler.hasPiece(square, position=position):
                moves.append(self.add_move(
                    position, piece_square, square, own_color))
        return moves

    def king_moves(self, position, king_square, squares, own_color):
        moves = []
        enemy_color = get_enemy_color(own_color)
        for square in squares:
            if self.positionHandler.hasColor(square, own_color, position):
                continue
            if self.positionHandler.hasColor(square, enemy_color, position):
                moves.append(self.add_move(
                    position, king_square, square, own_color))
            if not self.positionHandler.hasPiece(square, position=position):
                moves.append(self.add_move(
                    position, king_square, square, own_color))
        return moves

    def knight_moves(self, position, piece_square, squares, own_color):
        moves = []
        enemy_color = get_enemy_color(own_color)
        for square in squares:
            if self.positionHandler.hasColor(square, own_color, position):
                continue
            if self.positionHandler.hasColor(square, enemy_color, position):
                moves.append(self.add_move(
                    position, piece_square, square, own_color))
            if not self.positionHandler.hasPiece(square, position=position):
                moves.append(self.add_move(
                    position, piece_square, square, own_color))
        return moves

    def pawn_moves(self, position, pawn_square, squares, own_color):
        moves = []
        for square in squares:
            if self.positionHandler.hasPiece(square, position=position):
                return moves
            else:
                moves.append(self.add_move(
                    position, pawn_square, square, own_color))
        return moves

    def pawn_captures(self, position, pawn_square, squares, own_color):
        moves = []
        enemy_color = get_enemy_color(own_color)
        for square in squares:
            if self.positionHandler.hasColor(square, enemy_color, position):
                moves.append(self.add_move(
                    position, pawn_square, square, own_color))
        return moves

    def check_en_passant(self, position, own_color):
        moves = []
        enemy_color = get_enemy_color(own_color)

        # If no last move is set
        if not hasattr(self, 'last_move'):
            return moves

        # If last move is not pawn
        if not self.last_move['piece'] == "PAWN":
            return moves

        # If last move is not pawn two forward
        last_old_square = int(self.last_old_square())
        last_new_square = int(self.last_new_square())
        row_differnce = abs(last_new_square - last_old_square)
        if row_differnce != 16:
            return moves

        # If last move is not enemy pawn
        last_enemy_square_index = int(self.last_new_square())

        # if our pawn is next to the enemy pawn and the capture square is empty
        if last_enemy_square_index - LEFT:
            left_square = last_enemy_square_index - LEFT
        if last_enemy_square_index + RIGHT:
            right_square = last_enemy_square_index + RIGHT

        if own_color == 'WHITE':
            capture_square = last_enemy_square_index + UP
        else:
            capture_square = last_enemy_square_index - DOWN

        if self.positionHandler.hasPiece(left_square, "PAWN", position)\
                and self.positionHandler.hasColor(left_square, own_color, position)\
                and not self.positionHandler.hasPiece(capture_square, position=position):
            table_copy = self.positionHandler.copyTable(position)
            self.positionHandler.setEnpassantMove(
                last_enemy_square_index, left_square, capture_square, table_copy)
            if not self.check.is_in_check(own_color, table_copy):
                move = f"{left_square}:{capture_square}"
                # move = f"{self.test_for_squares_names(left_square)}:{self.test_for_squares_names(capture_square)}"
                moves.append(move)

        if self.positionHandler.hasPiece(right_square, "PAWN", position)\
                and self.positionHandler.hasColor(right_square, own_color, position)\
                and not self.positionHandler.hasPiece(capture_square, position=position):
            table_copy = self.positionHandler.copyTable(position)
            self.positionHandler.setEnpassantMove(
                last_enemy_square_index, right_square, capture_square, table_copy)
            if not self.check.is_in_check(own_color, table_copy):
                move = f"{right_square}:{capture_square}"
                # move = f"{self.test_for_squares_names(right_square)}:{self.test_for_squares_names(capture_square)}"
                moves.append(move)

        return moves

    def check_castling(self, position, own_color):
        moves = []
        if self.check.is_in_check(own_color, position):
            return moves
        if own_color == "WHITE":
            if self.white_kingcastle_rights:
                if not self.positionHandler.hasPiece(F1)\
                        and not self.positionHandler.hasPiece(G1):
                    moves.append("O-O")
            if self.white_queencastle_rights:
                if not self.positionHandler.hasPiece(D1)\
                        and not self.positionHandler.hasPiece(C1)\
                        and not self.positionHandler.hasPiece(B1):
                    moves.append("O-O-O")
        elif own_color == "BLACK":
            if self.black_kingcastle_rights:
                if not self.positionHandler.hasPiece(F8)\
                        and not self.positionHandler.hasPiece(G8):
                    moves.append("O-O")
            if self.black_queencastle_rights:
                if not self.positionHandler.hasPiece(D8)\
                        and not self.positionHandler.hasPiece(C8)\
                        and not self.positionHandler.hasPiece(B8):
                    moves.append("O-O-O")
        return moves


if __name__ == "__main__":
    l = LegalMovesNumpy()
    s = Position()
    s_list = s.getTable()

    s.setMove(D2, D5)
    s.setMove(E7, E6)
    l.set_last_move('PAWN', '52:36')

    # print(l.last_old_square())
    print(l.moves_list(s_list, 'BLACK'))
