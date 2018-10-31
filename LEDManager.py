import serial


class LEDManager(object):
    def __init__(self):
        try:
            self.ser = serial.Serial('COM8', 9600)
        except:
            print("could not establish connection")

    def setLED(self, LED1, LED2, LED3):

        if self.ser is not None:
            #Turns the 3 args into a single byte
            c = LED1 + LED2*2 + LED3*4
            b = bytes([c])

            #Writes b to the COM port
            self.ser.write(b)
