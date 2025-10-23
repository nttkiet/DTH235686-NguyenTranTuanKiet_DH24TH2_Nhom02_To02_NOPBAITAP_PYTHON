# ReadXML.py
from xml.dom.minidom import parse
import xml.dom.minidom

# Mở file XML bằng hàm parse
DOMTree = xml.dom.minidom.parse(r"D:\DTH235677_PyThon\DTH235677_TranDuyKhanh_DH24TH2_NHOM_02_NOPBAITAP_PYTHON\Bai_Tap_Chuong7\Bai3_XuLyXMLFile\employees.xml")

# Lấy phần tử gốc (root element)
collection = DOMTree.documentElement

# Lấy danh sách các employee
employees = collection.getElementsByTagName("employee")

print("Danh sách nhân viên trong file employees.xml:\n")

# Duyệt qua từng employee và in ra ID + Name
for emp in employees:
    emp_id = emp.getElementsByTagName("id")[0].childNodes[0].data
    emp_name = emp.getElementsByTagName("name")[0].childNodes[0].data
    print(f"ID: {emp_id} - Họ tên: {emp_name}")
