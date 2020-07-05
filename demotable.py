# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableWidgetdemo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200,700)
        self.table = QtWidgets.QTableWidget(Form)
        
        self.table.setObjectName("tableWidget")        

        # ================== WIDGET  QTableWidget ==================
      
        #self.table = QTableWidget(self)

        # Disable editing
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Disable drag and drop behavior
        self.table.setDragDropOverwriteMode(False)

        # Select entire row
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # Select one row at a time
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        #Specifies where the ellipsis "..." should appear when displayed
        # texts that don't fit
        self.table.setTextElideMode(QtCore.Qt.ElideRight)# Qt.ElideNone

        # Set word wrapping for text
        self.table.setWordWrap(False)

        # Disable sorting
        self.table.setSortingEnabled(False)

        #Set the number of columns
        self.table.setColumnCount(9)

        # Set the number of rows
        self.table.setRowCount(0)

        # Aligning the header text
        self.table.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|
                                                          QtCore.Qt.AlignCenter)

        # Disable highlighting of header text when selecting a row
        self.table.horizontalHeader().setHighlightSections(False)

        # Hacer que la última sección visible del encabezado ocupa todo el espacio disponible
        self.table.horizontalHeader().setStretchLastSection(True)

        # Ocultar encabezado vertical
        self.table.verticalHeader().setVisible(False)

        # Dibujar el fondo usando colores alternados
        self.table.setAlternatingRowColors(True)

        # Establecer altura de las filas
        self.table.verticalHeader().setDefaultSectionSize(20)
        
        # self.table.verticalHeader().setHighlightSections(True)

        #nombreColumnas = ("Id", "First name", "Last name", "Sex", "Date of birth", "Country")
        nombreColumnas=("Patient ID","P Name","Age","Gender","Address","Mobile No","Email-Id","Reg. Date","Blood Group")

        # Set horizontal header tags using tags
        self.table.setHorizontalHeaderLabels(nombreColumnas)
        
        # Contextual menu
        self.table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #self.table.customContextMenuRequested.connect(self.menuContextual)
        
        # Set width of columns
        #for indice, ancho in enumerate((80, 120, 120, 110, 150), start=0):
        #    self.table.setColumnWidth(indice, ancho)

        self.table.resize(900, 240)
        self.table.move(20, 56)







        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(310, 380, 121, 23))
        self.pushButton.setObjectName("pushButton")

        connection=sqlite3.connect('bloismia.db')
        result=connection.execute("select * from patient_det")
        self.table.setRowCount(0)

        for row_num,row_data in enumerate(result):
            self.table.insertRow(row_num)
            for col_num,data in enumerate(row_data):
                self.table.setItem(row_num,col_num,QtWidgets.QTableWidgetItem(str(data)))
        
        connection.close()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Refresh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
