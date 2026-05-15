cofee=150
sandwitch=250
pastry=120

coffee_qty=int(input("enter a number of coffee"))
sandwitch_qty=int(input("enter a number of sandwitdh"))
pastry_qty=int(input("enter a number of sandwitch"))

total_bill=(coffee*coffee_qty)+(sandwitch*sandwitch_qty)+(pastry*pastry_qty)
print("Total amount to pay",total_bill)





celsius=float(input("enter temptarure in celsius"))
fahrenhiet=(celsius*9/5)+32
kelvin=celsius+273.15

print("fahrenhiet:",fahrenhiet)
print("kelvin:",kelvin)




num=float(input("enter a number"))

if num%2==0:
    print("even")
    else
    print("odd")




total_class=int(input("total class"))
attended=int(input("classes attended"))

percntage=(attended/total_class)*100
print(f"attended:{percentage}%")
if percntage>=75
print("eligible for exam")
else
print("not eligble for exam")



str=input("enter a sentence")
words=str.split()
reversed_str=" ".join(word[::-1])
print(reversed_str)


p=float(input("enter a principal"))
r=float(input("enter a rate"))
t=float(input("enter a time"))

interest=(P*r*t)/100
print("simple interest",interest)



a=float(input("enter a number"))
b=float(input("enter a number"))
c=float(input("enter a number"))

if a>=b and a>=c
print("larget is ",a)
elif b>=c and b>=a
print("larget is",b)
else:
    print("larget is",c)




year=int(input("enter a year:"))
if(year%4==0 and year % 100!=0)or(year %400==0):
    print("Leap year")
    else
    print("Not leep year")





amount=float(input("enter a amount"))
if amount>5000:
    discount=amount*0.10
    print("total after 10% discount:",amount-discount)
    else:
        print("No discount",amount)





marks=float(input("enter a marks"))

if marks >=90:
    print("Grade A:")
   elif marks>=80:
    print("Grade B:")
    elif marks>=70
    print("Grade C:")
    elif marks>=60
    print("Grade D:")
    else
    print("Fail")