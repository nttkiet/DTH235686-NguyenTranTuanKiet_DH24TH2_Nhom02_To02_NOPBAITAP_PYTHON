from tkinter import *
from math import sqrt

# ====== HÀM XỬ LÝ ======
def giaiAction():
    try:
        a = float(stringHSA.get())
        b = float(stringHSB.get())
        c = float(stringHSC.get())

        if a == 0:  # bx + c = 0
            if b == 0 and c == 0:
                stringKQ.set("Vô số nghiệm")
            elif b == 0 and c != 0:
                stringKQ.set("Vô nghiệm")
            else:
                x = -c / b
                stringKQ.set("x = " + str(x))
        else:
            delta = b ** 2 - 4 * a * c
            if delta < 0:
                stringKQ.set("Vô nghiệm")
            elif delta == 0:
                stringKQ.set("Nghiệm kép x1 = x2 = " + str(-b / (2 * a)))
            else:
                x1 = (-b - sqrt(delta)) / (2 * a)
                x2 = (-b + sqrt(delta)) / (2 * a)
                stringKQ.set("x1 = " + str(x1) + "; x2 = " + str(x2))
    except ValueError:
        stringKQ.set("Vui lòng nhập số hợp lệ!")


def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringHSC.set("")
    stringKQ.set("")

# ====== GIAO DIỆN ======
root = Tk()
root.title("Giải phương trình bậc 2")

# Căn giữa cửa sổ
window_width = 500
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_pos = int((screen_width / 2) - (window_width / 2))
y_pos = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

# Biến lưu giá trị
stringHSA = StringVar()
stringHSB = StringVar()
stringHSC = StringVar()
stringKQ = StringVar()

# ====== GIAO DIỆN NHẬP ======
Label(root, text="PHƯƠNG TRÌNH BẬC 2", fg="red", font=("tahoma", 20, "bold")).grid(row=0, column=0, columnspan=2, pady=15)

Label(root, text="Hệ số a:", font=("tahoma", 12)).grid(row=1, column=0, sticky=E, padx=10, pady=5)
Entry(root, width=30, textvariable=stringHSA, font=("tahoma", 12)).grid(row=1, column=1, pady=5)

Label(root, text="Hệ số b:", font=("tahoma", 12)).grid(row=2, column=0, sticky=E, padx=10, pady=5)
Entry(root, width=30, textvariable=stringHSB, font=("tahoma", 12)).grid(row=2, column=1, pady=5)

Label(root, text="Hệ số c:", font=("tahoma", 12)).grid(row=3, column=0, sticky=E, padx=10, pady=5)
Entry(root, width=30, textvariable=stringHSC, font=("tahoma", 12)).grid(row=3, column=1, pady=5)

# ====== NÚT CHỨC NĂNG ======
frameButton = Frame(root)
frameButton.grid(row=4, column=0, columnspan=2, pady=15)

Button(frameButton, text="Giải", width=10, command=giaiAction, bg="#4CAF50", fg="white", font=("tahoma", 11, "bold")).pack(side=LEFT, padx=10)
Button(frameButton, text="Tiếp", width=10, command=tiepAction, bg="#2196F3", fg="white", font=("tahoma", 11, "bold")).pack(side=LEFT, padx=10)
Button(frameButton, text="Thoát", width=10, command=root.quit, bg="#f44336", fg="white", font=("tahoma", 11, "bold")).pack(side=LEFT, padx=10)

# ====== KẾT QUẢ ======
Label(root, text="Kết quả:", font=("tahoma", 12)).grid(row=5, column=0, sticky=E, padx=10)
Entry(root, width=30, textvariable=stringKQ, font=("tahoma", 12)).grid(row=5, column=1, pady=5)

root.mainloop()
