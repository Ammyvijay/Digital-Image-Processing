# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Img_Viewer.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Formm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(671, 461)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        Form.setFont(font)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 671, 461))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 10, 631, 391))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 631, 391))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap(str(self.img[0])))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(150, 420, 141, 31))        
        
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.previous)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 420, 141, 31))
        
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.next)

        self.img=[]

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Previous"))
        self.pushButton_2.setText(_translate("Form", "Next"))

    def imglist(self,imglist):
        #print(imglist)
        self.img=imglist
        self.k=0
        #self.label.setPixmap(QtGui.QPixmap(str(self.img[0])))
        image = QtGui.QPixmap(str(self.img[0]))
                   
        if image.width() > 640 or image.height() > 480:
            image = image.scaled(631, 391, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            print(str(image.width())+" Width ")
            print(str(image.height())+" Height ")

        self.label.setPixmap(image)


    def next(self):
        #print("Note  : "+str(self.k))
        if(self.k<len(self.img)-1):
            self.k=self.k+1
            
            image = QtGui.QPixmap(str(self.img[self.k]))
            
            if image.width() > 640 or image.height() > 480:
                image = image.scaled(631, 391, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                print(str(image.width())+" Width ")
                print(str(image.height())+" Height ")

            self.label.setPixmap(image)

            self.anim = QtCore.QPropertyAnimation(self.label, b"geometry")
            self.anim.setDuration(200)
            self.anim.setStartValue(QtCore.QRect(650, 0, 640, 480))
            self.anim.setEndValue(QtCore.QRect(0, 0, 640, 480))
            self.anim.start(QtCore.QAbstractAnimation.DeleteWhenStopped)
                            

    def previous(self,k):
        #print("Note  : "+str(self.k))
        if(self.k>0):            
            self.k=self.k-1
            
            image = QtGui.QPixmap(str(self.img[self.k]))
            
            if image.width() > 631 or image.height() > 391:
                image = image.scaled(631, 391, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                print(str(image.width())+" Width ")
                print(str(image.height())+" Height ")

            self.label.setPixmap(image)

            self.anim = QtCore.QPropertyAnimation(self.label, b"geometry")
            self.anim.setDuration(200)
            self.anim.setStartValue(QtCore.QRect(650, 0, 640, 480))
            self.anim.setEndValue(QtCore.QRect(0, 0, 640, 480))
            self.anim.start(QtCore.QAbstractAnimation.DeleteWhenStopped)
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Formm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
