from tkinter import *

root = Tk()
root.title("Đổi mật khẩu")
root.geometry("350x200")
# --- Căn giữa màn hình ---
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (450 // 2)
y = (screen_height // 2) - (300 // 2)
root.geometry(f"350x200+{x}+{y}")

Label(root, text="Enter New Password", font=("Tahoma",14), fg="purple").pack(pady=10)

frame = Frame(root)
frame.pack(pady=10)

Label(frame, text="Old Password:").grid(row=0, column=0, sticky=E, pady=3)
Label(frame, text="New Password:").grid(row=1, column=0, sticky=E, pady=3)
Label(frame, text="Re-enter Password:").grid(row=2, column=0, sticky=E, pady=3)

Entry(frame, show="*").grid(row=0, column=1, padx=10)
Entry(frame, show="*").grid(row=1, column=1, padx=10)
Entry(frame, show="*").grid(row=2, column=1, padx=10)

Button(root, text="OK", width=10).pack(side=LEFT, padx=40, pady=10)
Button(root, text="Cancel", width=10, command=root.quit).pack(side=RIGHT, padx=40, pady=10)

root.mainloop()
