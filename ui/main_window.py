# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/danon/Pictures/icon/cat/Pop cat closed.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 641, 481))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_Date = QtWidgets.QWidget()
        self.tab_Date.setObjectName("tab_Date")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_Date)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 631, 451))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_filterDate = QtWidgets.QHBoxLayout()
        self.horizontalLayout_filterDate.setObjectName("horizontalLayout_filterDate")
        self.comboBox_year = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_year.setObjectName("comboBox_year")
        self.horizontalLayout_filterDate.addWidget(self.comboBox_year)
        self.comboBox_month = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_month.setObjectName("comboBox_month")
        self.horizontalLayout_filterDate.addWidget(self.comboBox_month)
        self.pushButton_buildReportDate = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_buildReportDate.setObjectName("pushButton_buildReportDate")
        self.horizontalLayout_filterDate.addWidget(self.pushButton_buildReportDate)
        self.verticalLayout_2.addLayout(self.horizontalLayout_filterDate)
        self.horizontalLayout_reprotDate = QtWidgets.QHBoxLayout()
        self.horizontalLayout_reprotDate.setObjectName("horizontalLayout_reprotDate")
        self.tableView_reprotDate = QtWidgets.QTableView(self.verticalLayoutWidget_2)
        self.tableView_reprotDate.setObjectName("tableView_reprotDate")
        self.horizontalLayout_reprotDate.addWidget(self.tableView_reprotDate)
        self.verticalScrollBar_reprotDate = QtWidgets.QScrollBar(self.verticalLayoutWidget_2)
        self.verticalScrollBar_reprotDate.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_reprotDate.setObjectName("verticalScrollBar_reprotDate")
        self.horizontalLayout_reprotDate.addWidget(self.verticalScrollBar_reprotDate)
        self.verticalLayout_2.addLayout(self.horizontalLayout_reprotDate)
        self.tabWidget.addTab(self.tab_Date, "")
        self.tab_Emp = QtWidgets.QWidget()
        self.tab_Emp.setObjectName("tab_Emp")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_Emp)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 631, 451))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_filterEmp = QtWidgets.QHBoxLayout()
        self.horizontalLayout_filterEmp.setObjectName("horizontalLayout_filterEmp")
        self.comboBox_Emp = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_Emp.setObjectName("comboBox_Emp")
        self.horizontalLayout_filterEmp.addWidget(self.comboBox_Emp)
        self.pushButton_buildReportEmp = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_buildReportEmp.setObjectName("pushButton_buildReportEmp")
        self.horizontalLayout_filterEmp.addWidget(self.pushButton_buildReportEmp)
        self.verticalLayout_3.addLayout(self.horizontalLayout_filterEmp)
        self.horizontalLayout_reportEmp = QtWidgets.QHBoxLayout()
        self.horizontalLayout_reportEmp.setObjectName("horizontalLayout_reportEmp")
        self.tableView_reprotEmp = QtWidgets.QTableView(self.verticalLayoutWidget_3)
        self.tableView_reprotEmp.setObjectName("tableView_reprotEmp")
        self.horizontalLayout_reportEmp.addWidget(self.tableView_reprotEmp)
        self.verticalScrollBar_reprotEmp = QtWidgets.QScrollBar(self.verticalLayoutWidget_3)
        self.verticalScrollBar_reprotEmp.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_reprotEmp.setObjectName("verticalScrollBar_reprotEmp")
        self.horizontalLayout_reportEmp.addWidget(self.verticalScrollBar_reprotEmp)
        self.verticalLayout_3.addLayout(self.horizontalLayout_reportEmp)
        self.tabWidget.addTab(self.tab_Emp, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Отчет \"Окраска автомобилей\""))
        self.pushButton_buildReportDate.setText(_translate("MainWindow", "Построить отчет"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Date), _translate("MainWindow", "Отчет по дате"))
        self.pushButton_buildReportEmp.setText(_translate("MainWindow", "Построить отчет"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Emp), _translate("MainWindow", "Отчет по работникам"))
