# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'engine.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_EngineDialog(object):
    def setupUi(self, EngineDialog):
        if not EngineDialog.objectName():
            EngineDialog.setObjectName(u"EngineDialog")
        EngineDialog.resize(1011, 510)
        self.engineComboBox = QComboBox(EngineDialog)
        self.engineComboBox.setObjectName(u"engineComboBox")
        self.engineComboBox.setGeometry(QRect(240, 20, 491, 22))
        self.label = QLabel(EngineDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 12, 221, 31))
        self.label.setWordWrap(True)
        self.label_2 = QLabel(EngineDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 65, 211, 31))
        self.label_2.setWordWrap(True)
        self.keyEdit = QLineEdit(EngineDialog)
        self.keyEdit.setObjectName(u"keyEdit")
        self.keyEdit.setGeometry(QRect(240, 68, 491, 20))
        self.label_3 = QLabel(EngineDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 117, 211, 31))
        self.label_3.setWordWrap(True)
        self.secretEdit = QLineEdit(EngineDialog)
        self.secretEdit.setObjectName(u"secretEdit")
        self.secretEdit.setGeometry(QRect(240, 120, 491, 20))
        self.confirmButton = QPushButton(EngineDialog)
        self.confirmButton.setObjectName(u"confirmButton")
        self.confirmButton.setGeometry(QRect(20, 160, 981, 24))
        self.detailLabel = QLabel(EngineDialog)
        self.detailLabel.setObjectName(u"detailLabel")
        self.detailLabel.setGeometry(QRect(740, 11, 261, 41))
        font = QFont()
        font.setUnderline(True)
        self.detailLabel.setFont(font)
        self.detailLabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.detailLabel.setAlignment(Qt.AlignCenter)
        self.detailLabel.setWordWrap(True)
        self.rpmEdit = QLineEdit(EngineDialog)
        self.rpmEdit.setObjectName(u"rpmEdit")
        self.rpmEdit.setGeometry(QRect(250, 210, 71, 20))
        self.label_4 = QLabel(EngineDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 199, 241, 41))
        self.label_4.setWordWrap(True)
        self.label_5 = QLabel(EngineDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(340, 199, 201, 41))
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5.setWordWrap(True)
        self.rpsEdit = QLineEdit(EngineDialog)
        self.rpsEdit.setObjectName(u"rpsEdit")
        self.rpsEdit.setGeometry(QRect(630, 210, 371, 20))
        self.label_6 = QLabel(EngineDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 230, 231, 41))
        self.label_6.setWordWrap(True)
        self.tpmEdit = QLineEdit(EngineDialog)
        self.tpmEdit.setObjectName(u"tpmEdit")
        self.tpmEdit.setGeometry(QRect(250, 240, 71, 20))
        self.modelComboBox = QComboBox(EngineDialog)
        self.modelComboBox.setObjectName(u"modelComboBox")
        self.modelComboBox.setGeometry(QRect(750, 240, 251, 22))
        self.label_7 = QLabel(EngineDialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(340, 229, 101, 41))
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_7.setWordWrap(True)
        self.label_8 = QLabel(EngineDialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 270, 131, 20))
        self.label_8.setWordWrap(True)
        self.baseUrlEdit = QLineEdit(EngineDialog)
        self.baseUrlEdit.setObjectName(u"baseUrlEdit")
        self.baseUrlEdit.setGeometry(QRect(160, 270, 841, 20))
        self.customButton = QPushButton(EngineDialog)
        self.customButton.setObjectName(u"customButton")
        self.customButton.setGeometry(QRect(460, 240, 281, 24))
        self.label_9 = QLabel(EngineDialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 300, 601, 61))
        self.label_9.setWordWrap(True)
        self.timeoutEdit = QLineEdit(EngineDialog)
        self.timeoutEdit.setObjectName(u"timeoutEdit")
        self.timeoutEdit.setGeometry(QRect(620, 310, 381, 31))
        self.timeoutEdit.setText(u"")
        self.label_10 = QLabel(EngineDialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 380, 981, 81))
        self.label_10.setWordWrap(True)
        self.maxLengthEdit = QLineEdit(EngineDialog)
        self.maxLengthEdit.setObjectName(u"maxLengthEdit")
        self.maxLengthEdit.setGeometry(QRect(20, 465, 981, 31))
        self.maxLengthEdit.setText(u"5000")
        self.maxLengthEdit.setAlignment(Qt.AlignCenter)
        self.detectButton = QPushButton(EngineDialog)
        self.detectButton.setObjectName(u"detectButton")
        self.detectButton.setGeometry(QRect(750, 70, 251, 71))
        self.customPromptButton = QPushButton(EngineDialog)
        self.customPromptButton.setObjectName(u"customPromptButton")
        self.customPromptButton.setGeometry(QRect(20, 350, 981, 41))

        self.retranslateUi(EngineDialog)

        QMetaObject.connectSlotsByName(EngineDialog)
    # setupUi

    def retranslateUi(self, EngineDialog):
        EngineDialog.setWindowTitle(QCoreApplication.translate("EngineDialog", u"Translation Engine Settings", None))
        self.label.setText(QCoreApplication.translate("EngineDialog", u"Active Translation Engine:", None))
        self.label_2.setText(QCoreApplication.translate("EngineDialog", u"API_KEY:", None))
        self.label_3.setText(QCoreApplication.translate("EngineDialog", u"APP_SECRET:", None))
        self.secretEdit.setText("")
        self.confirmButton.setText(QCoreApplication.translate("EngineDialog", u"Confirm", None))
        self.detailLabel.setText(QCoreApplication.translate("EngineDialog", u"detail information", None))
        self.rpmEdit.setText(QCoreApplication.translate("EngineDialog", u"3", None))
        self.label_4.setText(QCoreApplication.translate("EngineDialog", u"RPM (requests per minute):", None))
        self.label_5.setText(QCoreApplication.translate("EngineDialog", u"RPS (requests per second):", None))
        self.rpsEdit.setText(QCoreApplication.translate("EngineDialog", u"3", None))
        self.label_6.setText(QCoreApplication.translate("EngineDialog", u"TPM (requests token limits):", None))
        self.tpmEdit.setText(QCoreApplication.translate("EngineDialog", u"40000", None))
        self.label_7.setText(QCoreApplication.translate("EngineDialog", u"model:", None))
        self.label_8.setText(QCoreApplication.translate("EngineDialog", u"base_url:", None))
        self.baseUrlEdit.setText("")
        self.baseUrlEdit.setPlaceholderText(QCoreApplication.translate("EngineDialog", u"http://my.test.server.example.com:8083", None))
        self.customButton.setText(QCoreApplication.translate("EngineDialog", u"custom model", None))
        self.label_9.setText(QCoreApplication.translate("EngineDialog", u"time_out (The max time wait for each request .for gpt-3.5 it's recommended to 120s , for gpt-4 it's recommened to 240s) :", None))
        self.label_10.setText(QCoreApplication.translate("EngineDialog", u"max_length (The max character length for each request. The actual limit unit of openai is token which is normally a word. But it'hard to define,so use max_length as a replacement. The max tokens of openai are 4096 for each request. Make sure the token is under the exceed limit , my suggestion is to set to 5000)", None))
#if QT_CONFIG(tooltip)
        self.detectButton.setToolTip(QCoreApplication.translate("EngineDialog", u"The proxy server will not take effect for network detection, If you use a proxy server, the result of detecting inaccessibility here may not be accurate", None))
#endif // QT_CONFIG(tooltip)
        self.detectButton.setText(QCoreApplication.translate("EngineDialog", u"detect network delay", None))
#if QT_CONFIG(tooltip)
        self.customPromptButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.customPromptButton.setText(QCoreApplication.translate("EngineDialog", u"Custom Prompt Template", None))
    # retranslateUi

