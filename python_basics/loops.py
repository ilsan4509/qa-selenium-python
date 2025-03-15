# Loops #

# if else #
greeting = "Good Morning"
#Indentation is important in Python
print("1. if else - greeting")
if greeting == "Morning":
    print("Condition Matches")
    print("second line")
else:
    print("condition do not match")

print("if else condition code is completed")

print("2. if else - start")
a = 3
if a > 2:
    print("Condition Matches")
    print("second line")
else:
    print("condition do not match")


print("if else condition code is completed")

# for loop #
print("3. for - obj")
obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i*2)

#sum of First Natural numbers 1+2+3+4+5 = 15
#range(i,j) -> i to j-1
print("4. for - summation")
summation = 0
#for(i=0; i<5; i+1) - Java
for j in range(1, 6):
    summation = summation + j
    print(summation)
print("Final summation =", summation)

print("5. for - k")
for k in range(1, 10, 2):
    print(k)
print("Final k =", k)

print("5. for - m")
for m in range(10):
    print(m)
print("Final m =", m)