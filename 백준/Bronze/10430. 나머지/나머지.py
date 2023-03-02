class CalNum:
    def __init__(self, A, B, C):
        self.A = int(A)
        self.B = int(B)
        self.C = int(C)
    
    def cal(self):
        first = (self.A+self.B)%self.C
        print(first)
        second = ((self.A%self.C) + (self.B%self.C))%self.C
        print(second)
        third = (self.A*self.B)%self.C
        print(third)
        fourth = ((self.A%self.C) * (self.B%self.C))%self.C
        print(fourth)

A, B, C = input().split()
N = CalNum(A, B, C)
N.cal()