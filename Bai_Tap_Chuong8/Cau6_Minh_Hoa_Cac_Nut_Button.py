from tkinter import *

root = Tk()
root.title("Các kiểu Style của Button")
root.geometry("500x300")
# --- Căn giữa màn hình ---
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (450 // 2)
y = (screen_height // 2) - (300 // 2)
root.geometry(f"500x300+{x}+{y}")

Label(root, text="Các loại style của Button trong Tkinter", font=("Tahoma", 14, "bold")).pack(pady=10)

styles = ["flat", "groove", "raised", "ridge", "solid", "sunken"]

for bw in range(1, 4):  # borderwidth 1 → 3
    frame = Frame(root)
    frame.pack(pady=5)
    Label(frame, text=f"borderwidth = {bw}", width=15).pack(side=LEFT)
    for s in styles:
        Button(frame, text=s, relief=s, borderwidth=bw, width=8).pack(side=LEFT, padx=3)

root.mainloop()

