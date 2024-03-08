def min_steps_to_friend(x):
    # Each step can cover a distance of 5
    # Calculate the minimum number of steps needed
    min_steps = (x + 4) // 5
    return min_steps

# Example usage:
friend_house_position = int(input())
result = min_steps_to_friend(friend_house_position)
print(result)