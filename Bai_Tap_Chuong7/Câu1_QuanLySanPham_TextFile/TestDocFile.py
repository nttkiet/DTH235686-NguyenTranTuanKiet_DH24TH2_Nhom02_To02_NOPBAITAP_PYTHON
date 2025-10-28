from XuLyFile import *

dssp = DocFile("database.txt")

def XuatSanPham(dssp):
    for row in dssp:
        for element in row:
            print(element, end='\t')
        print()

XuatSanPham(dssp)

def SortSp(dssp):
    for i in range(len(dssp)):
        for j in range(i+1, len(dssp)):
            a = dssp[i]
            b = dssp[j]
            if float(a[2]) < float(b[2]):  # so sánh giá giảm dần
                dssp[i], dssp[j] = b, a

SortSp(dssp)
print("Sản phẩm sau khi sắp xếp theo giá giảm dần:")
XuatSanPham(dssp)
