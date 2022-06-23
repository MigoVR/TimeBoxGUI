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
    tpTable.setRowCount(3)
    tpTable.setColumnCount(1)
    tpTable.setHorizontalHeaderLabels(["Top Priorities"])
    
    tpTable.setGeometry(300, 50, 100, 100)
    tpTable.show()

    # Creating header labels for each portion of our time box
    topPriorities = QtWidgets.QLabel(win) # Text label. Parameters dictates where it will be exist  
    topPriorities.setText("Top Priorities")
    topPriorities.move(50,50) # Change position of the label

    brainDump = QtWidgets.QLabel(win)
    brainDump.setText("Brain Dump")
    brainDump.move(50,150)


    win.show() # Display the window
    sys.exit(app.exec_()) # When the window closes so will the program. 

window(); 
