# -*- coding: utf-8 -*-
# pylint: disable=unsubscriptable-object,unused-import
from anki.lang import _
# Form implementation generated from reading ui file 'designer/clayout_top.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.templatesBox = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.templatesBox.sizePolicy().hasHeightForWidth())
        self.templatesBox.setSizePolicy(sizePolicy)
        self.templatesBox.setObjectName("templatesBox")
        self.horizontalLayout.addWidget(self.templatesBox)
        spacerItem = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.templateOptions = QtWidgets.QPushButton(Form)
        self.templateOptions.setText("")
        self.templateOptions.setAutoDefault(False)
        self.templateOptions.setDefault(False)
        self.templateOptions.setObjectName("templateOptions")
        self.horizontalLayout.addWidget(self.templateOptions)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.changesLabel = QtWidgets.QLabel(Form)
        self.changesLabel.setText("")
        self.changesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.changesLabel.setObjectName("changesLabel")
        self.verticalLayout.addWidget(self.changesLabel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_("Form"))
        self.label.setText(_("Card Type:"))
