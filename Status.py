from tkinter import *
import tkinter as tk
import time


class Status_frame:
    def __init__(self,root, x,y, read, write, pressure_read, pressure_write):
        self.read = read
        self.write=write
        self.root = root
        self.pressread = pressure_read
        self.presswrite= pressure_read
        # Laser
        self.label_las = Label(root, text="LASER")
        self.label_las.place(x=x,y=y)
        self.Laser_stat_opt =["ACTIVE", "INACTIVE"]
        self.laser_stat = Label(root, text=self.Laser_stat_opt[0],fg="white", bg="red")
        self.laser_stat.place(x=x+50,y=y)

        # Pressure
        self.label_press = Label(root, text="CHAMBER PRESSURE",  font=('Times', 16))
        self.label_press.place(x=x+420,y=y)
        self.press_stat = Label(root, text="1.6e-6",fg="black", bg="yellow", font=('Times', 16))
        self.press_stat.place(x=x+460,y=y+50)
        
        # CAROUSEL1
        self.label_car1 = Label(root, text="CAROUSEL 1")
        self.label_car1.place(x=x,y=y+30)
        self.car1_opt =["POSITION 1", "POSITION 2", "POSITION 3", "POSITION 4", "POSITION 5", "POSITION 6"]
        self.car1_stat = Label(root, text=self.car1_opt[0],fg="white", bg="red")
        self.car1_stat.place(x=x+75,y=y+30)

        # CAROUSEL 2    
        self.label_car2 = Label(root, text="CAROUSEL 2")
        self.label_car2.place(x=x+200,y=y+30)
        self.car1_stat = Label(root, text=self.car1_opt[0],fg="white", bg="red")
        self.car1_stat.place(x=x+275,y=y+30)
        
        # TARGET 1
        self.label_tar1 = Label(root, text="TARGET 1")
        self.label_tar1.place(x=x,y=y+60)
        self.tar1_opt =["ACTIVE", "INACTIVE"]
        self.tar1_stat = Label(root, text=self.tar1_opt[0],fg="white", bg="red")
        self.tar1_stat.place(x=x+75,y=y+60)

        # TARGET 2    
        self.label_tar2 = Label(root, text="TARGET 2")
        self.label_tar2.place(x=x+200, y=y+60)
        self.tar2_stat = Label(root, text=self.tar1_opt[0],fg="white", bg="red")
        self.tar2_stat.place(x=x+275,y=y+60)
        
        # Heater    
        self.label_hm = Label(root, text="Heater Motor")
        self.tar1_opt =["ACTIVE", "INACTIVE"]
        self.label_hm.place(x=x, y=y+90)
        self.HM_stat = Label(root, text=self.tar1_opt[0],fg="white", bg="red")
        self.HM_stat.place(x=x+100,y=y+90)

        self.label_ST = Label(root, text="Substrate Temperature")
        self.label_ST.place(x=x+200, y=y+90)
        self.ST_stat = Label(root, text="50",fg="black", bg="green")
        self.ST_stat.place(x=x+350,y=y+90)


        self.root.after(5000, self.update_parameters)
        self.root.after(8000, self.Pressure_Guage)

# This is refreshed whenever the program runs 
# 

    def Pressure_Guage(self):
      string  = "?GA2\r"    
      #print("here")
      ret = self.pressread(string.encode())
      returnString = (ret.decode().replace('\r','') if ret!=False else "00000")
      self.press_stat.config(text = returnString)
      print(returnString) 
      self.root.after(8000, self.Pressure_Guage)

      
#   
# 
    def status_command(self):
        string  = "SR\r\n"    
        ret = self.read(string.encode())
        returnString = (ret.decode().replace('\r','').replace('\n','') if ret!=False else "nothing because serial port is not connected yet")
        
        return returnString


    def update_parameters(self):

        #status_param = self.status_command()
        string  = "SR\r\n"    
        ret = self.read(string.encode())
        returnString = (ret.decode('ISO-8859-1').replace('\r','').replace('\n','') if ret!=False else "EEE")

        # Status Frame 
        status = returnString[0]
        # Encoder value 1
        encoder_val1 = returnString[1]
        # Encoder value 2
        encoder_val2 = returnString[2] 

        
        print("update_status")
        res = ''.join(format(ord(i), '08b') for i in status)  

        
        if (res[0] == '1'):
           self.tar1_stat.config(text=self.tar1_opt[1],fg="white", bg="red")
        else:
           self.tar1_stat.config(text=self.tar1_opt[0],fg="white", bg="red")     

        if (res[1] == '1'):
           self.tar2_stat.config(text=self.tar1_opt[1],fg="white", bg="red")
        else:
           self.tar2_stat.config(text=self.tar1_opt[0],fg="white", bg="red")     

        if (res[2] == '1'):
           self.car1_stat.config(text=self.tar1_opt[1],fg="white", bg="red")
        else:
           self.tar2_stat.config(text=self.tar1_opt[0],fg="white", bg="red")   


        self.root.after(5000, self.update_parameters)   



