import xml.etree.ElementTree as ET
from collections import Counter

# --- LỚP DỮ LIỆU ---
class Nhom:
    def __init__(self, ma, ten):
        self.ma = ma
        self.ten = ten

class ThietBi:
    def __init__(self, ma, ten, manhom):
        self.ma = ma
        self.ten = ten
        self.manhom = manhom


# --- CHƯƠNG TRÌNH CHÍNH ---
class QuanLyThietBi:
    def __init__(self):
        self.ds_nhom = []
        self.ds_tb = []

    def doc_du_lieu(self):
        # Đọc nhóm thiết bị
        tree_nhom = ET.parse("nhomthietbi.xml")
        root_nhom = tree_nhom.getroot()
        for n in root_nhom.findall("nhom"):
            ma = n.find("ma").text
            ten = n.find("ten").text
            self.ds_nhom.append(Nhom(ma, ten))

        # Đọc thiết bị
        tree_tb = ET.parse("thietbi.xml")
        root_tb = tree_tb.getroot()
        for tb in root_tb.findall("thietbi"):
            manhom = tb.attrib["manhom"]
            ma = tb.find("ma").text
            ten = tb.find("ten").text
            self.ds_tb.append(ThietBi(ma, ten, manhom))

    # --- Hiển thị ---
    def hien_thi_nhom(self):
        print("DANH SÁCH NHÓM THIẾT BỊ:")
        for n in self.ds_nhom:
            print(f"  {n.ma} - {n.ten}")

    def hien_thi_thiet_bi(self):
        print("\nDANH SÁCH THIẾT BỊ:")
        for tb in self.ds_tb:
            print(f"  {tb.ma} - {tb.ten} (Nhóm: {tb.manhom})")

    # --- Lọc theo nhóm ---
    def loc_theo_nhom(self, ma_nhom):
        print(f"\nTHIẾT BỊ THUỘC NHÓM {ma_nhom}:")
        kq = [tb for tb in self.ds_tb if tb.manhom == ma_nhom]
        if not kq:
            print("  Không có thiết bị nào.")
        else:
            for tb in kq:
                print(f"  {tb.ma} - {tb.ten}")

    # --- Nhóm có nhiều thiết bị nhất ---
    def nhom_nhieu_tb_nhat(self):
        dem = Counter(tb.manhom for tb in self.ds_tb)
        if not dem:
            print("Chưa có dữ liệu thiết bị.")
            return

        manhom_max = max(dem, key=dem.get)
        so_luong = dem[manhom_max]
        ten_nhom = next((n.ten for n in self.ds_nhom if n.ma == manhom_max), "Không rõ")

        print(f"\nNhóm có nhiều thiết bị nhất: {ten_nhom} ({so_luong} thiết bị)")


# --- CHẠY CHƯƠNG TRÌNH ---
if __name__ == "__main__":
    ql = QuanLyThietBi()
    ql.doc_du_lieu()
    ql.hien_thi_nhom()
    ql.hien_thi_thiet_bi()

    ql.loc_theo_nhom("n1")
    ql.nhom_nhieu_tb_nhat()
