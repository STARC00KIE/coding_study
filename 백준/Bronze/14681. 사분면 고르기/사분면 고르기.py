class cal:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        
    def comp(self):
        if (self.x > 0) and (self.y > 0):
            print("1")
        elif (self.x < 0) and (self.y > 0):
            print("2")
        elif (self.x < 0) and (self.y < 0):
            print("3")
        elif (self.x > 0) and (self.y < 0):
            print("4")
            
x = input()
y = input()
F = cal(x, y)
F.comp()