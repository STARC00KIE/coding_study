class chess:
    def __init__(self, king, queen, rook, bishop, knight, pon):
        self.king = int(king)
        self.queen = int(queen)
        self.rook = int(rook)
        self.bishop = int(bishop)
        self.knight = int(knight)
        self.pon = int(pon)
    
    def chessNum(self):
        king = 1 - self.king
        queen = 1 - self.queen
        rook = 2 - self.rook
        bishop = 2 - self.bishop
        knight = 2 - self.knight
        pon = 8 - self.pon
        print(king, queen, rook, bishop, knight, pon)

king, queen, rook, bishop, knight, pon = input().split()
N = chess(king, queen, rook, bishop, knight, pon)
num = N.chessNum()