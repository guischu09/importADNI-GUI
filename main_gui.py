# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imputADNI2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
from PyQt5.QtWidgets import QFileDialog, QMessageBox
################## GUilherme #####################
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from importADNI_develop import treat_dialog_text, get_corresponding_labels, deal_missing_data
import pandas as pd
################## GUilherme END #####################

from PyQt5.QtCore import QCoreApplication
import menu as m
from scraperADNI import ScraperADNI as Sa



########################################################################
# To-do: 
#   - Fechar ambas janelas quando fechar a principal
#   - Implementar código Schu para devolver colunas
#


################## GUilherme #################################### GUilherme ##################

# Select Features Window
class Ui_featureWindow(object):
    def setupUi(self, featureWindow):
        featureWindow.setObjectName("featureWindow")
        featureWindow.resize(897, 375)
         
        self.tableFeatures = QtWidgets.QTableWidget(featureWindow)
        self.tableFeatures.setGeometry(QtCore.QRect(50, 30, 801, 301))
        self.tableFeatures.setObjectName("tableFeatures")
       
        ############################# IMPORTANT ####################################
        
        # Write to table desired labels and corresponding matches
        
        self.tableFeatures.setColumnCount(self.NcolsTable(desired_labels))
        self.tableFeatures.setRowCount(self.NrowsTable(match)+1)  
      
        ## Escrever os cabeçarios:        
        for uu in range(self.NcolsTable(desired_labels)):
            self.tableFeatures.setItem(0,uu, QTableWidgetItem(desired_labels[uu]))
        
         ## Escrever o resto:        
        for uu in range(self.NcolsTable(desired_labels)):           
            for vv in range(len(match[uu])):
                self.tableFeatures.setItem(vv+1,uu, QTableWidgetItem(match[uu][vv]))
                            
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
    # WARNING: This function edits/uses global variables: desired_labels   
    def NcolsTable(self,desired_labels):
        return len(desired_labels)
        
    # WARNING: This function edits/uses global variables: match
    def NrowsTable(self,match):
        return len(max(match,key=len)) 
    
    def functions(self):
        self.selectFeatButton.clicked.connect(self.selectData)
        self.selectFeatButton.clicked.connect(self.dataFromSelectedFeatures)
        
    # WARNING: This function edits/uses global variables: selectedFeatures            
    def selectData(self):
        global selectedFeatures
        items = self.tableFeatures.selectedItems()
        selectedFeatures=[None]*len(items) 
        for i in range(len(items)):
            selectedFeatures[i] = str(self.tableFeatures.selectedItems()[i].text())
            
#        print(selectedFeatures)
        return selectedFeatures
    
     # WARNING: This function edits/uses global variables: selectedFeatures
    def dataFromSelectedFeatures(self):
        global DataSet  
        DataSet = DataSet.loc[:,selectedFeatures]
        print(DataSet)
        
        return(DataSet)
    
 ################## GUilherme End #################################### GUilherme End ##################


fileTempNames = []
fileCSVName = None
flagFileLoaded = False
flagTempFiles = False
 
