#Infinite Prime Generator

def prime_generator():
    num = 2
    while True:
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            yield num
        num += 1

gen = prime_generator()
primes = [next(gen) for _ in range(10)]
print(primes)


# Invert Dictionary Handling Duplicates
data = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
# Use setdefault to handle duplicates by storing values in a list
inverted = {}
for k, v in data.items():
    inverted.setdefault(v, []).append(k)
print(inverted)

#Student with Highest Total Marks
student = [
    {"name": "Alice", "marks": [80, 90, 85]},
    {"name": "Bob", "marks": [70, 75, 80]},
    {"name": "Charlie", "marks": [95, 92, 98]}
]

def student(student_list):
    return max(student_list, key=lambda s: sum(s['marks']))

best = student(student)
print(f"Top Student: {best['name']} with {sum(best['marks'])} marks")

#Normalize Numbers range is (0 to 10)
num=[10,20,30,40 ,50]
min,max=min(num),max(num)
normalized=list(map(lambda x:(x-min)/(max-min),num))
print(normalized)

#Sort Tuple of Tuples by Score
scores=(("alice",88),("Bob",95),("HDFC",75))
sorted=tuple(sorted(scores,key=lambda x:x[1]))
print(sorted)

#Palindromic Numbers Generator (1-1000)
def palindrome_gen():
    for n in range (1,1001):
        if str(n)==str(n)[::-1]:
            yield n
            print(list(palindrome_gen))


#Higher-Order Function Application

    return [func(x) for x in num_list]

numbers = [1, 2, 3, 4]
result = apply_func(lambda x: x * 10, numbers)
print(result)

#Set Operations for Unique/Common Words

set_a={"apple","banana","orange"}
set_b={"banana","chary","Mango"}
unique=set_a-set_b
common=set_a & set_b
unique1=set_b-set_a
print(f"Unique to A: {unique}, Common: {common}, Unique to B: {unique1}")


# Recursive Function to Flatten Nested Dictionary
def flatten_dict(d,path=()):
    item={}
    for k,v in d.item():
        new_path=path+(k,)
        if isinstance(v,dict):
            item.update(flatten_dict(v,new_path))
        else:
            item[new_path]=v
            return item
        nested={"a":1,"b":{"c":2,"d":{"e":3}}}
        print(flatten_dict(nested))


# Factorial via Generator and reduce()
from functools import reduce
def factorial_steps(n):
    for i in range(1,n+1):
        yield i
        n=5
        result=reduce(lambda x,y:x*y,factorial_steps(n))
        print(f"Factorial of{n} is {result}")