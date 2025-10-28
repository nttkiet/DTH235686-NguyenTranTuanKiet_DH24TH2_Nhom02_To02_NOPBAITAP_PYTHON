from tkinter import *

def convert():
    can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
    chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]

    try:
        nam = int(stringNam.get())
        can_chi = can[nam % 10] + " " + chi[nam % 12]
        stringKQ.set(can_chi)
    except:
        stringKQ.set("Lỗi nhập liệu!")

root = Tk()
root.title("Chuyển năm Dương lịch sang Âm lịch")
root.geometry("400x200")
root.configure(bg="lightyellow")
# --- Căn giữa màn hình ---
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (450 // 2)
y = (screen_height // 2) - (300 // 2)
root.geometry(f"400x300+{x}+{y}")

stringNam = StringVar()
stringKQ = StringVar()

Label(root, text="Nhập năm dương:", bg="lightyellow", font=("Tahoma", 12)).grid(row=0, column=0, padx=10, pady=10)
Entry(root, textvariable=stringNam, width=10, font=("Tahoma", 12)).grid(row=0, column=1, padx=10)
Button(root, text="Chuyển", command=convert, font=("Tahoma", 12), bg="lightblue").grid(row=0, column=2, padx=10)

Label(root, text="Năm âm:", bg="lightyellow", font=("Tahoma", 12)).grid(row=1, column=0, padx=10, pady=10)
Entry(root, textvariable=stringKQ, width=20, font=("Tahoma", 12)).grid(row=1, column=1, columnspan=2, padx=10)

root.mainloop()
