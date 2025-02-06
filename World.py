# Read the input string
s = input().strip()

# Count uppercase and lowercase letters
U = sum(1 for c in s if c.isupper())
L = len(s) - U

# Compare the counts and transform the string
if U > L:
    print(s.upper())  
else:
    print(s.lower()) 
