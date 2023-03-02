class cal:
    def __init__(self, H, M):
        self.H = int(H)
        self.M = int(M)
        
    def comp(self):
        tmp = self.M - 45
        if tmp >= 0:
            print(self.H, tmp)
        elif tmp < 0:
            if self.H == 0:
                self.H = 23
                self.M = 60+tmp
                print(self.H, self.M)
            else:
                self.H -= 1
                self.M = 60+tmp
                print(self.H, self.M)
            
H, M = input().split()
F = cal(H, M)
F.comp()