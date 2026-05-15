    #Take a string and return the longest word in the string
"""text="the quick brown fox jump over the lazy dog"
longer=max(text.split(),key=len)
print(longer)"""

#implement a basic calculator that take a string like "5 + 3" and return result
"""exprestion="5+3"
parts=exprestion.split()
num1=float(parts[0])
operator=parts[1]
num2=float(parts[2])
if operator=="+":
    result=num1+num2
elif operator=="-":
    result=num1-num2
elif operator=="*":
    result=num1*num2
elif operator=="/":
    result=num1/num2 if num2 !=0 else "error:Division by zero"
else:
    result="Error:Invalid operator"
    print(result)"""

#flatten a nested list(list containing sublists of arbitrart depth)into a single list 
"""def flatten(nested):
    result=[]
    for item in nested:
        if isinstance(item,list):
            result.extend(flatten(item))
        else:
            result.append(item)
            return result
        list=[1,[2,[3,4],5],[7,8]]
        print(flatten(list))"""

#take a list of strings,print all strings with length greater than3
str=["Hi","Hello","Sql","AI","Python","MI","QA","Test"]

"""for s in str:
    if len(s)>3:
        print(s)"""

#given a list of numbers,generate a dictionsry with numbers as keys and their factorial as values
"""numbers =[3,4,5,6]
factorial_dict={} 
for n in numbers:
    fact=1
    for i in range(1,n+1):
        fact*=i
        factorial_dict[n]=fact
        print(factorial_dict)"""

#implement of functions that check if a string is a palindrome (ignoreing space and case)
"""text="A man a plan a canal panama"
clean_text=text.replace(" "," ").lower()
is_palindrome=clean_text==clean_text[::-1]
print(f"Is '{text}'a palindrome? {is_palindrome}")"""

#given a list of strings ,create a new list containing only strings that are anagrams of the first string
"""str=["cinema", "iceman", "dog", "nameic", "cat", "manice"]
target=str[0]
target_sorted=sorted(target.lower())
anagrams=[word for word in str[1:] if sorted(word.lower())==target_sorted]
print(f"Target string:{target}")
print(f"Anagrams found:{anagrams}")"""

#print a pattern of numbers in pyramid shape for n rows
"""n=5
for i in range(1,n + 1):
    for j in range(1,i + 1):
        print(j, end=" ")
        print()"""


#take a sentence and return a dictionary where keys are words and values are the length of each word
"""sentence="python is great for data analysis"
word_length={word:len(word)for word in sentence.split()}
print(word_length)"""

#simulate a sentence and return a dictionary where keys are words and values are the length of each word
"""str="QA testing ensure software quality"
word_length={word:len(word)for word in str.split()}
print(word_length)"""


#given a list of numbers,generate all possible pairs(a,b)where a<b and sum of pair is even
number=[1,2,3,4,5]
pairs=[(number[i], number[j])

    for i in range(len(number)) 
    for j in range(i+1, len(number))
    if(number[i] + number[j] %2==0)]
print(pairs)