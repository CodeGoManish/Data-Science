
print(" 1.postion of substring")
str = "MANGO"
print(str.find("N"))
print("2.REPLACE")
str = "Waking up early is good habit"
print(str.replace("good","bad"))
print("3.Substring separated  by the delimiters" )
str1 = input("choose  string character")
print(str1.split())
print("4 .convert line into title form ")
str = input("Write a line")
print(str.title())
print("5 lower /upper" )
str = input("Write a sentence")
print(str.upper())
print(str.lower())
print("6.PALINDROME")
str =  input("enter any word" )
str1 = str[::-1]
if(str==str1):
    print("palindrome")
else:
    print("not palindrome")


