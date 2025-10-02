# Câu 7: Tính và xuất độ dài đoạn AB

from math import sqrt

print("Nhập tọa độ điểm A:")
xA = float(input("xA = "))
yA = float(input("yA = "))

print("Nhập tọa độ điểm B:")
xB = float(input("xB = "))
yB = float(input("yB = "))

dAB = sqrt((xB - xA) ** 2 + (yB - yA) ** 2)
print("Độ dài đoạn AB =", round(dAB, 2))