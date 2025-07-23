# -*- coding: utf-8 -*-
import os
import sys
import Import
import Spreadsheet
import DraftVecUtils
import Sketcher
import Part
import PartDesign
import FreeCAD as App
import FreeCADGui as Gui

from PySide import QtGui
from PySide import QtUiTools
from PySide import QtCore

class Ui_Dialog(object):
    #print('aaaaaaa')
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 375)
        Dialog.move(1000, 0)

        #flightWidth
        self.label_W = QtGui.QLabel('flightWidth',Dialog)
        self.label_W.setGeometry(QtCore.QRect(30, 13, 100, 22))
        self.le_W = QtGui.QLineEdit('500',Dialog)
        self.le_W.setGeometry(QtCore.QRect(100, 10, 60, 20))
        self.le_W.setAlignment(QtCore.Qt.AlignCenter)
        #L1
        self.label_L1 = QtGui.QLabel('length L1',Dialog)
        self.label_L1.setGeometry(QtCore.QRect(30, 38, 100, 22))
        self.le_L1 = QtGui.QLineEdit('6000',Dialog)
        self.le_L1.setGeometry(QtCore.QRect(100, 35, 60, 20))
        self.le_L1.setAlignment(QtCore.Qt.AlignCenter)
        #L2
        self.label_L2 = QtGui.QLabel('length L2',Dialog)
        self.label_L2.setGeometry(QtCore.QRect(30, 63, 100, 22))
        self.le_L2 = QtGui.QLineEdit('3000',Dialog)
        self.le_L2.setGeometry(QtCore.QRect(100, 60, 60, 20))
        self.le_L2.setAlignment(QtCore.Qt.AlignCenter)
        #傾斜角
        self.label_beta = QtGui.QLabel('tiltAngle',Dialog)
        self.label_beta.setGeometry(QtCore.QRect(30, 88, 100, 22))
        self.le_beta = QtGui.QLineEdit('30',Dialog)
        self.le_beta.setGeometry(QtCore.QRect(100, 85, 60, 20))
        self.le_beta.setAlignment(QtCore.Qt.AlignCenter)



        #作成
        self.pushButton = QtGui.QPushButton('create',Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 135, 50, 22))
        #更新
        self.pushButton2 = QtGui.QPushButton('update',Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(120, 135, 50, 22))
        #Import
        self.pushButton3 = QtGui.QPushButton('Import',Dialog)
        self.pushButton3.setGeometry(QtCore.QRect(190, 135, 50, 22))

         #質量計算
        self.pushButton_m = QtGui.QPushButton('massCulculation',Dialog)
        self.pushButton_m.setGeometry(QtCore.QRect(170, 13, 150,23))
        self.pushButton_m.setObjectName("pushButton") 
        #質量集計
        self.pushButton_m20 = QtGui.QPushButton('massTally_csv',Dialog)
        self.pushButton_m20.setGeometry(QtCore.QRect(170, 37, 150, 23))
        self.pushButton_m2 = QtGui.QPushButton('massTally_SpreadSheet',Dialog)
        self.pushButton_m2.setGeometry(QtCore.QRect(170, 62, 150, 23))
        #質量入力
        self.pushButton_m3 = QtGui.QPushButton('massImput[kg]',Dialog)
        self.pushButton_m3.setGeometry(QtCore.QRect(170, 87, 100, 23))
        self.pushButton_m3.setObjectName("pushButton")  
        self.le_mass = QtGui.QLineEdit(Dialog)
        self.le_mass.setGeometry(QtCore.QRect(270, 87, 50, 20))
        self.le_mass.setAlignment(QtCore.Qt.AlignCenter)  
        self.le_mass.setText('10.0')
        #密度
        self.lbl_gr = QtGui.QLabel('SpecificGravity',Dialog)
        self.lbl_gr.setGeometry(QtCore.QRect(167, 112, 80, 12))
        self.le_gr = QtGui.QLineEdit(Dialog)
        self.le_gr.setGeometry(QtCore.QRect(270,112, 50, 20))
        self.le_gr.setAlignment(QtCore.Qt.AlignCenter)  
        self.le_gr.setText('7.85')

        #図形
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 320, 200))
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignTop)  
        
        base=os.path.dirname(os.path.abspath(__file__))
        joined_path = os.path.join(base, "flightCv.png")
        self.label_6.setPixmap(QtGui.QPixmap(joined_path))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        #self.le_C.setText('5000')
        QtCore.QObject.connect(self.pushButton3, QtCore.SIGNAL("pressed()"), self.setParts)
        QtCore.QObject.connect(self.pushButton2, QtCore.SIGNAL("pressed()"), self.update)
        QtCore.QObject.connect(self.pushButton_m, QtCore.SIGNAL("pressed()"), self.massCulc)
        QtCore.QObject.connect(self.pushButton_m2, QtCore.SIGNAL("pressed()"), self.massTally)
        QtCore.QObject.connect(self.pushButton_m20, QtCore.SIGNAL("pressed()"), self.massTally2)
        QtCore.QObject.connect(self.pushButton_m3, QtCore.SIGNAL("pressed()"), self.massImput)
        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("pressed()"), self.create)
        #QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Flight Conveyor", None))

    def massImput(self):
         # 選択したオブジェクトを取得する
        c00 = Gui.Selection.getSelection()
        if c00:
            obj = c00[0]
        label='mass[kg]'
        g=float(self.le_mass.text())
        try:
            obj.addProperty("App::PropertyFloat", "mass",label)
            obj.mass=g
        except:
            obj.mass=g
         
    def massCulc(self):
        c00 = Gui.Selection.getSelection()
        if c00:
            obj = c00[0]
        label='mass[kg]'
        g0=float(self.le_gr.text())
        g=obj.Shape.Volume*g0*1000/10**9  
        try:
            obj.addProperty("App::PropertyFloat", "mass",label)
            obj.mass=g
        except:
            pass

    def massTally2(self):#csv
        doc = App.ActiveDocument
        objects = doc.Objects
        mass_list = []
        for obj in objects:
            if Gui.ActiveDocument.getObject(obj.Name).Visibility:
                if obj.isDerivedFrom("Part::Feature"):
                    if hasattr(obj, "mass"):
                        try:
                            mass_list.append([obj.Label, obj.dia,'1', obj.mass])
                        except:
                            mass_list.append([obj.Label, '','1', obj.mass])    

                else:
                     pass
        doc_path = doc.FileName
        csv_filename = os.path.splitext(os.path.basename(doc_path))[0] + "_counts_and_masses.csv"
        csv_path = os.path.join(os.path.dirname(doc_path), csv_filename)
        with open(csv_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Name",'Standard','Count', "Mass[kg]"])
            writer.writerows(mass_list) 
    def massTally(self):#spreadsheet
        doc = App.ActiveDocument
        # 新しいスプレッドシートを作成
        spreadsheet = doc.addObject("Spreadsheet::Sheet", "PartList")
        spreadsheet.Label = "Parts List"
        
        # ヘッダー行を記入
        headers = ['No',"Name",'Standard', 'Count','Unit[kg]','Mass[kg]']
        for header in enumerate(headers):
            spreadsheet.set(f"A{1}", headers[0])
            spreadsheet.set(f"B{1}", headers[1])
            spreadsheet.set(f"C{1}", headers[2])
            spreadsheet.set(f"D{1}", headers[3])
            spreadsheet.set(f"E{1}", headers[4])
            spreadsheet.set(f"F{1}", headers[5])
        # パーツを列挙して情報を書き込む
        row = 2
        i=1
        s=0
        for i,obj in enumerate(doc.Objects):
            if obj.Label=='本体' or obj.Label=='本体 (mirrored)' or obj.Label[:7]=='Channel' or obj.Label[:5]=='Angle' \
                or obj.Label[:6]=='Square' or obj.Label[:7]=='Extrude' or obj.Label[:6]=='Fusion' or obj.Label[:6]=='Corner' \
                    or obj.Label[:5]=='basic' or obj.Label[:4]=='Edge' or obj.Label[:3]=='hub' or obj.Label[:7]=='_8_tube'\
                        or obj.Label[:5]=='plate' or obj.Label[:6]=='keyway' or obj.Label[:4]=='tube' or obj.Label[:5]=='color'\
                            or obj.Label[:6]=='HShape':
                pass        
            else:  
                try:
                    spreadsheet.set(f"E{row}", f"{obj.mass:.2f}")  # Unit
                    s=obj.mass+s
                    if hasattr(obj, "Shape") and obj.Shape.Volume > 0:
                        try:
                            spreadsheet.set(f"A{row}", str(row-1))  # No
                            spreadsheet.set(f"B{row}", obj.Label)   #Name
                            try:
                                spreadsheet.set(f"C{row}", obj.dia)
                            except:
                                #spreadsheet.set(f"C{row}", obj.standard)
                                pass
                            if obj.Label[:7]=='Angular':
                                n=2
                            else:
                                n=1    
                            spreadsheet.set(f"D{row}", str(n))   # count
                            g=round(obj.mass*n,2)
                            spreadsheet.set(f"F{row}", str(g))   # g

                    
                            row += 1
                        except:
                            pass    
                except:
                    pass
                spreadsheet.set(f'F{row}',str(s))
        App.ActiveDocument.recompute()
        Gui.activeDocument().activeView().viewAxometric()    
        
    def setParts(self):
        global shtFlight
        global Sketch_m
        global idler
        global mainC
        global driveS
        global takeUp
        global trough
        global rollerAssy
        global cover
        global sprAssy
        global reducer
        global trestle
        global flightAssy
        global shtTrestle
        global stair
        selection = Gui.Selection.getSelection()
        if selection:
             selected_object = selection[0]
             if selected_object.TypeId == "App::Part":
                 parts_group = selected_object
                 for obj in parts_group.Group:
                     print(obj.Label)
                     if obj.Label[:9] == "shtFlight":
                         shtFlight = obj
                     elif obj.Label == "shtTrestle":
                         shtTrestle = obj    
                     elif obj.Label[:8]=='Sketch_m':
                         Sketch_m=obj 
                     elif obj.Label=='idlerShaftAssy':
                         idler=obj 
                     elif obj.Label=='mainChainAssy':
                         mainC=obj  
                     elif obj.Label=='driveShaftAssy':
                         driveS=obj  
                     elif obj.Label=='takeUpAssy':
                         takeUp=obj  
                     elif obj.Label=='trough':
                         trough=obj 
                     elif obj.Label=='rollerAssy002':
                         rollerAssy=obj  
                     elif obj.Label=='cover':
                         cover=obj 
                     elif obj.Label=='sprAssy':
                         sprAssy=obj
                     elif obj.Label=='reducer':
                         reducer=obj
                     elif obj.Label=='Trestle01':
                         trestle=obj    
                     elif obj.Label=='flightAssy001':
                         flightAssy=obj
                     elif obj.Label=='stair' :
                         stair=obj   


             self.le_W.setText(shtFlight.getContents('W0'))  
             self.le_L1.setText(shtFlight.getContents('l1'))  
             self.le_L2.setText(shtFlight.getContents('l2'))  
             self.le_beta.setText(shtFlight.getContents('beta'))
             H0=2500 + 0.5 * (float(shtFlight.getContents('l2')) - 4350)
             stair.H=H0
             stair.L=H0
                         

    def update(self):
         if shtFlight is None :
             App.Console.PrintError("select an object\n")
         else:
             L1=self.le_L1.text()
             L2=self.le_L2.text()
             W0=self.le_W.text()
             beta=self.le_beta.text()
             #factor=self.le_factor.text()
    
             shtFlight.set('l1',str(L1))
             shtFlight.set('l2',str(L2))
             shtFlight.set('W0',str(W0))
             shtFlight.set('beta',str(beta))
             H0=2500 + 0.5 * (float(shtFlight.getContents('l2')) - 4350)
             stair.H=H0
             stair.L=H0
             

             total_length = 0.0
             edges = Sketch_m.Geometry  # スケッチ内のジオメトリリスト
             for edge in edges:
               #if isinstance(edge, (Part.Line, Part.LineSegment, Part.Circle, Part.ArcOfCircle, Part.Ellipse, Part.ArcOfEllipse)):  # エッジのみ対象
                if isinstance(edge, (Part.LineSegment, Part.ArcOfCircle )):  # エッジのみ対象 
                   total_length += edge.length()
                   print(edge.length())
             
             print(f"スケッチ '{Sketch_m.Label}' の全体長さ: {total_length:.3f} mm")
                
             
             shtFlight.set('pL',str(total_length))
             n=int(total_length/1524)
             shtFlight.set('n',str(n))
             #print(total_length) 

             

             g0=7.85
             g=round(idler.Shape.Volume*g0*1000/10**9,2) 
             idler.mass=g

             g0=7.85
             g=round(mainC.Shape.Volume*g0*1000/10**9,2) 
             mainC.mass=g

             g0=7.85
             g=round(driveS.Shape.Volume*g0*1000/10**9,2) 
             driveS.mass=g

             g0=7.85
             g=round(takeUp.Shape.Volume*g0*1000/10**9,2) 
             takeUp.mass=g

             g0=7.85
             g=round(trough.Shape.Volume*g0*1000/10**9,2) 
             trough.mass=g

             g0=7.85
             g=round(rollerAssy.Shape.Volume*g0*1000/10**9,2) 
             rollerAssy.mass=g 

             g0=7.85
             g=round(cover.Shape.Volume*g0*1000/10**9,2) 
             cover.mass=g

             g0=7.85
             g=round(sprAssy.Shape.Volume*g0*1000/10**9,2) 
             sprAssy.mass=g

             g0=7.85
             g=round(reducer.Shape.Volume*g0*1000/10**9,2) 
             reducer.mass=g

             #g0=7.85
             #g=round(trestle.Shape.Volume*g0*1000/10**9,2) 
             #trestle.mass=g

             g0=7.85
             g=round(flightAssy.Shape.Volume*g0*1000/10**9,2) 
             flightAssy.mass=g
             #print('aaaaaaaaaaaaaaaaaaaaaaaaaaaa')
             App.ActiveDocument.recompute()

    def create(self): 
         fname='flightConveyor.FCStd'
         base=os.path.dirname(os.path.abspath(__file__))
         joined_path = os.path.join(base, fname) 

         try:
            Gui.ActiveDocument.mergeProject(joined_path)
         except:
            doc=App.newDocument()
            Gui.ActiveDocument.mergeProject(joined_path)
         Gui.SendMsgToActiveView("ViewFit")   
         
class main():
        d = QtGui.QWidget()
        d.ui = Ui_Dialog()
        d.ui.setupUi(d)
        d.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        d.show() 
        #script_window = Gui.getMainWindow().findChild(QtGui.QDialog, 'd') 
        #script_window.setWindowFlags(script_window.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)            