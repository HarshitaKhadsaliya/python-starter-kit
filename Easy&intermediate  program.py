"""students={'A':85,'B':90,'C':75}
inverted={v:k for k,v in students.items()}
print(inverted)"""

"""table= {x:{ y: x * y for y in range(1,6)}for x in range(1,10)}
print(table)"""

#tuple of 5 fruits and print first and last fruit
fruits("Apple","Banana","Cherry","Date","Orange")
print("First:",fruits[0])
print("Last:",fruits[-1])

#set of 10 number and remove all duplicates
list=[1,2,2,3,3,3,4,5,7,6]
num=set(list)
print(num)

#dictionary of 3 student with their marks and print the marks
students={"Alice":85,"Bob":95, "HDFC":60}
print("Bob's marks",students["Bob"])


#write a function greet_user(name)that prints greeting for a given name
def greet_user(name):
    print(f"Hello,{name}!Hello you're having g great day")
    greet_user("Meet")

#list of 5 number and print their squares using a lambda function and map   
num=[1,2,3,4,5]
squares=list(map(lambda x: x**2,num))
print(squares)


#create a dictionary of names and age update the age of one person and print the dictionary
people={"john":25,"Ravi":40,"Mali":50}
people["Ravi"]=31
print(people)

#Generator for first 5 even numbers

"""def even_gen():
    for in range(0,10,2):
    yield i
for val in even_gen():
    print(val)"""

#Set of colors (Check for "blue")    

color={"red","green","blue","yellow","pink"}
if "blue" in color:
    print("Blue exites in the set!")

#Tuple count of a particular number
number=(1,2,3,2,4,2,5)
count=number.count(2)
print(f"the number 2 appears{count} times")

#For loop over fruit prices
fruit={"Apple":1.2,"Banana":0.5,"Cherry":4.0}
for fruit,price in fruit():
    print(f"the price of{fruit}is ${price}")


#Dictionary Comprehension (Cubes)series is number 1-10
dict={x: x**3 for x in range(1,11)}
print(dict)


#Variable-length Arguments and returns their sum
def sum(*args):
    return sum(args)
print(sum(10,20,30,40,50))


#Fibonacci Generator
def fibonacci(n):
    a,b=0,1
    for _ in range(n):
        yield a
        a,a=b,a+b
print(list(fibonacci(10)))

#filter() for Odd Numbers list if 1-20
number=list(range(1,21))
odds=list(filter(lambda x: x %2==0,number))
print(odds)

#reduce() to Multiply Numbers list 1-5
from functools import reduce

num=[1,2,3,4,5]
pro=reduce(lambda x,y:x*y,num)
print(pro)


#Prime Number Lambda with filter()list 1-20
prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
primes = list(filter(prime, range(1, 21)))
print(primes)

# Merge Dictionaries using Comprehension

dict1={"a":1,"b":2}
dict2={"c":3,"d":4}
merged={k:v for d in (dict1,dict2) for k,v in d.items()}
print(merged)

#Set Intersection set{5,6,7,8} set of number 1-10
set1=set(range(1,11))
set={5,6,7,8}
common=set1.intersection(set)
print(common)

#Nested Dictionary 
students={"Raj":{"Math":90,"Science":80},
            "Riya":{"Math":75,"Science":50},
            "zoya":{"Math":95,"Science":91}}
for name,marks in students.items():
    total=sum(marks.values())
    print(f"{name}'sTotal marks:{total}")

 # Area of Rectangle default 1 and width not provided

"""def calculate_area(length, width=1):
    return length * width

print(f"Area with width: {calculate_area(10, 5)}")
print(f"Area with default width: {calculate_area(10)}")"""


