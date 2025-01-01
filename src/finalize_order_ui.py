# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'finalize_order.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_FinalizeOrder(object):
    def setupUi(self, FinalizeOrder):
        if not FinalizeOrder.objectName():
            FinalizeOrder.setObjectName(u"FinalizeOrder")
        FinalizeOrder.resize(605, 420)
        FinalizeOrder.setMinimumSize(QSize(605, 420))
        FinalizeOrder.setMaximumSize(QSize(605, 420))
        FinalizeOrder.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.verticalLayout_6 = QVBoxLayout(FinalizeOrder)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(FinalizeOrder)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(63, 107, 235);\n"
"padding: 3px;\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label)

        self.frame = QFrame(FinalizeOrder)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:1px solid rgb(209, 209, 209);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(323, 0))
        self.frame_2.setMaximumSize(QSize(323, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.frame_2)
        self.frame_41.setObjectName(u"frame_41")
        sizePolicy1.setHeightForWidth(self.frame_41.sizePolicy().hasHeightForWidth())
        self.frame_41.setSizePolicy(sizePolicy1)
        self.frame_41.setStyleSheet(u"QFrame{\n"
"	border: 1px solid  rgb(20, 129, 10);\n"
"	background-color: rgb(23, 161, 13);\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: transparent;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"	border: none;\n"
"}")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.frame_41)
        self.label_29.setObjectName(u"label_29")
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.horizontalLayout_7.addWidget(self.label_29)

        self.edit_subtotal = QLineEdit(self.frame_41)
        self.edit_subtotal.setObjectName(u"edit_subtotal")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.edit_subtotal.sizePolicy().hasHeightForWidth())
        self.edit_subtotal.setSizePolicy(sizePolicy2)
        self.edit_subtotal.setMaximumSize(QSize(50, 16777215))
        self.edit_subtotal.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edit_subtotal.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.edit_subtotal)


        self.verticalLayout_4.addWidget(self.frame_41)

        self.frame_43 = QFrame(self.frame_2)
        self.frame_43.setObjectName(u"frame_43")
        sizePolicy1.setHeightForWidth(self.frame_43.sizePolicy().hasHeightForWidth())
        self.frame_43.setSizePolicy(sizePolicy1)
        self.frame_43.setStyleSheet(u"QFrame{\n"
"	border: 1px solid  rgb(20, 129, 10);\n"
"	background-color: rgb(170, 170, 127);\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: transparent;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"	border: none;\n"
"}")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.frame_43)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.horizontalLayout_8.addWidget(self.label_30)

        self.edit_total_paid = QLineEdit(self.frame_43)
        self.edit_total_paid.setObjectName(u"edit_total_paid")
        self.edit_total_paid.setMaximumSize(QSize(50, 16777215))
        self.edit_total_paid.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edit_total_paid.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.edit_total_paid)


        self.verticalLayout_4.addWidget(self.frame_43)

        self.frame_44 = QFrame(self.frame_2)
        self.frame_44.setObjectName(u"frame_44")
        sizePolicy1.setHeightForWidth(self.frame_44.sizePolicy().hasHeightForWidth())
        self.frame_44.setSizePolicy(sizePolicy1)
        self.frame_44.setStyleSheet(u"QFrame{\n"
"	border: 1px solid  rgb(20, 129, 10);\n"
"	background-color: rgb(85, 85, 127);\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: transparent;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"	border: none;\n"
"}")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.frame_44)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.horizontalLayout_9.addWidget(self.label_31)

        self.edit_change = QLineEdit(self.frame_44)
        self.edit_change.setObjectName(u"edit_change")
        self.edit_change.setMaximumSize(QSize(50, 16777215))
        self.edit_change.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edit_change.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.edit_change)


        self.verticalLayout_4.addWidget(self.frame_44)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(323, 0))
        self.frame_3.setMaximumSize(QSize(323, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgb(253, 195, 64);\n"
"padding: 3px;\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_2.addWidget(self.label_2)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tbl_finalized_products = QTableWidget(self.frame_5)
        if (self.tbl_finalized_products.columnCount() < 3):
            self.tbl_finalized_products.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_finalized_products.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_finalized_products.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_finalized_products.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tbl_finalized_products.setObjectName(u"tbl_finalized_products")
        self.tbl_finalized_products.setMaximumSize(QSize(16777215, 16777215))
        self.tbl_finalized_products.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_5.addWidget(self.tbl_finalized_products)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.edit_customer_value = QLineEdit(self.frame_6)
        self.edit_customer_value.setObjectName(u"edit_customer_value")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.edit_customer_value.sizePolicy().hasHeightForWidth())
        self.edit_customer_value.setSizePolicy(sizePolicy4)
        self.edit_customer_value.setMinimumSize(QSize(0, 30))
        self.edit_customer_value.setMaximumSize(QSize(16777215, 16777215))
        self.edit_customer_value.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.edit_customer_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.edit_customer_value)

        self.btn_customer_value = QPushButton(self.frame_6)
        self.btn_customer_value.setObjectName(u"btn_customer_value")
        self.btn_customer_value.setMinimumSize(QSize(90, 25))
        self.btn_customer_value.setMaximumSize(QSize(90, 25))
        self.btn_customer_value.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_customer_value.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(243, 243, 243);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(30, 114, 156);\n"
