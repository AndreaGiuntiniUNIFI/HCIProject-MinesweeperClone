# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewGame(object):
    def setupUi(self, NewGame):
        NewGame.setObjectName("NewGame")
        NewGame.resize(437, 277)
        self.verticalLayout = QtWidgets.QVBoxLayout(NewGame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollAreaNewGame = QtWidgets.QScrollArea(NewGame)
        self.scrollAreaNewGame.setWidgetResizable(True)
        self.scrollAreaNewGame.setObjectName("scrollAreaNewGame")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 417, 257))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelsArea = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.labelsArea.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.labelsArea.setObjectName("labelsArea")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.labelsArea)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelMines = QtWidgets.QLabel(self.labelsArea)
        self.labelMines.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelMines.setIndent(35)
        self.labelMines.setObjectName("labelMines")
        self.horizontalLayout_3.addWidget(self.labelMines)
        self.labelHeight = QtWidgets.QLabel(self.labelsArea)
        self.labelHeight.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelHeight.setIndent(40)
        self.labelHeight.setObjectName("labelHeight")
        self.horizontalLayout_3.addWidget(self.labelHeight)
        self.labelWidth = QtWidgets.QLabel(self.labelsArea)
        self.labelWidth.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelWidth.setIndent(54)
        self.labelWidth.setObjectName("labelWidth")
        self.horizontalLayout_3.addWidget(self.labelWidth)
        self.helpingEmptyWidget = QtWidgets.QWidget(self.labelsArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helpingEmptyWidget.sizePolicy().hasHeightForWidth())
        self.helpingEmptyWidget.setSizePolicy(sizePolicy)
        self.helpingEmptyWidget.setObjectName("helpingEmptyWidget")
        self.horizontalLayout_3.addWidget(self.helpingEmptyWidget)
        self.verticalLayout_2.addWidget(self.labelsArea)
        self.ChoiceArea = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChoiceArea.sizePolicy().hasHeightForWidth())
        self.ChoiceArea.setSizePolicy(sizePolicy)
        self.ChoiceArea.setObjectName("ChoiceArea")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.ChoiceArea)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButtonsArea = QtWidgets.QWidget(self.ChoiceArea)
        self.radioButtonsArea.setObjectName("radioButtonsArea")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.radioButtonsArea)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.beginnerButton = QtWidgets.QRadioButton(self.radioButtonsArea)
        self.beginnerButton.setObjectName("beginnerButton")
        self.verticalLayout_4.addWidget(self.beginnerButton)
        self.intermediateButton = QtWidgets.QRadioButton(self.radioButtonsArea)
        self.intermediateButton.setObjectName("intermediateButton")
        self.verticalLayout_4.addWidget(self.intermediateButton)
        self.expertButton = QtWidgets.QRadioButton(self.radioButtonsArea)
        self.expertButton.setObjectName("expertButton")
        self.verticalLayout_4.addWidget(self.expertButton)
        self.customButton = QtWidgets.QRadioButton(self.radioButtonsArea)
        self.customButton.setEnabled(True)
        self.customButton.setObjectName("customButton")
        self.verticalLayout_4.addWidget(self.customButton)
        self.horizontalLayout_2.addWidget(self.radioButtonsArea)
        self.widthArea = QtWidgets.QWidget(self.ChoiceArea)
        self.widthArea.setObjectName("widthArea")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widthArea)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widthBeginner = QtWidgets.QLabel(self.widthArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widthBeginner.sizePolicy().hasHeightForWidth())
        self.widthBeginner.setSizePolicy(sizePolicy)
        self.widthBeginner.setAlignment(QtCore.Qt.AlignCenter)
        self.widthBeginner.setObjectName("widthBeginner")
        self.verticalLayout_6.addWidget(self.widthBeginner)
        self.widthIntermediate = QtWidgets.QLabel(self.widthArea)
        self.widthIntermediate.setAlignment(QtCore.Qt.AlignCenter)
        self.widthIntermediate.setObjectName("widthIntermediate")
        self.verticalLayout_6.addWidget(self.widthIntermediate)
        self.widthExpert = QtWidgets.QLabel(self.widthArea)
        self.widthExpert.setAlignment(QtCore.Qt.AlignCenter)
        self.widthExpert.setObjectName("widthExpert")
        self.verticalLayout_6.addWidget(self.widthExpert)
        self.widthCustom = QtWidgets.QSpinBox(self.widthArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widthCustom.sizePolicy().hasHeightForWidth())
        self.widthCustom.setSizePolicy(sizePolicy)
        self.widthCustom.setAlignment(QtCore.Qt.AlignCenter)
        self.widthCustom.setMinimum(1)
        self.widthCustom.setMaximum(100)
        self.widthCustom.setProperty("value", 30)
        self.widthCustom.setObjectName("widthCustom")
        self.verticalLayout_6.addWidget(self.widthCustom)
        self.horizontalLayout_2.addWidget(self.widthArea)
        self.heightArea = QtWidgets.QWidget(self.ChoiceArea)
        self.heightArea.setObjectName("heightArea")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.heightArea)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.heightBeginner = QtWidgets.QLabel(self.heightArea)
        self.heightBeginner.setAlignment(QtCore.Qt.AlignCenter)
        self.heightBeginner.setObjectName("heightBeginner")
        self.verticalLayout_5.addWidget(self.heightBeginner)
        self.heightIntermediate = QtWidgets.QLabel(self.heightArea)
        self.heightIntermediate.setAlignment(QtCore.Qt.AlignCenter)
        self.heightIntermediate.setObjectName("heightIntermediate")
        self.verticalLayout_5.addWidget(self.heightIntermediate)
        self.heightExpert = QtWidgets.QLabel(self.heightArea)
        self.heightExpert.setAlignment(QtCore.Qt.AlignCenter)
        self.heightExpert.setObjectName("heightExpert")
        self.verticalLayout_5.addWidget(self.heightExpert)
        self.heightCustom = QtWidgets.QSpinBox(self.heightArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heightCustom.sizePolicy().hasHeightForWidth())
        self.heightCustom.setSizePolicy(sizePolicy)
        self.heightCustom.setAlignment(QtCore.Qt.AlignCenter)
        self.heightCustom.setMinimum(1)
        self.heightCustom.setMaximum(100)
        self.heightCustom.setProperty("value", 20)
        self.heightCustom.setObjectName("heightCustom")
        self.verticalLayout_5.addWidget(self.heightCustom)
        self.horizontalLayout_2.addWidget(self.heightArea)
        self.minesArea = QtWidgets.QWidget(self.ChoiceArea)
        self.minesArea.setObjectName("minesArea")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.minesArea)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.minesBeginner = QtWidgets.QLabel(self.minesArea)
        self.minesBeginner.setAlignment(QtCore.Qt.AlignCenter)
        self.minesBeginner.setObjectName("minesBeginner")
        self.verticalLayout_3.addWidget(self.minesBeginner)
        self.minesIntermediate = QtWidgets.QLabel(self.minesArea)
        self.minesIntermediate.setAlignment(QtCore.Qt.AlignCenter)
        self.minesIntermediate.setObjectName("minesIntermediate")
        self.verticalLayout_3.addWidget(self.minesIntermediate)
        self.minesExpert = QtWidgets.QLabel(self.minesArea)
        self.minesExpert.setAlignment(QtCore.Qt.AlignCenter)
        self.minesExpert.setObjectName("minesExpert")
        self.verticalLayout_3.addWidget(self.minesExpert)
        self.minesCustom = QtWidgets.QSpinBox(self.minesArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minesCustom.sizePolicy().hasHeightForWidth())
        self.minesCustom.setSizePolicy(sizePolicy)
        self.minesCustom.setAlignment(QtCore.Qt.AlignCenter)
        self.minesCustom.setMinimum(1)
        self.minesCustom.setMaximum(9999)
        self.minesCustom.setProperty("value", 99)
        self.minesCustom.setObjectName("minesCustom")
        self.verticalLayout_3.addWidget(self.minesCustom)
        self.horizontalLayout_2.addWidget(self.minesArea)
        self.verticalLayout_2.addWidget(self.ChoiceArea)
        self.newGameButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.newGameButton.setObjectName("newGameButton")
        self.verticalLayout_2.addWidget(self.newGameButton)
        self.scrollAreaNewGame.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollAreaNewGame)

        self.retranslateUi(NewGame)
        QtCore.QMetaObject.connectSlotsByName(NewGame)

    def retranslateUi(self, NewGame):
        _translate = QtCore.QCoreApplication.translate
        NewGame.setWindowTitle(_translate("NewGame", "New Game..."))
        self.labelMines.setText(_translate("NewGame", "Mines"))
        self.labelHeight.setText(_translate("NewGame", "Height"))
        self.labelWidth.setText(_translate("NewGame", "Width"))
        self.beginnerButton.setText(_translate("NewGame", "Beginner"))
        self.intermediateButton.setText(_translate("NewGame", "Intermediate"))
        self.expertButton.setText(_translate("NewGame", "Expert"))
        self.customButton.setText(_translate("NewGame", "Custom"))
        self.widthBeginner.setText(_translate("NewGame", "9"))
        self.widthIntermediate.setText(_translate("NewGame", "16"))
        self.widthExpert.setText(_translate("NewGame", "30"))
        self.heightBeginner.setText(_translate("NewGame", "9"))
        self.heightIntermediate.setText(_translate("NewGame", "16"))
        self.heightExpert.setText(_translate("NewGame", "16"))
        self.minesBeginner.setText(_translate("NewGame", "10"))
        self.minesIntermediate.setText(_translate("NewGame", "40"))
        self.minesExpert.setText(_translate("NewGame", "99"))
        self.newGameButton.setText(_translate("NewGame", "New Game"))
