import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                            QTableWidget, QTableWidgetItem)


def window(): 
    app = QApplication(sys.argv) # Starts application 
    win = QMainWindow() 
    win.setGeometry(100, 100, 500, 800) # Define the size of the window. 
    win.setWindowTitle("Time Box")

    tpTable = QTableWidget(win) 
    tpTable.setRowCount(7)
    tpTable.setColumnCount(1)
    tpTable.setHorizontalHeaderLabels(["Top Priorities"])
    tpTable.setGeometry(25, 25, 200, 300)
    tpTable.show()

    bdTable = QTableWidget(win) 
    bdTable.setRowCount(10)
    bdTable.setColumnCount(1)
    bdTable.setHorizontalHeaderLabels(["Brain Dump"])
    bdTable.setGeometry(25, 350, 200, 300)
    bdTable.show()


    win.show() # Display the window
    sys.exit(app.exec_()) # When the window closes so will the program. 

window(); 
