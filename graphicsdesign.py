# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphicsdesign.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class ImageS(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 600)
        Form.setAutoFillBackground(True)
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        #self.label.setGeometry(QtCore.QRect(150, 10, 350, 500))
        #self.label.setPixmap(QtGui.QPixmap("../Design/designn/amazing-astronomy-background-bright-544268.jpg"))
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")        
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        
        self.label1 = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 10, 500,100))


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def img(self,name):
        #self.label.setPixmap(QtGui.QPixmap("../Design/designn/amazing-astronomy-background-bright-544268.jpg"))
        #self.label.setPixmap(QtGui.QPixmap(str(name)))

        image = QtGui.QPixmap(str(name))
            
        if image.width() > 900 or image.height() > 600:
            image = image.scaled(900,600, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        #w=image.width()
        #h=image.height()
        #print("Img Width : ",w)
        #print("Img Height : ",h)
        
        self.label.setGeometry(QtCore.QRect(50, 10,900,600))
            
        self.label.setPixmap(image)
        self.label1.setText(str(name))


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Image Viewer"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = ImageS()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
