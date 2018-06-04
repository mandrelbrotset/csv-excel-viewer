import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class main(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        self.setupUi(self)
        

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = main()         # create an instance of main
    sys.exit(app.exec())        # stops the script on exiting the gui
