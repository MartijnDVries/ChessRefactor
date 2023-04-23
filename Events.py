import pygame
from config import *
from PieceCollection import PieceCollection
from Moves import LegalMoves
from SquareTable import SquareTable
from Game import Game
from MainMenu import MainMenu


class EventChecker:

    def __init__(self):
        self.eventCollection = {'game': self.game, 'main_menu': self.main_menu}
        self.pieceCollection = PieceCollection()
        self.pieces = self.pieceCollection.pieceCollection
        self.tableClass = SquareTable()
        self.table = self.tableClass.squareTable
        self.move = LegalMoves()
        self.Game = Game()  

    def loadEvents(self, view, event):
        self.eventCollection[view](event)

    def mouseDownEventGame(self, event):
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for piece in self.pieces:
                piece.setActive(pos)

    def mouseMoveEventGame(self, event):
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            for piece in self.pieces:
                piece.dragTo(pos)

    def mouseUpEventGame(self, event):
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            for piece in self.pieces:
                if piece.active:
                    self.checkMove(piece, pos)
                    piece.place()

    def checkMove(self, piece, pos):
        if is_inside_board(pos):
            new_square = self.tableClass.getSquareFromPos(pos)
            if piece.name == "KING":
                if self.Castling(new_square, piece):
                  return
            if self.move.is_legal(f"{piece.square}:{new_square}", piece.name):
                self.makeMove(piece, new_square)
                return
        piece.placeback()

    def makeMove(self, piece, new_square):
        self.pieceCollection.update(new_square)
        self.tableClass.setMove(piece.square, new_square)
        new_pos = self.table[new_square][POSITION]
        piece.update(new_pos, new_square)
        self.Game.check_game_outcome()

    def Castling(self, new_square, piece):
        white_kingcastle_squares = ['g1', 'h1']
        white_queencastle_squares = ['c1', 'b1', 'a1']
        black_kingcastle_squares = ['g8', 'h8']
        black_queencastle_squares = ['c8', 'b8', 'a8']
        if piece.color == "WHITE":
            if new_square in white_kingcastle_squares:
                if self.move.is_legal('O-O', "KING"):
                    self.tableClass.castle("WHITE", "king_side")
                    rook = self.pieceCollection.getPiece('h1')
                    rook.update(self.tableClass.getPositionFromSquare('f1'), 'f1')
                    piece.update(self.tableClass.getPositionFromSquare('g1'), 'g1')
                    self.Game.check_game_outcome()
                    return True
            if new_square in white_queencastle_squares:
                if self.move.is_legal('O-O-O', "KING"):
                    self.tableClass.castle("WHITE", "queen_side")
                    rook = self.pieceCollection.getPiece('a1')
                    rook.update(self.tableClass.getPositionFromSquare('d1'), 'd1')
                    piece.update(self.tableClass.getPositionFromSquare('c1'), 'c1')
                    self.Game.check_game_outcome()
                    return True
        elif piece.color == "BLACK":
            if new_square in black_kingcastle_squares:
                if self.move.is_legal('O-O', "KING"):
                    self.tableClass.castle("BLACK", "king_side")
                    rook = self.pieceCollection.getPiece('h8')
                    rook.update(self.tableClass.getPositionFromSquare('f8'), 'f8')
                    piece.update(self.tableClass.getPositionFromSquare('g8'), 'g8')
                    self.Game.check_game_outcome()
                    return True
            if new_square in black_queencastle_squares:
                if self.move.is_legal('O-O-O', "KING"):
                    self.tableClass.castle("BLACK", "queen_side")
                    rook = self.pieceCollection.getPiece('a8')
                    rook.update(self.tableClass.getPositionFromSquare('d8'), 'd8')
                    piece.update(self.tableClass.getPositionFromSquare('c8'), 'c8')
                    self.Game.check_game_outcome()
                    return True

    def game(self, event):
        self.mouseDownEventGame(event)
        self.mouseUpEventGame(event)
        self.mouseMoveEventGame(event)


    def main_menu(self, event):
        pass
