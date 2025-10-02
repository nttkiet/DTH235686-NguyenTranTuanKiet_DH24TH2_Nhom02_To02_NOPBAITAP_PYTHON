# Câu 6: Đọc số n có tối đa 2 chữ số ra dạng chữ

def doc_so(n):
    chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    if n < 0 or n > 99:
        return "Số không hợp lệ"
    if n < 10:
        return chu_so[n]
    elif n < 20:
        if n == 10:
            return "mười"
        elif n == 15:
            return "mười lăm"
        else:
            return "mười " + chu_so[n % 10]
    else:
        hang_chuc = n // 10
        hang_don_vi = n % 10
        chuoi = chu_so[hang_chuc] + " mươi"
        if hang_don_vi == 0:
            return chuoi
        elif hang_don_vi == 1:
            return chuoi + " mốt"
        elif hang_don_vi == 5:
            return chuoi + " lăm"
        else:
            return chuoi + " " + chu_so[hang_don_vi]

# Nhập số n và đọc ra dạng chữ
n = int(input("Nhập số n (tối đa 2 chữ số): "))
print(doc_so(n))