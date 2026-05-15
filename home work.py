# take two numbers stsrts and end,print all [prime number in that range in python code
"""start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num, end=" ")"""


#print pattern each row i continue the number i repeted i time?

"""n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end="")
    print() """


#Take a number and calculate the sum of the factorials of the digits.
"""import math

num_str = input("Enter a number: ")
total_sum = 0
print("\nStep-by-step breakdown:")
for digit in num_str:
    d = int(digit)
    fact = math.factorial(d)
    total_sum += fact
    print(f"Factorial of {d} is {fact}")

print(f"\nFinal sum of factorials: {total_sum}")"""

#The computer choose or random number between 1 and 50 user a keeps guessing until correct given hint if the guess is higher or lower.
"""import random

secret_number = random.randint(1, 50)
attempts = 0

print("I'm thinking of a number between 1 and 50.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You found the number {secret_number} in {attempts} attempts.")
        break"""


#Take an integer and count how many digits are even and how many are odd?

"""num_str = input("Enter an integer: ")

even_count = 0
odd_count = 0

for digit in num_str:
    if digit.isdigit():
        n = int(digit)
        if n % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

print(f"\nResults for the number: {num_str}")
print(f"Even digits: {even_count}")
print(f"Odd digits: {odd_count}")"""


#Take a string and a character and count occurrences of that character without using built-in function.
"""text = input("Enter a string: ")
char_to_find = input("Enter the character to count: ")

count = 0

for char in text:
    if char == char_to_find:
        count += 1

print(f"The character '{char_to_find}' appears {count} times in the string.")"""


#Take n number as Input and print the multiplication table for each number.

"""n = float(input("How many numbers do you want to enter? "))

numbers = []

for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

for num in numbers:
    print(f"\n- Multiplication Table for {num} ---")
    for i in range(1, 11):
        result = num * i
        print(f"{num} x {i} = {result}")"""

#Take a number and some all digits that are prime. 2,3,5,7

"""num_str = input("Enter a number: ")

prime_sum = 0
found_primes = []

for digit in num_str:
    if digit.isdigit():
        d = int(digit)
        
        if d in [2, 3, 5, 7]:
            prime_sum += d
            found_primes.append(str(d))

if found_primes:
    print(f"Prime digits found: {', '.join(found_primes)}")
    print(f"Sum of prime digits: {prime_sum}")
else:
    print("No prime digits (2, 3, 5, 7) were found in the number.")"""


#printer Diamond star pattern for a given odd number n
"""n = int(input("Enter an odd number for diamond size: "))

if n % 2 == 0:
    print("Please enter an ODD number for a perfect diamond.")
else:
    for i in range(1, (n // 2) + 2):
        print(" " * (n // 2 - i + 1), end="")
        print("*" * (2 * i - 1))

    for i in range(n // 2, 0, -1):
        print(" " * (n // 2 - i + 1), end="")
        print("*" * (2 * i - 1))"""

#print a rectangle of size M*N with strats,but replace the diagonal with number 1 to min(M,N)
M = int(input("Enter number of rows (M): "))
N = int(input("Enter number of columns (N): "))

print(f"\nRectangle {M}x{N}:")

for i in range(M):
    for j in range(N):
        if i == j:
            print(i + 1, end=" ")
        else:
            print("*", end=" ")
    
    print()