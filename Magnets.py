#input magnets
n = int(input())
magnet1 = input().strip()

groups = 1  
for i in range(1, n):
    magnet2 = input().strip()
    
    if magnet2 != magnet1:
        groups += 1  
    magnet1 = magnet2 

print(groups)
