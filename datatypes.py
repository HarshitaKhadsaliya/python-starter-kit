#Take a string Input and print each character on a new line.
text="HEllo"
for char in text:
    print(char)

#count the number of space in a given string
text="Hello world,how are you "
space_count=text.count(' ')
print(f"number of space:{space_count}")   
    
#reverse a string without using slicing([::-1])
text="python"
reversed_text="".join(reversed(text))
print(reversed_text)    


#create a list of 5 numbers and print the sum of all elements
num=[10,20,30,40,50]
print(sum(num))

#Take a list of numbers and print only the positive number.
num=[-10,0,50,-20,30,100]
for n in num:
    if n > 0:
        print(n)


#Take a two string and concatenate them  with a space in between.
str1="HEllo"
str2="Surat"
result=str1+ " "+str2
print(result)

#Print the first and last character of given string.
text="python"
print(text[0],text[-1])

#Create a list of 10 integer and the maximum and minimum values.
num=[45,5,10,30,56,85,45,98,56,75]
maxnum=max[num]
minnum=min[num]
print(f"list:{num}")
print(f"Maximum Value: {maxnum}")
print(f"Minimum Value: {minnum}")