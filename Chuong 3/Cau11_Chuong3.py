# Câu 11: Kiểm tra số nguyên tố

while True:
    n = int(input("Nhập 1 số nguyên dương: "))
    if n < 2:
        print(n, "Không là số nguyên tố")
    else:
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            print(n, "Là số nguyên tố")
        else:
            print(n, "Không là số nguyên tố")
    hoi = input("Tiếp không Thím? (c/k): ")
    if hoi == "k":
        break
print("BYE!")