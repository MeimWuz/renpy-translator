# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1411, 856)
        self.actioncopyright = QAction(MainWindow)
        self.actioncopyright.setObjectName(u"actioncopyright")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(750, 30, 711, 511))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.log_text = QTextEdit(self.centralwidget)
        self.log_text.setObjectName(u"log_text")
        self.log_text.setGeometry(QRect(580, 35, 821, 761))
        self.log_text.setReadOnly(True)
        self.clearLogBtn = QPushButton(self.centralwidget)
        self.clearLogBtn.setObjectName(u"clearLogBtn")
        self.clearLogBtn.setGeometry(QRect(960, 5, 75, 24))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 571, 271))
        self.translateBtn = QPushButton(self.widget)
        self.translateBtn.setObjectName(u"translateBtn")
        self.translateBtn.setGeometry(QRect(240, 240, 75, 24))
        self.selectFilesBtn = QPushButton(self.widget)
        self.selectFilesBtn.setObjectName(u"selectFilesBtn")
        self.selectFilesBtn.setGeometry(QRect(480, 25, 81, 41))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 102, 61, 31))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 31, 31))
        self.label.setWordWrap(True)
        self.selectFilesText = QTextEdit(self.widget)
        self.selectFilesText.setObjectName(u"selectFilesText")
        self.selectFilesText.setGeometry(QRect(70, 25, 411, 41))
        self.selectDirBtn = QPushButton(self.widget)
        self.selectDirBtn.setObjectName(u"selectDirBtn")
        self.selectDirBtn.setGeometry(QRect(480, 100, 81, 41))
        self.selectDirText = QTextEdit(self.widget)
        self.selectDirText.setObjectName(u"selectDirText")
        self.selectDirText.setGeometry(QRect(70, 100, 411, 41))
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 0, 71, 20))
        font = QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 160, 41, 31))
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 205, 41, 31))
        self.targetComboBox = QComboBox(self.widget)
        self.targetComboBox.setObjectName(u"targetComboBox")
        self.targetComboBox.setGeometry(QRect(70, 165, 491, 22))
        self.sourceComboBox = QComboBox(self.widget)
        self.sourceComboBox.setObjectName(u"sourceComboBox")
        self.sourceComboBox.setGeometry(QRect(70, 210, 491, 22))
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 290, 571, 271))
        self.selectFilesText_2 = QTextEdit(self.widget_2)
        self.selectFilesText_2.setObjectName(u"selectFilesText_2")
        self.selectFilesText_2.setGeometry(QRect(70, 40, 411, 41))
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 45, 31, 31))
        self.label_5.setWordWrap(True)
        self.selectFilesBtn_2 = QPushButton(self.widget_2)
        self.selectFilesBtn_2.setObjectName(u"selectFilesBtn_2")
        self.selectFilesBtn_2.setGeometry(QRect(480, 40, 81, 41))
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(250, 10, 60, 20))
        self.label_6.setFont(font)
        self.selectDirBtn_2 = QPushButton(self.widget_2)
        self.selectDirBtn_2.setObjectName(u"selectDirBtn_2")
        self.selectDirBtn_2.setGeometry(QRect(480, 110, 81, 41))
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 115, 61, 31))
        self.selectDirText_2 = QTextEdit(self.widget_2)
        self.selectDirText_2.setObjectName(u"selectDirText_2")
        self.selectDirText_2.setGeometry(QRect(70, 110, 411, 41))
        self.extractBtn = QPushButton(self.widget_2)
        self.extractBtn.setObjectName(u"extractBtn")
        self.extractBtn.setGeometry(QRect(240, 230, 75, 24))
        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 185, 61, 31))
        self.tlNameText = QTextEdit(self.widget_2)
        self.tlNameText.setObjectName(u"tlNameText")
        self.tlNameText.setGeometry(QRect(70, 180, 491, 41))
        self.versionLabel = QLabel(self.centralwidget)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setGeometry(QRect(10, 810, 91, 16))
        self.copyrightLabel = QLabel(self.centralwidget)
        self.copyrightLabel.setObjectName(u"copyrightLabel")
        self.copyrightLabel.setGeometry(QRect(1140, 810, 241, 16))
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 580, 571, 221))
        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(250, 0, 60, 20))
        self.label_11.setFont(font)
        self.selectFontText = QTextEdit(self.widget_3)
        self.selectFontText.setObjectName(u"selectFontText")
        self.selectFontText.setGeometry(QRect(70, 100, 411, 41))
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 105, 30, 31))
        self.selectFontBtn = QPushButton(self.widget_3)
        self.selectFontBtn.setObjectName(u"selectFontBtn")
        self.selectFontBtn.setGeometry(QRect(480, 100, 81, 41))
        self.replaceFontBtn = QPushButton(self.widget_3)
        self.replaceFontBtn.setObjectName(u"replaceFontBtn")
        self.replaceFontBtn.setGeometry(QRect(240, 150, 75, 24))
        self.openFontStyleBtn = QPushButton(self.widget_3)
        self.openFontStyleBtn.setObjectName(u"openFontStyleBtn")
        self.openFontStyleBtn.setGeometry(QRect(200, 190, 161, 24))
        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 40, 61, 31))
        self.selectDirText_3 = QTextEdit(self.widget_3)
        self.selectDirText_3.setObjectName(u"selectDirText_3")
        self.selectDirText_3.setGeometry(QRect(70, 38, 411, 41))
        self.selectDirBtn_3 = QPushButton(self.widget_3)
        self.selectDirBtn_3.setObjectName(u"selectDirBtn_3")
        self.selectDirBtn_3.setGeometry(QRect(480, 38, 81, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1411, 22))
        self.aboutMenu = QMenu(self.menubar)
        self.aboutMenu.setObjectName(u"aboutMenu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.aboutMenu.menuAction())
        self.aboutMenu.addAction(self.actioncopyright)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ren'py Translator", None))
        self.actioncopyright.setText(QCoreApplication.translate("MainWindow", u"copyright", None))
        self.clearLogBtn.setText(QCoreApplication.translate("MainWindow", u"clear log", None))
        self.translateBtn.setText(QCoreApplication.translate("MainWindow", u"translate", None))
        self.selectFilesBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"directory", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"file(s)", None))
