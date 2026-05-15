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
    