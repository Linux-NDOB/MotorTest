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