#if QT_CONFIG(tooltip)
        self.selectFilesText.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.selectFilesText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input or choose or drag the file(s) you want to translate here. Examaple : F:\\GameName\\game\\tl\\language\\script.rpy", None))
        self.selectDirBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.selectDirText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input or choose or drag the directory you want translate here.  Example:F:\\GameName\\game\\tl\\language", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"translation", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"target", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"source", None))
#if QT_CONFIG(tooltip)
        self.selectFilesText_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.selectFilesText_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input or choose or drag the file(s) you want to extract here.    Examaple : F:\\GameName\\game\\script.rpy", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"file(s)", None))
        self.selectFilesBtn_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"extraction", None))
        self.selectDirBtn_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"directory", None))
        self.selectDirText_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input or choose or drag the directory you want to translate here.  Example:F:\\GameName\\game\\tl\\language", None))
        self.extractBtn.setText(QCoreApplication.translate("MainWindow", u"extract", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"tl name", None))
        self.tlNameText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"only needs in file(s) mode,if you input the directory , just fill nothing.                   input the directory name under game\\tl  Example: japanese or chinese  or  german", None))
        self.versionLabel.setText(QCoreApplication.translate("MainWindow", u"Version 1.2.5", None))
        self.copyrightLabel.setText(QCoreApplication.translate("MainWindow", u"\u00a92024 Last moment,All rights reserved.", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"font", None))
        self.selectFontText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input or choose or drag the font which supports the language after translation. Example : DejaVuSans.ttf (ren'py 's default font)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"font", None))
        self.selectFontBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.replaceFontBtn.setText(QCoreApplication.translate("MainWindow", u"replace font", None))
        self.openFontStyleBtn.setText(QCoreApplication.translate("MainWindow", u"open font style file", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"directory", None))
        self.selectDirText_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"input or choose or drag the directory you want to replace font here.  Example:F:\\GameName\\game\\tl\\language", None))
        self.selectDirBtn_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.aboutMenu.setTitle(QCoreApplication.translate("MainWindow", u"about", None))
    # retranslateUi

