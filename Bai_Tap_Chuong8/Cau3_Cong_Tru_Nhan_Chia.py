from tkinter import *

def congAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        stringKQ.set(a + b)
    except ValueError:
        stringKQ.set("Lỗi nhập liệu!")

def truAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        stringKQ.set(a - b)
    except ValueError:
        stringKQ.set("Lỗi nhập liệu!")

def nhanAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        stringKQ.set(a * b)
    except ValueError:
        stringKQ.set("Lỗi nhập liệu!")

def chiaAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        if b == 0:
            stringKQ.set("Không chia được cho 0")
        else:
            stringKQ.set(round(a / b, 3))
    except ValueError:
        stringKQ.set("Lỗi nhập liệu!")

# ------------------------------
# Giao diện chính
root = Tk()
root.title("Máy tính 4 phép cơ bản")
root.geometry("450x300")  # kích thước to hơn
root.update_idletasks()

# --- Căn giữa màn hình ---
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (450 // 2)
y = (screen_height // 2) - (300 // 2)
root.geometry(f"450x300+{x}+{y}")

# --- Biến ---
stringA = StringVar()
stringB = StringVar()
stringKQ = StringVar()

# --- Giao diện ---
Label(root, text="MÁY TÍNH CỘNG TRỪ NHÂN CHIA", fg="blue", font=("Tahoma", 18, "bold")).grid(row=0, column=0, columnspan=3, pady=10)

Label(root, text="Số A:", font=("Tahoma", 12)).grid(row=1, column=1, sticky=E, padx=10, pady=5)
Entry(root, width=20, textvariable=stringA, font=("Tahoma", 12)).grid(row=1, column=2, padx=10, pady=5)

Label(root, text="Số B:", font=("Tahoma", 12)).grid(row=2, column=1, sticky=E, padx=10, pady=5)
Entry(root, width=20, textvariable=stringB, font=("Tahoma", 12)).grid(row=2, column=2, padx=10, pady=5)

Label(root, text="Kết quả:", font=("Tahoma", 12)).grid(row=3, column=1, sticky=E, padx=10, pady=5)
Entry(root, width=20, textvariable=stringKQ, font=("Tahoma", 12)).grid(row=3, column=2, padx=10, pady=5)

frameButton = Frame(root)
frameButton.grid(row=1, column=0, rowspan=4, padx=10, pady=5)

Button(frameButton, text="Cộng (+)", command=congAction, width=12, font=("Tahoma", 11)).pack(pady=3)
Button(frameButton, text="Trừ (-)", command=truAction, width=12, font=("Tahoma", 11)).pack(pady=3)
Button(frameButton, text="Nhân (×)", command=nhanAction, width=12, font=("Tahoma", 11)).pack(pady=3)
Button(frameButton, text="Chia (÷)", command=chiaAction, width=12, font=("Tahoma", 11)).pack(pady=3)

Button(root, text="Thoát", command=root.quit, width=10, bg="lightgray", font=("Tahoma", 11)).grid(row=4, column=2, pady=10)

root.mainloop()
