# Task 1: Odd numbers below input
user_input = int(input("Enter a number: "))

# List of odd numbers less than input
odd_numbers = [i for i in range(user_input) if i % 2 != 0]
print("Odd numbers less than input:", odd_numbers)

# Another list of odd numbers (this might be a typo in the image, but for practice we repeat)
odd_numbers_copy = [num for num in odd_numbers]
print("Copied list of odd numbers:", odd_numbers_copy)

# Task 2: Capitalizing first letter of each fruit
fruits = ["apple", "banana", "cherry", "mango"]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("Capitalized fruits list:", capitalized_fruits)
