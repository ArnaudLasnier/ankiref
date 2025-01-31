# -*- coding: utf-8 -*-
# pylint: disable=unsubscriptable-object,unused-import
from anki.lang import _
# Form implementation generated from reading ui file 'designer/reschedule.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(325, 144)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.asNew = QtWidgets.QRadioButton(Dialog)
        self.asNew.setChecked(True)
        self.asNew.setObjectName("asNew")
        self.verticalLayout_2.addWidget(self.asNew)
        self.asRev = QtWidgets.QRadioButton(Dialog)
        self.asRev.setObjectName("asRev")
        self.verticalLayout_2.addWidget(self.asRev)
        self.rangebox = QtWidgets.QWidget(Dialog)
        self.rangebox.setEnabled(False)
        self.rangebox.setObjectName("rangebox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.rangebox)
        self.verticalLayout.setContentsMargins(20, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.rangebox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.min = QtWidgets.QSpinBox(self.rangebox)
        self.min.setMaximum(9999)
        self.min.setObjectName("min")
        self.gridLayout.addWidget(self.min, 0, 0, 1, 1)
        self.max = QtWidgets.QSpinBox(self.rangebox)
        self.max.setMaximum(9999)
        self.max.setObjectName("max")
        self.gridLayout.addWidget(self.max, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.rangebox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.rangebox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.asRev.toggled['bool'].connect(self.rangebox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.asNew, self.asRev)
        Dialog.setTabOrder(self.asRev, self.min)
        Dialog.setTabOrder(self.min, self.max)
        Dialog.setTabOrder(self.max, self.buttonBox)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_("Reschedule"))
        self.asNew.setText(_("Place at end of new card queue"))
        self.asRev.setText(_("Place in review queue with interval between:"))
        self.label_3.setText(_("~"))
        self.label_4.setText(_("days"))
