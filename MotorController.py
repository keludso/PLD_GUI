from tkinter import *
from initialize_parmas import constants

class carousel_motor:
    def __init__(self, name, root, read, write,x,y, num, position):
        self.write = write
        self.read = read
        self.num = num
        self.position = position

        # Debug window 
        self.label_debugMot = Label(root, text="target", bg="#9CC0E0", font=('Times', 10))
        self.label_debugMot.place(x=1150,y=490)

        # Setting up Carousel Motors 
        self.label_CM1 = Label(root, text=name)
        self.label_CM1.place(x=x,y=y+30)
        self.startButton_CM1 = Button(
            root,
            text="Start Motor",
            bg="green", fg="white",
            command=lambda: self.command(1,0)
        )
        self.startButton_CM1.place(x=x+150, y=y+30)

        self.stopButton_CM1 = Button(
            root,
            text="Stop Motor",
            bg="red", fg="white",
            command=lambda: self.command(2,0)
        )
        self.stopButton_CM1.place(x=x+250, y=y+30)

        # Encoder Values 
        self.label_ENC= Label(root, text="0x00")
        self.label_ENC.place(x=x+350,y=y+30)


        for i in range(6):
            self.posButton = Button(
                root,
                text="Position " + str(i+1),
                command=lambda : self.command(3, i)
                )
            self.posButton.place(x=x+65*i, y=y+60)
        
    # sends the command to the MSP
    def command(self,proto_command, pos):
        if proto_command == 1:
            string = "C%dON\r\n" % (int(self.num))

        elif proto_command == 2:
            string  = "c%dOF\r\n" % (int(self.num))

        elif proto_command == 3:
            string  = "C%d%d\r\n" % (int(self.num), int(self.position[pos], 16))    


            # cheking if the position is reached
        #if not self.write(string.encode()):
        #    pass#print(string)# raise Exception("No serial port defined")

        ret = self.read(string.encode())
        returnString = (ret.decode().replace('\r','') if ret!=False else "00000")    
        self.label_debugMot.config(text=returnString, bg="white", fg="black",)   

    def command_encoder(self):
        string = "E%d\r\n" % (int(self.num))
            
            # cheking if the position is reached
        #if not self.write(string.encode()):
        #    pass#print(string)# raise Exception("No serial port defined")

        ret = self.read(string.encode())
        returnString = (ret.decode().replace('\r','') if ret!=False else "00000")    

        self.label_debugMot.config(text=returnString, bg="white", fg="black",)   
class target_motor:
    def __init__(self, name, root, read, write,x,y, num):
        self.write = write
        self.read = read
        self.num = num

        # Debug window 
        self.label_debugMot = Label(root, text="target", font=('Times', 10))
        self.label_debugMot.place(x=1150,y=470)

        # Setting up Carousel Motors 
        self.label_TM1 = Label(root, text=name , bg="#9CC0E0")
        self.label_TM1.place(x=x,y=y+30)
        self.startButton_TM1 = Button(
            root,
            text="Start Motor",
            bg="green", fg="white",
            command=lambda: self.command(1)
        )
        self.startButton_TM1.place(x=x+150, y=y+30)

        self.stopButton_TM1 = Button(
            root,
            text="Stop Motor",
            bg="red", fg="white",
            command=lambda: self.command(2)
        )
        self.stopButton_TM1.place(x=x+250, y=y+30)

        
    # sends the command to the MSP
    def command(self,proto_command):
        if proto_command == 1:
            string = "T%dON\r\n" % (int(self.num))

        elif proto_command == 2:
            string  = "T%dOF\r\n" % (int(self.num))

 
        #if not self.write(string.encode()):
        #    pass#print(string)# raise Exception("No serial port defined")


        ret = self.read(string.encode())
        returnString = (ret.decode().replace('\r','') if ret!=False else "00000")    

        self.label_debugMot.config(text=returnString, bg="white", fg="black",)

class heater_motor:
    def __init__(self, name, root, read, write,x,y):
        self.write = write
        self.read = read
        # Setting up Carousel Motors 
        self.label_htr = Label(root, text=name, bg="#9CC0E0")
        self.label_htr.place(x=x,y=y+30)

        # Debug window 
        self.label_debugMot = Label(root, text="heater", font=('Times', 10))
        self.label_debugMot.place(x=1150,y=450)


        self.startButton_TM1 = Button(
            root,
            text="Start Motor",
            bg="green", fg="white",
            command=lambda: self.command(1)
        )
        self.startButton_TM1.place(x=x+150, y=y+30)

        self.stopButton_TM1 = Button(
            root,
            text="Stop Motor",
            bg="red", fg="white",
            command=lambda: self.command(2)
        )
        self.stopButton_TM1.place(x=x+250, y=y+30)

        self.loadpos_button = Button(
            root,
            text="Load position",
            bg="blue", fg="white",
            command=lambda: self.command(2)
        )
        self.loadpos_button.place(x=x+350, y=y+30)

        self.rheedpos_button = Button(
            root,
            text="RHEED position",
            bg="purple", fg="white",
            command=lambda: self.command(2)
        )
        self.rheedpos_button.place(x=x+450, y=y+30)
        
    # sends the command to the MSP
    def command(self,proto_command):
        if proto_command == 1:
            string = "TON\r\n" 

        elif proto_command == 2:
            string  = "TOF\r\n"

 
        #if not self.write(string.encode()):
            #pass#print(string)# raise Exception("No serial port defined")

            
        #print("here")
        ret = self.read(string.encode())
        returnString = (ret.decode().replace('\r','') if ret!=False else "00000")    

        self.label_debugMot.config(text=returnString, bg="white", fg="black",)

class MotorController:
    def __init__(self, root, read, write):
        self.read = read
        self.write = write
        self.label = Label(root, text="Motor Controller", bg="#9CC0E0", font=('Times', 14))
        self.label.place(x=10,y=240)
        m_pos_y = 260
        m_pos_x = 30
        # Debug window 
        

        position_CM1 = ['0x0A', '0x0B', '0x10', '0x45', '0x22', '0x55']

        CM1 = carousel_motor("CAROUSEL MOTOR 1",root, read, write,m_pos_x,m_pos_y, 1, position_CM1)

        CM2 = carousel_motor("CAROUSEL MOTOR 2",root, read, write,m_pos_x,m_pos_y+70, 2, position_CM1)

        TM1 = target_motor("TARGET MOTOR 1",root, read, write,m_pos_x,m_pos_y+150, 1)

        TM2 = target_motor("TARGET MOTOR 2",root, read, write,m_pos_x,m_pos_y+200, 2)

        HM = heater_motor("HEATER ",root, read, write,m_pos_x,m_pos_y+240)

