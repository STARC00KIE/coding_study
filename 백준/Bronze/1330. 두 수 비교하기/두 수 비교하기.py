class CompNum:
    def __init__(self, A, B):
        self.A = int(A)
        self.B = int(B)
        
    def comp(self):
        if self.A > self.B:
            print(">")
        elif self.A < self.B:
            print("<")
        else:
            print("==")
            
A, B = input().split()
F = CompNum(A, B)
F.comp()