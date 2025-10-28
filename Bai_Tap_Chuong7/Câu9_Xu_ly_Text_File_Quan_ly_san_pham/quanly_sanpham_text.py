import os

# -------------------------------
# Định nghĩa lớp DanhMuc và SanPham
# -------------------------------
class DanhMuc:
    def __init__(self, ma, ten):
        self.ma = ma
        self.ten = ten

class SanPham:
    def __init__(self, ma, ten, dongia, ma_danhmuc):
        self.ma = ma
        self.ten = ten
        self.dongia = float(dongia)
        self.ma_danhmuc = ma_danhmuc

# -------------------------------
# Chức năng chính
# -------------------------------
class QuanLySanPham:
    def __init__(self, file_name="sanpham.txt"):
        self.file_name = file_name
        self.danhmucs = []
        self.sanphams = []
        self.doc_file()

    def doc_file(self):
        if not os.path.exists(self.file_name):
            return
        with open(self.file_name, "r", encoding="utf-8") as f:
            for line in f:
                loai, data = line.strip().split(":", 1)
                info = data.split(",")
                if loai == "DM":
                    self.danhmucs.append(DanhMuc(*info))
                elif loai == "SP":
                    self.sanphams.append(SanPham(*info))

    def luu_file(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            for dm in self.danhmucs:
                f.write(f"DM:{dm.ma},{dm.ten}\n")
            for sp in self.sanphams:
                f.write(f"SP:{sp.ma},{sp.ten},{sp.dongia},{sp.ma_danhmuc}\n")

    def them_danhmuc(self, ma, ten):
        self.danhmucs.append(DanhMuc(ma, ten))

    def them_sanpham(self, ma, ten, dongia, ma_danhmuc):
        self.sanphams.append(SanPham(ma, ten, dongia, ma_danhmuc))

    def tim_sanpham(self, tu_khoa):
        return [sp for sp in self.sanphams if tu_khoa.lower() in sp.ten.lower()]

    def xoa_sanpham(self, ma):
        self.sanphams = [sp for sp in self.sanphams if sp.ma != ma]

    def sapxep_theo_gia(self):
        self.sanphams.sort(key=lambda x: x.dongia)

    def hien_thi(self):
        print("===== DANH SÁCH SẢN PHẨM =====")
        for sp in self.sanphams:
            print(f"{sp.ma} - {sp.ten} - {sp.dongia} - {sp.ma_danhmuc}")

# -------------------------------
# Chạy thử
# -------------------------------
if __name__ == "__main__":
    ql = QuanLySanPham()
    ql.them_danhmuc("DM01", "Điện thoại")
    ql.them_danhmuc("DM02", "Laptop")

    ql.them_sanpham("SP01", "iPhone 15", 25000000, "DM01")
    ql.them_sanpham("SP02", "MacBook Air", 32000000, "DM02")
    ql.luu_file()

    ql.hien_thi()
    print("\nTìm sản phẩm có chữ 'Mac':")
    for sp in ql.tim_sanpham("Mac"):
        print(sp.ten, "-", sp.dongia)
