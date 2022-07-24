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