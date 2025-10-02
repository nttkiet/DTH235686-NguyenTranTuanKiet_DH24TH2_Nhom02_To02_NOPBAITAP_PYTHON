#Câu 18: Vẽ các hình dưới đây
# Hình 1: Hình vuông n x n
n = int(input("Nhập chiều cao n: "))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

print()  # Cách dòng

# Hình 2: Đường chéo từ trái sang phải
for i in range(n):
    for j in range(n):
        if i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()