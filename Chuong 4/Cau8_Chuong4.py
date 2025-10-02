# Câu 8: Viết chương trình tính log_a(x) với x > 0, a > 0, a != 1

from math import log

a = float(input("Nhập cơ số a (>0, !=1): "))
x = float(input("Nhập số x (>0): "))

if a > 0 and a != 1 and x > 0:
    kq = log(x) / log(a)
    print(f"log_{a}({x}) =", round(kq, 4))
else:
    print("Giá trị a hoặc x không hợp lệ!")