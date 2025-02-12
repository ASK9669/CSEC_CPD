def minimum(k, r):
    for n in range(1, 11):  
        cost = n * k
        if cost % 10 == 0 or cost % 10 == r:
            return n
k, r = map(int, input().split())
print(minimum(k, r))
