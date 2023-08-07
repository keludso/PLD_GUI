from tkinter import *
from PIL import ImageTk, Image
import os




window = Tk()
window.geometry('1250x850')
frame = Frame(window)

canvas=Canvas(window, width=1250, height=850)
canvas.place(x=5,y=0)
canvas.create_rectangle(0, 0, 400, 400, fill='red')
# The image 

img = Image.open(r'Z:\d\dvashae\share1\Group Activity\PLD\Control_system\GUI\test2\PLD_image.PNG')
image1 = img.resize((270, 270))

pld_image = ImageTk.PhotoImage(image1)

label_image = Label(window,image=pld_image)
label_image.place(x= 850, y=220)



window.mainloop()