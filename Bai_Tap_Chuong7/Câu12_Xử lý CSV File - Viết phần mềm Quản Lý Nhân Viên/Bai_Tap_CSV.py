import csv
import random

file_path = "dulieu.csv"

# ====== HÀM TẠO FILE CSV NGẪU NHIÊN ======
def tao_file_csv():
    with open(file_path, mode="w", newline="") as f:
        writer = csv.writer(f)
        for _ in range(10):  # 10 dòng
            dong = [random.randint(1, 100) for _ in range(10)]  # 10 số ngẫu nhiên 1→100
            writer.writerow(dong)
    print("Đã tạo file CSV ngẫu nhiên thành công!")

# ====== HÀM ĐỌC FILE CSV VÀ TÍNH TỔNG ======
def doc_va_tinh_tong():
    try:
        with open(file_path, mode="r") as f:
            reader = csv.reader(f)
            print("\n--- DỮ LIỆU & TỔNG GIÁ TRỊ MỖI DÒNG ---")
            for i, row in enumerate(reader, start=1):
                so_nguyen = [int(x) for x in row]
                tong = sum(so_nguyen)
                print(f"Dòng {i}: {row}  => Tổng = {tong}")
    except FileNotFoundError:
        print("File chưa tồn tại. Vui lòng tạo file trước!")

# ====== MENU CHƯƠNG TRÌNH ======
def menu():
    while True:
        print("\n===== XỬ LÝ FILE CSV =====")
        print("1. Tạo file CSV ngẫu nhiên")
        print("2. Đọc file & tính tổng mỗi dòng")
        print("0. Thoát")
        chon = input("Nhập lựa chọn: ")

        if chon == "1":
            tao_file_csv()
        elif chon == "2":
            doc_va_tinh_tong()
        elif chon == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")

# ====== CHẠY CHƯƠNG TRÌNH ======
menu()
