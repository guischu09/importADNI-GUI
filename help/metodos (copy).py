def openFileNameDialog(self):    
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options = options)
    if fileName:
        print(fileName)

def saveFileDialog(self):    
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getSaveFileName(None, "QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
    if fileName:
        print(fileName)

# Proper way to deal with system when one close main window
def closeEvent(self):
    #Your desired functionality here
    print('Close button pressed')
    import sys
    sys.exit(0)

# Definir funções aqui
def mainFunctions(self):
    self.openFileButton.clicked.connect(self.openFileNameDialog)

# Para abrir outra janela:
# Gerar um outro .ui, converter para .py
# copiar a classe e colar no programa principal
# dentro da classe da janela principal, criar a seguinte função
# essas funções foram copiadas do final do arquivo gerado em .py (da janela secundaria)
def openWindow(self):
    self.window = QtWidgets.QDialog()
    self.ui = Ui_Dialog()
    self.ui.setupUi(self.window)
    self.window.show()

# Dentro de setupUI adicionar:
app.aboutToQuit.connect(self.closeEvent)
self.mainFunctions()

# No final, usar isso para abrir quando der Kernel Died
app = QCoreApplication.instance()
if app is None:
    app = QtWidgets.QApplication(sys.argv)

# Import liss
from PyQt5 import QtCore, QtWidgets
import sys
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QCoreApplication