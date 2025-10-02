# Câu 13: Hàm kiểm tra số hoàn thiện, số thịnh vượng

def tong_uoc_so(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

def la_hoan_thien(n):
    return tong_uoc_so(n) == n

def la_thinh_vuong(n):
    return tong_uoc_so(n) > n

n = int(input("Nhập số nguyên dương n: "))
if la_hoan_thien(n):
    print(n, "là số hoàn thiện")
elif la_thinh_vuong(n):
    print(n, "là số thịnh vượng")
else:
    print(n, "không phải là số hoàn thiện hoặc thịnh vượng")