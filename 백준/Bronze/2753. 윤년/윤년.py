class year:
    def __init__(self, num):
        self.num = int(num)
        
    def comp(self):
        if (self.num%4 == 0) and (self.num%100 != 0):
            print("1")
        elif self.num % 400 == 0:
            print("1")
        else:
            print("0")
            
num = input()
F = year(num)
F.comp()