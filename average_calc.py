#!/usr/bin/env python3
# Created by: Gustav I
# Created on: April 19, 2025
# This program calculates the average of all marks using arrays


# random library
import random

# Constants
MAX_ARRAY_SIZE = 10
MIN_NUM = 1
MAX_NUM = 100


# main function
def main():
    list_of_int = []

    print("=== Average Calculator ===")
    print("Generating random numbers...\n")

    # Generate and add 10 random numbers
    for _ in range(MAX_ARRAY_SIZE):
        num = random.randint(MIN_NUM, MAX_NUM)
        list_of_int.append(num)
        print(f"{num} added to the list!")

    print("\nAll numbers added!")
    print("List of numbers:", list_of_int)

    # Calculate the total using a loop
    total = 0
    for num in list_of_int:
        total += num

    # Calculate the average
    average = total / MAX_ARRAY_SIZE
    print(f"\nAverage: {average}")


# Call the main function
if __name__ == "__main__":
    main()
