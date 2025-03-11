#조건이 충족되지 않을 경우, 명시적으로 오류를 만들 수 있는 두가지 방법이 있다.
#raise Exception, assert

ItemsInCart = 0
#2 items will be added to cart

if ItemsInCart != 2:
    # raise Exception("Products Cart count not matching")
    #(assert)
    pass

assert(ItemsInCart == 2)

