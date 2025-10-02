# Câu 19: Tính giá trị biểu thức S(x, n)
# S(x, n) = x + x^3/3! + x^5/5! + ... + x^(2n+1)/(2n+1)!

x = float(input("Nhập x: "))
n = int(input("Nhập n: "))
S = x
for i in range(1, n + 1):
    mu = 2 * i + 1
    tu = x ** mu
    mau = 1
    for j in range(1, mu + 1):
        mau *= j
    S += tu / mau
print("S({0},{1}) = {2}".format(x, n, S))