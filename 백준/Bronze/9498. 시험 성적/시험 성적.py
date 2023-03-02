class Record:
    def __init__(self, res):
        self.res = int(res)

        
    def comp(self):
        if 90 <= self.res <= 100:
            print("A")
        elif 80 <= self.res <= 89:
            print("B")
        elif 70 <= self.res <= 79:
            print("C")
        elif 60 <= self.res <= 69:
            print("D")
        else:
            print("F")
            
res = input()
F = Record(res)
F.comp()