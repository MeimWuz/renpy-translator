# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1463, 909)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.log_text = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.log_text.setGeometry(QtCore.QRect(630, 50, 821, 801))
        self.log_text.setReadOnly(True)
        self.log_text.setObjectName("log_text")
        self.clearLogBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clearLogBtn.setGeometry(QtCore.QRect(1010, 5, 75, 24))
        self.clearLogBtn.setObjectName("clearLogBtn")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 601, 311))
        self.widget.setObjectName("widget")
        self.translateBtn = QtWidgets.QPushButton(parent=self.widget)
        self.translateBtn.setGeometry(QtCore.QRect(280, 280, 75, 24))
        self.translateBtn.setObjectName("translateBtn")
        self.selectFilesBtn = QtWidgets.QPushButton(parent=self.widget)
        self.selectFilesBtn.setGeometry(QtCore.QRect(510, 25, 81, 41))
        self.selectFilesBtn.setObjectName("selectFilesBtn")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 102, 61, 31))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(30, 30, 31, 31))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.selectFilesText = QtWidgets.QTextEdit(parent=self.widget)
        self.selectFilesText.setGeometry(QtCore.QRect(100, 25, 411, 41))
        self.selectFilesText.setToolTip("")
        self.selectFilesText.setObjectName("selectFilesText")
        self.selectDirBtn = QtWidgets.QPushButton(parent=self.widget)
        self.selectDirBtn.setGeometry(QtCore.QRect(510, 100, 81, 41))
        self.selectDirBtn.setObjectName("selectDirBtn")
        self.selectDirText = QtWidgets.QTextEdit(parent=self.widget)
        self.selectDirText.setGeometry(QtCore.QRect(100, 100, 411, 41))
        self.selectDirText.setObjectName("selectDirText")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(280, 0, 71, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(parent=self.widget)
        self.label_9.setGeometry(QtCore.QRect(20, 160, 41, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.widget)
        self.label_10.setGeometry(QtCore.QRect(20, 205, 41, 31))
        self.label_10.setObjectName("label_10")
        self.targetComboBox = QtWidgets.QComboBox(parent=self.widget)
        self.targetComboBox.setGeometry(QtCore.QRect(100, 165, 491, 22))
        self.targetComboBox.setObjectName("targetComboBox")
        self.sourceComboBox = QtWidgets.QComboBox(parent=self.widget)
        self.sourceComboBox.setGeometry(QtCore.QRect(100, 210, 491, 22))
        self.sourceComboBox.setObjectName("sourceComboBox")
        self.multiTranslateCheckBox = QtWidgets.QCheckBox(parent=self.widget)
        self.multiTranslateCheckBox.setGeometry(QtCore.QRect(20, 240, 561, 31))
        self.multiTranslateCheckBox.setTristate(False)
        self.multiTranslateCheckBox.setObjectName("multiTranslateCheckBox")
        self.backupCheckBox = QtWidgets.QCheckBox(parent=self.widget)
        self.backupCheckBox.setGeometry(QtCore.QRect(20, 280, 231, 24))
        self.backupCheckBox.setObjectName("backupCheckBox")
        self.widget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(10, 320, 601, 311))
        self.widget_2.setObjectName("widget_2")
        self.selectFilesText_2 = QtWidgets.QTextEdit(parent=self.widget_2)
        self.selectFilesText_2.setGeometry(QtCore.QRect(100, 40, 411, 41))
        self.selectFilesText_2.setToolTip("")
        self.selectFilesText_2.setObjectName("selectFilesText_2")
        self.label_5 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(20, 45, 31, 31))
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.selectFilesBtn_2 = QtWidgets.QPushButton(parent=self.widget_2)
        self.selectFilesBtn_2.setGeometry(QtCore.QRect(510, 40, 81, 41))
        self.selectFilesBtn_2.setObjectName("selectFilesBtn_2")
        self.label_6 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(280, 10, 60, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.selectDirBtn_2 = QtWidgets.QPushButton(parent=self.widget_2)
        self.selectDirBtn_2.setGeometry(QtCore.QRect(510, 160, 81, 41))
        self.selectDirBtn_2.setObjectName("selectDirBtn_2")
        self.label_7 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(20, 165, 71, 31))
        self.label_7.setObjectName("label_7")
        self.selectDirText_2 = QtWidgets.QTextEdit(parent=self.widget_2)
        self.selectDirText_2.setGeometry(QtCore.QRect(100, 160, 411, 41))
        self.selectDirText_2.setObjectName("selectDirText_2")
        self.extractBtn = QtWidgets.QPushButton(parent=self.widget_2)
        self.extractBtn.setGeometry(QtCore.QRect(270, 280, 75, 24))
        self.extractBtn.setObjectName("extractBtn")
        self.label_8 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(20, 235, 61, 31))
        self.label_8.setObjectName("label_8")
        self.tlNameText = QtWidgets.QTextEdit(parent=self.widget_2)
        self.tlNameText.setGeometry(QtCore.QRect(100, 230, 491, 41))
        self.tlNameText.setObjectName("tlNameText")
        self.label_13 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_13.setGeometry(QtCore.QRect(20, 105, 81, 31))
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.selectDirsText = QtWidgets.QTextEdit(parent=self.widget_2)
        self.selectDirsText.setGeometry(QtCore.QRect(100, 100, 411, 41))
        self.selectDirsText.setToolTip("")
        self.selectDirsText.setObjectName("selectDirsText")
        self.selectDirsBtn = QtWidgets.QPushButton(parent=self.widget_2)
        self.selectDirsBtn.setGeometry(QtCore.QRect(510, 100, 81, 41))
        self.selectDirsBtn.setObjectName("selectDirsBtn")
        self.filterCheckBox = QtWidgets.QCheckBox(parent=self.widget_2)
        self.filterCheckBox.setGeometry(QtCore.QRect(20, 280, 161, 20))
        self.filterCheckBox.setObjectName("filterCheckBox")
        self.label_14 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_14.setGeometry(QtCore.QRect(380, 282, 131, 16))
        self.label_14.setObjectName("label_14")
        self.filterLengthLineEdit = QtWidgets.QLineEdit(parent=self.widget_2)
        self.filterLengthLineEdit.setGeometry(QtCore.QRect(510, 280, 61, 20))
        self.filterLengthLineEdit.setObjectName("filterLengthLineEdit")
        self.versionLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.versionLabel.setGeometry(QtCore.QRect(10, 860, 91, 16))
        self.versionLabel.setObjectName("versionLabel")
        self.copyrightLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.copyrightLabel.setGeometry(QtCore.QRect(1190, 860, 241, 16))
        self.copyrightLabel.setObjectName("copyrightLabel")
        self.widget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(10, 630, 601, 221))
        self.widget_3.setObjectName("widget_3")
        self.label_11 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_11.setGeometry(QtCore.QRect(280, 0, 60, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.selectFontText = QtWidgets.QTextEdit(parent=self.widget_3)
        self.selectFontText.setGeometry(QtCore.QRect(100, 100, 411, 41))
        self.selectFontText.setObjectName("selectFontText")
        self.label_4 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(20, 105, 30, 31))
        self.label_4.setObjectName("label_4")
        self.selectFontBtn = QtWidgets.QPushButton(parent=self.widget_3)
        self.selectFontBtn.setGeometry(QtCore.QRect(510, 100, 81, 41))
        self.selectFontBtn.setObjectName("selectFontBtn")
        self.replaceFontBtn = QtWidgets.QPushButton(parent=self.widget_3)
        self.replaceFontBtn.setGeometry(QtCore.QRect(270, 150, 75, 24))
        self.replaceFontBtn.setObjectName("replaceFontBtn")
        self.openFontStyleBtn = QtWidgets.QPushButton(parent=self.widget_3)
        self.openFontStyleBtn.setGeometry(QtCore.QRect(230, 190, 161, 24))
        self.openFontStyleBtn.setObjectName("openFontStyleBtn")
        self.label_12 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_12.setGeometry(QtCore.QRect(20, 40, 61, 31))
        self.label_12.setObjectName("label_12")
        self.selectDirText_3 = QtWidgets.QTextEdit(parent=self.widget_3)
        self.selectDirText_3.setGeometry(QtCore.QRect(100, 38, 411, 41))
        self.selectDirText_3.setObjectName("selectDirText_3")
        self.selectDirBtn_3 = QtWidgets.QPushButton(parent=self.widget_3)
        self.selectDirBtn_3.setGeometry(QtCore.QRect(510, 38, 81, 41))
        self.selectDirBtn_3.setObjectName("selectDirBtn_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1463, 22))
        self.menubar.setObjectName("menubar")
        self.aboutMenu = QtWidgets.QMenu(parent=self.menubar)
        self.aboutMenu.setObjectName("aboutMenu")
        self.proxyMenu = QtWidgets.QMenu(parent=self.menubar)
        self.proxyMenu.setObjectName("proxyMenu")
        self.translationEngineMenu = QtWidgets.QMenu(parent=self.menubar)
        self.translationEngineMenu.setObjectName("translationEngineMenu")
        MainWindow.setMenuBar(self.menubar)
        self.actioncopyright = QtGui.QAction(parent=MainWindow)
        self.actioncopyright.setObjectName("actioncopyright")
        self.proxySettings = QtGui.QAction(parent=MainWindow)
        self.proxySettings.setObjectName("proxySettings")
        self.engineSettings = QtGui.QAction(parent=MainWindow)
        self.engineSettings.setObjectName("engineSettings")
        self.aboutMenu.addAction(self.actioncopyright)
        self.proxyMenu.addAction(self.proxySettings)
        self.translationEngineMenu.addAction(self.engineSettings)
        self.menubar.addAction(self.aboutMenu.menuAction())
        self.menubar.addAction(self.proxyMenu.menuAction())
        self.menubar.addAction(self.translationEngineMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ren\'py Translator"))
        self.clearLogBtn.setText(_translate("MainWindow", "clear log"))
        self.translateBtn.setText(_translate("MainWindow", "translate"))
        self.selectFilesBtn.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "directory"))
        self.label.setText(_translate("MainWindow", "file(s)"))
        self.selectFilesText.setPlaceholderText(_translate("MainWindow", "input or choose or drag the file(s) you want to translate here. Examaple : F:\\GameName\\game\\tl\\language\\script.rpy"))
        self.selectDirBtn.setText(_translate("MainWindow", "..."))
        self.selectDirText.setPlaceholderText(_translate("MainWindow", "input or choose or drag the directory you want translate here.  Example:F:\\GameName\\game\\tl\\language"))
        self.label_3.setText(_translate("MainWindow", "translation"))
        self.label_9.setText(_translate("MainWindow", "target"))
        self.label_10.setText(_translate("MainWindow", "source"))
        self.multiTranslateCheckBox.setText(_translate("MainWindow", "Multi-Translate (If disabled translation will continue after the previous file has been translated)"))
        self.backupCheckBox.setText(_translate("MainWindow", "Generate Backup Files (xxx.rpy.bak)"))
        self.selectFilesText_2.setPlaceholderText(_translate("MainWindow", "input or choose or drag the file(s) you want to extract here.    Examaple : F:\\GameName\\game\\script.rpy"))
        self.label_5.setText(_translate("MainWindow", "file(s)"))
        self.selectFilesBtn_2.setText(_translate("MainWindow", "..."))
        self.label_6.setText(_translate("MainWindow", "extraction"))
        self.selectDirBtn_2.setText(_translate("MainWindow", "..."))
        self.label_7.setText(_translate("MainWindow", "tl directory"))
        self.selectDirText_2.setPlaceholderText(_translate("MainWindow", "input or choose or drag the directory you want to translate here.  Example:F:\\GameName\\game\\tl\\language"))
        self.extractBtn.setText(_translate("MainWindow", "extract"))
        self.label_8.setText(_translate("MainWindow", "tl name"))
        self.tlNameText.setPlaceholderText(_translate("MainWindow", "only force needs in file(s)/directory(s) mode , for tl directory , fill nothing is acceptable. input the directory name under game\\tl  Example: japanese or chinese"))
        self.label_13.setText(_translate("MainWindow", "directory(s)"))
        self.selectDirsText.setPlaceholderText(_translate("MainWindow", "input or choose or drag the directory(s) you want to extract here.    Examaple : F:\\GameName\\game\\character"))
        self.selectDirsBtn.setText(_translate("MainWindow", "..."))
        self.filterCheckBox.setText(_translate("MainWindow", "Enable filter for extract"))
        self.label_14.setText(_translate("MainWindow", "filter length less than"))
        self.versionLabel.setText(_translate("MainWindow", "Version 1.7.0"))
        self.copyrightLabel.setText(_translate("MainWindow", "©2024 Last moment,All rights reserved."))
        self.label_11.setText(_translate("MainWindow", "font"))
        self.selectFontText.setPlaceholderText(_translate("MainWindow", "input or choose or drag the font which supports the language after translation. Example : DejaVuSans.ttf (ren\'py \'s default font)"))
        self.label_4.setText(_translate("MainWindow", "font"))
        self.selectFontBtn.setText(_translate("MainWindow", "..."))
        self.replaceFontBtn.setText(_translate("MainWindow", "replace font"))
        self.openFontStyleBtn.setText(_translate("MainWindow", "open font style file"))
        self.label_12.setText(_translate("MainWindow", "directory"))
        self.selectDirText_3.setPlaceholderText(_translate("MainWindow", "input or choose or drag the directory you want to replace font here.  Example:F:\\GameName\\game\\tl\\language"))
        self.selectDirBtn_3.setText(_translate("MainWindow", "..."))
        self.aboutMenu.setTitle(_translate("MainWindow", "about"))
        self.proxyMenu.setTitle(_translate("MainWindow", "proxy"))
        self.translationEngineMenu.setTitle(_translate("MainWindow", "translation engine"))
        self.actioncopyright.setText(_translate("MainWindow", "copyright"))
        self.proxySettings.setText(_translate("MainWindow", "proxy settings"))
        self.engineSettings.setText(_translate("MainWindow", "engine settings"))
