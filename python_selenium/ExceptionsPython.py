#Two ways to explicitly raise an error when a condition is not met

#raise Exception, assert

ItemsInCart = 0
#2 items will be added to cart

if ItemsInCart != 2:
    # raise Exception("Products Cart count not matching")
    #(assert)
    pass

assert(ItemsInCart == 0)


#try, catch
try:
    with open('wrong_name.txt', 'r') as reader:
        reader.read()

except:
    print("Some how i reached this block because there is failure in try block")


try:
    with open('wrong_name.txt', 'r') as reader:
        reader.read()

except Exception as e: #Python error message
    print(e)

# Reason for using finally
# If failures keep occurring before reaching finally,
# the junk data created for automation may not be properly cleaned up.
# Therefore, all cookies must be deleted.
finally:
    print("cleaning up resources")
