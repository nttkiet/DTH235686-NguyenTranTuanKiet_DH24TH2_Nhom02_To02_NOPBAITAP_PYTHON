# Câu 9: Viết chương trình tính căn bậc 2 lồng nhau S(n)

from math import sqrt

n = int(input("Nhập n: "))
S = 0
for i in range(n):
    S = sqrt(2 + S)
print("Giá trị S(", n, ") =", round(S, 4))