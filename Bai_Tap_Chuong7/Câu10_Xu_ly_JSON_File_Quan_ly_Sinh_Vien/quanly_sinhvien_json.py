import json
import os

class Lop:
    def __init__(self, ma_lop, ten_lop):
        self.ma_lop = ma_lop
        self.ten_lop = ten_lop

class SinhVien:
    def __init__(self, ma, ten, namsinh, ma_lop):
        self.ma = ma
        self.ten = ten
        self.namsinh = int(namsinh)
        self.ma_lop = ma_lop

class QuanLySinhVien:
    def __init__(self, file_name="sinhvien.json"):
        self.file_name = file_name
        self.lops = []
        self.sinhviens = []
        self.doc_file()

    def doc_file(self):
        if not os.path.exists(self.file_name):
            return
        with open(self.file_name, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.lops = [Lop(**lop) for lop in data["lops"]]
            self.sinhviens = [SinhVien(**sv) for sv in data["sinhviens"]]

    def luu_file(self):
        data = {
            "lops": [lop.__dict__ for lop in self.lops],
            "sinhviens": [sv.__dict__ for sv in self.sinhviens]
        }
        with open(self.file_name, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def them_lop(self, ma_lop, ten_lop):
        self.lops.append(Lop(ma_lop, ten_lop))

    def them_sinhvien(self, ma, ten, namsinh, ma_lop):
        self.sinhviens.append(SinhVien(ma, ten, namsinh, ma_lop))

    def tim_sinhvien(self, tu_khoa):
        return [sv for sv in self.sinhviens if tu_khoa.lower() in sv.ten.lower()]

    def xoa_sinhvien(self, ma):
        self.sinhviens = [sv for sv in self.sinhviens if sv.ma != ma]

    def sapxep_theo_ten(self):
        self.sinhviens.sort(key=lambda x: x.ten)

    def hien_thi(self):
        print("===== DANH SÁCH SINH VIÊN =====")
        for sv in self.sinhviens:
            print(f"{sv.ma} - {sv.ten} - {sv.namsinh} - {sv.ma_lop}")

# -------------------------------
# Chạy thử
# -------------------------------
if __name__ == "__main__":
    ql = QuanLySinhVien()
    ql.them_lop("CTK45", "Công nghệ thông tin K45")

    ql.them_sinhvien("SV01", "An", 2004, "CTK45")
    ql.them_sinhvien("SV02", "Bình", 2003, "CTK45")
    ql.luu_file()

    ql.hien_thi()
    print("\nTìm sinh viên tên 'An':")
    for sv in ql.tim_sinhvien("An"):
        print(sv.ten, "-", sv.namsinh)
