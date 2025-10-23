import json

# Tạo Python Object (dạng dict)
pythonObject = {
    "ten": "Trần Duy Thanh",
    "tuoi": 50,
    "ma": "nv1"
}

# Chuyển đổi từ Python Object sang JSON String
jsonString = json.dumps(pythonObject, ensure_ascii=False, indent=4)

# In ra kết quả
print("Chuỗi JSON sau khi chuyển đổi:")
print(jsonString)
