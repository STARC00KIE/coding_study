class CalNum:
    def __init__(self, num1, num2, second=0, third=0, fourth=0):
        self.num1 = int(num1)
        self.num2 = int(num2)
        self.second = second
        self.thrid = third
        self.fourth = fourth
    
    def cal1(self):
        tmp = self.num2%10
        self.second = self.num1 * tmp
        print(self.second)
        self.num2 -= tmp
        
    def cal2(self):
        tmp = self.num2%100
        self.third = self.num1 * tmp // 10
        print(self.third)
        self.num2 -= tmp
        
    def cal3(self):
        tmp = self.num2%1000
        self.fourth = self.num1 * tmp // 100
        print(self.fourth)
        self.num2 -= tmp
    
    def result(self):
        res = self.second + self.third*10 + self.fourth*100
        print(res)
        
num1 = input()
num2 = input()
N = CalNum(num1, num2)
N.cal1()
N.cal2()
N.cal3()
N.result()