"}")

        self.verticalLayout_7.addWidget(self.btn_customer_value, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_45 = QFrame(self.frame_4)
        self.frame_45.setObjectName(u"frame_45")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_45.sizePolicy().hasHeightForWidth())
        self.frame_45.setSizePolicy(sizePolicy5)
        self.frame_45.setMaximumSize(QSize(16777215, 200))
        self.frame_45.setStyleSheet(u"QFrame{\n"
"	border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-right: 1px solid rgb(32, 32, 32);\n"
"	border-bottom: 1px solid rgb(32, 32, 32);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_45)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_90 = QLabel(self.frame_45)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setStyleSheet(u"border-color: transparent;")

        self.horizontalLayout.addWidget(self.label_90)

        self.frame_59 = QFrame(self.frame_45)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"}")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_59)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(-1, 0, -1, 9)
        self.edit_cpf_account = QLineEdit(self.frame_59)
        self.edit_cpf_account.setObjectName(u"edit_cpf_account")
        self.edit_cpf_account.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.edit_cpf_account.setReadOnly(True)

        self.verticalLayout_54.addWidget(self.edit_cpf_account)

        self.edit_phone_account = QLineEdit(self.frame_59)
        self.edit_phone_account.setObjectName(u"edit_phone_account")
        self.edit_phone_account.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.edit_phone_account.setReadOnly(True)

        self.verticalLayout_54.addWidget(self.edit_phone_account)

        self.edit_name_account = QLineEdit(self.frame_59)
        self.edit_name_account.setObjectName(u"edit_name_account")
        self.edit_name_account.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.edit_name_account.setReadOnly(True)

        self.verticalLayout_54.addWidget(self.edit_name_account)

        self.edit_balance_account = QLineEdit(self.frame_59)
        self.edit_balance_account.setObjectName(u"edit_balance_account")
        self.edit_balance_account.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.edit_balance_account.setReadOnly(True)

        self.verticalLayout_54.addWidget(self.edit_balance_account)


        self.horizontalLayout.addWidget(self.frame_59)


        self.verticalLayout_3.addWidget(self.frame_45)


        self.gridLayout.addWidget(self.frame_4, 0, 1, 2, 1)


        self.verticalLayout.addWidget(self.frame)


        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.frame_7 = QFrame(FinalizeOrder)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy3.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy3)
        self.frame_7.setMinimumSize(QSize(0, 50))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.btn_order_finalized = QPushButton(self.frame_7)
        self.btn_order_finalized.setObjectName(u"btn_order_finalized")
        self.btn_order_finalized.setGeometry(QRect(220, 10, 160, 30))
        self.btn_order_finalized.setMinimumSize(QSize(160, 30))
        self.btn_order_finalized.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_order_finalized.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(243, 243, 243);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(30, 114, 156);\n"
"}")

        self.verticalLayout_6.addWidget(self.frame_7)


        self.retranslateUi(FinalizeOrder)

        QMetaObject.connectSlotsByName(FinalizeOrder)
    # setupUi

    def retranslateUi(self, FinalizeOrder):
        FinalizeOrder.setWindowTitle(QCoreApplication.translate("FinalizeOrder", u"FinalizeOrder", None))
        self.label.setText(QCoreApplication.translate("FinalizeOrder", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">FINALIZING ORDER</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("FinalizeOrder", u"<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Subtotal R$</span></p></body></html>", None))
        self.edit_subtotal.setText(QCoreApplication.translate("FinalizeOrder", u"00.00", None))
        self.label_30.setText(QCoreApplication.translate("FinalizeOrder", u"<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Total Paid R$</span></p></body></html>", None))
        self.edit_total_paid.setText(QCoreApplication.translate("FinalizeOrder", u"00.00", None))
        self.label_31.setText(QCoreApplication.translate("FinalizeOrder", u"<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Change R$</span></p></body></html>", None))
        self.edit_change.setText(QCoreApplication.translate("FinalizeOrder", u"00.00", None))
        self.label_2.setText(QCoreApplication.translate("FinalizeOrder", u"<html><head/><body><p align=\"center\">ORDER ITEMS</p></body></html>", None))
        ___qtablewidgetitem = self.tbl_finalized_products.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FinalizeOrder", u"product", None));
        ___qtablewidgetitem1 = self.tbl_finalized_products.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FinalizeOrder", u"quantity", None));
        ___qtablewidgetitem2 = self.tbl_finalized_products.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FinalizeOrder", u"price /unit", None));
        self.edit_customer_value.setText("")
        self.edit_customer_value.setPlaceholderText(QCoreApplication.translate("FinalizeOrder", u"Customer Paid", None))
        self.btn_customer_value.setText(QCoreApplication.translate("FinalizeOrder", u"Confirm", None))
        self.label_90.setText(QCoreApplication.translate("FinalizeOrder", u"<html><head/><body><p align=\"center\"><img src=\":/icons/assets/account.png\"/></p></body></html>", None))
        self.edit_cpf_account.setText("")
        self.edit_cpf_account.setPlaceholderText(QCoreApplication.translate("FinalizeOrder", u"CPF - without user", None))
        self.edit_phone_account.setPlaceholderText(QCoreApplication.translate("FinalizeOrder", u"PHONE - without user", None))
        self.edit_name_account.setPlaceholderText(QCoreApplication.translate("FinalizeOrder", u"NAME - without user", None))
        self.edit_balance_account.setPlaceholderText(QCoreApplication.translate("FinalizeOrder", u"BALANCE - without user", None))
        self.btn_order_finalized.setText(QCoreApplication.translate("FinalizeOrder", u"CONFIRM", None))
    # retranslateUi

