# Read input
n = int(input())  # number of events
events = list(map(int, input().split()))  # list of events

# Initialize the number of available officers and untreated crimes
available_officers = 0
untreated_crimes = 0

# Process each event
for event in events:
    if event == -1:
        # A crime occurred
        if available_officers > 0:
            available_officers -= 1  # Assign one officer to the crime
        else:
            untreated_crimes += 1  # No officer available, crime goes untreated
    else:
        # Recruited officers
        available_officers += event

# Output the number of untreated crimes
print(untreated_crimes)
