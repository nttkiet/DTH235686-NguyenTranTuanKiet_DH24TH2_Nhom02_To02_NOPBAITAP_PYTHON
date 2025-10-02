# Câu 10: Vẽ hình dùng sleep

from time import sleep

def hinh1(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '* ' * (i + 1))

def hinh2(n):
    for i in range(n):
        print('* ' * (n - i) + ' ' * (2 * i))

def hinh3(n):
    for i in range(n):
        print('* ' * n)

def hinh4(n):
    for i in range(n):
        print(' ' * i + '* ' * (n - i))

n = 5
hinh1(n)
sleep(5)
print()
hinh2(n)
sleep(5)
print()
hinh3(n)
sleep(5)
print()
hinh4(n)