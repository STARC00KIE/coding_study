from math import gcd # 내장 라이브러리

def solution(numer1, denom1, numer2, denom2):
    """
    a/b + c/d
    (a*d + b*c)/
    """
    num3 = denom1 * numer2 + denom2 * numer1
    denom3 = denom1 * denom2
    frac_gcd = gcd(num3, denom3)
    return [num3//frac_gcd, denom3//frac_gcd]

from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):
    frac3 = Fraction(numer1, denom1) + Fraction(numer2, denom2)
    return [frac3.numerator, frac3.denominator]