
# -*- coding: utf-8 -*-
 
# Form implementation generated from reading ui file 'featureWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QTableView

 ### Temporary
global desired_labels
desired_labels = ['tau','abeta']    
global match 
match = [['PTAU_UPENNBIOMK9_04_19_17','TAU_UPENNBIOMK9_04_19_17'],['ABETA_UPENNBIOMK9_04_19_17']]

class Ui_featureWindow(object):
    def setupUi(self, featureWindow):
        featureWindow.setObjectName("featureWindow")
        featureWindow.resize(897, 375)
         
        self.tableFeatures = QtWidgets.QTableWidget(featureWindow)
        self.table_view = QTableView()
                 
        self.tableFeatures.setGeometry(QtCore.QRect(50, 30, 801, 301))
        self.tableFeatures.setObjectName("tableFeatures")
       
        ############################# IMPORTANT ####################################
         
        self.tableFeatures.setColumnCount(self.NcolsTable(desired_labels))
        self.tableFeatures.setRowCount(self.NrowsTable(match)+1)  
        
#            print('yes')
        
        
        
        ## Escrever os cabeçarios:        
        for uu in range(self.NcolsTable(desired_labels)):
            self.tableFeatures.setItem(0,uu, QTableWidgetItem(desired_labels[uu]))
        
         ## Escrever o resto:        
        for uu in range(self.NcolsTable(desired_labels)):           
            for vv in range(len(match[uu])):
                self.tableFeatures.setItem(vv+1,uu, QTableWidgetItem(match[uu][vv]))
        
        

#        print(self.tableFeatures.cellClicked)
#        print(self.tableFeatures.setItemSelected)
                
        ############################# IMPORTANT ####################################
         
 
        self.selectFeatButton = QtWidgets.QPushButton(featureWindow)
        self.selectFeatButton.setGeometry(QtCore.QRect(770, 340, 81, 22))
        self.selectFeatButton.setObjectName("selectFeatButton")
        
        self.functions()
         
        self.feat_window_label = QtWidgets.QLabel(featureWindow)
        self.feat_window_label.setGeometry(QtCore.QRect(350, 10, 191, 20))
        self.feat_window_label.setObjectName("feat_window_label")
 
        self.retranslateUi(featureWindow)
        QtCore.QMetaObject.connectSlotsByName(featureWindow)
 
    def retranslateUi(self, featureWindow):
        _translate = QtCore.QCoreApplication.translate
        featureWindow.setWindowTitle(_translate("featureWindow", "Dialog"))
        self.selectFeatButton.setText(_translate("featureWindow", "Select"))
        self.feat_window_label.setText(_translate("featureWindow", "Select the desired features: "))
         
        
        #####################################################
   
    def NcolsTable(self,desired_labels):
        return len(desired_labels)
        
    def NrowsTable(self,match):
        return len(max(match,key=len)) 
    
    def functions(self):
        self.selectFeatButton.clicked.connect(self.selectData)
            
    def selectData(self):
        items = self.tableFeatures.selectedItems()
        selectedFeatures=[None]*len(items) 
        for i in range(len(items)):
            selectedFeatures[i] = str(self.tableFeatures.selectedItems()[i].text())
            
        print(selectedFeatures)
        return selectedFeatures

         
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    featureWindow = QtWidgets.QDialog()
    ui = Ui_featureWindow()
    ui.setupUi(featureWindow)
    featureWindow.show()
    sys.exit(app.exec_())
