# Destrcutor will clear all images at the end
# View Image is successfully build
# Thumbnails Created for more memory handling
# Image Location Updated
# Logic Error Cleared
# Clear the Object Memory ...
# Clear Particular Item also delete sucessfully
# Clear None also build Successfully
# Clear All Button build successfully
# Unselect all then press processing None " Divide by Zero Error " Cleared...
# Progressbar issues fixed...
# Group box aligment set
# Button in Image places Successfully
# Custom checkbox all select main check box also selected and otherwise unselected
# Custom Checkbox select verification is working perfectly
# Database Image Successfully Added
# Tab Order Index Numbered
# Data Duplication and Replication Avoided
# Database Connection Successfully implemented
# Onclick Event Summarized
# Data Cleared Created
# Clickable Lable Created
# If Empty group Images the select all check box is disabled and then have only enabled
# Select all and Unselect all features added
# Filename morethan 21 character comes # symbol indicates changed
# Animation Added
# Features added add or append the images in a list
try:

    import sys
    import os
    import threading
    import sqlite3
    import cv2
    import time    
    import gc
        
    from datetime import datetime
    from pathlib import Path
    from PIL import Image
    from PyQt5 import QtCore, QtGui, QtWidgets,QtSql

    from graphicsdesign import ImageS
    from Img_Viewer import Ui_Formm
    from demotable import Ui_Form
    from imgprocess import imgpro
    from ImgGal import Widgetss

    class Ui_MainWindow(object):

        def __init__(self): 
            print('Patient Object created') 

        
        #======================================================================
        def openWindow(self):
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_Form()
            self.ui.setupUi(self.window)
            self.window.show()        

        def viewWindow(self,imglist):
            """
            self.viewwin=QtWidgets.QMainWindow()
            self.vui=Ui_Formm()
            self.vui.setupUi(self.viewwin)     
            self.vui.imglist(imglist)       
            self.viewwin.show()        
            """
            self.viewwin=QtWidgets.QMainWindow()
            self.vui=Widgetss()            
            self.vui.setupUi(self.viewwin,imglist)
            self.viewwin.show()

        def save(self):
            msg=QtWidgets.QMessageBox()
            
            no=self.lineEdit.text()
            name=self.lineEdit_2.text()
            age=self.lineEdit_3.text()
            gender=""
            if(self.radioButton.isChecked()==True):
                gender="Male"
            elif(self.radioButton_2.isChecked()==True):
                gender="Female"
            elif(self.radioButton_3.isChecked()==True):
                gender="Transgender"

            add=self.textEdit.toPlainText()
            ph=self.lineEdit_4.text()
            email=self.lineEdit_5.text()

        
            #====================================================================

            blod=self.comboBox.currentText()
            datee=self.dateEdit.text()
            if len(no)==0:
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle("Warning")
                msg.setText("Enter the Patient ID !") 
            elif len(name)==0:
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle("Warning")
                msg.setText("Enter the Patient Name !") 
            elif len(age)==0:
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle("Warning")
                msg.setText("Enter the Patient Age !") 
            elif (self.radioButton.isChecked()==False) and (self.radioButton_2.isChecked()==False) and (self.radioButton_3.isChecked()==False):
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle("Warning")
                msg.setText("Select the Gender Option !")
            elif len(add)==0:
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle("Warning")
                msg.setText("Enter the Patient Address !") 
            elif len(ph)==0:
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle("Warning")
                msg.setText("Enter the Patient Mobile No !") 
            elif len(email)==0:
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle("Warning")
                msg.setText("Enter the Email ID !")
            elif blod=="Select": 
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle("Warning")
                msg.setText("Select the Blood Group !")
            #elif self.photovar==0:
            #    msg.setIcon(QtWidgets.QMessageBox.Warning)
            #    msg.setWindowTitle("Warning")
            #    msg.setText("Attach a Patient Image !")

            else:
        
                #======================================================================
                try:
                    self.sqliteConnection = sqlite3.connect('bloismia.db')
                    cursor = self.sqliteConnection.cursor()
                    cursor.execute("SELECT * FROM patient_det WHERE pid=?", (no,))

                    rows = cursor.fetchmany()               
                    flagdb=0
                    for record in rows:
                        print("Data :   ",record[0])
                        flagdb=1
                                
                    #cursor.close()
                        
                    if(flagdb==0):
                        
                        #self.query.exec_("insert into patient_det values ("
                        #   "'"+no+"','"+name+"',"+age+",'"+gender+"','"+add+"','"+ph+"','"+email+"','"+datee+"','"+blod+"')")
                        
                        cursor.execute("""insert into patient_det values (?,?,?,?,?,?,?,?,?)""",(no,name,age,gender,add,ph,email,datee,blod))
                        self.imgsave(cursor,no)
                        
                        #im = open(str(self.imgpho),'rb').read()
                        #cursor.execute("""insert into pat_img values (?,?,?)""", (no,name,sqlite3.Binary(im)) )
                    

                        msg.setIcon(QtWidgets.QMessageBox.Information)
                        msg.setWindowTitle("Success")
                        msg.setText("Successfully Inserted Data and Images")
                        self.clearTI()
                            
                        #=========================== Clearing All Data =========================================
                        flagdb=0
                        
                        
                    else:
                        msg.setIcon(QtWidgets.QMessageBox.Warning)
                        msg.setWindowTitle("Warning")
                        msg.setText("Already Record Found ")

                except sqlite3.Error as e:
                    print("Error :",e)
                finally:
                    if (self.sqliteConnection):
                        #self.sqliteConnection.close()
                        print("The SQLite connection is closed")
                        self.sqliteConnection.commit()
                        #cursor.close()
                        #self.sqliteConnection.close()
                
                
                #----------------------------------------------------------------------
                
                
                #======================================================================

            
            msg.exec_()

        #=======================================================================

        def cleardata(self):

            msg=QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Did you want to Erase Data !!! \n Only Text Press 'Yes' else All Data & Image 'No'")
            msg.setWindowTitle("Alert")
            msg.setStandardButtons(QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
            msg.setDefaultButton(QtWidgets.QMessageBox.Yes)
            yes=msg.button(QtWidgets.QMessageBox.Yes)
            no=msg.button(QtWidgets.QMessageBox.No)            
            msg.exec_()

            
            if msg.clickedButton()==yes:
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.lineEdit_4.setText("")
                self.lineEdit_5.setText("")
                
                self.radioButton.setChecked(False)
                self.radioButton_2.setChecked(False)
                self.radioButton_3.setChecked(False)

                self.textEdit.setText("")
                self.dateEdit.setDate(QtCore.QDate.currentDate())
                self.comboBox.setCurrentIndex(0)

            elif msg.clickedButton()==no:

                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.lineEdit_4.setText("")
                self.lineEdit_5.setText("")
                
                self.radioButton.setChecked(False)
                self.radioButton_2.setChecked(False)
                self.radioButton_3.setChecked(False)

                self.textEdit.setText("")
                self.dateEdit.setDate(QtCore.QDate.currentDate())
                
                self.comboBox.setCurrentIndex(0)
                self.progressBar.setValue(0)
                self.clr=True
                self.Clearr()
                self.clr=False
                #self.labelphoto.setStyleSheet("""border-image : url(employee.png); background-repeat:no-repeat; 
                #background-color:#FFFFFF;
                #""")
                #self.photovar=0
                #self.imgpho=""

                print("All Data Cleared")

            


        #=======================================================================

        def imgsave(self,cursor,pid):
            
            number=0
            if(len(self.fileName)>0):
                for i in self.fileName :
                    with open(i,'rb') as f:
                        ImgData=f.read()
                        ImgId=pid+"---"+str(number)
                        #print(number)
                        
                        cursor.execute("""insert into Patient_Img (Patient_ID,Img_ID,Img_Name,Img_Data) values (?,?,?,?) """,(pid,ImgId,str(self.img_name[number]),ImgData))
                        
                        number=number+1
                        
                print("Ok---------- Image Connection ")
            
            else:
                print("No Images Uploaded from the Patient ")

        
        def clearTI(self):

            msg=QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Did you want to Erase All Data after saving ?")
            msg.setWindowTitle("Alert")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok|QtWidgets.QMessageBox.Cancel)
            msg.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            yes=msg.button(QtWidgets.QMessageBox.Ok)
            msg.exec_()

            if msg.clickedButton()==yes:
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.lineEdit_4.setText("")
                self.lineEdit_5.setText("")
                
                self.radioButton.setChecked(False)
                self.radioButton_2.setChecked(False)
                self.radioButton_3.setChecked(False)

                self.textEdit.setText("")
                self.dateEdit.setDate(QtCore.QDate.currentDate())
                #self.dateEdit.setDate(QtCore.QDate(2000,1,1))
                self.comboBox.setCurrentIndex(0) 
                
                self.progressBar.setValue(0)
                self.clr=True
                self.Clearr()
                self.clr=False
                #self.labelphoto.setStyleSheet("""border-image : url(employee.png); background-repeat:no-repeat; 
                #background-color:#FFFFFF;
                #""")
                #self.photovar=0
                #self.imgpho=""
                print("All Data Cleared")


            
            

        #=======================================================================

        def setupUi(self, MainWindow):
            #================================ Database =============================
            #------------------------------- File Dialog list --------------------------------------
            
            p = Path('ImgThumbnails/')
            p.mkdir(exist_ok=True)

            #self.cleartempimg()

            #q = Path('ResultImg/')
            #q.mkdir(exist_ok=True)
            
            self.fileName=[]
            self.img_name=[]  
            self.thumb=[]                                     
            #----------------------------------------------------------------------------------

            self.ma="""
                QMainWindow::separator {
                background-color: yellow;
                width: 10px; /* when vertical */
                height: 10px; /* when horizontal */
                }

                QMainWindow::separator:hover {
                background-color: red;
                }
            """

            MainWindow.setObjectName("MainWindow")
            MainWindow.setStyleSheet(self.ma)        
            MainWindow.setFixedSize(1000, 650)
            MainWindow.setWindowIcon(QtGui.QIcon('logo.png')) 
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            #====================================================================
            oImage = QtGui.QImage("E:/dip/rc/a7.jpg")
            sImage = oImage.scaled(QtCore.QSize(1300,650))                   # resize Image to widgets size
            palette = QtGui.QPalette()
            palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(sImage))                        
            #MainWindow.setPalette(palette)

            #=====================================================================
            paleta = QtGui.QPalette()
            paleta.setColor(QtGui.QPalette.Background, QtGui.QColor(135,206,235))
            MainWindow.setPalette(paleta)
            
            #---------------------------testing frame -------------------------

            self.fra1=""" 
                QFrame {            
                border-radius: 4px;                
                }
            
            """
                #background-image: url(images/welcome.png);
                #border: 2px solid green;
            #------------------------------------------------------------------

            fpaint = QtGui.QPalette()
            fpaint.setColor(QtGui.QPalette.Background, QtGui.QColor(135,200,205))

            self.frameleft = QtWidgets.QFrame(self.centralwidget)
            self.frameleft.setGeometry(QtCore.QRect(80, 60, 350, 550))
            self.frameleft.setAutoFillBackground(True)
            #self.frame.setStyleSheet("rgb(47, 255, 130)")
            self.frameleft.setFrameShape(QtWidgets.QFrame.WinPanel)
            self.frameleft.setFrameShadow(QtWidgets.QFrame.Sunken)        
            self.frameleft.setPalette(fpaint)
            self.frameleft.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frameleft.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frameleft.setObjectName("frameleft")
            self.frameleft.setStyleSheet(self.fra1)

            #-----------------------------------------------------------------

            #self.frameprofile=QtWidgets.QFrame(self.centralwidget)
            #self.frameprofile.setGeometry(QtCore.QRect(910, 60, 250, 300))
            #self.frameprofile.setStyleSheet("""

            #    QFrame {            
            #    border-radius: 4px;                
               
            #    }
            #    """
            #)

            #self.labelpro = QtWidgets.QLabel(self.frameprofile)
            #self.labelpro.setGeometry(QtCore.QRect(40, 79, 90, 24))            
            #self.labelpro.setObjectName("labelprofile")
            #self.labelpro.setText("Patient Photo")

            #self.labelphoto=QtWidgets.QPushButton(self.frameprofile)
            #self.labelphoto.setGeometry(QtCore.QRect(10, 124, 150, 170))            
            #self.labelphoto.setObjectName("labelphoto")
            #self.labelphoto.setText("Patient Photo")
            #self.labelphoto.setStyleSheet("""border-image : url(employee.png); background-repeat:no-repeat; 
            #background-color:#FFFFFF;
            #""")
            #self.labelphoto.clicked.connect(self.patimgphoto)
            #self.photovar=0


            



            #-----------------------------------------------------------------

            self.shadow = QtWidgets.QGraphicsDropShadowEffect()
            self.shadow.setBlurRadius(5)
            self.shadow.setXOffset(3)
            self.shadow.setYOffset(3)


            #=================================================================

            gpaint = QtGui.QPalette()
            gpaint.setColor(QtGui.QPalette.Background, QtGui.QColor(255,182,193))

            self.frameright = QtWidgets.QFrame(self.centralwidget)
            self.frameright.setGeometry(QtCore.QRect(450, 60, 460, 550))
            self.frameright.setAutoFillBackground(True)
            #self.frame.setStyleSheet("rgb(47, 255, 130)")
            self.frameright.setFrameShape(QtWidgets.QFrame.WinPanel)
            self.frameright.setFrameShadow(QtWidgets.QFrame.Raised)       
            self.frameright.setPalette(gpaint)
            self.frameright.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frameright.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frameright.setStyleSheet(self.fra1)
            self.frameright.setObjectName("frameright")


            # ==================== FRAME ENCABEZADO ====================
            
            palet = QtGui.QPalette()
            palet.setColor(QtGui.QPalette.Background, QtGui.QColor(33,117,155))

            frame = QtWidgets.QFrame(self.centralwidget)
            frame.setFrameShape(QtWidgets.QFrame.NoFrame)
            frame.setFrameShadow(QtWidgets.QFrame.Sunken)
            frame.setAutoFillBackground(True)
            frame.setPalette(palet)
            frame.setFixedWidth(1300)
            frame.setFixedHeight(89)
            frame.move(0, 0)
            
            fuenteTitulo = QtGui.QFont()
            fuenteTitulo.setPointSize(16)
            fuenteTitulo.setBold(True)
            fuenteTitulo.setFamily("Times New Roman")
            
            labelTitulo = QtWidgets.QLabel("<font color='white'>Bloismia Digital Image Processing</font>", frame)
            labelTitulo.setFont(fuenteTitulo)        
            labelTitulo.move(340,30)

            fuenteSubtitulo = QtGui.QFont()
            fuenteSubtitulo.setPointSize(30)

            #====================================================================

            # CSS Styles         

            self.but1="""
                QPushButton {
                background-color: #20B2AA;
                
                color: #F0F0F0;
                border-radius: 4px;
                padding: 3px;
                outline: none;
                /* Issue #194 - Special case of QPushButton inside dialogs, for better UI */
                min-width: 80px;
                }

                QPushButton:disabled {
                background-color: #32414B;
                border: 1px solid #32414B;
                color: #787878;
                border-radius: 4px;
                padding: 3px;
                }

                QPushButton:checked {
                background-color: #20B2AA;
                border: 1px solid #32414B;
                border-radius: 4px;
                padding: 3px;
                outline: none;
                }

                QPushButton:checked:disabled {
                background-color: #19232D;
                border: 1px solid #32414B;
                color: #787878;
                border-radius: 4px;
                padding: 3px;
                outline: none;
                }

                QPushButton:checked:selected {
                background: #20B2AA;
                color: #32414B;
                }

                QPushButton::menu-indicator {
                subcontrol-origin: padding;
                subcontrol-position: bottom right;
                bottom: 4px;
                }

                QPushButton:pressed {
                background-color: #20B2AA;
                border: 1px solid #19232D;
                }

                QPushButton:pressed:hover {
                border: 1px solid #148CD2;
                }

                QPushButton:hover {
                border: 1px solid #148CD2;
                color: #F0F0F0;
                }

                QPushButton:selected {
                background: #1464A0;
                color: #32414B;
                }

                QPushButton:hover {
                border: 1px solid #148CD2;
                color: #F0F0F0;
                }

                QPushButton:focus {
                border: 1px solid #1464A0;
                }


            """

            self.but2="""
                QPushButton {
                background-color: #FF496F;
                
                color: #F0F0F0;
                border-radius: 4px;
                padding: 3px;
                outline: none;
                /* Issue #194 - Special case of QPushButton inside dialogs, for better UI */
                min-width: 80px;
                }

                QPushButton:disabled {
                background-color: #32414B;
                border: 1px solid #32414B;
                color: #787878;
                border-radius: 4px;
                padding: 3px;
                }

                QPushButton:checked {
                background-color: #20B2AA;
                border: 1px solid #32414B;
                border-radius: 4px;
                padding: 3px;
                outline: none;
                }

                QPushButton:checked:disabled {
                background-color: #19232D;
                border: 1px solid #32414B;
                color: #787878;
                border-radius: 4px;
                padding: 3px;
                outline: none;
                }

                QPushButton:checked:selected {
                background: #20B2AA;
                color: #32414B;
                }

                QPushButton::menu-indicator {
                subcontrol-origin: padding;
                subcontrol-position: bottom right;
                bottom: 4px;
                }

                QPushButton:pressed {
                background-color: #FF9672;
                border: 1px solid #19232D;
                }

                QPushButton:pressed:hover {
                border: 1px solid #148CD2;
                }

                QPushButton:hover {
                border: 1px solid #148CD2;
                color: #F0F0F0;
                }

                QPushButton:selected {
                background: #1464A0;
                color: #32414B;
                }

                QPushButton:hover {
                border: 1px solid #148CD2;
                color: #F0F0F0;
                }

                QPushButton:focus {
                border: 1px solid #1464A0;
                }


            """

            #Groupbox

            self.color="""

                QGroupBox{
                    border: 0px;
                    background-color:#FFFFFF;                               
                    border-color:#FB1554;
                    border-width:2px;
                    border-style:dashed;          
                    border-radius:15px
                }          

                QLabel{
                    background-color:#FFFFFF;                
                }

                QCheckBox{
                    background-color:#FFFFFF;                
                }

                QPushButton{
                    background-color:#FFFFFF;                
                }

            """

            #border: 2px solid grey;

            self.prog = """
            QProgressBar{
                border-radius: 5px;
                text-align: center
            }

            QProgressBar::chunk {
                background-color: SpringGreen;
                border-radius: 5px;
            }

            """

            # MediumSizeFont

            mediumSizeFont=QtGui.QFont()
            mediumSizeFont.setFamily("HP Simplified")
            mediumSizeFont.setPointSize(11)

            # SmallSizeFont
            smallSizeFont=QtGui.QFont()
            smallSizeFont.setFamily("Bahnschrift SemiCondensed")
            smallSizeFont.setCapitalization(True)
            smallSizeFont.setPointSize(10)
            
            #=====================================================================

            self.menu="""
                
                QMenu {
                    background-color: #ABABAB; /* sets background of the menu */
                    border: 1px solid black;
                }

                QMenu::item {
                    /* sets background of menu item. set this to something non-transparent
                        if you want menu color and menu item color to be different */
                    background-color: transparent;
                }

                QMenu::item:selected { /* when user selects item using mouse or keyboard */
                    background-color: #654321;
                }

                QMenuBar {
                    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                                    stop:0 lightgray, stop:1 darkgray);
                    spacing: 3px; /* spacing between menu bar items */
                }

                QMenuBar::item {
                    padding: 1px 4px;
                    background: transparent;
                    border-radius: 4px;
                }

                QMenuBar::item:selected { /* when selected using mouse or keyboard */
                    background: #a8a8a8;
                }

                QMenuBar::item:pressed {
                    background: #888888;
                }

            """
            #=====================================================================
            #self.labelpro.setFont(mediumSizeFont)
            #=====================================================================
            self.label_1 = QtWidgets.QLabel(self.frameleft)
            self.label_1.setGeometry(QtCore.QRect(40, 80, 90, 24))
            self.label_1.setFont(mediumSizeFont)
            self.label_1.setObjectName("label")
            #=====================================================================
            self.label_2 = QtWidgets.QLabel(self.frameleft)
            self.label_2.setGeometry(QtCore.QRect(40, 120, 90, 24))
            self.label_2.setFont(mediumSizeFont)
            self.label_2.setObjectName("label_2")
            #=====================================================================
            self.label_3 = QtWidgets.QLabel(self.frameleft)
            self.label_3.setGeometry(QtCore.QRect(40, 160, 90, 24))
            self.label_3.setFont(mediumSizeFont)
            self.label_3.setObjectName("label_3")
            #=====================================================================
            self.label_4 = QtWidgets.QLabel(self.frameleft)
            self.label_4.setGeometry(QtCore.QRect(40, 200, 90, 24))
            self.label_4.setFont(mediumSizeFont)
            self.label_4.setObjectName("label_4")
            #=====================================================================
            self.label_5 = QtWidgets.QLabel(self.frameleft)
            self.label_5.setGeometry(QtCore.QRect(40, 240, 90, 24))
            self.label_5.setFont(mediumSizeFont)
            self.label_5.setObjectName("label_5")
            #=====================================================================
            self.label_6 = QtWidgets.QLabel(self.frameleft)
            self.label_6.setGeometry(QtCore.QRect(40, 310, 90, 24))
            self.label_6.setFont(mediumSizeFont)
            self.label_6.setObjectName("label_6")
            #=====================================================================
            self.label_7 = QtWidgets.QLabel(self.frameleft)
            self.label_7.setGeometry(QtCore.QRect(40, 350, 90, 24))
            self.label_7.setFont(mediumSizeFont)
            self.label_7.setObjectName("label_7")
            #=====================================================================
            self.label_8 = QtWidgets.QLabel(self.frameleft)
            self.label_8.setGeometry(QtCore.QRect(40, 400, 90, 24))
            self.label_8.setFont(mediumSizeFont)
            self.label_8.setObjectName("label_8")
            #=====================================================================
            self.label_9 = QtWidgets.QLabel(self.frameleft)
            self.label_9.setGeometry(QtCore.QRect(40, 440, 90, 24))
            self.label_9.setFont(mediumSizeFont)
            self.label_9.setObjectName("label_9")
            #=====================================================================
            self.lineEdit = QtWidgets.QLineEdit(self.frameleft)
            self.lineEdit.setGeometry(QtCore.QRect(150, 80, 161, 22))            
            self.lineEdit.setMaxLength(10)
            self.lineEdit.setFont(smallSizeFont)
            self.lineEdit.setAlignment(QtCore.Qt.AlignRight)
            self.lineEdit.setObjectName("lineEdit")
            self.lineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]+")))            
            self.lineEdit.setFrame(False)
            #=====================================================================
            self.lineEdit_2 = QtWidgets.QLineEdit(self.frameleft)
            self.lineEdit_2.setGeometry(QtCore.QRect(150, 120, 161, 22))
            self.lineEdit_2.setFont(smallSizeFont)
            self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight)        
            self.lineEdit_2.setObjectName("lineEdit_2")
            self.lineEdit_2.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[ A-Za-z]+")))                 
            self.lineEdit_2.setMaxLength(25)
            self.lineEdit_2.setFrame(False)
            #=====================================================================
            self.lineEdit_3 = QtWidgets.QLineEdit(self.frameleft)
            self.lineEdit_3.setGeometry(QtCore.QRect(150, 160, 161, 22))
            self.lineEdit_3.setFont(smallSizeFont)
            self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight)
            self.lineEdit_3.setObjectName("lineEdit_3")
            self.lineEdit_3.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]+")))                 
            self.lineEdit_3.setMaxLength(2)
            self.lineEdit_3.setFrame(False)
            #=====================================================================
            self.textEdit = QtWidgets.QTextEdit(self.frameleft)
            self.textEdit.setGeometry(QtCore.QRect(150, 225, 161, 71))
            self.textEdit.setFont(smallSizeFont)        
            self.textEdit.setObjectName("textEdit")        
            #self.textEdit.setMaximumSize(50)
            #self.textEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[ 0-9A-Z]")))                 
            

            #=====================================================================
            self.lineEdit_4 = QtWidgets.QLineEdit(self.frameleft)
            self.lineEdit_4.setGeometry(QtCore.QRect(150, 315, 161, 22))
            self.lineEdit_4.setFont(smallSizeFont)
            self.lineEdit_4.setAlignment(QtCore.Qt.AlignRight)
            self.lineEdit_4.setObjectName("lineEdit_4")
            self.lineEdit_4.setMaxLength(10)
            self.lineEdit_4.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]+")))
            self.lineEdit_4.setFrame(False)
            #=====================================================================
            self.lineEdit_5 = QtWidgets.QLineEdit(self.frameleft)
            self.lineEdit_5.setGeometry(QtCore.QRect(150, 355, 161, 22))
            self.lineEdit_5.setFont(smallSizeFont)
            self.lineEdit_5.setAlignment(QtCore.Qt.AlignRight)
            self.lineEdit_5.setObjectName("lineEdit_5")
            self.lineEdit_5.setMaxLength(25)
            #self.lineEdit_5.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")))
            #self.lineEdit_5.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('^[a-z]\d{3}$')))
            #self.lineEdit_5.focusInEvent(QtGui.QFocusEvent)
            self.lineEdit_5.setFrame(False)

            """

            if self.lineEdit_5.gotFocus():
                print("got focus")
            elif self.lineEdit_5.lostFocus():
                print("lost focus")

            """

            #=====================================================================
            self.dateEdit = QtWidgets.QDateEdit(self.frameleft)
            self.dateEdit.setGeometry(QtCore.QRect(150, 395, 161, 22))
            self.dateEdit.setAlignment(QtCore.Qt.AlignRight)
            self.dateEdit.setFont(smallSizeFont)
            self.dateEdit.setObjectName("dateEdit")
            self.dateEdit.setDate(QtCore.QDate.currentDate())
            self.dateEdit.setMinimumDate(QtCore.QDate(2000,1,1))
            self.dateEdit.setMaximumDate(QtCore.QDate(2050,1,1))
            self.dateEdit.setFrame(False)
            #=====================================================================
            self.comboBox = QtWidgets.QComboBox(self.frameleft)
            self.comboBox.setFont(smallSizeFont)
            self.comboBox.setGeometry(QtCore.QRect(150, 435, 161, 22))        
            self.comboBox.addItem("Select", QtCore.Qt.AlignRight)
            self.comboBox.addItem("A Positive", QtCore.Qt.AlignRight)
            self.comboBox.addItem("A Negative", QtCore.Qt.AlignRight)
            self.comboBox.addItem("B Positive", QtCore.Qt.AlignRight)
            self.comboBox.addItem("B Negative", QtCore.Qt.AlignRight)
            self.comboBox.addItem("AB Positive", QtCore.Qt.AlignRight)
            self.comboBox.addItem("AB Negative",QtCore.Qt.AlignRight)
            
            self.comboBox.setFrame(True)
            self.comboBox.setObjectName("comboBox")
            #=====================================================================
            self.radioButton = QtWidgets.QRadioButton(self.frameleft)
            self.radioButton.setGeometry(QtCore.QRect(150, 198, 51, 17))
            self.radioButton.setObjectName("radioButton")
            
            #=====================================================================
            self.radioButton_2 = QtWidgets.QRadioButton(self.frameleft)
            self.radioButton_2.setGeometry(QtCore.QRect(210, 198, 61, 17))
            self.radioButton_2.setObjectName("radioButton_2")
            #=====================================================================
            self.radioButton_3 = QtWidgets.QRadioButton(self.frameleft)
            self.radioButton_3.setGeometry(QtCore.QRect(280, 198, 61, 17))
            self.radioButton_3.setObjectName("radioButton_3")
            #=====================================================================
            self.checkBox = QtWidgets.QCheckBox(self.frameright)
            self.checkBox.setGeometry(QtCore.QRect(20, 80, 70, 17))
            self.checkBox.setObjectName("checkBox")
            #=====================================================================        
            self.gridLayoutWidget = QtWidgets.QWidget(self.frameright)
            self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 110, 420, 385))
            self.gridLayoutWidget.setStyleSheet("QWidget { background-color : #AFEEEE;  border: 0px;}")
            self.gridLayoutWidget.setObjectName("gridLayoutWidget")
            #=====================================================================
            self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)        
            self.gridLayout.setContentsMargins(0, 0, 0, 0)
            self.gridLayout.setObjectName("gridLayout")
            #=====================================================================
            self.scrollWidget = QtWidgets.QWidget(self.gridLayoutWidget)
            self.scrollWidget.setObjectName("scrollwidget")
            scrollPaint = QtGui.QPalette()
            scrollPaint.setColor(QtGui.QPalette.Background, QtGui.QColor(236,240,241))
            self.scrollWidget.setPalette(scrollPaint)
            self.scrollWidget.setLayout(self.gridLayout)
            #=================================================================================
            
            self.scrollArea = QtWidgets.QScrollArea(self.gridLayoutWidget)                
            self.scrollArea.setGeometry(QtCore.QRect(0, 0, 420, 385))
            self.scrollArea.setWidgetResizable(True)
            self.scrollArea.setObjectName("scrollArea")
            self.scrollArea.setWidget(self.scrollWidget)

            # Keep a reference to groupboxes for later use
            
            self.groupboxes = []  
            self.ckselectFile=[]
            self.Imgbutton=[]
            self.imglabel=[]
            self.cksel=0
            self.processimg=[]
            self.imgclick=[]
            

            #===================  Color ================================


            
        
            #=====================================================================
            self.pushButton = QtWidgets.QPushButton(self.frameright)
            #self.pushButton.setGraphicsEffect(self.shadow)                    
            self.pushButton.setGeometry(QtCore.QRect(20, 510, 75, 23))
            self.pushButton.setStyleSheet(self.but2)
            self.pushButton.setObjectName("pushButton")
            #=====================================================================
            self.pushButton_2 = QtWidgets.QPushButton(self.frameleft)
            #self.pushButton_2.setGraphicsEffect(self.shadow)                    
            self.pushButton_2.setGeometry(QtCore.QRect(60, 490, 75, 23))
            self.pushButton_2.setStyleSheet(self.but1)
            self.pushButton_2.setObjectName("pushButton_2")
            #=====================================================================
            self.pushButton_3 = QtWidgets.QPushButton(self.frameleft)
            #self.pushButton_3.setGraphicsEffect(self.shadow)                    
            self.pushButton_3.setGeometry(QtCore.QRect(170, 490, 75, 23))
            self.pushButton_3.setStyleSheet(self.but1)
            self.pushButton_3.setObjectName("pushButton_3")
            #=====================================================================
            self.pushButton_4 = QtWidgets.QPushButton(self.frameright)
            self.pushButton_4.setStyleSheet(self.but2)
            self.pushButton_4.setGeometry(QtCore.QRect(100, 79, 75, 23))
            self.pushButton_4.setObjectName("pushButton_4")
            #=====================================================================
            self.pushButton_5 = QtWidgets.QPushButton(self.frameright)
            self.pushButton_5.setStyleSheet(self.but2)  
            self.pushButton_5.setGeometry(QtCore.QRect(190, 79, 75, 23))
            self.pushButton_5.setObjectName("pushButton_5")                
            #=====================================================================
            #self.pushButton_6 = QtWidgets.QPushButton(self.frameright)
            #self.pushButton_6.setStyleSheet(self.but2)  
            #self.pushButton_6.setGeometry(QtCore.QRect(350, 79, 30, 23))
            #self.pushButton_6.setObjectName("pushButton_6") 
            
            #=====================================================================
            font = QtGui.QFont()
            font.setFamily("A770-Deco")
            font.setPointSize(24)
            #=====================================================================
            self.progressBar = QtWidgets.QProgressBar(self.frameright)
            self.progressBar.setGeometry(QtCore.QRect(125, 510, 250, 20))
            self.completed=0
            self.progressBar.setValue(self.completed)
            self.progressBar.setStyleSheet(self.prog)        
            self.progressBar.setObjectName("progressBar")
            #=====================================================================
            MainWindow.setCentralWidget(self.centralwidget)
            #=====================================================================
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 21))
            self.menubar.setObjectName("menubar")
            self.menubar.setStyleSheet(self.menu)
            
            self.menuFile = QtWidgets.QMenu(self.menubar)
            self.menuFile.setObjectName("menuFile")
            self.menuFile.setStyleSheet(self.menu)
            MainWindow.setMenuBar(self.menubar)

            #=====================================================================
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            self.statusbar.setFont(mediumSizeFont)
            self.statusbar.showMessage('Welcome to Bloismia Image Processing ')
            self.statusbar.setStyleSheet("QStatusBar{padding-left:8px; background:rgba(0,0,0,0);color:black;}")        
            MainWindow.setStatusBar(self.statusbar)
                    
            self.actionPatient_List = QtWidgets.QAction(MainWindow)
            self.actionPatient_List.setObjectName("actionPatient_List")
            self.actionPatient_List.setShortcut("Ctrl+V")
            self.actionPatient_List.triggered.connect(self.openWindow)

            self.actionExit = QtWidgets.QAction(MainWindow)
            self.actionExit.setObjectName("actionExit")
            self.actionExit.setShortcut("Ctrl+Q")
            self.actionExit.triggered.connect(sys.exit)

            self.menuFile.addAction(self.actionPatient_List)
            self.menuFile.addAction(self.actionExit)
            self.menubar.addAction(self.menuFile.menuAction())

            #=====================================================================

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #============================================================================================




        #============================================================================================
        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            #=====================================================================
            MainWindow.setWindowTitle(_translate("MainWindow", "Bloismia Digital Image Processing"))
            #QtGui.QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
            # Always on top
                    
            #=====================================================================
            self.label_1.setText(_translate("MainWindow", "Patient No:"))
            self.label_2.setText(_translate("MainWindow", "Name :"))
            self.label_3.setText(_translate("MainWindow", "Age :"))
            self.label_4.setText(_translate("MainWindow", "Gender :"))
            self.label_5.setText(_translate("MainWindow", "Address :"))
            self.label_6.setText(_translate("MainWindow", "Phone No:"))
            self.label_7.setText(_translate("MainWindow", "Email ID :"))
            self.label_8.setText(_translate("MainWindow", "Register Date :"))
            self.label_9.setText(_translate("MainWindow", "Blood Group :"))
            #=====================================================================
            self.radioButton.setText(_translate("MainWindow", "Male"))
            self.radioButton_2.setText(_translate("MainWindow", "Female"))
            self.radioButton_3.setText(_translate("MainWindow", "Other"))
            #=====================================================================
            self.checkBox.setText(_translate("MainWindow", "Select All"))
            self.checkBox.clicked.connect(self.selectAll)
            self.flagg=0
            self.checkBox.setEnabled(False)        
            #=====================================================================
            self.pushButton.setText(_translate("MainWindow", "WBC Analysis"))
            self.pushButton.clicked.connect(lambda:self.checkstate(1))
            self.pushButton_2.setText(_translate("MainWindow", "Submit"))
            self.pushButton_2.clicked.connect(self.save)
            self.pushButton_3.setText(_translate("MainWindow", "Clear"))
            self.pushButton_3.clicked.connect(self.cleardata)
            self.pushButton_4.setText(_translate("MainWindow", "Load Images"))
            self.pushButton_4.clicked.connect(self.browser)
            self.pushButton_5.setText(_translate("MainWindow", "Clear Images"))
            self.pushButton_5.clicked.connect(self.Clearr)
            self.clr=False
            #self.pushButton_6.setText(_translate("MainWindow", "View"))
            #self.pushButton_6.clicked.connect(lambda:self.checkstate(2))
            self.menuFile.setTitle(_translate("MainWindow", "File"))
            self.actionPatient_List.setText(_translate("MainWindow", "Patient List"))
            self.actionExit.setText(_translate("MainWindow", "Exit"))
            #=====================================================================
            
            #---------------------- Tab Order

            self.frameleft.setTabOrder(self.lineEdit,self.lineEdit_2)
            self.frameleft.setTabOrder(self.lineEdit_2,self.lineEdit_3)
            self.frameleft.setTabOrder(self.lineEdit_3,self.radioButton)
            self.frameleft.setTabOrder(self.radioButton,self.radioButton_2)
            self.frameleft.setTabOrder(self.radioButton_2,self.radioButton_3)
            self.frameleft.setTabOrder(self.radioButton_3,self.textEdit)
            self.frameleft.setTabOrder(self.textEdit,self.lineEdit_4)
            self.frameleft.setTabOrder(self.lineEdit_4,self.lineEdit_5)
            self.frameleft.setTabOrder(self.lineEdit_5,self.dateEdit)
            self.frameleft.setTabOrder(self.dateEdit,self.comboBox)
            self.frameleft.setTabOrder(self.comboBox,self.pushButton_2)
            self.frameleft.setTabOrder(self.pushButton_2,self.pushButton_3)

            #=====================================================================

            #-------------------------------- Database Connection -----------------------------------
            self.db=QtSql.QSqlDatabase.addDatabase('QSQLITE')
            self.db.setDatabaseName('bloismia.db')
                    
            if not self.db.open():
                QtWidgets.QMessageBox.critical(None,QtWidgets.qApp.tr("Cannot Open Database"),
                QtWidgets.qApp.tr("Unable to Establish a Database Connection"),
                QtWidgets.QMessageBox.Cancel)
                return False
            else:
                print("Connection Established Successfully ")
            
            self.query=QtSql.QSqlQuery()
            self.query.exec_("CREATE TABLE if not exists patient_det ( "
                        "pid     TEXT  PRIMARY KEY,"
                        "pname   TEXT,"
                        "age     INT,"
                        "gender  VARCHAR (10),"
                        "address TEXT,"
                        "mob     TEXT,"
                        "email   TEXT,"
                        "rdate   DATE,"
                        "bgrp    TEXT"
                    ")")
            print("Patient Table Successfuly Created")

            self.query.exec_("CREATE TABLE if not exists Patient_Img ("
                    "Patient_ID TEXT REFERENCES patient_det (pid),"
                    "Img_ID     VARCHAR (30) PRIMARY KEY,"
                    "Img_Name   TEXT,"
                    "Img_Data   BLOB"
                    ")")

            print("Patient Image Table Successfuly Created")

            self.query.exec_("CREATE TABLE if not exists Result_Img ("
                    "Patient_ID TEXT,"                    
                    "Img_Name   TEXT,"
                    "Img_Data   BLOB"
                    ")")

            self.query.exec_("CREATE TABLE if not exists pat_img ("
                    "Patient_ID TEXT,"        
                    "Patient_Name TEXT,"                                
                    "Img_Data   BLOB"
                    ")")

            print("Result Image and Patient Photo Table Successfuly Created")


            
            
        #=======================================================================

        #======================================================================
        
        def browser(self):
            try:
                                
                print("Browsering !!!")
                                            
                filetemp=QtWidgets.QFileDialog.getOpenFileNames(self.gridLayoutWidget,"Open File","E:/lab/DIP Case study/Images/","Images (*.gif *.jpg *.png)")[0]
                
                self.imgcompress(filetemp)         
                print("Image Thumbnails Created Successfully")                       
                #self.imgdata()
                self.resource(filetemp)
                print("Resources is finished")
                                    
                #---------------------------------------------------------------
                self.fileName.extend(filetemp)
                print("File Size :"+str(len(self.fileName)))
                filetemp.clear()
                
                #==========================================================================================
                self.cksel=0
                                
                a=len(self.fileName)/3
                #==========================================================
                if(a%2==0):                    
                    res=round(a)
                else:                        
                    res=round(a)+1

                #=========================================================
                # Img Location Added
                
                
                
                k=0
                print(" Alert ! The Image Files are added in GridLayout ")
                for i in range(res):
                    for j in range(3):                
                        if(k<len(self.fileName)):        
                            #self.gridLayout.addWidget(self.groupboxes[k],i,j)
                            #self.gridLayout[0].cellRect(QtCore.QRect(2,1))
                            #self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 21))
                            t1 = threading.Thread(target=self.imgadded,args=(k,i,j))
                            t1.start()
                            #time.sleep(3)                        
                            #print(k,"   Note")
                            k=k+1
                        else:
                            break
                        
                        
                self.flagg=1
                
                self.checkBox.setEnabled(True)
                if not self.checkBox.checkState():
                    self.checkBox.setChecked(True)                
                
                self.selectAll()
                # Calulation Purpose Changing the value...
                self.cksel=len(self.fileName)                
                self.pushButton_5.setText("Clear All Images")
                
                print("Images, Img Name added Successfully")
            except Exception as e:
                print("Error : ",e)


        def imgadded(self,k,i,j):
            self.gridLayout.addWidget(self.groupboxes[k],i,j)
            #self.gridLayout[0].cellRect(QtCore.QRect(2,1))
            #self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 21))

        def singleimg(self,name):
            self.oneview=QtWidgets.QMainWindow()            
            ui = ImageS()
            ui.setupUi(self.oneview)
            ui.img(name)
            self.oneview.show()
                                            
        def ImgFileNameSplit(self,z):
            p=len(z)
            q=0        
            while q<p:
                if z[q]=="/":
                    b=(z[q+1:p])                                
                q=q+1
            return b
        
        def selectAll(self):        
            if(self.flagg==1):
                if(self.checkBox.checkState()):                
                    print("Select All")
                    i=0
                    while(i<len(self.ckselectFile)):
                        self.ckselectFile[i].setChecked(True)
                        i=i+1
                    self.pushButton_5.setText("Clear All Images")
                    self.pushButton_5.setGeometry(QtCore.QRect(190, 79, 85, 23))
                else:
                    print("UnSelect All")
                    i=0
                    while(i<len(self.ckselectFile)):
                        self.ckselectFile[i].setChecked(False)
                        i=i+1
                    self.pushButton_5.setText("Clear Images")
                    self.pushButton_5.setGeometry(QtCore.QRect(190, 79, 75, 23))
            
        def Clearr(self):
                    
            try:
                if((str(self.pushButton_5.text())=="Clear All Images")or(self.clr)):
                    j=0
                    for i in self.groupboxes:
                        i.hide()
                        i.deleteLater()                    
                        print(self.fileName[j])
                        j=j+1
                    self.groupboxes.clear()          

                    for i in self.ckselectFile:
                        i.deleteLater()
                    self.ckselectFile.clear()

                    for i in self.Imgbutton:
                        i.deleteLater()
                    self.Imgbutton.clear()

                    for i in self.imglabel:
                        i.deleteLater()
                    self.imglabel.clear()

                    for i in self.imgclick:
                        i.deleteLater()
                    self.imgclick.clear()

                    self.fileName.clear()                                                
                    self.img_name.clear()

                    for i in self.thumb:
                        os.remove("ImgThumbnails/"+str(i))
                    self.thumb.clear()

                    self.checkBox.setChecked(False)
                    self.checkBox.setDisabled(True)
                    self.pushButton_5.setText("Clear Images")
                    self.completed=0
                    self.cksel=0
                    self.progressBar.setValue(self.completed)
                    print("Clear All Images")
                    
                    if self.clr==False:
                        msg=QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Warning)
                        msg.setWindowTitle("Warning")
                        msg.setText("All Images Cleared")
                        msg.exec_()

                elif(str(self.pushButton_5.text())=="Clear Selected Images"):
                    
                    cl=0
                    deldata=[]
                    
                    for i in self.ckselectFile:                    
                        if i.checkState():
                            print(self.fileName[cl])
                            self.groupboxes[cl].hide()                            

                            # Delete the Objects
                            self.groupboxes[cl].deleteLater()                                                                        
                            self.Imgbutton[cl].deleteLater()
                            self.ckselectFile[cl].deleteLater()
                            self.imglabel[cl].deleteLater()
                            self.imgclick[cl].deleteLater()


                            deldata.append(self.fileName[cl])
                            deldata.append(self.groupboxes[cl])
                            deldata.append(self.Imgbutton[cl])      
                            deldata.append(self.ckselectFile[cl])
                            deldata.append(self.img_name[cl])
                            deldata.append(self.imglabel[cl])
                            deldata.append(self.thumb[cl])
                            deldata.append(self.imgclick[cl])
                        cl=cl+1
                    
                    for j in range(0,len(deldata),8):                                        
                        self.fileName.remove(deldata[j])
                        self.groupboxes.remove(deldata[j+1])
                        self.Imgbutton.remove(deldata[j+2])
                        self.ckselectFile.remove(deldata[j+3])
                        self.img_name.remove(deldata[j+4])
                        self.imglabel.remove(deldata[j+5])
                        os.remove("ImgThumbnails/"+str(deldata[j+6]))
                        self.thumb.remove(deldata[j+6])
                        self.imgclick.remove(deldata[j+7])
                                        
                    des=len(self.fileName)
                    k=0
                    for i in range(des):
                        for j in range(3):                
                            if(k<len(self.fileName)):        
                                self.gridLayout.addWidget(self.groupboxes[k],i,j)                                                        
                                k=k+1
                            else:
                                break
                                                                    
                    self.cksel=0                        
                    print("Clear Selected Images")
                    self.pushButton_5.setText("Clear Images")
                    msg=QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setWindowTitle("Warning")
                    msg.setText("Selected Images Cleared")
                    msg.exec_()
                    
                elif(str(self.pushButton_5.text())=="Clear Images"):
                    print("Clear Images")
                    msg=QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setWindowTitle("Warning")
                    msg.setText("No Images Selected")
                    msg.exec_()

                    print("Group Boxes Size : "+str(len(self.groupboxes)))
                    print("Check Box Size : "+str(len(self.ckselectFile)))
                    print("Img Button Size : "+str(len(self.Imgbutton)))
                    print("Img Label Size : "+str(len(self.imglabel)))
                    print("Image File Name : "+str(len(self.img_name)))
                    print("Selected Image : "+str(self.cksel))
                    print("self.thumb : ",str(len(self.thumb)))
                    print("The ToolButton View : ",str(len(self.imgclick)))
                
                
            except Exception as e:
                print("Error : ",e)
               

        def checkedcon(self,checked):
            n=len(self.fileName)
            if checked:
                self.cksel=self.cksel+1
                
                if(n==self.cksel):
                    self.checkBox.setChecked(True)
                    self.pushButton_5.setText("Clear All Images")
                    self.pushButton_5.setGeometry(QtCore.QRect(190, 79, 85, 23))
                elif(self.cksel!=0):
                    self.pushButton_5.setText("Clear Selected Images")
                    self.checkBox.setChecked(False)
                    self.pushButton_5.setGeometry(QtCore.QRect(190, 79, 120, 23))            

            else:
                self.cksel=self.cksel-1                

                if(self.cksel==0):
                    self.pushButton_5.setText('Clear Images')
                    self.checkBox.setChecked(False)
                    self.pushButton_5.setGeometry(QtCore.QRect(190, 79, 75, 23))
                elif(n!=self.cksel):
                    self.checkBox.setChecked(False)
                    self.pushButton_5.setText("Clear Selected Images")
                    self.pushButton_5.setGeometry(QtCore.QRect(190, 79, 120, 23))
                    


        def checkstate(self,opt):
            if len(self.fileName)!=0:
                j=0
                #self.processimg=[]
                self.processimg.clear()
                for i in self.ckselectFile:
                    if i.checkState():                        
                        self.processimg.append(self.fileName[j])
                    j=j+1
                print("Images are Send to Image Processing")
                #print(self.processimg[:])
                if len(self.processimg)==0:
                    msg=QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setWindowTitle("Warning")
                    if(opt==1):
                        msg.setText("Please Select the Image to Image Processing !!!")
                    elif(opt==2):
                        msg.setText("Please Select the Images to view !!!")
                    msg.exec_()
                else:
                    if opt==1:
                        self.imgcovert()
                    elif opt==2:
                        self.view()
            else:
                msg=QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle("Warning")
                msg.setText("Please Upload an Image !!!")
                msg.exec_()

        def cleartempimg(self):
            filelist = [ f for f in os.listdir("./ImgThumbnails") if f.endswith(".gif") ]
            for f in filelist:
                os.remove(os.path.join("./ImgThumbnails", f))
            print("Temp Data Cleared")
        
        def imgcompress(self,fileTemp):
            n=len(self.fileName)
            for i in range(len(fileTemp)):                
                now = datetime.now()
                dt_string = now.strftime("%H_%M_%S")
                
                #Thumbnails            
                img=Image.open(str(fileTemp[i]))
                img.thumbnail((128,128),Image.ANTIALIAS)
                #img.save("./test/"+b+".png","PNG")

                z=fileTemp[i]                
                b=self.ImgFileNameSplit(z)

                k=i+n
                img.save("./ImgThumbnails/"+str(b[:-4])+"_"+str(dt_string)+"_"+str(k)+".gif","GIF")
                self.thumb.append(str(b[:-4])+"_"+str(dt_string)+"_"+str(k)+".gif")

            
        def imgcovert(self):
                        
            if self.lineEdit.text()=="":
                msg=QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle("Warning")
                msg.setText("Please Enter the Patient id  !!!")
                msg.exec_()
            
            else:
                    
                self.progressBar.setValue(0)                
                print("Started ----")
                pid=self.lineEdit.text()
                print("Patient ID img : ",str(pid))

                ip=imgpro()
                ip.process(self.processimg,str(pid))
                
                print("Stoped ----")
                self.progressBar.setValue(100)

        def view(self):
            #print(self.processimg[:])
            self.viewWindow(self.processimg)


        def download(self):       
            while self.completed<100:
                self.completed+=0.0001
                self.progressBar.setValue(self.completed)
            self.checkstate()

        def resource(self,fileTemp):
            print("-------------------------------start----------------------")
            #print(fileTemp)
            n=len(self.fileName)
            for k in range(len(fileTemp)):
                
                groupbox = QtWidgets.QGroupBox(self.scrollWidget)
                groupbox.setStyleSheet(self.color)

                print(fileTemp[k])
                #=============================
                z=fileTemp[k]
                #print(z)
                
                # Image File Separating by last name
                b=self.ImgFileNameSplit(z)
                
                #Image File Name
                self.img_name.append(b)
                
                                                
                #Image
                imgB=QtWidgets.QPushButton(groupbox)                        
                imgB.setCursor(QtCore.Qt.PointingHandCursor)
                imgB.setGeometry(QtCore.QRect(8,5,110,100))
                #imgB.setStyleSheet("border-image : url("+fileTemp[k]+"); background-repeat:no-repeat;")
                imgB.setStyleSheet("border-image : url(ImgThumbnails/"+self.thumb[n+k]+"); background-repeat:no-repeat;")
                imgB.setObjectName(z)
                #imgB.setToolTip(str(b))
                imgB.setCheckable(True)
                #imgB.setStyleSheet(self.color)
                #imgB.toggle()
                imgB.clicked.connect(self.click)
                self.Imgbutton.append(imgB)

                #close_tb = QtWidgets.QToolButton(groupbox,clicked=self.fn)
                #close_tb.setIcon(QtGui.QIcon("close.png"))
                #close_tb.setGeometry(QtCore.QRect(105,5,13,13))
                #close_tb.setStyleSheet("""
                #    QToolTip {
                #        border: 2px solid darkkhaki;
                #        padding: 5px;
                #        border-radius: 3px;
                #        opacity: 200;
                #    }
                #    """)

                view_tb = QtWidgets.QToolButton(groupbox)
                view_tb.setIcon(QtGui.QIcon("close.png"))
                view_tb.clicked.connect(self.imgclicked)
                view_tb.setGeometry(QtCore.QRect(105,25,13,13))
                view_tb.setObjectName(z)
                view_tb.setCheckable(True)
                view_tb.setStyleSheet("""
                    QToolTip {
                        border: 2px solid darkkhaki;
                        padding: 5px;
                        border-radius: 3px;
                        opacity: 200;
                    }
                    """)
                self.imgclick.append(view_tb)
                
                                                                
                #CheckBox                         
                ckbox=QtWidgets.QCheckBox(groupbox)
                ckbox.setChecked(True)
                ckbox.setGeometry(QtCore.QRect(8,5,16,18))
                ckbox.setStyleSheet(self.color)
                ckbox.stateChanged.connect(self.checkedcon)            
                self.ckselectFile.append(ckbox)            
                                                
                #-----------------  Letter Checking
                #if(len(b)>22):
                #    b=(b[:20])+'#'
                #============================================
                
                imgnamelabel=QtWidgets.QLabel(groupbox)      #File Name
                imgnamelabel.setText(b)
                imgnamelabel.setFont(QtGui.QFont('Times New Roman',7))
                imgnamelabel.setStyleSheet(self.color)
                imgnamelabel.setGeometry(QtCore.QRect(8,105,110,15))
                self.imglabel.append(imgnamelabel)
                
                groupbox.setFixedWidth(125)
                groupbox.setFixedHeight(126)                
                self.groupboxes.append(groupbox)

                
                
            
        def closeEvent(self, event):
            quit_msg = "Are you sure you want to exit the program ?"
            reply = QtGui.QMessageBox.question(self, 'Message', 
                            quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

        #def patimgphoto(self):
        #    print("Browsering Patient Photo !!!")            
        #    filetemp=QtWidgets.QFileDialog.getOpenFileName(self.frameprofile,"Open File","E:/lab/DIP Case study/Images/","Images (*.gif *.jpg *.png)")[0]
            #print(str(filetemp))
        #    if len(filetemp)!=0:
        #        self.labelphoto.setStyleSheet("border-image : url("+str(filetemp)+"); background-repeat:no-repeat; background-color:#FFFFFF; border-radius: 4px; ")
        #        self.imgpho=filetemp
        #        self.photovar=1                                            

        def fn(self,clicked):
            #print("Position : "+str(self.gridLayout.getItemPosition(2)))
            print("Group Boxes Size : "+str(self.groupboxes))
            print("Check Box Size : "+str(self.ckselectFile))
            print("Img Button Size : "+str(self.Imgbutton))
            print("Img Label Size : "+str(self.imglabel))
            print("Image File Name : "+str(self.img_name))
            print("Selected Image : "+str(self.cksel))
            print("The Grid Items are : "+str(self.gridLayout.count()))
            print("The Grid Layout Length : "+str(len(self.gridLayout)))
            print("The ToolButton View : ",str(len(self.imgclick)))

        def click(self):
            print("Hello World")                        
            for widget in self.Imgbutton:
                #print("---------------------------------"+str(widget))
                if widget.isChecked():
                    name = widget.objectName()
                    #print(str(name))
                    self.singleimg(str(name))
                    widget.toggle()
                    #self.singleimg()
                #print("---------------------------------Done")

        def imgclicked(self):
            print("Done :) ")
            #i=0
            for widget in self.imgclick:
                #print("---------------------------------"+str(widget))
                if widget.isChecked():
                    name = widget.objectName()
                    print(str(name))
                    widget.toggle()
                    self.selectAll
                    #print(str(self.fileName[i])+"  ---  "+str(i))
                    #self.singleimg(str(self.fileName[i]))
                    #self.singleimg()
                #print("---------------------------------Done")
                #i=i+1
            print("Method Finished work")


        def __del__(self): 
            self.cleartempimg()
            print('Destructor called, Patient deleted.')
            
            
            
            
        
    if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)    
        MainWindow = QtWidgets.QMainWindow()    
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()    

        gc.collect()        
        sys.exit(app.exec_())
        
        
        

except Exception as e:
    print("Error : ",e)