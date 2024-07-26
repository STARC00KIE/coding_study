def solution(num_list):
    prod = 1
    sumprod = sum(num_list)**2
    for i in num_list:
        prod *= i
    
    if prod < sumprod:
        print(f'{prod}  {sumprod}')
        return 1
    else:
        return 0