import minimalmodbus

class kcell:
    def __init__(self,port,baudrate):
       self.instrument = minimalmodbus.Instrument(port, 1)  # port name, slave address (in decimal) 
       self.instrument.serial.baudrate = baudrate 
       self.instrument.close_port_after_each_call = True
       
    
    
    def read_temperature(self,address):
        try:
            temperature = self.instrument.read_register(address, 1)  # Registernumber, number of decimals
            return temperature
        except IOError:
            print("Failed to read from instrument")

    def set_temperature(self, address, NEW_TEMPERATURE):
        try:
            self.instrument.write_register(address, NEW_TEMPERATURE, 1)  # Registernumber, value, number of decimals for storage
        except IOError:
            print("Failed to read from instrument")
 