# worker.py
from PySide2.QtCore import QThread, QObject, Signal, Slot
import time
import json, os, serial
from json.decoder import JSONDecodeError

class Worker(QObject):
    finished = Signal()
    intReady = Signal(int)
    

    @Slot()
    def procCounter(self): # A slot takes no params
        while True:
            try:
                arduino_port = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
                time.sleep(1)
                if arduino_port.isOpen():
                    while arduino_port.inWaiting() == 0: pass
                    if arduino_port.inWaiting() > 0:
                        write_json = open('datos.json', 'w')
                        for i in range(3):
                            line = arduino_port.readline().rstrip().decode('utf-8')
                            write_json.write(line)
                            print(line.strip())
                            # time.sleep(0.1)
                        write_json.close()

                        # READ JSON
                        filesize = os.path.getsize('datos.json')

                        if filesize == 0:

                            #self.intReady.emit(1500)
                            print("Empty file")

                        else:
                            with open("datos.json") as data_json:
                                obj_json = json.load(data_json)
                                data_json.close()

                            ppm = obj_json["ppm"]
                            

                            self.intReady.emit(ppm)
                            time.sleep(1)
                            
                        self.finished.emit()
                        
                else:
                    print("not found")

            except  serial.SerialException as e:
                print(e)

            except KeyboardInterrupt as e:
                print(e)







