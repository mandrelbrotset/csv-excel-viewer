import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import mainWindow
import pandas as pd

class main(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        self.setupUi(self)

        self.openFileButton.clicked.connect(self.openFile)
        self.actionOpen.triggered.connect(self.openFile)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 641, 391))
        self.tableWidget.setHidden(True)

        self.show()

    def openFile(self):
        supportedFileTypes = "csv files (*.csv);;excel files (*.xls*)"
        name, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "",supportedFileTypes)
        print(fileType)
        if fileType == "excel files (*.xls*)":
            print("type is excel")
            self.f = pd.read_excel(name)
        elif fileType == "csv files (*.csv)":
            print("type is csv")
            self.f = pd.read_csv(name)

        if len(name) > 0:
            self.openFileButton.setHidden(True)
            self.setupTable()

    def setupTable(self):
        self.header = list(self.f.dtypes.index)

        self.tableWidget.setGeometry(QtCore.QRect(2, 2, 1000, 600))
        self.tableWidget.setRowCount(self.f.shape[0])
        self.tableWidget.setColumnCount(self.f.shape[1])
        self.tableWidget.setObjectName("tableWidget")
        self.vBoxLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.vBoxLayout.addWidget(self.tableWidget)
        self.setLayout(self.vBoxLayout)

        self.tableWidget.setHorizontalHeaderLabels(self.header)

        col = 0
        for index, row in self.f.iterrows():
            for j, column in row.iteritems():
                self.tableWidget.setItem(index, col, QtWidgets.QTableWidgetItem(str(column)))
                col += 1
            col = 0

        self.openFileButton.setHidden(True)
        self.tableWidget.setVisible(True)
        
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = main()         # create an instance of main
    sys.exit(app.exec())        # stops the script on exiting the gui
