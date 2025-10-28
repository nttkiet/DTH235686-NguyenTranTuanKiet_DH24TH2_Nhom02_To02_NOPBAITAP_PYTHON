from tkinter import *

# --- Hàm xử lý ---
def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringKQ.set("")

def giaiAction():
    try:
        a = float(stringHSA.get())
        b = float(stringHSB.get())
        if a == 0 and b == 0:
            stringKQ.set("Vô số nghiệm")
        elif a == 0 and b != 0:
            stringKQ.set("Vô nghiệm")
        else:
            x = -b / a
            stringKQ.set(f"x = {x:.2f}")
    except ValueError:
        stringKQ.set("Nhập sai dữ liệu!")

# --- Cửa sổ chính ---
root = Tk()
root.title("Giải Phương Trình Bậc 1")

# Kích thước cửa sổ
window_width = 500
window_height = 300

# Lấy kích thước màn hình
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Tính toán vị trí để nằm giữa màn hình
x_pos = int((screen_width / 2) - (window_width / 2))
y_pos = int((screen_height / 2) - (window_height / 2))

# Đặt kích thước & vị trí cửa sổ
root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")
root.resizable(False, False)  # Không cho thay đổi kích thước

# --- Biến lưu dữ liệu ---
stringHSA = StringVar()
stringHSB = StringVar()
stringKQ = StringVar()

# --- Giao diện ---
Label(root, text="🧮 GIẢI PHƯƠNG TRÌNH BẬC 1", fg="blue", font=("Tahoma", 20, "bold")).pack(pady=15)

frameInput = Frame(root)
frameInput.pack(pady=10)

Label(frameInput, text="Hệ số a:", font=("Tahoma", 12)).grid(row=0, column=0, padx=10, pady=5, sticky=E)
Entry(frameInput, width=30, textvariable=stringHSA, font=("Tahoma", 12)).grid(row=0, column=1, pady=5)

Label(frameInput, text="Hệ số b:", font=("Tahoma", 12)).grid(row=1, column=0, padx=10, pady=5, sticky=E)
Entry(frameInput, width=30, textvariable=stringHSB, font=("Tahoma", 12)).grid(row=1, column=1, pady=5)

frameButton = Frame(root)
frameButton.pack(pady=10)
Button(frameButton, text="Giải", width=10, font=("Tahoma", 11), command=giaiAction).pack(side=LEFT, padx=10)
Button(frameButton, text="Tiếp", width=10, font=("Tahoma", 11), command=tiepAction).pack(side=LEFT, padx=10)
Button(frameButton, text="Thoát", width=10, font=("Tahoma", 11), command=root.quit).pack(side=LEFT, padx=10)

frameResult = Frame(root)
frameResult.pack(pady=10)
Label(frameResult, text="Kết quả:", font=("Tahoma", 12)).grid(row=0, column=0, padx=10)
Entry(frameResult, width=35, textvariable=stringKQ, font=("Tahoma", 12), state="readonly").grid(row=0, column=1)

# --- Chạy chương trình ---
root.mainloop()
