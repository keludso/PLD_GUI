from tkinter import *
from SerialPortSelector import SerialPortSelector
from MotorController import MotorController
from Growth_cycle import Growth_cycle
from Kcell import kcell
from Status import Status_frame
from PIL import ImageTk, Image
import os


window = Tk()
window.geometry('1250x850')
#window.config(bg="skyblue")  # specify background color

frame = Frame(window)

# Create a canvas widget
canvas1=Canvas(window, width=1250, height=850)
canvas1.place(x=0,y=0)
canvas1.create_rectangle(2, 2, 700, 220, fill='skyblue')
canvas1.create_rectangle(2, 230, 700, 580, fill='#9CC0E0')
canvas1.create_rectangle(2, 590, 1240, 800, fill='#9CD0E0')
# Add a line in canvas widget


Status_info_frame = Label(window, text="Current Status", font=('Times', 14)).place(x=10,y=5)
Comm_frame = Label(window, text="Communication", font=('Times', 14)).place(x= 850,y=0)

# Initialize Communication ports 
motorPortSelector = SerialPortSelector(window,"Motor",850,50,115200)
equipmentPortSelector = SerialPortSelector(window,"Equipment",1000,50,9600,ending=b'\r') # the gauge only uses CR at the end of messages, so set ending to CR

# Setting the Status Frame
status_frame = Status_frame(window, 10,35, motorPortSelector.readCommand, motorPortSelector.write, equipmentPortSelector.readCommand, equipmentPortSelector.write)

# Setting up the Controller

motor_controller = MotorController(window,motorPortSelector.readCommand, motorPortSelector.write)

# Initializing Kcells

Kcell = kcell(window,'COM5',9600) # initializing kcell
# Pressure Guage 

# Growth Parameter

growth_table = Growth_cycle(window, motorPortSelector.readCommand, motorPortSelector.write, Kcell.kcell_1.set_temperature, Kcell.kcell_2.set_temperature)

# The image 
img = Image.open(r'Z:\d\dvashae\share1\Group Activity\PLD\Control_system\GUI\test2\PLD_image.PNG')
image1 = img.resize((350, 350))

pld_image = ImageTk.PhotoImage(image1)

label_image = Label(window,image=pld_image)
label_image.place(x= 750, y=170)
window.mainloop()


