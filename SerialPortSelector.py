from tkinter import *
import tkinter as tk
from serial_comms import serial_ports
import serial
import time 


class SerialPortSelector:
    def __init__(self,root,name,x,y,baud,ending = b'\r\n',logger = None):
        self.frame = Frame(root)
        self.frame.place(x=x,y=y)
        self.port = None
        self.portClicked = StringVar();
        self.label = Label(self.frame, text="")
        self.portButton = None
        self.baud = baud
        self.portOptions = serial_ports()
        self.portClicked.set(self.portOptions[0])
        self.drop = OptionMenu(self.frame, self.portClicked, *self.portOptions)
        self.drop.pack(side = TOP)
        self.portButton = Button(self.frame, text=f"Select {name} Serial Port", command = self.callback).pack(side=BOTTOM)
        self.label.place(x=x-10,y=y+30)
        self.inUse = False;
        self.ending = ending

    def updatePorts(self):
        self.label.config(text = "")

        self.portOptions = serial_ports()
        self.portClicked.set(self.portOptions[0])
        self.drop['menu'].delete(0, 'end')
        for choice in self.portOptions:
            self.drop['menu'].add_command(label=choice,command = tk._setit(self.portClicked,choice))

    # this is called whenever the select button is clicked
    def callback(self):
        selected_port = self.portClicked.get()
        if self.port != None and self.port.port == selected_port:
            return
        try:
            self.port = serial.Serial(selected_port, baudrate=self.baud, stopbits=1, timeout = 1.0)
        except PermissionError:
            print("Port already opened")
            pass
        except Exception as e:
            self.port = None

        # for i in self.controllers:
        #     i.ser = self.port
        self.label.config(
            text=("Selected COM Port: " + selected_port)
            if self.port != None
            else 'Error connecting to port: "%s"' % selected_port
        )


    def getSer(self):
        if self.inUse:return -1
        self.inUse = True
        return self.port
    
    def close(self): self.port.close()

    def releaseSer(self):
        self.inUse = False

    def write(self,data):
        ser = self.getSer()
        while(ser==-1):
            print("waiting for serial port to become available")
            ser = self.getSer()
        if ser!=None:
            ser.write(data)
            self.releaseSer()
            return True
        else: 
            self.releaseSer()
            return False
        
    def readCommand(self,data):
        ser = self.getSer()
        ret = False
        
        while(ser==-1):
            print("waiting for serial port to become available")
            ser = self.getSer()
        if ser!=None:
            ser.write(data)
            ret = ser.read_until(self.ending)
            
        self.releaseSer()
        return ret
    
    # remove the port for refresh
    def removePort(self):
        if(self.port!=None):
            self.port.close()
            self.port = None