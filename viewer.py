import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import mainWindow, defaultWidget
import pandas as pd

class main(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        self.setupUi(self)

        self.default_widget = QtWidgets.QWidget(self)
        self.default_widget.setGeometry(0, 20, 789, 557)
        self.defaultView = defaultWidget.Ui_Form()
        self.defaultView.setupUi(self.default_widget)

        self.button = self.defaultView.openFileButton
        self.button.clicked.connect(self.openFile)
        self.actionOpen.triggered.connect(self.openFile)

        self.centralwidget.setHidden(True)
        self.default_widget.setVisible(True)

        self.show()

        x = self.default_widget.palette()
        x.setColor(self.default_widget.backgroundRole(), QtCore.Qt.green)
        self.default_widget.setAutoFillBackground(True)
        self.default_widget.setPalette(x)

        # y = self.centralwidget.palette()
        # y.setColor(self.centralwidget.backgroundRole(), QtCore.Qt.red)
        # self.centralwidget.setAutoFillBackground(True)
        # self.centralwidget.setPalette(y)

    def openFile(self):
        supportedFileTypes = "excel files (*.xls*);;csv files (*.csv)"
        name, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "",supportedFileTypes)
        print(fileType)
        if fileType == "excel files (*.xls*)":
            print("type is excel")
            self.f = pd.read_excel(name)
        elif fileType == "csv files (*.csv)":
            print("type is csv")
            self.f = pd.read_csv(name)

        if len(name) > 0:
            self.default_widget.setHidden(True)
            self.centralwidget.setVisible(True)
            self.setupTable()

    def setupTable(self):
        self.header = list(self.f.dtypes.index)
        
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)

        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Name"))
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Email"))

        self.centralwidget.setVisible(True)
        self.default_widget.setHidden(True)

        self.show()
        
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = main()         # create an instance of main
    sys.exit(app.exec())        # stops the script on exiting the gui
