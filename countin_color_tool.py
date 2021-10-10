from tkinter import filedialog, Tk, Label, LEFT
import getpass
from PIL import Image
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
colors = im.getcolors()

# label
for cnt, (num, rgb) in enumerate(colors):
    # error
    print(rgb)
    lbl = Label(text="■", foreground=conv_webcolor(rgb))
    lbl.grid(side=LEFT)

root.mainloop()

    