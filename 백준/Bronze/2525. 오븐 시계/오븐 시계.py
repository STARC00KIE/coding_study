class oven:
    def __init__(self, hour, min, time):
        self.hour = hour
        self.min = min
        self.time = time
    
    def sum(self):
        self.min += self.time
    
    def result(self):
        if self.min >= 60:
            if self.min % 60 == 0:
                tmp = self.min // 60
                self.hour += tmp
                if self.hour >= 24:
                    self.hour -= 24
                self.min = 0
            else:
                tmp = self.min // 60
                self.hour += tmp
                if self.hour >= 24:
                    self.hour -= 24
                self.min -= tmp*60
        min = self.min
        hour = self.hour
        return(hour, min)


hour, min = map(int, input().split())
time = int(input())
N = oven(hour, min, time)
N.sum()
hour, min = N.result()
print(hour, min)