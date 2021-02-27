import serial
import time
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import Tkinter


class Monitor():
    def __init__(self):
        self.pulse = [-1]
        self.counter = [0]
        self.DEVICE='/dev/ttyACM0'
        self.BAUD_RATE='9600'
        self.bpm = [56]
        self.comport = serial.Serial(self.DEVICE,int(self.BAUD_RATE))
        self.o =0

    def animate(self,i):
        self.InfoComSerial()
        plt.cla()
        plt.plot(self.counter,self.pulse)

    def startup(self):
        print('\nObtendo informacoes sobre a comunicacao serial\n')
        # Iniciando conexao serial
        #comport = serial.Serial(DEVICE, 9600, timeout=1)
        time.sleep(1.8) # Entre 1.5s a 2s
        print('\nStatus Porta: %s ' % (self.comport.isOpen()))
        print('Device conectado: %s ' % (self.comport.name))
        print('\n###############################################\n')

    def InfoComSerial(self):
        if self.comport.inWaiting():
            data = self.comport.readline()
            try:
                console_output=str(data.decode('utf-8')).strip('\r\n')
                if len(console_output) != 0:
                    if console_output[0] == '%':
                        console_output = list(console_output)
                        console_output.pop(0)
                        console_output.pop(-1)
                        console_output = "".join(console_output)
                        num = unicode(console_output,'utf-8').isnumeric()
                        if num:
                            if int(console_output) !=0 :
                                self.bpm.append(int(console_output))
                    else:
                        num = unicode(console_output,'utf-8').isnumeric()
                        if num :
                            self.pulse.append(int(console_output))
                            self.o+=1
                            self.counter.append(self.o)
                            if len(self.counter)>125:
                                self.counter.pop(0)
                                self.pulse.pop(0)
                    print("Seu BPM e:{}".format(self.bpm[-1]))
                    media = 0
                    if len(self.bpm)>125:
                        self.bpm.pop(0)
                    for i in self.bpm:
                        media = media + i
                    media = media / len(self.bpm)
                    print("Seu BPM Medio e:{}".format(media))
            except:
                return

if __name__ == '__main__':
    plotter = Monitor()
    ani = FuncAnimation(plt.gcf(),plotter.animate,interval=1)
    plt.show()
    