import pygame
from config import *
from PieceCollection import PieceCollection
from MovesNumpy import LegalMovesNumpy
from Position import Position
from Coordinates import Coordinates
from Game import Game


class GameEvents:

    def __init__(self):
        self.pieceCollection = PieceCollection()
        self.pieces = self.pieceCollection.pieceCollection
        self.positionHandler = Position()
        self.coordinates = Coordinates().coordinates
        self.table = self.positionHandler.position
        self.move = LegalMovesNumpy()
        self.Game = Game()

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
            new_square = self.positionHandler.getSquareFromPos(pos)
            if piece.name == "KING":
                if self.Castling(new_square, piece):
                    return
            if piece.name == "PAWN":
                if self.en_passant(new_square, piece):
                    return
            if self.move.is_legal(f"{piece.square}:{new_square}", piece.name):
                self.positionHandler.setMove(piece.square, new_square)
                self.updateEvent(piece, new_square)
                return
        piece.placeback()

    def updateEvent(self, piece, new_square):
        self.pieceCollection.update(new_square)
        new_pos = self.coordinates[new_square]
        piece.update(new_pos, new_square)
        self.Game.check_game_outcome()

    def en_passant(self, new_square, piece):
        if abs(int(piece.square) - new_square) == 7\
                or abs(int(piece.square) - new_square) == 9:
            if not self.positionHandler.hasPiece(new_square):
                ep_move = f'{piece.square}:{new_square}'
                if self.Game.turn == 'WHITE':
                    ep_square = new_square - DOWN
                else:
                    ep_square = new_square + UP
                if self.move.is_legal(ep_move, piece.name):
                    self.positionHandler.setEnpassantMove(
                        ep_square, new_square, piece.square)
                    self.updateEvent(piece, new_square)
                    return True

    def Castling(self, new_square, piece):
        white_kingcastle_squares = {G1, H1}
        white_queencastle_squares = {C1, B1, A1}
        black_kingcastle_squares = {G8, H8}
        black_queencastle_squares = {C8, B8, A8}
        if piece.color == "WHITE":
            if new_square in white_kingcastle_squares:
                if self.move.is_legal('O-O', "KING"):
                    self.positionHandler.castle("WHITE", "king_side")
                    rook = self.pieceCollection.getPiece(H1)
                    rook.update(
                        self.positionHandler.getPositionFromSquare(F1),  F1)
                    piece.update(
                        self.positionHandler.getPositionFromSquare(G1), G1)
                    self.Game.check_game_outcome()
                    return True
            if new_square in white_queencastle_squares:
                if self.move.is_legal('O-O-O', "KING"):
                    self.positionHandler.castle("WHITE", "queen_side")
                    rook = self.pieceCollection.getPiece(A1)
                    rook.update(
                        self.positionHandler.getPositionFromSquare(D1), D1)
                    piece.update(
                        self.positionHandler.getPositionFromSquare(C1), C1)
                    self.Game.check_game_outcome()
                    return True
        elif piece.color == "BLACK":
            if new_square in black_kingcastle_squares:
                if self.move.is_legal('O-O', "KING"):
                    self.positionHandler.castle("BLACK", "king_side")
                    rook = self.pieceCollection.getPiece(H8)
                    rook.update(
                        self.positionHandler.getPositionFromSquare(F8), F8)
                    piece.update(
                        self.positionHandler.getPositionFromSquare(G8), G8)
                    self.Game.check_game_outcome()
                    return True
            if new_square in black_queencastle_squares:
                if self.move.is_legal('O-O-O', "KING"):
                    self.positionHandler.castle("BLACK", "queen_side")
                    rook = self.pieceCollection.getPiece(A8)
                    rook.update(
                        self.positionHandler.getPositionFromSquare(D8), D8)
                    piece.update(
                        self.positionHandler.getPositionFromSquare(C8), C8)
                    self.Game.check_game_outcome()
                    return True

    def events(self, event):
        self.mouseDownEventGame(event)
        self.mouseUpEventGame(event)
        self.mouseMoveEventGame(event)
