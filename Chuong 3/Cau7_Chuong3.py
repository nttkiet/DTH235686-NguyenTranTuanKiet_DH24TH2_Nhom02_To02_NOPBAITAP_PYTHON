# Câu 7: Tìm ngày kế sau ngày vừa nhập

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 0

def next_day(day, month, year):
    d_in_m = days_in_month(month, year)
    if day < d_in_m:
        return day + 1, month, year
    else:
        if month == 12:
            return 1, 1, year + 1
        else:
            return 1, month + 1, year

# Nhập ngày, tháng, năm
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

if 1 <= month <= 12 and 1 <= day <= days_in_month(month, year):
    nd, nm, ny = next_day(day, month, year)
    print(f"Ngày kế tiếp là: {nd}/{nm}/{ny}")
else:
    print("Ngày không hợp lệ")