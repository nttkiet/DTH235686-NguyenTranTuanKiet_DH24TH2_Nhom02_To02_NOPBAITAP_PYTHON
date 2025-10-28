from tkinter import *

def convert():
    try:
        f = float(stringF.get())
        c = (5/9) * (f - 32)
        stringC.set(f"{c:.2f} °C")
    except:
        stringC.set("Lỗi nhập liệu!")

root = Tk()
root.title("Chuyển độ F sang độ C")
root.geometry("400x200")
root.configure(bg="#F5FF82")  # nền vàng nhạt
# --- Căn giữa màn hình ---
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (450 // 2)
y = (screen_height // 2) - (300 // 2)
root.geometry(f"400x200+{x}+{y}")

stringF = StringVar()
stringC = StringVar()

Label(root, text="Nhập độ F:", bg="#F5FF82", font=("Tahoma", 12)).grid(row=0, column=0, padx=10, pady=10)
Entry(root, textvariable=stringF, width=10, font=("Tahoma", 12)).grid(row=0, column=1, padx=10)
Button(root, text="Chuyển", command=convert, font=("Tahoma", 12), bg="lightblue").grid(row=0, column=2, padx=10)

Label(root, text="Độ C:", bg="#F5FF82", font=("Tahoma", 12)).grid(row=1, column=0, padx=10, pady=10)
Entry(root, textvariable=stringC, width=20, font=("Tahoma", 12)).grid(row=1, column=1, columnspan=2, padx=10)

root.mainloop()
