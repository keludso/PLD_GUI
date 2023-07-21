from tkinter import *



class table_col:
    def __init__(self,root,name,x,y,min,max):
        # Setting up Kcell 
        self.label_Kcell = Label(root, text=name)
        self.label_Kcell.place(x=x,y=y)
        self.numSelector = Spinbox(root, from_=min, to_=max, wrap =True)
        self.numSelector.place(x=x,y=y+30)

        




class Growth_cycle:
    def __init__(self,root,read,write, kcell_readtemp, kcell_settemp):
        self.root = root
        self.read = read
        self.write = write
        self.kcell_readtemp = kcell_readtemp
        self.kcell_settemp = kcell_settemp
        self.label = Label(root, text="GROWTH TABLE", font=('Times', 14))
        self.label.place(x=10,y=600)


        time_sel = table_col(self.root,"Time (min)",50, 650,0,1000)
        Carousel1 = table_col(self.root,"Target 1",150, 650,0,6)
        Carousel2 = table_col(self.root,"Target 2",250, 650,0,6)
        substratetemp = table_col(self.root,"Substrate Temp",350, 650,50,1200)
        Kcell1 = table_col(self.root,"KCELL 1",450, 650,min = 30, max=300)
        Kcell2 = table_col(self.root,"KCELL 2",550, 650,min = 30, max=300)
        Kcell3 = table_col(self.root,"KCELL 3",650, 650,min = 30, max=300)

        

        self.startButton = Button(
            root,
            text="Start GROWTH",
            bg="green", fg="white",
            command=lambda: self.command(1)
        )
        self.startButton.place(x=950, y=650)

        self.stopButton = Button(
            root,
            text="STOP",
            bg="red", fg="white",
            command=lambda: self.command(1)
        )
        self.stopButton.place(x=1050, y=650)



    def command(self,proto_command):

        # First Set position of the targets 

        string = "C1"


        if proto_command == 1:
            string = "T%dON\r\n" % (int(self.num))

        elif proto_command == 2:
            string  = "T%dOF\r\n" % (int(self.num))

 
        if not self.write(string.encode()):
            pass#print(string)# raise Exception("No serial port defined")

