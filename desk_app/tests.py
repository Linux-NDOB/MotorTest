#from django.test import TestCase

# Create your tests here.
from datetime import date

print(str(date.today()))

if (self.ppmv >= 1500):
    self.ui.resultado.setText("NEGATIVO");
    self.resultado = "No puede rodar"
elif (self.ppmv < 1500):
    self.ui.resultado.setText("POSITIVO");
    self.resultado = "Si puede rodar"

    # 1 - create Worker and Thread inside the Form
    self.obj = modulo.Worker()  # no parent!
    self.thread = PySide2.QtCore.QThread()  # no parent!

    # 2 - Connect Worker`s Signals to Form method slots to post data.
    self.obj.intReady.connect(self.intReady)

    # 3 - Move the Worker object to the Thread object
    self.obj.moveToThread(self.thread)

    # 4 - Connect Worker Signals to the Thread slots
    self.obj.finished.connect(self.thread.quit)

    # 5 - Connect Thread started signal to Worker operational slot method

    self.thread.started.connect(self.obj.procCounter)

    # * - Thread finished signal will close the app if you want!
    # self.thread.finished.connect(app.exit)

    # 6 - Start the thread
    # self.thread.start()

    # self.onIntReady(self)

    while i :
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

                        # self.intReady.emit(1500)
                        print("Empty file")

                    else:
                        with open("datos.json") as data_json:
                            obj_json = json.load(data_json)
                            data_json.close()

                        ppm = obj_json["ppm"]

                        self.ppmv = ppm
                        # Imported from worker vars
                        # self.ui.ppm.rpb_textValue = str(1000)
                        self.ui.ppm.setText(str(1000))

                        if (self.ppmv < 30000):
                            print(self.ppmv)
                            self.ui.resultado.setText("Inf al 3%");
                            self.resultado = "Menor al 3%"

                        self.ppmv = int(self.ui.ppm.text())

                        if (int(self.ppmv) > 30000):
                            print(self.ppmv)
                            self.ui.resultado.setText("Sup al 3%");
                            self.resultado = "Mayor al 3%"


            else:
                print("not found")

        except  serial.SerialException as e:
            print(e)

        except KeyboardInterrupt as e:
            print(e)