import math

def aaa():
    Y, W = map(int, input().split())
    max_roll = max(Y, W)
    outcomes = 6 - max_roll + 1
    value = math.gcd(outcomes, 6)
    nu = outcomes // value
    de = 6 // value
    print(f"{nu}/{de}")
aaa()
