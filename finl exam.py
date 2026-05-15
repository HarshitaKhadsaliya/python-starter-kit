#check whether a given string is a palindrome
a=input("enter a sting")
a=a.replace(" "," ")

if a==a[::-1]:
    print("it is palindrome")
else: 
    print("it is palindrome")
#gcd using loops and if else statement 
a=float(input("enter a number"))
b=float(input("enter a number"))

  num1, num2 = a,b

 while a !=b:
   if a>b:
      a=a-b
   else:
      b=b-a
print("enter the gcd number:{a}")

#take a string and count the member of words 
a=input("enter a name")
word=a.split()
b =len(a)
print("enter string length:{b}")

#print the following pattern n=5
n=5
 
 for i in range (1,n+1):
    for j in range(i):
       print("*", end=" ")
            print()


#n number as input and print the sum of their square
n = float(input("How many numbers do you want to enter? "))
sum=0
for i in range(1, n + 1):
    num = float(input("Enter number {i}: "))
    square = num ** 2
    sum += square

print(f"The sum of the squares is: {sum}")

#Counter frequency is character in a string.
text = input("Enter a string: ")
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1  # If char exists, increment the count
    else:
        frequency[char] = 1   # If char is new, start at 1

# Printing the result
text = input("Enter a string: ")
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1  # If char exists, increment the count
    else:
        frequency[char] = 1   # If char is new, start at 1

# Printing the result
text = input("Enter a string: ")
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1  # If char exists, increment the count
    else:
        frequency[char] = 1   # If char is new, start at 1

# Printing the result
text = input("Enter a string: ")
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1  # If char exists, increment the count
    else:
        frequency[char] = 1   # If char is new, start at 1

# Printing the result
print("Character frequencies:")
for char, count in frequency.items():
    print(f"'{char}': {count}")text = input("Enter a string: ")
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1  # If char exists, increment the count
    else:
        frequency[char] = 1   # If char is new, start at 1

# Counter frequency is character in a string.
a=input("enter a string")
frequency={}

for char in text:
    if char in frequency:
    frequency[char]+=1
else:
frequency[char]=1

print("Character frequencies:")
for char, count in frequency.items():
    print(f"'{char}': {count}")

#print all odd numbers from 50 doew to 1 using a loop
print("Odd numbers from 50 down to 1:")

# Start at 49, stop at 1 (using 0 because the end is exclusive), step by -2
print("Odd numbers from 50 down to 1:")
for i in range(49, 0, -2):
    print(i, end=" ") 

#basic calculator that take two numbers and operator and performs operations
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operator == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operator == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operator == '/':
    # Check for division by zero
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error! Division by zero is not allowed.")

else:
    print("Invalid operator! Please use +, -, *, or /.")    

