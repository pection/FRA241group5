# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StudentProfile.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class STUDENT(object):
    stuID = 58340500001
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setFixedSize(250, 420)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit2 = QtGui.QLabel(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(150, 75, 80, 20))
        self.lineEdit2.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit2.setStyleSheet("background-color: white;font-size: 13pt;border:1px solid black")
        self.label_3 = QtGui.QLabel(self.centralwidget)

        self.label_3.setGeometry(QtCore.QRect(20, 100, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit3 = QtGui.QLabel(self.centralwidget)
        self.lineEdit3.setGeometry(QtCore.QRect(150, 110, 80, 20))
        self.lineEdit3.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit3.setStyleSheet("background-color: white;font-size: 13pt;border:1px solid black")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20,130, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit4 = QtGui.QLabel(self.centralwidget)
        self.lineEdit4.setGeometry(QtCore.QRect(150, 140, 80, 20))
        self.lineEdit4.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit4.setStyleSheet("background-color: white;font-size: 13pt;border:1px solid black")
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 350, 210, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.send = QtGui.QPushButton(self.centralwidget)
        self.send.setGeometry(QtCore.QRect(180, 380, 50, 20))
        self.send.setObjectName(_fromUtf8("pushButton_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.back = QtGui.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(20, 380, 50, 20))
        self.back.setObjectName(_fromUtf8("pushButton_2"))
        self.dec = QtGui.QPushButton(self.centralwidget)
        self.dec.setGeometry(QtCore.QRect(75, 380, 50, 20))
        self.dec.setObjectName(_fromUtf8("pushButton_2"))
        self.inc = QtGui.QPushButton(self.centralwidget)
        self.inc.setGeometry(QtCore.QRect(125, 380, 50, 20))
        self.inc.setObjectName(_fromUtf8("pushButton_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 294, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20,155, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.q = QtGui.QLabel(self.centralwidget)
        self.q.setGeometry(QtCore.QRect(20, 190, 210, 150))
        self.q.setObjectName(_fromUtf8("lineEdit"))
        self.q.setStyleSheet("background-color: white;font-size: 13pt;border:1px solid black")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Student Profile", None))
        self.label_2.setText(_translate("MainWindow", "Student ID: ", None))
        self.label_3.setText(_translate("MainWindow", "จำนวนการคำถาม:  ", None))
        self.label_4.setText(_translate("MainWindow", "จำนวนการคลิก:  ", None))
        self.label_5.setText(_translate("MainWindow", "คำถามทั้งหมด", None))
        self.send.setText(_translate("MainWindow", "SHOW", None))
        self.back.setText(_translate("MainWindow", "BACK", None))
        self.dec.setText(_translate("MainWindow", "<< -", None))
        self.inc.setText(_translate("MainWindow", "+ >>", None))
        self.lineEdit.setText(_translate("MainWindow", str(self.stuID), None))
        QtCore.QObject.connect(self.dec, QtCore.SIGNAL("clicked()"), lambda: self.ID(-1))
        QtCore.QObject.connect(self.inc, QtCore.SIGNAL("clicked()"), lambda: self.ID(1))

    def ID(self,i):
        self.stuID += i
        self.lineEdit.setText(_translate("MainWindow", str(self.stuID), None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = STUDENT()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

