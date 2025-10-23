import csv

# Mở file datacsv.csv
with open(r"D:\DTH235677_TranDuyKhanh_DH24TH2_NHOM_02_NOPBAITAP_PYTHON\Bai_Tap_Chuong7\datacsv.csv", newline='', encoding='utf-8') as f:
    # Đọc file, ngăn cách bởi dấu chấm phẩy
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)

    # Duyệt từng dòng trong file
    for row in reader:
        # row[0] là mã, row[1] là tên
        print(row[0], "\t", row[1])
