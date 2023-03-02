num1, num2 = input().split()
num1 = list(num1[-1::-1])
num2 = list(num2[-1::-1])
num1 = ''.join(num1)
num2 = ''.join(num2)

if int(num1)>int(num2):
    print(num1)
else:
    print(num2)