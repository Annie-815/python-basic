#if statements in python
is_hot = False
is_cold = False
if is_hot:
    print("it is a hot day")
    print("drink plenty of water")
elif is_cold:
    print("it is a cold day")
    print("wear warm clothes")
else:
    print("its a lovely day")
print("Enjoy your day")
#calculate down payment of a house based on a condition
has_good_credit = False
price = 1000000
if has_good_credit:
    down_payment = 10/100 * price
    print(down_payment)
else:
    down_payment = 20/100 * price
    print(down_payment)
