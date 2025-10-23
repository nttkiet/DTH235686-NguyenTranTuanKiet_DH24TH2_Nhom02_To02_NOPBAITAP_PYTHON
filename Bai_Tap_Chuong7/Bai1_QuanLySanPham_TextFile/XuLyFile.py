def LuuFile(path, data):
    file = open(path, 'a', encoding='utf-8')
    file.writelines(data)
    file.writelines("\n")
    file.close()

def DocFile(path):
    arrProduct = []
    file = open(path, 'r', encoding='utf-8')
    for line in file:
        data = line.strip()
        arr = data.split(';')
        arrProduct.append(arr)
    file.close()
    return arrProduct
LuuFile("database.txt", "sv1;Cocacolala;15.5"
                        "sp2;Bưởi 5 Roi;18.0"
                        "sp3;Bia 333;14.5")
