import os
import cv2 as cv2
import sqlite3
from pathlib import Path
#from caseProject17 import Ui_MainWindow

class imgpro(object):

    def __init__(self):
        self.processimg=[]
        self.sqliteConnection = sqlite3.connect('bloismia.db')
        self.cursor = self.sqliteConnection.cursor()
        q = Path('ResultImg/')
        q.mkdir(exist_ok=True)

        #self.u=Ui_MainWindow()        

    def ImgFileNameSplit(self,z):
        p=len(z)
        q=0        
        while q<p:
            if z[q]=="/":
                b=(z[q+1:p])                                
            q=q+1
        return b    

    def process(self,imglist,pid):

        self.processimg=imglist

        j=0
        for i in self.processimg:
            img=cv2.imread(i,0)
            equ=cv2.equalizeHist(img)
            z=self.ImgFileNameSplit(str(i))
            sampname=str(j)+" "+z
            des=cv2.resize(equ,(700,400))
            cv2.imshow(sampname,des)            

            cv2.imwrite("./ResultImg/"+sampname,des)        

            #cv2.imwrite( 'im.jpg' )
            im = open("./ResultImg/"+sampname,'rb').read()
            print(type(im))
            #db.execute("insert into images values(?,?)",("pattern",sqlite3.Binary(im)))
            #self.cursor.execute("""insert into Result_Img (Img_Data) values (?) """,(sqlite3.Binary(im)))
            self.cursor.execute("""insert into Result_Img (Patient_ID,Img_Name,Img_Data) values (?,?,?) """,(pid,sampname,sqlite3.Binary(im)))
            os.remove("./ResultImg/"+sampname)
            j=j+1

        #self.imgresultsave(pid)

        self.sqliteConnection.commit()
        self.cursor.close()
        self.sqliteConnection.close()
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    def imgresultsave(self,pid):
        try:
            imgfolder = os.listdir('ResultImg/')
            print(imgfolder[0])
            #for entry in entries:
            #    print(entry)            
            ImgData=os.path.abspath(imgfolder[0])
            print(ImgData)
            self.insert_picture(ImgData)
            
            #with open(ImgData, 'rb') as input_file:
            #    ablob = input_file.read()
            #    self.cursor.execute("""insert into Result_Img (Patient_ID,Img_Name,Img_Data) values (?,?,?) """,(pid,sampname,sqlite3.Binary(ablob)))
                #base=os.path.basename(ImgData)
                #afile, ext = os.path.splitext(base)
                #sql = '''INSERT INTO PICTURES  (PICTURE, TYPE, FILE_NAME) VALUES(?, ?, ?);'''
                #conn.execute(sql,[sqlite3.Binary(ablob), ext, afile]) 
            #    self.sqliteConnection.commit()
    
            print("Image Saved")
        except Exception as e:
            print("Error : ",str(e))

    def insert_picture(self,picture_file):
        with open(picture_file, 'rb') as input_file:
            ablob = input_file.read()
            base=os.path.basename(picture_file)
            afile, ext = os.path.splitext(base)
            #sql = '''INSERT INTO PICTURES  (PICTURE, TYPE, FILE_NAME) VALUES(?, ?, ?);'''
            #conn.execute(sql,[sqlite3.Binary(ablob), ext, afile]) 
            self.cursor.execute("""insert into Result_Img (Img_Data) values (?,?,?) """,(sqlite3.Binary(ablob)))
            #conn.commit()
            self.sqliteConnection.commit()
        
        
            









"""
j=0
for i in self.processimg:
    img=cv2.imread(i,0)
    equ=cv2.equalizeHist(img)
    sampname="Img "+str(j)
    des=cv2.resize(equ,(700,400))
    cv2.imshow(sampname,des)
    j=j+1        
    
    self.completed+=round(iprem)
    self.progressBar.setValue(self.completed)

self.progressBar.setValue(100)        
cv2.waitKey(0)
cv2.destroyAllWindows()
"""