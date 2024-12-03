tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2)

def product_of_tup1():
    product1 = 1
    for num in tup1:
        product1 = product1 * num
    return product1

def product_of_tup2():
    product2 = 1
    for num in tup2:
        product2 = product2 * num
    return product2

product1 = product_of_tup1()
product2 = product_of_tup2()

total = product1 * product2

print("Product of numbers in tup1:", product1)
print("Product of numbers in tup2:", product2)
print("Total product of numbers in both tuples:", total)