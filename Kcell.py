import minimalmodbus
from tkinter import *
import tkinter as tk
import time

class kcell_block:
    def __init__(self,root,port,baudrate, text, address, x,y):
       self.root = root
       self.instrument = minimalmodbus.Instrument(port, address)  # port name, slave address (in decimal) 
       self.instrument.serial.baudrate = baudrate 
       self.instrument.close_port_after_each_call = True

       self.label_ST = Label(root, text=text, bg="skyblue")
       self.label_ST.place(x=x, y=y)
       self.ST_stat = Label(root, text="50",fg="black", bg="green")
       self.ST_stat.place(x=x+70,y=150)
       
       self.root.after(10000, self.read_temperature,4096)
    
    
    def read_temperature(self,address):
        try:
            temperature = self.instrument.read_register(address, 1)  # Registernumber, number of decimals
            print(temperature)
            self.ST_stat.config(text=temperature)
            #return temperature
        except IOError:
            print("Failed to read from instrument")

        self.root.after(10000, self.read_temperature,4096)    

    def set_temperature(self, address, NEW_TEMPERATURE):
        try:
            self.instrument.write_register(address, NEW_TEMPERATURE, 1)  # Registernumber, value, number of decimals for storage
        except IOError:
            print("Failed to read from instrument")



class kcell:
    def __init__(self,root, port, baudrate):
        self.root = root
        self.port =port
        self.baudrate = baudrate

        self.kcell_1 = kcell_block(self.root, self.port, self.baudrate, "Kcell 1", 1,10,150)
        self.kcell_2 = kcell_block(self.root, self.port, self.baudrate, "Kcell 2", 2,150,150)