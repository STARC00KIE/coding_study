def solution(price):
    if price >= 500000:
        price = price * 0.8
    elif price >= 300000:
        price = price * 0.9
    elif price >= 100000:
        price = price * 0.95
    else:
        pass
    return int(price)