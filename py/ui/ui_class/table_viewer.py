# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_viewer.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(959, 464)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_row = QtWidgets.QComboBox(Dialog)
        self.comboBox_row.setObjectName("comboBox_row")
        self.horizontalLayout.addWidget(self.comboBox_row)
        self.pushButton_edit_row = QtWidgets.QPushButton(Dialog)
        self.pushButton_edit_row.setObjectName("pushButton_edit_row")
        self.horizontalLayout.addWidget(self.pushButton_edit_row)
        self.pushButton_delete_row = QtWidgets.QPushButton(Dialog)
        self.pushButton_delete_row.setObjectName("pushButton_delete_row")
        self.horizontalLayout.addWidget(self.pushButton_delete_row)
        self.pushButton_create_new_row = QtWidgets.QPushButton(Dialog)
        self.pushButton_create_new_row.setObjectName("pushButton_create_new_row")
        self.horizontalLayout.addWidget(self.pushButton_create_new_row)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.DialogViewerTable = QtWidgets.QTableView(Dialog)
        self.DialogViewerTable.setObjectName("DialogViewerTable")
        self.verticalLayout.addWidget(self.DialogViewerTable)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Просмотр таблицы"))
        self.pushButton_edit_row.setText(_translate("Dialog", "Отредактировать выбранную строку"))
        self.pushButton_delete_row.setText(_translate("Dialog", "Удалить выбранную строку"))
        self.pushButton_create_new_row.setText(_translate("Dialog", "Создать новую строку"))