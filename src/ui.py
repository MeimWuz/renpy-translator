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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1051, 512)
        self.actioncopyright = QAction(MainWindow)
        self.actioncopyright.setObjectName(u"actioncopyright")
        self.proxySettings = QAction(MainWindow)
        self.proxySettings.setObjectName(u"proxySettings")
        self.engineSettings = QAction(MainWindow)
        self.engineSettings.setObjectName(u"engineSettings")
        self.customEngineSettings = QAction(MainWindow)
        self.customEngineSettings.setObjectName(u"customEngineSettings")
        self.actionedit = QAction(MainWindow)
        self.actionedit.setObjectName(u"actionedit")
        self.actionEnglish = QAction(MainWindow)
        self.actionEnglish.setObjectName(u"actionEnglish")
        self.actionEnglish.setText(u"English")
        self.actionChinese = QAction(MainWindow)
        self.actionChinese.setObjectName(u"actionChinese")
        self.actionChinese.setText(u"Chinese")
        self.actionJapanese = QAction(MainWindow)
        self.actionJapanese.setObjectName(u"actionJapanese")
        self.actionJapanese.setText(u"Japanese")
        self.actionSpanish = QAction(MainWindow)
        self.actionSpanish.setObjectName(u"actionSpanish")
        self.actionSpanish.setText(u"Spanish")
        self.actionPortuguese = QAction(MainWindow)
        self.actionPortuguese.setObjectName(u"actionPortuguese")
        self.actionPortuguese.setText(u"Portuguese")
        self.actionArabic = QAction(MainWindow)
        self.actionArabic.setObjectName(u"actionArabic")
        self.actionArabic.setText(u"Arabic")
        self.actionHindi = QAction(MainWindow)
        self.actionHindi.setObjectName(u"actionHindi")
        self.actionHindi.setText(u"Hindi")
        self.actionFrench = QAction(MainWindow)
        self.actionFrench.setObjectName(u"actionFrench")
        self.actionFrench.setText(u"French")
        self.actionBengali = QAction(MainWindow)
        self.actionBengali.setObjectName(u"actionBengali")
        self.actionBengali.setText(u"Bengali")
        self.actionRussian = QAction(MainWindow)
        self.actionRussian.setObjectName(u"actionRussian")
        self.actionRussian.setEnabled(True)
        self.actionRussian.setText(u"Russian")
        self.actionUrdu = QAction(MainWindow)
        self.actionUrdu.setObjectName(u"actionUrdu")
        self.actionUrdu.setText(u"Urdu")
        self.actionreplace_font = QAction(MainWindow)
        self.actionreplace_font.setObjectName(u"actionreplace_font")
        self.actionunpack_game = QAction(MainWindow)
        self.actionunpack_game.setObjectName(u"actionunpack_game")
        self.actionlight_amber = QAction(MainWindow)
        self.actionlight_amber.setObjectName(u"actionlight_amber")
        self.actionlight_amber.setText(u"light_amber")
        self.actionlight_blue = QAction(MainWindow)
        self.actionlight_blue.setObjectName(u"actionlight_blue")
        self.actionlight_blue.setText(u"light_blue")
        self.actionlight_cyan = QAction(MainWindow)
        self.actionlight_cyan.setObjectName(u"actionlight_cyan")
        self.actionlight_cyan.setText(u"light_cyan")
        self.actionlight_cyan_500 = QAction(MainWindow)
        self.actionlight_cyan_500.setObjectName(u"actionlight_cyan_500")
        self.actionlight_cyan_500.setText(u"light_cyan_500")
        self.actionlight_lightgreen = QAction(MainWindow)
        self.actionlight_lightgreen.setObjectName(u"actionlight_lightgreen")
        self.actionlight_lightgreen.setText(u"light_lightgreen")
        self.actionlight_pink = QAction(MainWindow)
        self.actionlight_pink.setObjectName(u"actionlight_pink")
        self.actionlight_pink.setText(u"light_pink")
        self.actionlight_purple = QAction(MainWindow)
        self.actionlight_purple.setObjectName(u"actionlight_purple")
        self.actionlight_purple.setText(u"light_purple")
        self.actionlight_red = QAction(MainWindow)
        self.actionlight_red.setObjectName(u"actionlight_red")
        self.actionlight_red.setText(u"light_red")
        self.actionlight_teal = QAction(MainWindow)
        self.actionlight_teal.setObjectName(u"actionlight_teal")
        self.actionlight_teal.setText(u"light_teal")
        self.actionlight_yellow = QAction(MainWindow)
        self.actionlight_yellow.setObjectName(u"actionlight_yellow")
        self.actionlight_yellow.setText(u"light_yellow")
        self.actiondark_amber = QAction(MainWindow)
        self.actiondark_amber.setObjectName(u"actiondark_amber")
        self.actiondark_amber.setText(u"dark_amber")
        self.actiondark_blue = QAction(MainWindow)
        self.actiondark_blue.setObjectName(u"actiondark_blue")
        self.actiondark_blue.setText(u"dark_blue")
        self.actiondark_cyan = QAction(MainWindow)
        self.actiondark_cyan.setObjectName(u"actiondark_cyan")
        self.actiondark_cyan.setText(u"dark_cyan")
        self.actiondark_lightgreen = QAction(MainWindow)
        self.actiondark_lightgreen.setObjectName(u"actiondark_lightgreen")
        self.actiondark_lightgreen.setText(u"dark_lightgreen")
        self.actiondark_pink = QAction(MainWindow)
        self.actiondark_pink.setObjectName(u"actiondark_pink")
        self.actiondark_pink.setText(u"dark_pink")
        self.actiondark_purple = QAction(MainWindow)
        self.actiondark_purple.setObjectName(u"actiondark_purple")
        self.actiondark_purple.setText(u"dark_purple")
        self.actiondark_red = QAction(MainWindow)
        self.actiondark_red.setObjectName(u"actiondark_red")
        self.actiondark_red.setText(u"dark_red")
        self.actiondark_teal = QAction(MainWindow)
        self.actiondark_teal.setObjectName(u"actiondark_teal")
        self.actiondark_teal.setText(u"dark_teal")
        self.actiondark_yellow = QAction(MainWindow)
        self.actiondark_yellow.setObjectName(u"actiondark_yellow")
        self.actiondark_yellow.setText(u"dark_yellow")
        self.actionextract_translation = QAction(MainWindow)
        self.actionextract_translation.setObjectName(u"actionextract_translation")
        self.actionruntime_extraction = QAction(MainWindow)
        self.actionruntime_extraction.setObjectName(u"actionruntime_extraction")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.clearLogBtn = QPushButton(self.centralwidget)
        self.clearLogBtn.setObjectName(u"clearLogBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearLogBtn.sizePolicy().hasHeightForWidth())
        self.clearLogBtn.setSizePolicy(sizePolicy)
        self.clearLogBtn.setMaximumSize(QSize(65535, 24))

        self.gridLayout.addWidget(self.clearLogBtn, 3, 1, 1, 2)

        self.copyrightLabel = QLabel(self.centralwidget)
        self.copyrightLabel.setObjectName(u"copyrightLabel")
        self.copyrightLabel.setMaximumSize(QSize(400, 16))

        self.gridLayout.addWidget(self.copyrightLabel, 4, 2, 1, 1)

        self.log_text = QTextEdit(self.centralwidget)
        self.log_text.setObjectName(u"log_text")
        self.log_text.setMinimumSize(QSize(100, 400))
        self.log_text.setMaximumSize(QSize(65535, 65535))
        self.log_text.setReadOnly(True)

        self.gridLayout.addWidget(self.log_text, 0, 1, 3, 2)

        self.versionLabel = QLabel(self.centralwidget)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setMaximumSize(QSize(91, 16))

        self.gridLayout.addWidget(self.versionLabel, 4, 0, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(600, 420))
        self.translateBtn = QPushButton(self.widget)
        self.translateBtn.setObjectName(u"translateBtn")
        self.translateBtn.setGeometry(QRect(384, 390, 181, 24))
        self.selectFilesBtn = QPushButton(self.widget)
        self.selectFilesBtn.setObjectName(u"selectFilesBtn")
        self.selectFilesBtn.setGeometry(QRect(490, 25, 81, 81))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 122, 81, 51))
        self.label_2.setWordWrap(True)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 30, 71, 61))
        self.label.setWordWrap(True)
        self.selectFilesText = QTextEdit(self.widget)
        self.selectFilesText.setObjectName(u"selectFilesText")
        self.selectFilesText.setGeometry(QRect(80, 25, 411, 81))
        self.selectDirBtn = QPushButton(self.widget)
        self.selectDirBtn.setObjectName(u"selectDirBtn")
        self.selectDirBtn.setGeometry(QRect(490, 110, 81, 81))
        self.selectDirText = QTextEdit(self.widget)
        self.selectDirText.setObjectName(u"selectDirText")
        self.selectDirText.setGeometry(QRect(80, 110, 411, 81))
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(260, 0, 141, 20))
        font = QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 190, 41, 41))
        self.label_9.setWordWrap(True)
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 230, 41, 41))
        self.label_10.setWordWrap(True)
        self.targetComboBox = QComboBox(self.widget)
        self.targetComboBox.setObjectName(u"targetComboBox")
        self.targetComboBox.setGeometry(QRect(80, 200, 491, 22))
        self.sourceComboBox = QComboBox(self.widget)
        self.sourceComboBox.setObjectName(u"sourceComboBox")
        self.sourceComboBox.setGeometry(QRect(80, 240, 491, 22))
        self.multiTranslateCheckBox = QCheckBox(self.widget)
        self.multiTranslateCheckBox.setObjectName(u"multiTranslateCheckBox")
        self.multiTranslateCheckBox.setGeometry(QRect(0, 340, 191, 31))
        self.multiTranslateCheckBox.setChecked(True)
        self.multiTranslateCheckBox.setTristate(False)
        self.backupCheckBox = QCheckBox(self.widget)
        self.backupCheckBox.setObjectName(u"backupCheckBox")
        self.backupCheckBox.setGeometry(QRect(0, 390, 481, 24))
        self.localGlossaryCheckBox = QCheckBox(self.widget)
        self.localGlossaryCheckBox.setObjectName(u"localGlossaryCheckBox")
        self.localGlossaryCheckBox.setGeometry(QRect(0, 300, 591, 20))
        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(260, 270, 131, 20))
        self.label_15.setMaximumSize(QSize(16777215, 20))
        self.originalRadioButton = QRadioButton(self.widget)
        self.originalRadioButton.setObjectName(u"originalRadioButton")
        self.originalRadioButton.setGeometry(QRect(390, 270, 101, 20))
        self.originalRadioButton.setMaximumSize(QSize(16777215, 20))
        self.currentRadioButton = QRadioButton(self.widget)
        self.currentRadioButton.setObjectName(u"currentRadioButton")
        self.currentRadioButton.setGeometry(QRect(490, 270, 111, 20))
        self.currentRadioButton.setMaximumSize(QSize(16777215, 20))
        self.currentRadioButton.setChecked(True)
        self.skipTranslatedCheckBox = QCheckBox(self.widget)
        self.skipTranslatedCheckBox.setObjectName(u"skipTranslatedCheckBox")
        self.skipTranslatedCheckBox.setGeometry(QRect(0, 270, 261, 20))
        self.skipTranslatedCheckBox.setChecked(True)
        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(190, 310, 411, 51))
        self.label_16.setWordWrap(True)

        self.gridLayout.addWidget(self.widget, 0, 0, 3, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1051, 22))
        self.aboutMenu = QMenu(self.menubar)
        self.aboutMenu.setObjectName(u"aboutMenu")
        self.proxyMenu = QMenu(self.menubar)
        self.proxyMenu.setObjectName(u"proxyMenu")
        self.translationEngineMenu = QMenu(self.menubar)
        self.translationEngineMenu.setObjectName(u"translationEngineMenu")
        self.advancedMenu = QMenu(self.menubar)
        self.advancedMenu.setObjectName(u"advancedMenu")
        self.menulanguage = QMenu(self.menubar)
        self.menulanguage.setObjectName(u"menulanguage")
        self.menutheme = QMenu(self.menubar)
        self.menutheme.setObjectName(u"menutheme")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.aboutMenu.menuAction())
        self.menubar.addAction(self.proxyMenu.menuAction())
        self.menubar.addAction(self.translationEngineMenu.menuAction())
        self.menubar.addAction(self.advancedMenu.menuAction())
        self.menubar.addAction(self.menulanguage.menuAction())
        self.menubar.addAction(self.menutheme.menuAction())
        self.aboutMenu.addAction(self.actioncopyright)
        self.proxyMenu.addAction(self.proxySettings)
        self.translationEngineMenu.addAction(self.engineSettings)
        self.translationEngineMenu.addAction(self.customEngineSettings)
        self.advancedMenu.addAction(self.actionedit)
        self.advancedMenu.addAction(self.actionruntime_extraction)
        self.advancedMenu.addAction(self.actionextract_translation)
        self.advancedMenu.addAction(self.actionreplace_font)
        self.advancedMenu.addAction(self.actionunpack_game)
        self.menulanguage.addAction(self.actionArabic)
        self.menulanguage.addAction(self.actionBengali)
        self.menulanguage.addAction(self.actionChinese)
        self.menulanguage.addAction(self.actionEnglish)
        self.menulanguage.addAction(self.actionFrench)
        self.menulanguage.addAction(self.actionHindi)
        self.menulanguage.addAction(self.actionJapanese)
        self.menulanguage.addAction(self.actionPortuguese)
        self.menulanguage.addAction(self.actionRussian)
        self.menulanguage.addAction(self.actionSpanish)
        self.menulanguage.addSeparator()
        self.menulanguage.addAction(self.actionUrdu)
        self.menutheme.addAction(self.actionlight_amber)
        self.menutheme.addAction(self.actionlight_blue)
        self.menutheme.addAction(self.actionlight_cyan)
        self.menutheme.addAction(self.actionlight_cyan_500)
        self.menutheme.addAction(self.actionlight_lightgreen)
        self.menutheme.addAction(self.actionlight_pink)
        self.menutheme.addAction(self.actionlight_purple)
        self.menutheme.addAction(self.actionlight_red)
        self.menutheme.addAction(self.actionlight_teal)
        self.menutheme.addAction(self.actionlight_yellow)
        self.menutheme.addAction(self.actiondark_amber)
        self.menutheme.addAction(self.actiondark_blue)
        self.menutheme.addAction(self.actiondark_cyan)
        self.menutheme.addAction(self.actiondark_lightgreen)
        self.menutheme.addAction(self.actiondark_pink)
        self.menutheme.addAction(self.actiondark_purple)
        self.menutheme.addAction(self.actiondark_red)
        self.menutheme.addAction(self.actiondark_teal)
        self.menutheme.addAction(self.actiondark_yellow)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ren'py Translator", None))
        self.actioncopyright.setText(QCoreApplication.translate("MainWindow", u"copyright", None))
        self.proxySettings.setText(QCoreApplication.translate("MainWindow", u"proxy settings", None))
        self.engineSettings.setText(QCoreApplication.translate("MainWindow", u"engine settings", None))
        self.customEngineSettings.setText(QCoreApplication.translate("MainWindow", u"custom engine", None))
        self.actionedit.setText(QCoreApplication.translate("MainWindow", u"edit from rpy", None))
        self.actionreplace_font.setText(QCoreApplication.translate("MainWindow", u"replace font", None))
        self.actionunpack_game.setText(QCoreApplication.translate("MainWindow", u"unpack game package", None))
        self.actionextract_translation.setText(QCoreApplication.translate("MainWindow", u"extract translation", None))
        self.actionruntime_extraction.setText(QCoreApplication.translate("MainWindow", u"runtime extraction", None))
        self.clearLogBtn.setText(QCoreApplication.translate("MainWindow", u"clear log", None))
        self.copyrightLabel.setText(QCoreApplication.translate("MainWindow", u"\u00a92024 Last moment,All rights reserved.", None))
        self.versionLabel.setText(QCoreApplication.translate("MainWindow", u"Version 2.0.2", None))
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
        self.multiTranslateCheckBox.setText(QCoreApplication.translate("MainWindow", u"Multi-threaded translation", None))
        self.backupCheckBox.setText(QCoreApplication.translate("MainWindow", u"Generate Backup Files (xxx.rpy.bak)", None))
        self.localGlossaryCheckBox.setText(QCoreApplication.translate("MainWindow", u"Local Glossary (replace certain words with preset content)", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Translation Source", None))
        self.originalRadioButton.setText(QCoreApplication.translate("MainWindow", u"Original", None))
        self.currentRadioButton.setText(QCoreApplication.translate("MainWindow", u"Current", None))
        self.skipTranslatedCheckBox.setText(QCoreApplication.translate("MainWindow", u"Skip Translated (Original != Current)", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"(If disable, translation will continue after the previous file has been translated)", None))
        self.aboutMenu.setTitle(QCoreApplication.translate("MainWindow", u"about", None))
        self.proxyMenu.setTitle(QCoreApplication.translate("MainWindow", u"proxy", None))
        self.translationEngineMenu.setTitle(QCoreApplication.translate("MainWindow", u"translation engine", None))
        self.advancedMenu.setTitle(QCoreApplication.translate("MainWindow", u"advanced options", None))
        self.menulanguage.setTitle(QCoreApplication.translate("MainWindow", u"language", None))
        self.menutheme.setTitle(QCoreApplication.translate("MainWindow", u"theme", None))
    # retranslateUi

