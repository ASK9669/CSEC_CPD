def mn():
    s = input().strip()
    t = input().strip()
    x= 0 
    for instruction in t:
        if s[x] == instruction:
            x+= 1
            if x== len(s):
                break
    print(x + 1)
mn()
