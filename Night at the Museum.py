def min_rotations_to_print_name(name):
    current_position = 0
    total_rotations = 0
    
    for char in name:
        target_position = ord(char) - ord('a')
        
        # Calculate clockwise and counterclockwise distances
        clockwise_distance = abs(target_position - current_position)
        counterclockwise_distance = 26 - clockwise_distance
        
        # Add the minimum of the two distances to the total
        total_rotations += min(clockwise_distance, counterclockwise_distance)
        
        # Update the current position to the target
        current_position = target_position
    
    return total_rotations

name = input().strip()

print(min_rotations_to_print_name(name))
