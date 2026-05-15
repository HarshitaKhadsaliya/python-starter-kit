
#1. Name Shortener App
full_name=input("enter full name")
initials =[name[0].upper()for name in full_name.split()]
print(".".join(initials)+".")


#2. Restaurant Menu System
menu={"Pizza":200,"Burger":100,"coke":50}
print("menu:",menu)
order=input("what do you like order?")
if order in menu:
    print(f"Total cost:{menu[order]}")
else:
    print("Item not found")



#3. Email Validator
email=input("enter mail:")
if "@" in email and email.endwith(".com"):
 print("valid") 
else:
 print("Not valid")





#4. Unique Words Extractor
str=input("enter a Shentence:").lower()
Words=set(str.split())
print("Words",words)



#5. Class Marks Tracker
marks={}
for i in range(5):
    name=input("enter a name")
    score=float(input(f"enter marks for{name}:"))
    marks[name]=score

    topper=max(marks,key=marks.get)
    print(f"topper:{topper}with {marks[topper]}marks")



#6. Bus Seat Allocation
seats=list(range(1,11))
print("available sets:",seats)
choice=int(input("enter a number to book(1-10):"))
seats[choice-1]="Booked"
print("updated seats:",setas)


#7. Vowel Counter
def vowel(text):
    vowels="aeiouAEIOU"
    count=sum(1 for  char in text if char in vowels)
    return count

    msg=input("enter a string")
    print("vowel count ",count_vowels(msg))



#8. Fruit Basket Organizer
fruits=("apple","banana","apple","cherry","apple")
pick=input("enter fruit name to count").lower()
print(f"the fruit{pick}appears{fruits.count(pick)}times")



#9. Password Strength Checker
pwd=input("enter a password")
has_upper=any(c.isupper() for c in pwd)
has_lower=any(c.islower() for c in pwd)
has_digit=any(c.isdigit() for c in pwd)
has_special=any(c.isspecial() for c in pwd)

if all([has_upper,has_lower,has_digit,has_special]):
    print("Strong password")
else:
    print("weak password")




#10. Student Subject Selection
math_student={"Alice","Bob","Charlie"}
science_students={"Charlie","David","Alice"}
print("both subject(Intersection):",math_student & science_students)
print("only math(Diffrence):",math_studdents-science_students)
