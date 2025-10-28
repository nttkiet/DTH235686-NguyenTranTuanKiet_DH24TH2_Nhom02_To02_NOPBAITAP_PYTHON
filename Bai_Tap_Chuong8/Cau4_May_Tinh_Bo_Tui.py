from tkinter import *

def nhap(giatri):
    hien_thi.set(hien_thi.get() + str(giatri))

def xoa():
    hien_thi.set("")

def tinh():
    try:
        ketqua = eval(hien_thi.get())
        hien_thi.set(str(ketqua))
    except:
        hien_thi.set("Lỗi!")

root = Tk()
root.title("Máy tính bỏ túi")
root.geometry("300x400")
# --- Căn giữa màn hình ---
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (450 // 2)
y = (screen_height // 2) - (300 // 2)
root.geometry(f"300x400+{x}+{y}")

hien_thi = StringVar()

Entry(root, textvariable=hien_thi, font=("Tahoma", 20), justify='right').pack(fill=BOTH, ipadx=8, ipady=10, padx=10, pady=10)

frame = Frame(root)
frame.pack()

# Tạo các nút
nut = [
    ('7','8','9','/'),
    ('4','5','6','*'),
    ('1','2','3','-'),
    ('0','.','=','+')
]

for dong in nut:
    hang = Frame(frame)
    hang.pack()
    for n in dong:
        if n == '=':
            Button(hang, text=n, width=6, height=2, font=("Tahoma",14),
                   command=tinh).pack(side=LEFT, padx=2, pady=2)
        else:
            Button(hang, text=n, width=6, height=2, font=("Tahoma",14),
                   command=lambda val=n: nhap(val)).pack(side=LEFT, padx=2, pady=2)

Button(root, text="C", font=("Tahoma",14), width=28, command=xoa, bg="lightgray").pack(pady=5)

root.mainloop()
