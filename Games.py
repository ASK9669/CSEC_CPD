n=int(input())
team=[]
for i in range(n):
    hi,ai=map(int,input().split())
    team.append((hi,ai))
count=0
for i in range(n):
    for j in range(n):
        if i!=j:
            if team[i][0] == team[j][1]:
                count += 1
print(count)
