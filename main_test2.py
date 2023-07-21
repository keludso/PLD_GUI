from tkinter import *
from SerialPortSelector import SerialPortSelector
from MotorController import MotorController
from Growth_cycle import Growth_cycle
from Kcell import kcell
from Status import Status_frame


window = Tk()
window.geometry('1250x850')
frame = Frame(window)

# Create a canvas widget
canvas1=Canvas(window, width=1200, height=850)
canvas1.place(x=5,y=0)
# Add a line in canvas widget
canvas1.create_line(5,220,750,220, fill="black", width=2)
canvas1.create_line(5,590,1250,590, fill="black", width=2)
canvas1.create_line(750,0,750,590, fill="black", width=2)

Status_info_frame = Label(window, text="Current Status", font=('Times', 14)).place(x=10,y=0)
Comm_frame = Label(window, text="Communication", font=('Times', 14)).place(x= 850,y=0)

# Initialize Communication ports 
motorPortSelector = SerialPortSelector(window,"Motor",850,50,115200)
equipmentPortSelector = SerialPortSelector(window,"Equipment",1000,50,9600,ending=b'\r') # the gauge only uses CR at the end of messages, so set ending to CR

# Setting the Status Frame
status_frame = Status_frame(window, 10,35, motorPortSelector.readCommand, motorPortSelector.write, equipmentPortSelector.readCommand, equipmentPortSelector.write)

# Setting up the Controller

motor_controller = MotorController(window,motorPortSelector.readCommand, motorPortSelector.write)

# Initializing Kcells

Kcell = kcell('COM1',9600) # initializing kcell

# Pressure Guage 



# Growth Parameter

growth_table = Growth_cycle(window, motorPortSelector.readCommand, motorPortSelector.write, Kcell.read_temperature, Kcell.set_temperature)


window.mainloop()


