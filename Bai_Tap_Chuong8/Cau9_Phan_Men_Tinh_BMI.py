import tkinter as tk
from tkinter import messagebox

# ===== Hàm tính BMI =====
def tinh_bmi():
    try:
        chieu_cao = float(entry_chieu_cao.get())
        can_nang = float(entry_can_nang.get())

        if chieu_cao <= 0 or can_nang <= 0:
            messagebox.showerror("Lỗi", "Chiều cao và cân nặng phải lớn hơn 0!")
            return

        bmi = can_nang / (chieu_cao ** 2)
        entry_bmi.delete(0, tk.END)
        entry_bmi.insert(0, f"{bmi:.2f}")

        # Phân loại BMI
        if bmi < 18.5:
            tinh_trang = "Gầy"
            nguy_co = "Thấp"
        elif bmi < 25:
            tinh_trang = "Bình thường"
            nguy_co = "Trung bình"
        elif bmi < 30:
            tinh_trang = "Hơi béo"
            nguy_co = "Cao"
        else:
            tinh_trang = "Béo phì"
            nguy_co = "Rất cao"

        entry_tinh_trang.delete(0, tk.END)
        entry_tinh_trang.insert(0, tinh_trang)
        entry_nguy_co.delete(0, tk.END)
        entry_nguy_co.insert(0, nguy_co)
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số!")

# ===== Thoát =====
def thoat():
    root.destroy()

# ===== Giao diện chính =====
root = tk.Tk()
root.title("Chương trình tính BMI")
root.geometry("450x400")   # kích thước lớn, dễ nhìn
root.configure(bg="yellow")
# --- Căn giữa màn hình ---
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (450 // 2)
y = (screen_height // 2) - (300 // 2)
root.geometry(f"450x400+{x}+{y}")


# Căn giữa cửa sổ
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (450 // 2)
y = (screen_height // 2) - (400 // 2)
root.geometry(f"450x400+{x}+{y}")

# ===== Tiêu đề =====
title = tk.Label(root, text="TÍNH CHỈ SỐ BMI", bg="yellow", fg="blue", font=("Arial", 16, "bold"))
title.pack(pady=10)

# ===== Khung nhập liệu =====
frame = tk.Frame(root, bg="yellow")
frame.pack(pady=10)

tk.Label(frame, text="Nhập chiều cao (m):", bg="yellow", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
entry_chieu_cao = tk.Entry(frame, font=("Arial", 12))
entry_chieu_cao.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Nhập cân nặng (kg):", bg="yellow", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
entry_can_nang = tk.Entry(frame, font=("Arial", 12))
entry_can_nang.grid(row=1, column=1, pady=5)

# ===== Nút tính BMI =====
btn_tinh = tk.Button(frame, text="Tính BMI", bg="lightblue", font=("Arial", 12, "bold"), command=tinh_bmi)
btn_tinh.grid(row=2, columnspan=2, pady=10)

# ===== Kết quả =====
tk.Label(frame, text="BMI của bạn:", bg="yellow", font=("Arial", 12)).grid(row=3, column=0, sticky="w", pady=5)
entry_bmi = tk.Entry(frame, font=("Arial", 12))
entry_bmi.grid(row=3, column=1, pady=5)

tk.Label(frame, text="Tình trạng của bạn:", bg="yellow", font=("Arial", 12)).grid(row=4, column=0, sticky="w", pady=5)
entry_tinh_trang = tk.Entry(frame, font=("Arial", 12))
entry_tinh_trang.grid(row=4, column=1, pady=5)

tk.Label(frame, text="Nguy cơ phát triển bệnh:", bg="yellow", font=("Arial", 12)).grid(row=5, column=0, sticky="w", pady=5)
entry_nguy_co = tk.Entry(frame, font=("Arial", 12))
entry_nguy_co.grid(row=5, column=1, pady=5)

# ===== Nút thoát =====
btn_thoat = tk.Button(root, text="Thoát", bg="orange", font=("Arial", 12, "bold"), command=thoat)
btn_thoat.pack(pady=10)

root.mainloop()
