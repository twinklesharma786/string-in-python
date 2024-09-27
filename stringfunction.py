'''
# string lib
 # slicing
# with slicing we can access substring .it can get optimal start and stop indices.

'''
string='hello word'
print(string[3:8])
'''
# strip()
'''
string='banana'
string.strip()
print("all the fruit",string,"is my favourites")
'''
#istrip()
'''
string="banana   "
x=string.lstrip()
print("all the fruit",x,"is my favourites")
'''
#rstrip()
'''
string="  banana "
x=string.rstrip()
print("all the fruit",x,"is my favourites")
'''
#strip with character
'''
string= ",,,,,rrttgg.....banana....rrr"

x = string.strip(",.grt")

print(x)
'''
# removeprefix()
'''
string = 'GeeksforGeeks'
x=string.removeprefix("Geeksfor")
print(x)
'''
#removesuffix()
'''
string = 'GeeksforGeeks'
x=string.removesuffix("Geeks")
print(x)
'''
#replace()
'''
string = "I like bananas"

x = string.replace("bananas", "apples")

print(x)
'''
#re.split()
#Split the string at every white-space character:
'''
import re
string= "The rain in Spain"
string2=re.split("\s", string)
print(string2)
'''
#re.sub()
'''
import re
#Replace all white-space characters with the digit "9":

string= "The rain in Spain"
x = re.sub("\s", "9", string)
print(x)
y= re.sub("\s", "9", string ,2)
print(y)
'''
#.rsplit()
'''
txt = "apple, banana, cherry"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)

print(x)

# note that the result has only 2 elements "apple, banana" is the first element, and "cherry" is the last.
'''
#.join()
'''
list_of_strings =["string","method","in","tuple"]
s=" ".join(list_of_strings)
print(s)
'''
#.upper()
'''
string=" python is awesome!"
x=string.upper()
print(x
'''
#.lower()
'''
string=" python is awesome!"
x=string.lower()
print(x)
'''
#.capitalize()
'''
string = "hello, and welcome to my world."
x = string.capitalize()
print (x)
'''
#.islower()
'''
string = "hello, and welcome to my world."
x = string.islower()
print (x)
string1 = "HELLO WORLD."
y= string1.islower()
print (y)
'''
#.isupper()
'''
string = "hello, and welcome to my world."
x = string.isupper()
print (x)
string1 = "HELLO WORLD."
y= string1.isupper()
print (y)
'''
#isapha()
#Check if all the characters in the text is alphabetic:

'''
txt = "CompanyX"
x = txt.isalpha()
print(x)

string = "Company12"
y = string.isalpha()
print(y)
'''
#isnumeric()
'''
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
c = "10km2"
d = "-1"
e = "1.5"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())
'''
#isalnum()
'''
string = "Company12"
y = string.isalnum()
print(y)
'''
#count()
#Return the number of times the value "apple" appears in the string:
'''
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
'''
#.find()
#Where in the text is the word "welcome"?:
'''
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
'''
#.rfind()
#Where in the text is the last occurrence of the string "casa"?:
'''
txt = "Hello, welcome to my world."
x = txt.rfind("welcome")
print(x)
'''
#startswith()
#Check if the string starts with "Hello":
'''
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)
'''
#endswith()
#Check if the string ends with a punctuation sign (.):
'''
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
'''
#partition()
# Return a tuple where the string is parted into three parts:
'''
txt ="could i have a banana please"
x=txt.partition("banana")
print(x)
'''
#center()
#Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:
'''
txt = "banana"
x = txt.center(20)
y=txt.center(20,"0")
print(x)
'''
#ljust()
#Return a 20 characters long, left justified version of the word "banana":
'''
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")
'''
#rjust()
#Return a 20 characters long, right justified version of the word "banana":
'''
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")
'''
#f-string()
'''
num=1
language="python"
print(f"{language}is the number{num}")
'''
#swapcase()
#Make the lower case letters upper case and the upper case letters lower case:
'''
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)
'''
#zfill()
#Fill the strings with zeros until they are 10 characters long:
'''
a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))
'''
