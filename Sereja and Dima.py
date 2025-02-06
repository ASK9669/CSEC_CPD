
n = int(input())  # number of cards
cards = list(map(int, input().split()))  # list of cards

#  scores
sereja = 0
dima = 0

# Initialize pointers for the left and right ends of the cards
left = 0
right = n - 1

turn = True
while left <= right:
    # Compare the leftmost and rightmost card
    if cards[left] > cards[right]:
        chosen_card = cards[left]
        left += 1
    else:
        chosen_card = cards[right]
        right -= 1
    
    if turn:
        sereja += chosen_card  # Sereja's turn
    else:
        dima += chosen_card  # Dima's turn
    

    turn = not turn

# Output the result
print(sereja , dima)
