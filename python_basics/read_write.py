file = open('test.txt')
#Read all the contents of file
# print(file.read())

#read n number of characters by passing parameter
# print(file.read(2))

#read one single line at a time readLine()
# print(file.readline())
# print(file.readline())

#print line by line using readLine method
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

#values = [1, 2, 3, cat, dog, a, b, c]
# for line in file.readlines():
#     print(line)

file.close() #Closing the file is important to free up system resources

# read the file and store all the lines in list
# reverse the list
# write the list back to the file

#'r' read, 'w' write
with open('test.txt', 'r') as reader: #[1, 2, 3, cat, dog, a, b, c]
    content = reader.readlines()
    reversed(content) #[c, b, a, dog, cat, 3, 2, 1]
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)