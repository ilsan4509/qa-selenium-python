# Python String Data Type #
e = "string in a double quote"
f = 'string in a single quote'
print(e)
print(f)

# using ',' to concatenate the two or several strings
print(e, "concatenated with", f)
# using '+' to concate the two or several strings
print(e + " concated with " + f)


# Python List Data Type #
values = [1,2, "paper", 4, 5]

#List is data type that allows multiple values and can be different data types

print(values[0]) #1
print(values[3]) #4
print(values[-1]) #5
print(values[1:-1]) #[2, 'paper', 4]

values.insert(3, "rock") #[1, 2, 'paper', 'stone', 4, 5]
print(values)

values.append("end") #[1, 2, 'paper', 'stone', 4, 5, 'end']
print(values)
