# Read the first line of input
a1, a2, a3, a4 = map(int, input().split())
s = input().strip()
totals = 0
# Iterate through each character in the string and add corresponding calories
for char in s:
    if char == '1':
        totals += a1
    elif char == '2':
        totals += a2
    elif char == '3':
        totals += a3
    elif char == '4':
        totals += a4

print(totals)
