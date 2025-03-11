#(조건이 충족되지 않을 경우, 명시적으로 오류를 만들 수 있는 두가지 방법)
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
