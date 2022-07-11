#2circle(2sets)
#Copyright (C) 2022 Pataradanai akkratch & Chayanon saensuk - All Rights Reserved
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
window = Tk()

window.geometry("510x610")
window.configure(bg = "#FFFFFF")
def alert():
    canvas.create_text(
    65.0,
    430.0,
    text="กรอกค่าผิด",
    font=("Fredoka Regular", 8 * 1)
    )
#plot venn diagram
def plot():
    plt.close()
    A = int(entry_1.get())
    B = int(entry_2.get())
    C = int(entry_3.get())
    if A+B >= C:
        items =[A-C,B-C,C]
        labels = ['set A','set B']
        venn2(subsets=items,set_labels=labels,set_colors=("blue","red"),alpha=0.7)
        plt.show()
    else:
        entry_3.delete(0, END)
        entry_3.insert(0, "")
        alert()
#To use assets1 folder
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)




#gui
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
    39.0,
    59.0,
    472.0,
    563.0,
    fill="#4181FF",
    outline="")

canvas.create_text(
    154.0,
    0.0,
    anchor="nw",
    text="2 circles",
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
    relief="flat",
    command =close
)
button_1.place(
    x=210,
    y=566,
    width=96.0,
    height=41.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    254.0,
    345.5,
    image=entry_image_1
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_2.place(
    x=102.0,
    y=321.0,
    width=304.0,
    height=47.0
)

canvas.create_text(
    50.0,
    336.0,
    anchor="nw",
    text="n(B)",
    
    font=("Fredoka Regular", 15 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    254.0,
    279.5,
    image=entry_image_2
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=102.0,
    y=255.0,
    width=304.0,
    height=47.0
)

canvas.create_text(
    50.0,
    270.0,
    anchor="nw",
    text="n(A)",
    
    font=("Fredoka Regular", 15 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    254.0,
    413.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_3.place(
    x=102.0,
    y=389.0,
    width=304.0,
    height=47.0
)

canvas.create_text(
    65.0,
    410.0,
    text="n(A∩B)",
    
    font=("Fredoka Regular", 15 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    254.0,
    149.0,
    image=image_image_1
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    master = window, 
   
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
window.iconbitmap(relative_to_assets("window.ico"))
window.title("2เซต")
window.resizable(False, False)
window.mainloop()