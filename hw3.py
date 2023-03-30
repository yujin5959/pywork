def get_fixed_price(d_rate, d_price):
    fixed_price = d_price / (1 - d_rate/100)
    return fixed_price

d_rate = int(input("할인율은? "))
A_d_price = int(input("A 상품의 할인 가격은? "))
B_d_price = int(input("B 상품의 할인 가격은? "))

A_fixed_price = get_fixed_price(d_rate, A_d_price)
B_fixed_price = get_fixed_price(d_rate, B_d_price)

print("A 상품의 정가는", int(A_fixed_price), "원")
print("B 상품의 정가는", int(B_fixed_price), "원")
