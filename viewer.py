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
        self.centralwidget.event()

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 641, 391))
        self.tableWidget.setHidden(True)

        self.show()

        print(self.centralwidget.size())

    def refresh(self):
        print("size changed!")
        print(self.centralwidget.size())

    def openFile(self):
        # declare accepted file types
        supportedFileTypes = "csv files (*.csv);;excel files (*.xls*)"

        name, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", supportedFileTypes)
        # if the file is an excel file, use an excel parser
        if fileType == "excel files (*.xls*)":
            #debug print("type is excel")
            self.f = pd.read_excel(name)
        # if the file is an csv file, use a csv parser
        elif fileType == "csv files (*.csv)":
            #debug print("type is csv")
            self.f = pd.read_csv(name)
        # open the file if a file was selected
        if len(name) > 0:
            # hide the "Open file" button
            self.openFileButton.setHidden(True)
            # call method to render the file
            self.setupTable()

    def setupTable(self):
        # get the header of the table in the selected file
        self.header = list(self.f.dtypes.index)

        self.tableWidget.setGeometry(QtCore.QRect(2, 2, 1000, 600))
        # set the number of rows in the table to the number of rows in the file
        self.tableWidget.setRowCount(self.f.shape[0])
        # set the number of columns to the number of columns in the file
        self.tableWidget.setColumnCount(self.f.shape[1])
        self.tableWidget.setObjectName("tableWidget")
        self.vBoxLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.vBoxLayout.addWidget(self.tableWidget)
        self.setLayout(self.vBoxLayout)

        # set horizontal headers to the header of the table in the file
        self.tableWidget.setHorizontalHeaderLabels(self.header)
        # hide the row numbers
        self.tableWidget.verticalHeader().setHidden(True)

        col = 0
        for index, row in self.f.iterrows():
            for j, column in row.iteritems():
                self.tableWidget.setItem(index, col, QtWidgets.QTableWidgetItem(str(column)))
                col += 1
            col = 0

        # show the widget with the table
        self.tableWidget.setVisible(True)
        
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = main()         # create an instance of main
    sys.exit(app.exec())        # stops the script on exiting the gui
