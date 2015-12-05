from tkinter import *
from PIL import Image, ImageDraw

canvas_width = 200
canvas_height = 200
master = Tk()
w = Canvas(master, width=canvas_width, height=canvas_height)
image = Image.new("RGB", (200, 200), (255, 255, 255))
draw = ImageDraw.Draw(image)


def paint(event):
    python_black = "#000000"
    brush_size = 5
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    w.create_oval(x1, y1, x2, y2, fill=python_black)
    draw.ellipse((x1, y1, x2, y2), fill=python_black)


def save():
    filename = "data/custom_img.png"
    image.save(filename)
    global master
    master.withdraw()
    master.quit()


def clear():
    w.delete("all")
    global image
    image = Image.new("RGB", (200, 200), (255, 255, 255))
    global draw
    draw = ImageDraw.Draw(image)


def launch():
    master.deiconify()
    master.title("Draw your digit")
    master.wm_geometry("%dx%d+%d+%d" % (250, 270, 10, 10))
    w.pack(expand=YES, fill=BOTH)
    w.bind("<B1-Motion>", paint)
    done_button = Button(master, text="Done!", width=10, bg='white', command=save)
    done_button.place(x=canvas_width / 7, y=canvas_height + 20)
    clear_button = Button(master, text="Clear!", width=10, bg='white', command=clear)
    clear_button.place(x=(canvas_width / 7) + 80, y=canvas_height + 20)
    mainloop()
