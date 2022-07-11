#3circle(3sets)
#Copyright (C) 2022 Pataradanai akkratch & Chayanon saensuk - All Rights Reserved
from pathlib import Path
from matplotlib_venn import venn3
import matplotlib.pyplot as plt
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
def plot():
    plt.close()
    a= int(entry_1.get()) #A
    b = int(entry_2.get()) #B
    c = int(entry_3.get()) #AB
    d = int(entry_4.get()) #C
    e = int(entry_5.get()) #AC
    f = int(entry_6.get()) #BC
    g = int(entry_7.get()) #ABC
    h = c-g
    i = e-g
    j = f-g
    k = a-h-i-g
    l = b-h-j-g
    m = d-i-j-g
    items2 = [k,l,h,m,i,j,g]
    labels2 = ['set A','set B','set C']

    venn3(subsets=items2,set_labels=labels2,set_colors=('red','blue','green'),alpha=0.5)
    plt.show()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("510x600")
window.configure(bg = "#FFFFFF")


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
canvas.create_rectangle(
    49.0,
    72.0,
    460.0,
    549.0,
    fill="#FF6A6A",
    outline="#FF0000")

canvas.create_text(
    154.0,
    0.0,
    anchor="nw",
    text="3 circles",
    fill="#000000",
    font=("Fredoka Regular", 48 * -1)
)
def close():
    exit()
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=close,
    relief="flat"
)
button_1.place(
    x=210,
    y=556,
    width=96.0,
    height=41.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    176.5,
    430.5,
    image=entry_image_1
)
entry_6 = Entry( 
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_6.place( 
    x=119.0,
    y=416.0,
    width=115.0,
    height=27.0
)


entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    328.5,
    430.5,
    image=entry_image_2
)
entry_4 = Entry( 
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_4.place( 
    x=271.0,
    y=416.0,
    width=115.0,
    height=27.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    176.5,
    388.5,
    image=entry_image_3
)
entry_5 = Entry( 
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_5.place( 
    x=119.0,
    y=374.0,
    width=115.0,
    height=27.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    328.5,
    388.5,
    image=entry_image_4
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_2.place(
    x=271.0,
    y=374.0,
    width=115.0,
    height=27.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    175.5,
    346.5,
    image=entry_image_5
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_3.place(
    x=118.0,
    y=332.0,
    width=115.0,
    height=27.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    327.5,
    346.5,
    image=entry_image_6
)
entry_1 = Entry( 
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place( 
    x=270.0,
    y=332.0,
    width=115.0,
    height=27.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    175.5,
    302.5,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_7.place(
    x=118.0,
    y=288.0,
    width=115.0,
    height=27.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    254.0,
    175.0,
    image=image_image_1
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=plot,
    relief="flat"
)
button_2.place(
    x=92.0,
    y=458.0,
    width=324.0,
    height=76.0
)

canvas.create_text(
    50.0,
    295.0,
    anchor="nw",
    text="n(A∩B∩C)",
    
    font=("Fredoka Regular", 12 * -1)
)

canvas.create_text(
    60.0,
    337.0,
    anchor="nw",
    text="n(A∩B)",
    
    font=("Fredoka Regular", 12 * -1)
)

canvas.create_text(
    60.0,
    379.0,
    anchor="nw",
    text="n(A∩C)",
    
    font=("Fredoka Regular", 12 * -1)
)

canvas.create_text(
    60.0,
    421.0,
    anchor="nw",
    text="n(B∩C)",
    
    font=("Fredoka Regular", 12 * -1)
)

canvas.create_text(
    415.0,
    337.0,
    anchor="nw",
    text="n(A)",
    
    font=("Fredoka Regular", 12 * -1)
)

canvas.create_text(
    415.0,
    379.0,
    anchor="nw",
    text="n(B)",
    
    font=("Fredoka Regular", 12 * -1)
)

canvas.create_text(
    415.0,
    421.0,
    anchor="nw",
    text="n(C)",
    
    font=("Fredoka Regular", 12 * -1)
)
window.iconbitmap(relative_to_assets("window.ico"))
window.title("3เซต")
window.resizable(False, False)
window.mainloop()
