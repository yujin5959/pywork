cart = {}  # 빈 딕셔너리 생성

# 구입
while True:
    name = input("상품명? ")
    if not name:
        break
    quantity = int(input("수량은? "))
    cart[name] = quantity
    print(f"장바구니에{name} {quantity}개가 담겼습니다.")

print(f"장바구니 보기: {cart}")

# 검색
search = input("장바구니에서 확인하고자하는 상품은? ")
if search in cart:
    print(f"{search}은(는) {cart[search]}개 담겨 있습니다.")
else:
    print(f"{search}은(는) 장바구니에 없습니다.")
