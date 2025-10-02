# Câu 12: Hàm oscillate

def oscillate(a, b):
    lst = []
    x = a
    for i in range(b):
        lst.append(x)
        if x < 0:
            x = -x
        else:
            x = x - 1
    return lst

for n in oscillate(-3, 15):
    print(n, end=' ')
print()