# String #
str = "Hello. My name is Seonggon"
str1 = " Consulting firm"
str3 = "Seonggon"

print(str[1])
print(str[0:5])  # substring in python
print(str+str1)

print(str3 in str) # substring check
var = str.split(".")
print(var)
print(var[0]) #Hello
str4 = "  great  "
print(str4.strip())
print(str4.rstrip()) # delete right side