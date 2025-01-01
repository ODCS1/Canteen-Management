# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connection.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_dlgConnection(object):
    def setupUi(self, dlgConection):
        if not dlgConection.objectName():
            dlgConection.setObjectName(u"dlgConection")
        dlgConection.resize(497, 235)
        dlgConection.setMinimumSize(QSize(497, 235))
        dlgConection.setMaximumSize(QSize(497, 235))
        font = QFont()
        font.setPointSize(11)
        dlgConection.setFont(font)
        dlgConection.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.gridLayout = QGridLayout(dlgConection)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(dlgConection)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.edServer = QLineEdit(dlgConection)
        self.edServer.setObjectName(u"edServer")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edServer.sizePolicy().hasHeightForWidth())
        self.edServer.setSizePolicy(sizePolicy)
        self.edServer.setMinimumSize(QSize(0, 30))
        self.edServer.setFont(font)

        self.gridLayout.addWidget(self.edServer, 0, 1, 1, 2)

        self.label_2 = QLabel(dlgConection)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        self.edDatabase = QLineEdit(dlgConection)
        self.edDatabase.setObjectName(u"edDatabase")
        sizePolicy.setHeightForWidth(self.edDatabase.sizePolicy().hasHeightForWidth())
        self.edDatabase.setSizePolicy(sizePolicy)
        self.edDatabase.setMinimumSize(QSize(0, 30))
        self.edDatabase.setFont(font)

        self.gridLayout.addWidget(self.edDatabase, 1, 2, 1, 1)

        self.edPassword = QLineEdit(dlgConection)
        self.edPassword.setObjectName(u"edPassword")
        sizePolicy.setHeightForWidth(self.edPassword.sizePolicy().hasHeightForWidth())
        self.edPassword.setSizePolicy(sizePolicy)
        self.edPassword.setMinimumSize(QSize(0, 30))
        self.edPassword.setFont(font)
        self.edPassword.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.edPassword, 3, 2, 1, 1)

        self.label_4 = QLabel(dlgConection)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.edUser = QLineEdit(dlgConection)
        self.edUser.setObjectName(u"edUser")
        sizePolicy.setHeightForWidth(self.edUser.sizePolicy().hasHeightForWidth())
        self.edUser.setSizePolicy(sizePolicy)
        self.edUser.setMinimumSize(QSize(0, 30))
        self.edUser.setFont(font)

        self.gridLayout.addWidget(self.edUser, 2, 2, 1, 1)

        self.label_3 = QLabel(dlgConection)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(dlgConection)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStyleSheet(u"background-color: rgb(197, 197, 197);")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 3, Qt.AlignRight)


        self.retranslateUi(dlgConection)
        self.buttonBox.accepted.connect(dlgConection.accept)
        self.buttonBox.rejected.connect(dlgConection.reject)

        QMetaObject.connectSlotsByName(dlgConection)
    # setupUi

    def retranslateUi(self, dlgConection):
        dlgConection.setWindowTitle(QCoreApplication.translate("dlgConnection", u"Database Connection", None))
        self.label.setText(QCoreApplication.translate("dlgConnection", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Server:</span></p></body></html>", None))
        self.edServer.setText(QCoreApplication.translate("dlgConnection", u"NB\\SQLEXPRESS", None))
        self.edServer.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("dlgConnection", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Database:</span></p></body></html>", None))
        self.edDatabase.setText(QCoreApplication.translate("dlgConnection", u"Canteen", None))
        self.edPassword.setPlaceholderText(QCoreApplication.translate("dlgConnection", u"...", None))
        self.label_4.setText(QCoreApplication.translate("dlgConnection", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Password:</span></p></body></html>", None))
        self.edUser.setText(QCoreApplication.translate("dlgConnection", u"user-admin", None))
        self.edUser.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("dlgConnection", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">User:</span></p></body></html>", None))
    # retranslateUi

