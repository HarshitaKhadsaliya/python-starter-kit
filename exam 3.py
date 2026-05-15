
#1. Online Store Inventory1. Online Store Inventory
inventory={"Apple":[10,50],"Bread":[5,30]}
item=input("enter item to buy:")
qty=int(input("enter quantity"))

if item in inventory: 
    if inventory[item][0]>=qty:
      inventory[item[0]] -= qty

    total_bill = qty * inventory[item][1]
    print(f"Bill: ₹{total_bill}")
    print(f"Remaining {item} stock: {inventory[item][0]}")   
    else:
    print(f"Requirement exceeds stock! Only {inventory[item][0]} left.")
else:
    print("Item not found in inventory.")








#2. Movie Ratings Aggregator
Movie = {"Inception":[5,4,5],"Interstellar":[4,3,5]}

def avg_ratings(data):
    for movie,rating in data.items():
        avg=sum(rating)/len(rating)
        print(f"{movie}:{avg:2f}")
avg_ratings(Movie)

#3. Electricity Bill Generator
def cal_bill(units):
    if units<=100:
        bill=units*5
    elif units<=200:
        bill=(100*5)+(100*8)+((units-200)*10)
        return bill
    usage=150 
    print(f"total bill for (usage)unit is:₹{calculate_bill(usage)}")   

    

#4  Email ID Formatter
name=["johna Doe","jane smith","Alice cooper"]

format_email=lambda name:f"{name.split()[0].lower()}.{name.split()[1].lower()}@college.com"
email_ids=list(map(format_email,name))
for email in email_ids:
    print(email)


#6. Duplicate Remover using Sets

items=["apple","banana","apple","orange","banana","grape"]
unique_item=set(items)
sorted_items=sorted(unique_item)
print("original:",items)
print("cleaned & Sorted:",sorted_items)



#6 Fibonacci Generator App
def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,a=b,a+b
        fib=fibonacci()
        print("first 10 fibonacci terms:")
        for _ in range(10):
            print(next(fib))



#7 Simple Student Report Card System
students = {
    "Alice": {"Math": 85, "Science": 90, "English": 88, "Photo": "alice_pic.jpg"},
    "Bob": {"Math": 70, "Science": 65, "English": 72, "Photo": "bob_pic.jpg"}
}

def generate_report(data):
    print("--- STUDENT REPORT CARD SYSTEM ---")
    
    for name, info in data.items():
        # Calculate Total and Average
        grades = [info["Math"], info["Science"], info["English"]]
        total = sum(grades)
        avg = total / len(grades)
        
        # Determine Pass/Fail
        status = "PASS" if avg >= 50 else "FAIL"
        
        # Display the Report
        print(f"\nStudent: {name}")
        print(f"Photo File: {info['Photo']}") # Image reference
        print(f"Average Score: {avg:.2f}")
        print(f"Status: {status}")
        print("-" * 30)

generate_report(students)



#8 Employee Salary Processor
from functools import reduce
employee=[
  {"name":"Raj","salary":50000},
  {"name":"Bob","salary":30000},
  {"name":"Charlie","salary":75000},
  {"name":"David","salary":20000}
]
threshold=40000
high_earners=list(filter(lambda x:x['salary']>threshold,employee))
salaries=[e['salary']for e in high_earners]
total_expense =reduce(lambda a,b:a+b,salaries)
print(f"High Earners:{high_earners}")
print(f"Total company Expense for high earners:${total_expense}")


#10 Crypto Price Tracker
crypto_price={"Bitcoin":65000,"Ethereum":35000,"Solana":150,"Dogecoin":0.15}
def crypto(prices):
    highest_name=max(prices,key=prices.get)
    return highest_name
top_crypto=get_highest_crypto(crypto_price)
print(f"The cryptocurrency with the highest price is:{top_crypto}")
print(f"price:${crypto_price[top_crypto]}")