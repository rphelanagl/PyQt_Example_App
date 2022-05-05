import pandas as pd
import sys
import datetime as dt
from py_SAPHANA_GetIntervalData5minMapMethod import py_SAPHANA_GetIntervalData5minMapMethod

#Import the pyqt-specific libraries
from PyQt5 import uic, QtWidgets, QtGui, QtCore

#7001351477

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.app = None
        self.init_ui()
        
    def init_ui(self):
        """Import the QtDesigner ui file, show it, and assign functions to the UI's buttons
        """
        print("Loading my ui file...")
        self.app = uic.loadUi('applicationinterface.ui')
        self.app.show()

        print("Linking functions to ui interface objects...")
        self.app.getIntervalDataButton.clicked.connect(self.getIntervalData)

    
    def getIntervalData(self):
        """Runs when the "Get Interval Data" button is clicked. Uses the inputs to acquire the data from SAP HANA
        """
        #Convert the start and end time input fields into datetime objects
        start_date = dt.datetime.strptime(self.app.startDateField.text(), '%d/%m/%Y')
        end_date = dt.datetime.strptime(self.app.endDateField.text(), '%d/%m/%Y')
        NMI_LIST = []
        NMI_LIST.append(self.app.inputNMI.text())
        print(NMI_LIST)
        #Get all state's RRP's, Get E Q B K\n",
        print("Retrieving data from HANA, please wait...")
        data = py_SAPHANA_GetIntervalData5minMapMethod(NMI_LIST, start_date, end_date, rrp=True, rrp_states=['ALL'], suffixes=False, suffix_list=[])
        print("Data received. Exporting to Excel...")
        self.exportToExcel(data)
        print("Done")

    def exportToExcel(self,data):
        """Exports the inputted dataframe to an Excel spreadsheet (default is Temp C drive)
        """
        #Convert the start and end time input fields into datetime objects
        start_date = dt.datetime.strptime(self.app.startDateField.text(), '%d/%m/%Y')
        end_date = dt.datetime.strptime(self.app.endDateField.text(), '%d/%m/%Y')
        startdatestring = start_date.strftime('%d.%m.%y')
        enddatestring = end_date.strftime('%d.%m.%y')
        filename = "5min_IntervalData" + "_" + self.app.inputNMI.text() + "_" + startdatestring + "_" + enddatestring + ".xlsx"
        filepath = "C:\\temp\\" + filename
        with pd.ExcelWriter(filepath) as writer:  
            data.to_excel(writer, engine="xlsxwriter", sheet_name='5minData')

# Code to get the app running
if __name__ == '__main__':
    print("Starting application please wait...")
    application = QtWidgets.QApplication(sys.argv)
    my_window = Window()
    print("Opening window...")
    sys.exit(application.exec())