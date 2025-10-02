# Câu 8: Nhập vào 2 giá trị a, b và phép toán '+', '-', '*', '/'. Xuất kết quả theo phép toán đã nhập.

a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
op = input("Nhập phép toán (+, -, *, /): ")

if op == '+':
    print("Kết quả:", a + b)
elif op == '-':
    print("Kết quả:", a - b)
elif op == '*':
    print("Kết quả:", a * b)
elif op == '/':
    if b != 0:
        print("Kết quả:", a / b)
    else:
        print("Lỗi: Không thể chia cho 0")
else:
    print("Phép toán không hợp lệ")