from ChessPiece import Piece
from Container import ServiceContainer



def parseTable(piece, color):
  piece = piece.lower()
  color = color.lower()
  image_file = f"{color}_{piece}"

  return image_file, color

def getCollection():
  table = ServiceContainer.squareTable
  pieceCollection = []
  POSITION = 0
  OCCUPIED = 1
  COLOR = 2
  PIECENAME = 3
  for square in table:
    if table[square][OCCUPIED]:
      pieceCollection.append(Piece(*parseTable(table[square][PIECENAME], table[square][COLOR]), square, table[square][POSITION]))
  return pieceCollection

pieceCollection = getCollection()


if __name__ == "__main__":
  pieceCollection = getCollection()
  print(pieceCollection)
