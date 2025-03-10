# Data Type - String #
e = "string in a double quote"
f = 'string in a single quote'
print(e)
print(f)

# using ',' to concatenate the two or several strings
print(e, "concatenated with", f)
# using '+' to concate the two or several strings
print(e + " concated with " + f)


# Data Type - List #
#List is data type that allows multiple values and can be different data types
values = [1,2, "paper", 4, 5]

print(values[0]) #1
print(values[3]) #4
print(values[-1]) #5
print(values[1:-1]) #[2, 'paper', 4]

values.insert(3, "rock") #[1, 2, 'paper', 'stone', 4, 5]
print(values)

values.append("end") #[1, 2, 'paper', 'stone', 4, 5, 'end']
print(values)

values[2] = "PAPER" #[1, 2, 'PAPER', 'stone', 4, 5, 'end']
print(values)

del values[0] #[2, 'PAPER', 'stone', 4, 5, 'end']
print(values)


# Data Type - Tuple #
#Same as List Data type but immutable
val = (1, 2, "paper", 4.5)
print(val) #(1, 2, 'paper', 4.5)
print(val[1]) #2
# val[1] = "PAPER"  #Tuples don't support item assignment

# Data Type - Dictionary #
dic = {"a":2, 4:"bcd", "e":"Hello"}

print(dic[4]) #bcd
print(dic["e"]) #Hello

dict = {} #empty dictionary
dict["FistName"] = "Seonggon"
dict["LastName"] = "Kim"

print(dict)#{'FistName': 'Seonggon', 'LastName': 'Kim'}
print(dict["LastName"])#Kim
