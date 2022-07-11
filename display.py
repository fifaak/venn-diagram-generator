#main program
#Copyright (C) 2022 Pataradanai akkratch & Chayanon saensuk - All Rights Reserved


from subprocess import call
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
window = Tk()
window.geometry("1024x406")
window.configure(bg = "#FFFFFF")
def gui1():
    file = (__file__)
    str(file)
    file = file.replace("display.py","venn_1.py")
    print(file)
    str_path = file
    path = Path(str_path)
    call(['python',(path)])
def gui2():
    file = (__file__)
    str(file)
    file = file.replace("display.py","venn_2.py")
    print(file)
    str_path = file
    path = Path(str_path)
    call(['python',(path)])
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 576,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)
canvas.create_text(
    140.0,
    0.0,
    anchor="nw",
    text="Venn diagram generator program",
    fill="#000000",
    font=("Fredoka", 48 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    844.0,
    228.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=gui1,
    relief="flat"
)
button_1.place(
    x=0.0,
    y=65.0,
    width=334.0,
    height=344.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=gui2,
    relief="flat"
)
button_2.place(
    x=334.0,
    y=67.0,
    width=326.0,
    height=322.0
)
window.iconbitmap(relative_to_assets("window.ico"))
window.title("โปรแกรมสร้างแผนภาพเวนน์ออยเลอร์")
window.resizable(False, False)
window.mainloop()