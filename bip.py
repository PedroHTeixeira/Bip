import serial
import time
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


class Monitor():
    def __init__(self):
        self.pulse = [500]
        self.counter = [0]
        self.DEVICE='/dev/ttyACM0'
        self.BAUD_RATE='9600'
        self.bpm = []
        

    def animate(self,i):
        plt.cla()
        plt.plot(self.counter,self.pulse)

    def InfoComSerial(self):
        
        temp_data = []
        o=0
        nmbr = '0'
        print('\nObtendo informacoes sobre a comunicacao serial\n')
        # Iniciando conexao serial
        #comport = serial.Serial(DEVICE, 9600, timeout=1)
        comport = serial.Serial(self.DEVICE,int(self.BAUD_RATE))
        time.sleep(1.8) # Entre 1.5s a 2s
        print('\nStatus Porta: %s ' % (comport.isOpen()))
        print('Device conectado: %s ' % (comport.name))
        print('\n###############################################\n')
        
        while comport.isOpen():
            if comport.inWaiting():
                data = comport.readline()
                console_output=str(data.decode('utf-8')).strip('\r\n')
                if len(console_output) != 0:
                    if console_output[0] == '%':
                        console_output = list(console_output)
                        console_output.pop(0)
                        console_output.pop(-1)
                        console_output = "".join(console_output)
                        num = unicode(console_output,'utf-8').isnumeric()
                        if num:
                            self.bpm.append(int(console_output))
                    else:
                        num = unicode(console_output,'utf-8').isnumeric()
                        if num :
                            self.pulse.append(int(console_output))
                            o+=1
                            self.counter.append(o)
                    print(self.pulse)
                    plt.pause(1)
                    plt.draw()
                
            

if __name__ == '__main__':
    plotter = Monitor()
    ani = FuncAnimation(plt.gcf(),plotter.animate,interval=1)
    plt.show(block=False)
    plotter.InfoComSerial()
    