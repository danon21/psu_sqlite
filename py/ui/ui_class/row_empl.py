# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'row_empl.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogViewerRowEmpl(object):
    def setupUi(self, DialogViewerRowEmpl):
        DialogViewerRowEmpl.setObjectName("DialogViewerRowEmpl")
        DialogViewerRowEmpl.resize(402, 253)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DialogViewerRowEmpl)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(DialogViewerRowEmpl)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.line = QtWidgets.QFrame(DialogViewerRowEmpl)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label = QtWidgets.QLabel(DialogViewerRowEmpl)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_full_name = QtWidgets.QLineEdit(DialogViewerRowEmpl)
        self.lineEdit_full_name.setObjectName("lineEdit_full_name")
        self.verticalLayout.addWidget(self.lineEdit_full_name)
        self.label_5 = QtWidgets.QLabel(DialogViewerRowEmpl)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEdit_job_title = QtWidgets.QLineEdit(DialogViewerRowEmpl)
        self.lineEdit_job_title.setObjectName("lineEdit_job_title")
        self.verticalLayout.addWidget(self.lineEdit_job_title)
        self.label_2 = QtWidgets.QLabel(DialogViewerRowEmpl)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_address = QtWidgets.QLineEdit(DialogViewerRowEmpl)
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.verticalLayout.addWidget(self.lineEdit_address)
        self.label_3 = QtWidgets.QLabel(DialogViewerRowEmpl)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_phone = QtWidgets.QLineEdit(DialogViewerRowEmpl)
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.verticalLayout.addWidget(self.lineEdit_phone)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(DialogViewerRowEmpl)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(DialogViewerRowEmpl)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout.addWidget(self.frame_2)
        self.pushButton_save = QtWidgets.QPushButton(DialogViewerRowEmpl)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.pushButton_cancel = QtWidgets.QPushButton(DialogViewerRowEmpl)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(DialogViewerRowEmpl)
        QtCore.QMetaObject.connectSlotsByName(DialogViewerRowEmpl)

    def retranslateUi(self, DialogViewerRowEmpl):
        _translate = QtCore.QCoreApplication.translate
        DialogViewerRowEmpl.setWindowTitle(_translate("DialogViewerRowEmpl", "Запись таблицы \"Сотрудники\""))
        self.label_4.setText(_translate("DialogViewerRowEmpl", "КЛЮЧ СОТРУДНИКА: "))
        self.label.setText(_translate("DialogViewerRowEmpl", "ФИО сотрудника:"))
        self.label_5.setText(_translate("DialogViewerRowEmpl", "Должность сотрудника:"))
        self.label_2.setText(_translate("DialogViewerRowEmpl", "Адрес сотрудника:"))
        self.label_3.setText(_translate("DialogViewerRowEmpl", "Телефон сотрудника:"))
        self.pushButton_save.setText(_translate("DialogViewerRowEmpl", "Сохранить"))
        self.pushButton_cancel.setText(_translate("DialogViewerRowEmpl", "Отмена"))