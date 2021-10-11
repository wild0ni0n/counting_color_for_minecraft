from tkinter import filedialog, Tk, Label, messagebox, Canvas
import getpass
from PIL import Image, ImageTk
from typing import Tuple


def conv_webcolor(rgb: Tuple[int, int, int]):
    hex_colors = list(map(lambda x: hex(x)[2:].zfill(2), rgb))
    return '#' + "".join(hex_colors).upper()

# initialized window
root = Tk()
root.title('Counting Color Tool for Minecraft')
root.geometry("400x300")

# open file dialog and read image
filetype=[('PNG','*.png'), ('すべてのファイル', '*.*')]
initialdir="C:\\Users\\{}\\Pictures".format(getpass.getuser())
filepath = filedialog.askopenfilename(filetypes=filetype, initialdir=initialdir)
im = Image.open(filepath)
colors = im.getcolors(im.size[0] * im.size[1])
if len(colors) > 255:
    messagebox.showerror("エラー", "画像の色数が多すぎます。255色以下に減色してください")
    exit()

# show image
#pi = ImageTk.PhotoImage(im)
#canvas = Canvas(bg = "black", width=im.size[0], height=im.size[1])
#canvas.create_image(30, 30, image=pi)


# label    
lbl_head_title1 = Label(text="色コード")
lbl_head_title2 = Label(text="使用数")
lbl_head_title1.grid(row=0, column=1)
lbl_head_title2.grid(row=0, column=3)


for num, (cnt, rgb) in enumerate(colors):
    print(rgb)
    if len(rgb) == 4:
        (rgb) = (rgb)[:3]
    webcolor = conv_webcolor(rgb)

    lbl_webcolor = Label(text=webcolor)
    lbl_colorbox = Label(text="■", foreground=webcolor)
    lbl_color_count = Label(text=cnt)

    lbl_webcolor.grid(row=num+1, column=1)
    lbl_colorbox.grid(row=num+1, column=2)
    lbl_color_count.grid(row=num+1, column=3)

root.mainloop()

    