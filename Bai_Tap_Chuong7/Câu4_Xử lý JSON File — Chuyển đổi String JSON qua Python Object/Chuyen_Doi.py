import json

# Chuỗi JSON
jsonString = '{ "ma": "nv1", "age": 50, "ten": "Trần Duy Thanh" }'

# Chuyển đổi từ JSON String sang Python Object (dict)
dataObject = json.loads(jsonString)

# In toàn bộ dữ liệu
print("Dữ liệu sau khi chuyển đổi:", dataObject)

# Truy xuất từng phần tử trong object
print("Mã =", dataObject["ma"])
print("Tuổi =", dataObject["age"])
print("Tên =", dataObject["ten"])