# From Web Window
class Ui_FromWebWindow(object):
    def setupUi(self, FromWebWindow):
        FromWebWindow.setObjectName("FromWebWindow")
        FromWebWindow.resize(441, 427)
        self.centralwidget = QtWidgets.QWidget(FromWebWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelSelectMenu = QtWidgets.QLabel(self.centralwidget)
        self.labelSelectMenu.setGeometry(QtCore.QRect(10, 10, 281, 17))
        self.labelSelectMenu.setObjectName("labelSelectMenu")
        self.listMainMenu = QtWidgets.QListWidget(self.centralwidget)
        self.listMainMenu.setGeometry(QtCore.QRect(10, 30, 201, 131))
        self.listMainMenu.setObjectName("listMainMenu")
        self.listSubMenu = QtWidgets.QListWidget(self.centralwidget)
        self.listSubMenu.setGeometry(QtCore.QRect(230, 30, 201, 131))
        self.listSubMenu.setObjectName("listSubMenu")
        self.buttonConfirm = QtWidgets.QPushButton(self.centralwidget)
        self.buttonConfirm.setGeometry(QtCore.QRect(330, 170, 99, 27))
        self.buttonConfirm.setObjectName("buttonConfirm")
        self.listData = QtWidgets.QListWidget(self.centralwidget)
        self.listData.setEnabled(False)
        self.listData.setGeometry(QtCore.QRect(10, 210, 421, 151))
        self.listData.setAutoFillBackground(True)
        self.listData.setObjectName("listData")
        self.buttonConfirmDownload = QtWidgets.QPushButton(self.centralwidget)
        self.buttonConfirmDownload.setGeometry(QtCore.QRect(330, 370, 99, 27))
        self.buttonConfirmDownload.setObjectName("buttonConfirmDownload")
        self.labelSelectData = QtWidgets.QLabel(self.centralwidget)
        self.labelSelectData.setGeometry(QtCore.QRect(10, 190, 131, 17))
        self.labelSelectData.setObjectName("labelSelectData")
        FromWebWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(FromWebWindow)
        self.statusBar.setObjectName("statusBar")
        FromWebWindow.setStatusBar(self.statusBar)
        
        self.retranslateUi(FromWebWindow)
        QtCore.QMetaObject.connectSlotsByName(FromWebWindow)
        
        self.d = FromWebWindow
        self.functions()
        
    def retranslateUi(self, FromWebWindow):
        _translate = QtCore.QCoreApplication.translate
        FromWebWindow.setWindowTitle(_translate("FromWebWindow", "ADNI Data From Web"))
        self.labelSelectMenu.setText(_translate("FromWebWindow", "Select a item on the menu and submenu:"))
        self.buttonConfirm.setText(_translate("FromWebWindow", "Select"))
        self.buttonConfirmDownload.setText(_translate("FromWebWindow", "Use Data"))
        self.labelSelectData.setText(_translate("FromWebWindow", "Select a database:"))
    
    def functions(self):
        self.populateMainMenu()
        self.listMainMenu.itemClicked.connect(self.mainMenuSelected)
        self.listSubMenu.itemDoubleClicked.connect(self.subMenuSelected)
        self.buttonConfirm.clicked.connect(self.buttonConfirmPressed)
        self.buttonConfirmDownload.clicked.connect(self.buttonConfirmDownloadPressed)
        self.setStatus("Ready")
    
    # Action when Main Menu is selected
    def mainMenuSelected(self):
        selected_item = self.listMainMenu.currentItem().text()
        self.populateSubMenu(selected_item)
    
    # Populate Main Menu
    def populateMainMenu(self):
        for x in sorted(m.menu_principal.keys()):
            self.listMainMenu.addItem(x)
    
    # Populate Sub Menu
    def populateSubMenu(self, selected_item):
        self.listSubMenu.clear()
        for x in sorted(m.menu_principal[selected_item].keys()):
            self.listSubMenu.addItem(x)
    
    # Action when Sub Menu is selected
    def buttonConfirmPressed(self):
        selected_mainItem = self.listMainMenu.currentItem()
        selected_item = self.listSubMenu.currentItem()
        
        if selected_mainItem != None and selected_item != None:
            self.subMenuSelected()
    
    # Populate subMenu
    def subMenuSelected(self):
        selected_mainItem = self.listMainMenu.currentItem().text()
        selected_item = self.listSubMenu.currentItem().text()      
        
        link = m.menu_principal[selected_mainItem][selected_item]
        
        self.setStatus("Loading...")
        self.populateDataList(link)
        self.setStatus("Ready")
    
    # Populate list of data
    def populateDataList(self, link):
        self.listData.clear()
        self.listData.setEnabled(True)
        
        self.sa = Sa()
        self.data_dict = self.sa.getDataList(link)
        
        for x in sorted(self.data_dict.keys()):
            if x.find("PDF") == -1:
                self.listData.addItem(x)
    
    # Action when Data is selected for Download
    # WARNING: This function edits/uses global variables: fileTempNames, fileCSVName, flagTempFiles
    def buttonConfirmDownloadPressed(self):
        selected_data = self.listData.currentItem()
        
        if selected_data != None:
            selected_data = selected_data.text()
            if self.confirmationFromWebWindow() == True:
                self.setStatus("Downloading...")
                x = os.getcwd() + "/"
                x += self.sa.getData(self.data_dict[selected_data], selected_data)
                
                global flagTempFiles
                flagTempFiles = True
                
                global fileTempNames
                fileTempNames.append(str(x))
                
                global fileCSVName
                fileCSVName = str(x)
                
                ui.fileLoaded()
                self.sa.close()
                self.d.close()
    
    # Open a confirmation box and return its value
    def confirmationFromWebWindow(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
    
        msg.setText("Sure?")
        msg.setWindowTitle("Confirmation Box")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    	
        retval = msg.exec_()
        
        if retval == 1024:
            return True
        else:
            return False
    
    def setStatus(self, status):
        self.statusBar.showMessage(status)

    
# Main Window
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 247)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBoxSelectSource = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxSelectSource.setGeometry(QtCore.QRect(100, 30, 121, 23))
        self.comboBoxSelectSource.setObjectName("comboBoxSelectSource")
        self.comboBoxSelectSource.addItem("")
        self.comboBoxSelectSource.addItem("")
        self.labelInputData = QtWidgets.QLabel(self.centralwidget)
        self.labelInputData.setGeometry(QtCore.QRect(10, 10, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelInputData.setFont(font)
        self.labelInputData.setObjectName("labelInputData")
        self.labelDesiredFeatures = QtWidgets.QLabel(self.centralwidget)
        self.labelDesiredFeatures.setGeometry(QtCore.QRect(10, 60, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelDesiredFeatures.setFont(font)
        self.labelDesiredFeatures.setObjectName("labelDesiredFeatures")
        self.lineDesiredFeatures = QtWidgets.QLineEdit(self.centralwidget)
        self.lineDesiredFeatures.setEnabled(False)
        self.lineDesiredFeatures.setGeometry(QtCore.QRect(10, 80, 261, 23))
        self.lineDesiredFeatures.setObjectName("lineDesiredFeatures")
        self.buttonCheckFeatures = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCheckFeatures.setEnabled(False)
        self.buttonCheckFeatures.setGeometry(QtCore.QRect(280, 80, 61, 23))
        self.buttonCheckFeatures.setObjectName("buttonCheckFeatures")
        self.labelMissingData = QtWidgets.QLabel(self.centralwidget)
        self.labelMissingData.setGeometry(QtCore.QRect(10, 110, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelMissingData.setFont(font)
        self.labelMissingData.setObjectName("labelMissingData")
        self.buttonRun = QtWidgets.QPushButton(self.centralwidget)
        self.buttonRun.setEnabled(False)
        self.buttonRun.setGeometry(QtCore.QRect(130, 130, 61, 23))
        self.buttonRun.setObjectName("buttonRun")
        self.comboBoxMissingData = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxMissingData.setEnabled(False)
        self.comboBoxMissingData.setGeometry(QtCore.QRect(10, 130, 111, 23))
        self.comboBoxMissingData.setObjectName("comboBoxMissingData")
        self.comboBoxMissingData.addItem("")
        self.comboBoxMissingData.addItem("")
        self.comboBoxMissingData.addItem("")
        self.comboBoxMissingData.addItem("")
        self.buttonBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBrowse.setGeometry(QtCore.QRect(10, 30, 81, 23))
        self.buttonBrowse.setObjectName("buttonBrowse")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 380, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionZimmer_lab = QtWidgets.QAction(MainWindow)
        self.actionZimmer_lab.setObjectName("actionZimmer_lab")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionZimmer_lab)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())
                
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ADNI Data Filter"))
        self.comboBoxSelectSource.setItemText(0, _translate("MainWindow", "From System"))
        self.comboBoxSelectSource.setItemText(1, _translate("MainWindow", "From Web"))
        self.labelInputData.setText(_translate("MainWindow", "Input Data:"))
        self.labelDesiredFeatures.setText(_translate("MainWindow", "Desired Features:"))
        self.buttonCheckFeatures.setText(_translate("MainWindow", "Check"))
        self.labelMissingData.setText(_translate("MainWindow", "Missing Data Options:"))
        self.buttonRun.setText(_translate("MainWindow", "Run"))
        self.comboBoxMissingData.setItemText(0, _translate("MainWindow", "Remove All"))
        self.comboBoxMissingData.setItemText(1, _translate("MainWindow", "None"))
        self.comboBoxMissingData.setItemText(2, _translate("MainWindow", "Impute with KNN"))
        self.comboBoxMissingData.setItemText(3, _translate("MainWindow", "Impute with MICE"))
        self.buttonBrowse.setText(_translate("MainWindow", "Browse (...)"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionZimmer_lab.setText(_translate("MainWindow", "Zimmer-lab"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
    
    # Define actions
    def functions(self):
        app.aboutToQuit.connect(self.closeEvent)
        self.setStatus("Welcome!")
        self.fileNames = []
        self.buttonBrowse.clicked.connect(self.buttonBrowsePressed)
        
        ################## GUilherme################## GUilherme
        self.buttonCheckFeatures.clicked.connect(self.check_matches)
        self.buttonCheckFeatures.clicked.connect(self.openFromfeatureWindow)
        ################## GUilherme################## GUilherme
    
    # Action when Browse (...) is pressed
    def buttonBrowsePressed(self):
        if(self.comboBoxSelectSource.currentText() == "From System"):
            self.openFileNameDialog()
        else:
            self.openFromWebWindow()
    
    # Open From Web Window
    def openFromWebWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_FromWebWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
        ################## GUilherme################## GUilherme
    def openFromfeatureWindow(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_featureWindow()
        self.ui.setupUi(self.window2)
        self.window2.show()

        ################## GUilherme################## GUilherme
        
    
    # Open a file dialog and load file
    # WARNING: This function edits/uses global variables: fileCSVName
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None, "Abrir arquivo", "","CSV Files (*.csv)", options = options)
        if fileName:
            global fileCSVName
            fileCSVName = str(fileName)
            self.fileLoaded()
    
    def saveFileDialog(self): 
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(None, "QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)
        
############################# GUilherme #################################### GUilherme ##################
# WARNING: This function edits/uses global variables: fileCSVName, desired_labels, match
    def check_matches(self):
        global desired_labels, match, DataSet
        desired_labels = str(self.lineDesiredFeatures.text())              
        desired_labels = treat_dialog_text(desired_labels)
        
        DataSet = pd.read_csv(fileCSVName)
        possible_labels = list(DataSet.columns)
        
#        possible_labels = ['PTAU_UPENNBIOMK9_04_19_17','TAU_UPENNBIOMK9_04_19_17','RID_UPENNBIOMK9_04_19_17','ABETA_UPENNBIOMK9_04_19_17']
        match =[None]*len(desired_labels)  
         
        for idx in range(len(desired_labels)):
            input_label = desired_labels[idx]      
            match[idx] = get_corresponding_labels(input_label,possible_labels)
        print(match)

        return (desired_labels,match)
    

        
#        def 
        
        
        
        #####
#         def buttonConfirmDownloadPressed(self):
#        selected_data = self.listData.currentItem()
#        
#        if selected_data != None:
#            selected_data = selected_data.text()
#            if self.confirmationFromWebWindow() == True:
#                self.setStatus("Downloading...")
#                x = os.getcwd() + "/"
#                x += self.sa.getData(self.data_dict[selected_data], selected_data)
#                
#                global flagTempFiles
#                flagTempFiles = True
#                
#                global fileTempNames
#                fileTempNames.append(str(x))
#                
#                global fileCSVName
#                fileCSVName = str(x)
#                
#                ui.fileLoaded()
#                self.sa.close()
#                self.d.close()
#    
#    # Open a confirmation box and return its value
#    def confirmationFromWebWindow(self):
#        msg = QMessageBox()
#        msg.setIcon(QMessageBox.Information)
#    
#        msg.setText("Sure?")
#        msg.setWindowTitle("Confirmation Box")
#        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#    	
#        retval = msg.exec_()
#        
#        if retval == 1024:
#            return True
#        else:
#            return False
################## GUilherme End ################## GUilherme End ################## GUilherme End 
    
    # Enable options/buttons on main window 
    # WARNING: This function edits/uses global variables: flagFileLoaded
    def fileLoaded(self):
        global flagFileLoaded
        flagFileLoaded = True
        
        print fileCSVName
        
        self.setStatus("File Loaded!")
        self.buttonCheckFeatures.setEnabled(True)
        self.lineDesiredFeatures.setEnabled(True)
        self.comboBoxMissingData.setEnabled(True)
        self.buttonRun.setEnabled(True)
        
    
    # Delete downloaded files after use them
    # WARNING: This function edits/uses global variables: fileTempNames
    def deleteFiles(self):      
        global fileTempNames
        for x in fileTempNames:
            try:
                os.remove(x)
            except:
                pass
   
    # Set status text
    def setStatus(self, status):
        self.statusBar.showMessage(status)
    
    # Treat close of the program
    # WARNING: This function edits/uses global variables: flagFileLoaded
    def closeEvent(self):       
        global flagFileLoaded
        if flagFileLoaded: 
            self.deleteFiles()
        
        sys.exit(0)

if __name__ == "__main__":
    app = QCoreApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())