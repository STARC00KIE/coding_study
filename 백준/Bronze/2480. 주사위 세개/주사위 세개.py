class dice:
    def __init__(self, *di, dice_num = 0, cnt =0):
        self.dice3 = list(di)
        self.dice_num = dice_num
        self.cnt = cnt
    
    def dice_chk(self):
        dicelst = []
        dicelst = self.dice3
        for i in range(6):   # 0, 1, 2
            if dicelst.count(i+1) > 1:
                self.dice_num = dicelst.count(i+1) # 소 나온 개수
                self.cnt = i+1
    
    def result(self):
        if self.dice_num == 3:
            res = self.cnt*1000 + 10000
        elif self.dice_num == 2:
            res = self.cnt*100 + 1000
        else:
            tmp = max(self.dice3)
            res = tmp*100
        return res


d1, d2, d3 = map(int, input().split())
N = dice(d1, d2, d3)
N.dice_chk()
res = N.result()
print(res)