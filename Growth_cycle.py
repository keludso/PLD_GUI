from tkinter import *



class table_col:
    def __init__(self,root,name,x,y,min,max):
        # Setting up Kcell 
        self.label_Kcell = Label(root, text=name, bg="#9CD0E0",fg="black")
        self.label_Kcell.place(x=x,y=y)
        self.numSelector = Spinbox(root, from_=min, to_=max)
        self.numSelector.place(x=x,y=y+30)

        
class Growth_cycle:
    def __init__(self,root,read,write, kcell1_settemp, kcell2_settemp):
        self.root = root
        self.read = read
        self.write = write
        self.kcell_settemp = kcell1_settemp
        self.kcel2_settemp = kcell2_settemp
        self.label = Label(root, text="GROWTH TABLE", font=('Times', 14),bg="#9CD0E0",fg="black")
        self.label.place(x=10,y=600)


        self.time_sel = table_col(self.root,"Time (min)",50, 650,0,1000)
        self.Carousel1 = table_col(self.root,"Target 1",150, 650,0,6)
        self.Carousel2 = table_col(self.root,"Target 2",250, 650,0,6)
        self.substratetemp = table_col(self.root,"Substrate Temp",350, 650,50,1200)
        self.Kcell1 = table_col(self.root,"KCELL 1",450, 650,min = 30, max=300)
        self.Kcell2 = table_col(self.root,"KCELL 2",570, 650,min = 30, max=300)
        self.Kcell3 = table_col(self.root,"KCELL 3",690, 650,min = 30, max=300)

        

        self.startButton = Button(
            root,
            text="Start GROWTH",
            bg="green", fg="white",
            command=lambda: self.command(1)
        )
        self.startButton.place(x=450, y=600)

        self.stopButton = Button(
            root,
            text="STOP",
            bg="red", fg="white",
            command=lambda: self.command(1)
        )
        self.stopButton.place(x=650, y=600)

        self.setButton = Button(
            root,
            text="SET",
            bg="green", fg="white",
            command=lambda: self.command(3)
        )
        self.setButton.place(x=950, y=660)


    def command(self,proto_command):

        # First Set position of the targets 

        string = "C1"


        if proto_command == 1:
            string = "T%dON\r\n" % (int(self.num))

        elif proto_command == 2:
            string  = "T%dOF\r\n" % (int(self.num))

        elif proto_command ==3:
            for i in range(7):
                self.label_time = Label(self.root, text=(str(self.time_sel.numSelector.get())), bg="#9CD0E0",fg="black")
                self.label_time.place(x=50,y=700)    

                self.label_car1 = Label(self.root, text=(str(self.Carousel1.numSelector.get())), bg="#9CD0E0",fg="black")
                self.label_car1.place(x=150,y=700)  

                self.label_car2 = Label(self.root, text=(str(self.Carousel2.numSelector.get())), bg="#9CD0E0",fg="black")
                self.label_car2.place(x=250,y=700)  

                self.label_subst_temp = Label(self.root, text=(str(self.substratetemp.numSelector.get())), bg="#9CD0E0",fg="black")
                self.label_subst_temp.place(x=350,y=700) 
 
        if not self.write(string.encode()):
            pass#print(string)# raise Exception("No serial port defined")

