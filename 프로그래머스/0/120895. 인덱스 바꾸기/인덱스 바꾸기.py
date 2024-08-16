def solution(my_string, num1, num2):
    my_string = list(my_string)
    snum1 = my_string[num1]
    snum2 = my_string[num2]
    
    my_string[num1] = snum2
    my_string[num2] = snum1

    return "".join(my_string)