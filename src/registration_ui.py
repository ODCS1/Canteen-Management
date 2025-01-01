# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registration.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(880, 668)
        MainWindow.setMinimumSize(QSize(880, 668))
        MainWindow.setMaximumSize(QSize(880, 668))
        MainWindow.setStyleSheet(u"background-color: rgb(12, 12, 12);\n"
"border: none;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border: none;\n"
"	font-family: Arial\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"")
        self.gridLayout_22 = QGridLayout(self.centralwidget)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(3, 3, 9, 0)
        self.left_menu = QFrame(self.centralwidget)
        self.left_menu.setObjectName(u"left_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_menu.sizePolicy().hasHeightForWidth())
        self.left_menu.setSizePolicy(sizePolicy)
        self.left_menu.setMaximumSize(QSize(9, 16777215))
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.left_menu)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_2 = QFrame(self.left_menu)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setBaseSize(QSize(0, 0))
        self.frame_2.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(178, 189, 198);\n"
"	border-radius: 5px;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(150, 159, 166);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(109, 116, 121);\n"
"}\n"
"\n"
"QLabel{\n"
"	background-color: rgb(178, 189, 198);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_25 = QFrame(self.frame_2)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(178, 189, 198);\n"
"	border-radius: 3px;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_25)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.frame_25)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy1)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/assets/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.btn_home)

        self.label_18 = QLabel(self.frame_25)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.label_18)


        self.verticalLayout_3.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_2)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(178, 189, 198);\n"
"	border-radius: 3px;\n"
"	padding: 2px;\n"
"}")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_26)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_accounts = QPushButton(self.frame_26)
        self.btn_accounts.setObjectName(u"btn_accounts")
        sizePolicy1.setHeightForWidth(self.btn_accounts.sizePolicy().hasHeightForWidth())
        self.btn_accounts.setSizePolicy(sizePolicy1)
        self.btn_accounts.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_accounts.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/accounts.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_accounts.setIcon(icon1)
        self.btn_accounts.setIconSize(QSize(32, 32))

        self.verticalLayout_5.addWidget(self.btn_accounts)

        self.label_19 = QLabel(self.frame_26)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.label_19)


        self.verticalLayout_3.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.frame_2)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(178, 189, 198);\n"
"	border-radius: 3px;\n"
"	padding: 2px;\n"
"}")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_27)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.btn_order = QPushButton(self.frame_27)
        self.btn_order.setObjectName(u"btn_order")
        sizePolicy1.setHeightForWidth(self.btn_order.sizePolicy().hasHeightForWidth())
        self.btn_order.setSizePolicy(sizePolicy1)
        self.btn_order.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_order.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(178, 189, 198);\n"
"	border-radius: 3px;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(150, 159, 166);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(109, 116, 121);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/list.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_order.setIcon(icon2)
        self.btn_order.setIconSize(QSize(32, 32))

        self.verticalLayout_31.addWidget(self.btn_order)

        self.label_20 = QLabel(self.frame_27)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_31.addWidget(self.label_20)


        self.verticalLayout_3.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_2)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(178, 189, 198);\n"
"	border-radius: 3px;\n"
"	padding: 2px;\n"
"}")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_28)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.btn_products = QPushButton(self.frame_28)
        self.btn_products.setObjectName(u"btn_products")
        sizePolicy1.setHeightForWidth(self.btn_products.sizePolicy().hasHeightForWidth())
        self.btn_products.setSizePolicy(sizePolicy1)
        self.btn_products.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/products.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_products.setIcon(icon3)
        self.btn_products.setIconSize(QSize(32, 32))

        self.verticalLayout_32.addWidget(self.btn_products)

        self.label_21 = QLabel(self.frame_28)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_32.addWidget(self.label_21)


        self.verticalLayout_3.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_2)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(178, 189, 198);\n"
"	border-radius: 3px;\n"
"	padding: 2px;\n"
"}")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_29)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.btn_cash = QPushButton(self.frame_29)
        self.btn_cash.setObjectName(u"btn_cash")
        sizePolicy1.setHeightForWidth(self.btn_cash.sizePolicy().hasHeightForWidth())
        self.btn_cash.setSizePolicy(sizePolicy1)
        self.btn_cash.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/assets/cash-machine.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_cash.setIcon(icon4)
        self.btn_cash.setIconSize(QSize(32, 32))

        self.verticalLayout_33.addWidget(self.btn_cash)

        self.label_30 = QLabel(self.frame_29)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_33.addWidget(self.label_30)


        self.verticalLayout_3.addWidget(self.frame_29)

        self.frame_46 = QFrame(self.frame_2)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(178, 189, 198);\n"
"	border-radius: 3px;\n"
"	padding: 2px;\n"
"}")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_46)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.btn_about = QPushButton(self.frame_46)
        self.btn_about.setObjectName(u"btn_about")
        sizePolicy1.setHeightForWidth(self.btn_about.sizePolicy().hasHeightForWidth())
        self.btn_about.setSizePolicy(sizePolicy1)
        self.btn_about.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/assets/information-button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_about.setIcon(icon5)
        self.btn_about.setIconSize(QSize(32, 32))

        self.verticalLayout_34.addWidget(self.btn_about)

        self.label_34 = QLabel(self.frame_46)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_34.addWidget(self.label_34)


        self.verticalLayout_3.addWidget(self.frame_46)

        self.frame_43 = QFrame(self.frame_2)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(178, 189, 198);\n"
"	border-radius: 3px;\n"
"	padding: 2px;\n"
"}")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_43)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.btn_exit = QPushButton(self.frame_43)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy1.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy1)
        self.btn_exit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/assets/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_exit.setIcon(icon6)
        self.btn_exit.setIconSize(QSize(32, 32))

        self.verticalLayout_35.addWidget(self.btn_exit)

        self.label_32 = QLabel(self.frame_43)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_35.addWidget(self.label_32)


        self.verticalLayout_3.addWidget(self.frame_43)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_7.addWidget(self.frame_2)


        self.gridLayout_22.addWidget(self.left_menu, 0, 0, 1, 1)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 9)
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_toggle = QPushButton(self.top_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_toggle.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"} \n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(62, 62, 62);\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/assets/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_toggle.setIcon(icon7)
        self.btn_toggle.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_toggle, 0, Qt.AlignLeft)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy2)
        self.main_frame.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.main_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_2 = QVBoxLayout(self.pg_home)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.graphicsView = QGraphicsView(self.pg_home)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setStyleSheet(u"background-image: url(:/icons/assets/canteen-logo.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"background-attachment: fixed;\n"
"")

        self.verticalLayout_2.addWidget(self.graphicsView)

        self.Pages.addWidget(self.pg_home)
        self.pg_register = QWidget()
        self.pg_register.setObjectName(u"pg_register")
        self.verticalLayout_8 = QVBoxLayout(self.pg_register)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tabWidget = QTabWidget(self.pg_register)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_register = QWidget()
        self.tab_register.setObjectName(u"tab_register")
        self.verticalLayout_11 = QVBoxLayout(self.tab_register)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_4 = QFrame(self.tab_register)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.lbs_cadastroConta = QLabel(self.frame_4)
        self.lbs_cadastroConta.setObjectName(u"lbs_cadastroConta")
        self.lbs_cadastroConta.setMaximumSize(QSize(16777215, 70))
        self.lbs_cadastroConta.setStyleSheet(u"border: 1px solid rgb(56, 56, 56);")
        self.lbs_cadastroConta.setIndent(-1)

        self.verticalLayout_14.addWidget(self.lbs_cadastroConta)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_8)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.txt_value = QLineEdit(self.frame_8)
        self.txt_value.setObjectName(u"txt_value")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.txt_value.sizePolicy().hasHeightForWidth())
        self.txt_value.setSizePolicy(sizePolicy3)
        self.txt_value.setMaximumSize(QSize(16777215, 30))
        self.txt_value.setStyleSheet(u"")
        self.txt_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_value, 1, 2, 1, 1)

        self.txt_phone = QLineEdit(self.frame_8)
        self.txt_phone.setObjectName(u"txt_phone")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.txt_phone.sizePolicy().hasHeightForWidth())
        self.txt_phone.setSizePolicy(sizePolicy4)
        self.txt_phone.setMaximumSize(QSize(150, 30))
        self.txt_phone.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_phone, 1, 1, 1, 1)

        self.txt_email = QLineEdit(self.frame_8)
        self.txt_email.setObjectName(u"txt_email")
        sizePolicy4.setHeightForWidth(self.txt_email.sizePolicy().hasHeightForWidth())
        self.txt_email.setSizePolicy(sizePolicy4)
        self.txt_email.setMaximumSize(QSize(16777215, 30))
        self.txt_email.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_email, 1, 0, 1, 1)

        self.txt_name = QLineEdit(self.frame_8)
        self.txt_name.setObjectName(u"txt_name")
        sizePolicy4.setHeightForWidth(self.txt_name.sizePolicy().hasHeightForWidth())
        self.txt_name.setSizePolicy(sizePolicy4)
        self.txt_name.setMaximumSize(QSize(450, 30))
        self.txt_name.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.txt_name.setStyleSheet(u"")
        self.txt_name.setAlignment(Qt.AlignCenter)
        self.txt_name.setReadOnly(False)

        self.gridLayout_2.addWidget(self.txt_name, 0, 0, 1, 2)

        self.txt_cpf = QLineEdit(self.frame_8)
        self.txt_cpf.setObjectName(u"txt_cpf")
        self.txt_cpf.setMaximumSize(QSize(16777215, 30))
        self.txt_cpf.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_cpf, 0, 2, 1, 1)

        self.btn_register = QPushButton(self.frame_8)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setMinimumSize(QSize(160, 30))
        self.btn_register.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_register.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 15px;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(243, 243, 243);\n"
"}")

        self.gridLayout_2.addWidget(self.btn_register, 2, 1, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_8)


        self.verticalLayout_11.addWidget(self.frame_4)

        self.tabWidget.addTab(self.tab_register, "")
        self.tab_accounts = QWidget()
        self.tab_accounts.setObjectName(u"tab_accounts")
        self.verticalLayout_10 = QVBoxLayout(self.tab_accounts)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_16 = QLabel(self.tab_accounts)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_10.addWidget(self.label_16)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tbl_accounts = QTableWidget(self.tab_accounts)
        if (self.tbl_accounts.columnCount() < 6):
            self.tbl_accounts.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_accounts.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_accounts.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_accounts.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_accounts.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_accounts.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_accounts.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tbl_accounts.setObjectName(u"tbl_accounts")
        self.tbl_accounts.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: rgb(148, 148, 148);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"MS Shell Dlg2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(252, 252, 252);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_5.addWidget(self.tbl_accounts)

        self.frame_3 = QFrame(self.tab_accounts)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(0, 24, 74);\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: rgb(230, 230, 230);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btn_update_account = QPushButton(self.frame_3)
        self.btn_update_account.setObjectName(u"btn_update_account")
        self.btn_update_account.setMinimumSize(QSize(120, 30))
        self.btn_update_account.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_update_account.setStyleSheet(u"QPushButton:hover{\n"
"	color: rbg(255, 255, 255);\n"
"	background-color: rgb(255, 170, 0);\n"
"}")

        self.verticalLayout_9.addWidget(self.btn_update_account)

        self.btn_delete_account = QPushButton(self.frame_3)
        self.btn_delete_account.setObjectName(u"btn_delete_account")
        self.btn_delete_account.setMinimumSize(QSize(120, 30))
        self.btn_delete_account.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_delete_account.setStyleSheet(u"QPushButton:hover{\n"
"	color: rbg(255, 255, 255);\n"
"	background-color: rgb(199, 66, 0);\n"
"}")

        self.verticalLayout_9.addWidget(self.btn_delete_account)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.tab_accounts, "")

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_register)
        self.pg_order = QWidget()
        self.pg_order.setObjectName(u"pg_order")
        self.gridLayout_19 = QGridLayout(self.pg_order)
        self.gridLayout_19.setSpacing(6)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(9, 9, 0, 9)
        self.label_17 = QLabel(self.pg_order)
        self.label_17.setObjectName(u"label_17")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy5)

        self.gridLayout_19.addWidget(self.label_17, 0, 1, 1, 1)

        self.label_10 = QLabel(self.pg_order)
        self.label_10.setObjectName(u"label_10")
        sizePolicy5.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy5)
        self.label_10.setMaximumSize(QSize(16777215, 70))
        self.label_10.setStyleSheet(u"")

        self.gridLayout_19.addWidget(self.label_10, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.pg_order)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 9, 3, -1)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QSize(200, 0))
        self.frame_6.setMaximumSize(QSize(200, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_6)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy5.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy5)
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_10)
        self.verticalLayout_20.setSpacing(3)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color: rgb(63, 107, 235);\n"
"padding: 3px;")

        self.verticalLayout_20.addWidget(self.label_5)

        self.frame_14 = QFrame(self.frame_10)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy6)
        self.frame_14.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_14)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.tbl_selected_products = QTableWidget(self.frame_14)
        if (self.tbl_selected_products.columnCount() < 2):
            self.tbl_selected_products.setColumnCount(2)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbl_selected_products.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbl_selected_products.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        self.tbl_selected_products.setObjectName(u"tbl_selected_products")
        self.tbl_selected_products.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_13.addWidget(self.tbl_selected_products)


        self.verticalLayout_20.addWidget(self.frame_14)


        self.verticalLayout_16.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy6.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy6)
        self.frame_11.setMaximumSize(QSize(16777215, 150))
        self.frame_11.setStyleSheet(u"background-color: transparent;\n"
"\n"
"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_11)
        self.verticalLayout_21.setSpacing(3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.frame_11)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy)
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_38)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.btn_decrease_2 = QPushButton(self.frame_38)
        self.btn_decrease_2.setObjectName(u"btn_decrease_2")
        self.btn_decrease_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_decrease_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(178, 189, 198);\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(150, 159, 166);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(109, 116, 121);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/assets/negative-two.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_decrease_2.setIcon(icon8)
        self.btn_decrease_2.setIconSize(QSize(32, 32))

        self.gridLayout_17.addWidget(self.btn_decrease_2, 0, 1, 1, 1)

        self.btn_decrease_1 = QPushButton(self.frame_38)
        self.btn_decrease_1.setObjectName(u"btn_decrease_1")
        self.btn_decrease_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_decrease_1.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(178, 189, 198);\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(150, 159, 166);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(109, 116, 121);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/assets/negative-one.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_decrease_1.setIcon(icon9)
        self.btn_decrease_1.setIconSize(QSize(32, 32))

        self.gridLayout_17.addWidget(self.btn_decrease_1, 0, 2, 1, 1)

        self.btn_increase_1 = QPushButton(self.frame_38)
        self.btn_increase_1.setObjectName(u"btn_increase_1")
        self.btn_increase_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_increase_1.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(178, 189, 198);\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(150, 159, 166);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(109, 116, 121);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/assets/positive-one.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_increase_1.setIcon(icon10)
        self.btn_increase_1.setIconSize(QSize(32, 32))

        self.gridLayout_17.addWidget(self.btn_increase_1, 0, 3, 1, 1)

        self.btn_increase_2 = QPushButton(self.frame_38)
        self.btn_increase_2.setObjectName(u"btn_increase_2")
        self.btn_increase_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_increase_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(178, 189, 198);\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(150, 159, 166);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(109, 116, 121);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/assets/positive-two.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_increase_2.setIcon(icon11)
        self.btn_increase_2.setIconSize(QSize(32, 32))

        self.gridLayout_17.addWidget(self.btn_increase_2, 0, 4, 1, 1)


        self.verticalLayout_21.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frame_11)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_39)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
        self.frame_42 = QFrame(self.frame_39)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"QFrame{\n"
"	border: 1px solid rgb(227, 173, 57);\n"
"	padding: 2px;\n"
"	background-color: rgb(253, 195, 64);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: transparent;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLabel{\n"
"	border: none;\n"
"}")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.frame_42)
        self.label_28.setObjectName(u"label_28")
        sizePolicy5.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy5)
        self.label_28.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_4.addWidget(self.label_28)

        self.edit_item_quantity = QLineEdit(self.frame_42)
        self.edit_item_quantity.setObjectName(u"edit_item_quantity")
        sizePolicy.setHeightForWidth(self.edit_item_quantity.sizePolicy().hasHeightForWidth())
        self.edit_item_quantity.setSizePolicy(sizePolicy)
        self.edit_item_quantity.setMaximumSize(QSize(50, 16777215))
        self.edit_item_quantity.setStyleSheet(u"")
        self.edit_item_quantity.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edit_item_quantity.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.edit_item_quantity)


        self.horizontalLayout.addWidget(self.frame_42)

        self.frame_41 = QFrame(self.frame_39)
        self.frame_41.setObjectName(u"frame_41")
        sizePolicy5.setHeightForWidth(self.frame_41.sizePolicy().hasHeightForWidth())
        self.frame_41.setSizePolicy(sizePolicy5)
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
        self.label_29.setStyleSheet(u"color: rgb(0, 0, 0)")

        self.horizontalLayout_7.addWidget(self.label_29)

        self.edit_total_value = QLineEdit(self.frame_41)
        self.edit_total_value.setObjectName(u"edit_total_value")
        sizePolicy.setHeightForWidth(self.edit_total_value.sizePolicy().hasHeightForWidth())
        self.edit_total_value.setSizePolicy(sizePolicy)
        self.edit_total_value.setMaximumSize(QSize(50, 16777215))
        self.edit_total_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edit_total_value.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.edit_total_value)


        self.horizontalLayout.addWidget(self.frame_41)


        self.verticalLayout_21.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.frame_11)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy)
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_40)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.btn_finalize_order = QPushButton(self.frame_40)
        self.btn_finalize_order.setObjectName(u"btn_finalize_order")
        self.btn_finalize_order.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_finalize_order.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(178, 189, 198);\n"
"	border-radius: 3px;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(150, 159, 166);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(109, 116, 121);\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/assets/racing-flag.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_finalize_order.setIcon(icon12)
        self.btn_finalize_order.setIconSize(QSize(32, 32))

        self.gridLayout_18.addWidget(self.btn_finalize_order, 0, 0, 1, 1)

        self.btn_cancel_order = QPushButton(self.frame_40)
        self.btn_cancel_order.setObjectName(u"btn_cancel_order")
        self.btn_cancel_order.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cancel_order.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(178, 189, 198);\n"
"	border-radius: 3px;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(150, 159, 166);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(109, 116, 121);\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/assets/no.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_cancel_order.setIcon(icon13)
        self.btn_cancel_order.setIconSize(QSize(32, 32))

        self.gridLayout_18.addWidget(self.btn_cancel_order, 0, 2, 1, 1)

        self.btn_delete_product = QPushButton(self.frame_40)
        self.btn_delete_product.setObjectName(u"btn_delete_product")
        self.btn_delete_product.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_delete_product.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(178, 189, 198);\n"
"	border-radius: 3px;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(150, 159, 166);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(109, 116, 121);\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/icons/assets/trash.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_delete_product.setIcon(icon14)
        self.btn_delete_product.setIconSize(QSize(32, 32))

        self.gridLayout_18.addWidget(self.btn_delete_product, 0, 1, 1, 1)


        self.verticalLayout_21.addWidget(self.frame_40)


        self.verticalLayout_16.addWidget(self.frame_11)


        self.horizontalLayout_6.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_7)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.frame_30 = QFrame(self.frame_7)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy)
        self.frame_30.setMinimumSize(QSize(180, 0))
        self.frame_30.setMaximumSize(QSize(180, 300))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_30)
        self.verticalLayout_15.setSpacing(3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.frame_30)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"background-color: rgb(63, 107, 235);\n"
"padding: 3px;")

        self.verticalLayout_15.addWidget(self.label_31)

        self.frame_44 = QFrame(self.frame_30)
        self.frame_44.setObjectName(u"frame_44")
        sizePolicy6.setHeightForWidth(self.frame_44.sizePolicy().hasHeightForWidth())
        self.frame_44.setSizePolicy(sizePolicy6)
        self.frame_44.setStyleSheet(u"QFrame{\n"
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
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_44)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.frame_59 = QFrame(self.frame_44)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"}")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_59)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(-1, 0, -1, 9)
        self.label_90 = QLabel(self.frame_59)
        self.label_90.setObjectName(u"label_90")

        self.verticalLayout_54.addWidget(self.label_90)

        self.edit_account_cpf = QLineEdit(self.frame_59)
        self.edit_account_cpf.setObjectName(u"edit_account_cpf")
        self.edit_account_cpf.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_54.addWidget(self.edit_account_cpf)

        self.edit_account_phone = QLineEdit(self.frame_59)
        self.edit_account_phone.setObjectName(u"edit_account_phone")
        self.edit_account_phone.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.edit_account_phone.setReadOnly(True)

        self.verticalLayout_54.addWidget(self.edit_account_phone)

        self.edit_account_name = QLineEdit(self.frame_59)
        self.edit_account_name.setObjectName(u"edit_account_name")
        self.edit_account_name.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.edit_account_name.setReadOnly(True)

        self.verticalLayout_54.addWidget(self.edit_account_name)

        self.edit_account_balance = QLineEdit(self.frame_59)
        self.edit_account_balance.setObjectName(u"edit_account_balance")
        self.edit_account_balance.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.edit_account_balance.setReadOnly(True)

        self.verticalLayout_54.addWidget(self.edit_account_balance)


        self.verticalLayout_55.addWidget(self.frame_59)

        self.btn_confirm_account = QPushButton(self.frame_44)
        self.btn_confirm_account.setObjectName(u"btn_confirm_account")
        self.btn_confirm_account.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_confirm_account.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 15px;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(243, 243, 243);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_55.addWidget(self.btn_confirm_account)


        self.verticalLayout_15.addWidget(self.frame_44)


        self.gridLayout_20.addWidget(self.frame_30, 1, 0, 1, 1)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMaximumSize(QSize(16777215, 300))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_9)
        self.verticalLayout_18.setSpacing(3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: rgb(63, 107, 235);\n"
"padding: 3px;")

        self.verticalLayout_18.addWidget(self.label_4)

        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy2.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy2)
        self.frame_12.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	margin: 0px;\n"
"	padding: 0px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_12)
        self.verticalLayout_22.setSpacing(6)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.ProductTypes = QStackedWidget(self.frame_12)
        self.ProductTypes.setObjectName(u"ProductTypes")
        sizePolicy2.setHeightForWidth(self.ProductTypes.sizePolicy().hasHeightForWidth())
        self.ProductTypes.setSizePolicy(sizePolicy2)
        self.ProductTypes.setStyleSheet(u"")
        self.pg_products_home = QWidget()
        self.pg_products_home.setObjectName(u"pg_products_home")
        self.pg_products_home.setStyleSheet(u"background: white  url(:/icons/assets/canteen-logo-300x300.png) no-repeat center contain;")
        self.ProductTypes.addWidget(self.pg_products_home)
        self.pg_snacks = QWidget()
        self.pg_snacks.setObjectName(u"pg_snacks")
        self.verticalLayout_23 = QVBoxLayout(self.pg_snacks)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_15 = QFrame(self.pg_snacks)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy2.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy2)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_15)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(3, 3, 3, 3)
        self.frame_54 = QFrame(self.frame_15)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_54)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.btn_coxinha = QPushButton(self.frame_54)
        self.btn_coxinha.setObjectName(u"btn_coxinha")
        sizePolicy1.setHeightForWidth(self.btn_coxinha.sizePolicy().hasHeightForWidth())
        self.btn_coxinha.setSizePolicy(sizePolicy1)
        self.btn_coxinha.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_coxinha.setStyleSheet(u"")
        icon15 = QIcon()
        icon15.addFile(u":/icons/assets/coxinha.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_coxinha.setIcon(icon15)
        self.btn_coxinha.setIconSize(QSize(64, 64))

        self.verticalLayout_49.addWidget(self.btn_coxinha)

        self.label_42 = QLabel(self.frame_54)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_49.addWidget(self.label_42)


        self.gridLayout_3.addWidget(self.frame_54, 0, 0, 1, 1)

        self.frame_55 = QFrame(self.frame_15)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_55)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.btn_sfiha = QPushButton(self.frame_55)
        self.btn_sfiha.setObjectName(u"btn_sfiha")
        sizePolicy1.setHeightForWidth(self.btn_sfiha.sizePolicy().hasHeightForWidth())
        self.btn_sfiha.setSizePolicy(sizePolicy1)
        self.btn_sfiha.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_sfiha.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/icons/assets/sfiha-chicken.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_sfiha.setIcon(icon16)
        self.btn_sfiha.setIconSize(QSize(64, 64))

        self.verticalLayout_51.addWidget(self.btn_sfiha)

        self.label_43 = QLabel(self.frame_55)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_51.addWidget(self.label_43)


        self.gridLayout_3.addWidget(self.frame_55, 0, 1, 1, 1)

        self.frame_56 = QFrame(self.frame_15)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_56)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.btn_burger = QPushButton(self.frame_56)
        self.btn_burger.setObjectName(u"btn_burger")
        sizePolicy1.setHeightForWidth(self.btn_burger.sizePolicy().hasHeightForWidth())
        self.btn_burger.setSizePolicy(sizePolicy1)
        self.btn_burger.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_burger.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/icons/assets/burger.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_burger.setIcon(icon17)
        self.btn_burger.setIconSize(QSize(64, 64))

        self.verticalLayout_52.addWidget(self.btn_burger)

        self.label_44 = QLabel(self.frame_56)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_52.addWidget(self.label_44)


        self.gridLayout_3.addWidget(self.frame_56, 0, 2, 1, 1)

        self.frame_57 = QFrame(self.frame_15)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_57)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.btn_croissant = QPushButton(self.frame_57)
        self.btn_croissant.setObjectName(u"btn_croissant")
        sizePolicy1.setHeightForWidth(self.btn_croissant.sizePolicy().hasHeightForWidth())
        self.btn_croissant.setSizePolicy(sizePolicy1)
        self.btn_croissant.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_croissant.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u":/icons/assets/croissant.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_croissant.setIcon(icon18)
        self.btn_croissant.setIconSize(QSize(64, 64))

        self.verticalLayout_53.addWidget(self.btn_croissant)

        self.label_45 = QLabel(self.frame_57)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_53.addWidget(self.label_45)


        self.gridLayout_3.addWidget(self.frame_57, 0, 3, 1, 1)

        self.frame_58 = QFrame(self.frame_15)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_58)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.btn_pao_de_queijo = QPushButton(self.frame_58)
        self.btn_pao_de_queijo.setObjectName(u"btn_pao_de_queijo")
        sizePolicy1.setHeightForWidth(self.btn_pao_de_queijo.sizePolicy().hasHeightForWidth())
        self.btn_pao_de_queijo.setSizePolicy(sizePolicy1)
        self.btn_pao_de_queijo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_pao_de_queijo.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u":/icons/assets/pao-de-queijo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_pao_de_queijo.setIcon(icon19)
        self.btn_pao_de_queijo.setIconSize(QSize(64, 64))

        self.verticalLayout_50.addWidget(self.btn_pao_de_queijo)

        self.label_46 = QLabel(self.frame_58)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_50.addWidget(self.label_46)


        self.gridLayout_3.addWidget(self.frame_58, 1, 0, 1, 1)


        self.verticalLayout_23.addWidget(self.frame_15)

        self.label_6 = QLabel(self.pg_snacks)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setStyleSheet(u"background-color: rgb(255, 78, 78);\n"
"padding: 3px;")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_6.setMargin(0)

        self.verticalLayout_23.addWidget(self.label_6)

        self.ProductTypes.addWidget(self.pg_snacks)
        self.pg_drinks = QWidget()
        self.pg_drinks.setObjectName(u"pg_drinks")
        self.verticalLayout_24 = QVBoxLayout(self.pg_drinks)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_16 = QFrame(self.pg_drinks)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy2.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy2)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_16)
        self.gridLayout_5.setSpacing(3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(3, 3, 3, 3)
        self.frame_60 = QFrame(self.frame_16)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_60)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.btn_water = QPushButton(self.frame_60)
        self.btn_water.setObjectName(u"btn_water")
        sizePolicy1.setHeightForWidth(self.btn_water.sizePolicy().hasHeightForWidth())
        self.btn_water.setSizePolicy(sizePolicy1)
        self.btn_water.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_water.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon20 = QIcon()
        icon20.addFile(u":/icons/assets/water.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_water.setIcon(icon20)
        self.btn_water.setIconSize(QSize(64, 64))

        self.verticalLayout_56.addWidget(self.btn_water)

        self.label_47 = QLabel(self.frame_60)
        self.label_47.setObjectName(u"label_47")

        self.verticalLayout_56.addWidget(self.label_47)


        self.gridLayout_5.addWidget(self.frame_60, 0, 0, 1, 1)

        self.frame_62 = QFrame(self.frame_16)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_62)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.btn_dellvale = QPushButton(self.frame_62)
        self.btn_dellvale.setObjectName(u"btn_dellvale")
        sizePolicy1.setHeightForWidth(self.btn_dellvale.sizePolicy().hasHeightForWidth())
        self.btn_dellvale.setSizePolicy(sizePolicy1)
        self.btn_dellvale.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_dellvale.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon21 = QIcon()
        icon21.addFile(u":/icons/assets/del-valle-juices.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_dellvale.setIcon(icon21)
        self.btn_dellvale.setIconSize(QSize(64, 64))

        self.verticalLayout_58.addWidget(self.btn_dellvale)

        self.label_48 = QLabel(self.frame_62)
        self.label_48.setObjectName(u"label_48")

        self.verticalLayout_58.addWidget(self.label_48)


        self.gridLayout_5.addWidget(self.frame_62, 0, 1, 1, 1)

        self.frame_63 = QFrame(self.frame_16)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_63)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.btn_tea_lipton = QPushButton(self.frame_63)
        self.btn_tea_lipton.setObjectName(u"btn_tea_lipton")
        sizePolicy1.setHeightForWidth(self.btn_tea_lipton.sizePolicy().hasHeightForWidth())
        self.btn_tea_lipton.setSizePolicy(sizePolicy1)
        self.btn_tea_lipton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_tea_lipton.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon22 = QIcon()
        icon22.addFile(u":/icons/assets/tea-lipton.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_tea_lipton.setIcon(icon22)
        self.btn_tea_lipton.setIconSize(QSize(64, 64))

        self.verticalLayout_59.addWidget(self.btn_tea_lipton)

        self.label_49 = QLabel(self.frame_63)
        self.label_49.setObjectName(u"label_49")

        self.verticalLayout_59.addWidget(self.label_49)


        self.gridLayout_5.addWidget(self.frame_63, 0, 2, 1, 1)

        self.frame_61 = QFrame(self.frame_16)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_61)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.btn_tea_matte = QPushButton(self.frame_61)
        self.btn_tea_matte.setObjectName(u"btn_tea_matte")
        sizePolicy1.setHeightForWidth(self.btn_tea_matte.sizePolicy().hasHeightForWidth())
        self.btn_tea_matte.setSizePolicy(sizePolicy1)
        self.btn_tea_matte.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_tea_matte.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon23 = QIcon()
        icon23.addFile(u":/icons/assets/tea-leao.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_tea_matte.setIcon(icon23)
        self.btn_tea_matte.setIconSize(QSize(64, 64))

        self.verticalLayout_57.addWidget(self.btn_tea_matte)

        self.label_50 = QLabel(self.frame_61)
        self.label_50.setObjectName(u"label_50")

        self.verticalLayout_57.addWidget(self.label_50)


        self.gridLayout_5.addWidget(self.frame_61, 1, 0, 1, 1)


        self.verticalLayout_24.addWidget(self.frame_16)

        self.label_7 = QLabel(self.pg_drinks)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"background-color: rgb(255, 78, 78);\n"
"padding: 3px;")

        self.verticalLayout_24.addWidget(self.label_7)

        self.ProductTypes.addWidget(self.pg_drinks)
        self.pg_sandwiches = QWidget()
        self.pg_sandwiches.setObjectName(u"pg_sandwiches")
        self.verticalLayout_25 = QVBoxLayout(self.pg_sandwiches)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_17 = QFrame(self.pg_sandwiches)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy2.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy2)
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_17)
        self.gridLayout_6.setSpacing(3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(3, 3, 3, 3)
        self.frame_64 = QFrame(self.frame_17)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_64)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.btn_hamburger = QPushButton(self.frame_64)
        self.btn_hamburger.setObjectName(u"btn_hamburger")
        sizePolicy1.setHeightForWidth(self.btn_hamburger.sizePolicy().hasHeightForWidth())
        self.btn_hamburger.setSizePolicy(sizePolicy1)
        self.btn_hamburger.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_hamburger.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon24 = QIcon()
        icon24.addFile(u":/icons/assets/hamburger.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_hamburger.setIcon(icon24)
        self.btn_hamburger.setIconSize(QSize(64, 64))

        self.verticalLayout_60.addWidget(self.btn_hamburger)

        self.label_51 = QLabel(self.frame_64)
        self.label_51.setObjectName(u"label_51")

        self.verticalLayout_60.addWidget(self.label_51)


        self.gridLayout_6.addWidget(self.frame_64, 0, 0, 1, 1)

        self.frame_65 = QFrame(self.frame_17)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_65)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.btn_grilled_cheese = QPushButton(self.frame_65)
        self.btn_grilled_cheese.setObjectName(u"btn_grilled_cheese")
        sizePolicy1.setHeightForWidth(self.btn_grilled_cheese.sizePolicy().hasHeightForWidth())
        self.btn_grilled_cheese.setSizePolicy(sizePolicy1)
        self.btn_grilled_cheese.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_grilled_cheese.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon25 = QIcon()
        icon25.addFile(u":/icons/assets/grilled-chesse.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_grilled_cheese.setIcon(icon25)
        self.btn_grilled_cheese.setIconSize(QSize(64, 64))

        self.verticalLayout_61.addWidget(self.btn_grilled_cheese)

        self.label_52 = QLabel(self.frame_65)
        self.label_52.setObjectName(u"label_52")

        self.verticalLayout_61.addWidget(self.label_52)


        self.gridLayout_6.addWidget(self.frame_65, 0, 1, 1, 1)


        self.verticalLayout_25.addWidget(self.frame_17)

        self.label_11 = QLabel(self.pg_sandwiches)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"background-color: rgb(255, 78, 78);\n"
"padding: 3px;")

        self.verticalLayout_25.addWidget(self.label_11)

        self.ProductTypes.addWidget(self.pg_sandwiches)
        self.pg_sweets = QWidget()
        self.pg_sweets.setObjectName(u"pg_sweets")
        self.verticalLayout_26 = QVBoxLayout(self.pg_sweets)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_18 = QFrame(self.pg_sweets)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy2.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy2)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_18)
        self.gridLayout_7.setSpacing(3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(-1, 3, 3, 3)
        self.frame_66 = QFrame(self.frame_18)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_66)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.btn_lollipop = QPushButton(self.frame_66)
        self.btn_lollipop.setObjectName(u"btn_lollipop")
        sizePolicy1.setHeightForWidth(self.btn_lollipop.sizePolicy().hasHeightForWidth())
        self.btn_lollipop.setSizePolicy(sizePolicy1)
        self.btn_lollipop.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_lollipop.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon26 = QIcon()
        icon26.addFile(u":/icons/assets/lollipop-7belo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_lollipop.setIcon(icon26)
        self.btn_lollipop.setIconSize(QSize(64, 64))

        self.verticalLayout_62.addWidget(self.btn_lollipop)

        self.label_53 = QLabel(self.frame_66)
        self.label_53.setObjectName(u"label_53")

        self.verticalLayout_62.addWidget(self.label_53)


        self.gridLayout_7.addWidget(self.frame_66, 0, 0, 1, 1)

        self.frame_67 = QFrame(self.frame_18)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_67)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.btn_candy_azedinho = QPushButton(self.frame_67)
        self.btn_candy_azedinho.setObjectName(u"btn_candy_azedinho")
        sizePolicy1.setHeightForWidth(self.btn_candy_azedinho.sizePolicy().hasHeightForWidth())
        self.btn_candy_azedinho.setSizePolicy(sizePolicy1)
        self.btn_candy_azedinho.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_candy_azedinho.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon27 = QIcon()
        icon27.addFile(u":/icons/assets/candy-azedinho.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_candy_azedinho.setIcon(icon27)
        self.btn_candy_azedinho.setIconSize(QSize(64, 64))

        self.verticalLayout_63.addWidget(self.btn_candy_azedinho)

        self.label_54 = QLabel(self.frame_67)
        self.label_54.setObjectName(u"label_54")

        self.verticalLayout_63.addWidget(self.label_54)


        self.gridLayout_7.addWidget(self.frame_67, 0, 1, 1, 1)

        self.frame_68 = QFrame(self.frame_18)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_68)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.btn_mentos = QPushButton(self.frame_68)
        self.btn_mentos.setObjectName(u"btn_mentos")
        sizePolicy1.setHeightForWidth(self.btn_mentos.sizePolicy().hasHeightForWidth())
        self.btn_mentos.setSizePolicy(sizePolicy1)
        self.btn_mentos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_mentos.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon28 = QIcon()
        icon28.addFile(u":/icons/assets/mentos.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_mentos.setIcon(icon28)
        self.btn_mentos.setIconSize(QSize(64, 64))

        self.verticalLayout_64.addWidget(self.btn_mentos)

        self.label_55 = QLabel(self.frame_68)
        self.label_55.setObjectName(u"label_55")

        self.verticalLayout_64.addWidget(self.label_55)


        self.gridLayout_7.addWidget(self.frame_68, 0, 2, 1, 1)


        self.verticalLayout_26.addWidget(self.frame_18)

        self.label_12 = QLabel(self.pg_sweets)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"background-color: rgb(255, 78, 78);\n"
"padding: 3px;")

        self.verticalLayout_26.addWidget(self.label_12)

        self.ProductTypes.addWidget(self.pg_sweets)
        self.pg_sodas = QWidget()
        self.pg_sodas.setObjectName(u"pg_sodas")
        self.verticalLayout_27 = QVBoxLayout(self.pg_sodas)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_19 = QFrame(self.pg_sodas)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy2.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy2)
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_19)
        self.gridLayout_8.setSpacing(3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(3, 3, 3, 3)
        self.frame_69 = QFrame(self.frame_19)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_69)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.btn_coca_cola = QPushButton(self.frame_69)
        self.btn_coca_cola.setObjectName(u"btn_coca_cola")
        sizePolicy1.setHeightForWidth(self.btn_coca_cola.sizePolicy().hasHeightForWidth())
        self.btn_coca_cola.setSizePolicy(sizePolicy1)
        self.btn_coca_cola.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_coca_cola.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon29 = QIcon()
        icon29.addFile(u":/icons/assets/coca-cola.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_coca_cola.setIcon(icon29)
        self.btn_coca_cola.setIconSize(QSize(64, 64))

        self.verticalLayout_65.addWidget(self.btn_coca_cola)

        self.label_56 = QLabel(self.frame_69)
        self.label_56.setObjectName(u"label_56")

        self.verticalLayout_65.addWidget(self.label_56)


        self.gridLayout_8.addWidget(self.frame_69, 0, 0, 1, 1)

        self.frame_70 = QFrame(self.frame_19)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_70)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.btn_coca_cola_zero = QPushButton(self.frame_70)
        self.btn_coca_cola_zero.setObjectName(u"btn_coca_cola_zero")
        sizePolicy1.setHeightForWidth(self.btn_coca_cola_zero.sizePolicy().hasHeightForWidth())
        self.btn_coca_cola_zero.setSizePolicy(sizePolicy1)
        self.btn_coca_cola_zero.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_coca_cola_zero.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon30 = QIcon()
        icon30.addFile(u":/icons/assets/coca-cola-zero.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_coca_cola_zero.setIcon(icon30)
        self.btn_coca_cola_zero.setIconSize(QSize(64, 64))

        self.verticalLayout_67.addWidget(self.btn_coca_cola_zero)

        self.label_57 = QLabel(self.frame_70)
        self.label_57.setObjectName(u"label_57")

        self.verticalLayout_67.addWidget(self.label_57)


        self.gridLayout_8.addWidget(self.frame_70, 0, 1, 1, 1)

        self.frame_71 = QFrame(self.frame_19)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_71)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.btn_guarana = QPushButton(self.frame_71)
        self.btn_guarana.setObjectName(u"btn_guarana")
        sizePolicy1.setHeightForWidth(self.btn_guarana.sizePolicy().hasHeightForWidth())
        self.btn_guarana.setSizePolicy(sizePolicy1)
        self.btn_guarana.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_guarana.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon31 = QIcon()
        icon31.addFile(u":/icons/assets/guarana.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_guarana.setIcon(icon31)
        self.btn_guarana.setIconSize(QSize(64, 64))

        self.verticalLayout_68.addWidget(self.btn_guarana)

        self.label_58 = QLabel(self.frame_71)
        self.label_58.setObjectName(u"label_58")

        self.verticalLayout_68.addWidget(self.label_58)


        self.gridLayout_8.addWidget(self.frame_71, 0, 2, 1, 1)

        self.frame_72 = QFrame(self.frame_19)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_72)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.btn_guarana_zero = QPushButton(self.frame_72)
        self.btn_guarana_zero.setObjectName(u"btn_guarana_zero")
        sizePolicy1.setHeightForWidth(self.btn_guarana_zero.sizePolicy().hasHeightForWidth())
        self.btn_guarana_zero.setSizePolicy(sizePolicy1)
        self.btn_guarana_zero.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_guarana_zero.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon32 = QIcon()
        icon32.addFile(u":/icons/assets/guarana-zero.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_guarana_zero.setIcon(icon32)
        self.btn_guarana_zero.setIconSize(QSize(64, 64))

        self.verticalLayout_69.addWidget(self.btn_guarana_zero)

        self.label_59 = QLabel(self.frame_72)
        self.label_59.setObjectName(u"label_59")

        self.verticalLayout_69.addWidget(self.label_59)


        self.gridLayout_8.addWidget(self.frame_72, 0, 3, 1, 1)

        self.frame_73 = QFrame(self.frame_19)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_73)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.btn_orange_fanta = QPushButton(self.frame_73)
        self.btn_orange_fanta.setObjectName(u"btn_orange_fanta")
        sizePolicy1.setHeightForWidth(self.btn_orange_fanta.sizePolicy().hasHeightForWidth())
        self.btn_orange_fanta.setSizePolicy(sizePolicy1)
        self.btn_orange_fanta.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_orange_fanta.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon33 = QIcon()
        icon33.addFile(u":/icons/assets/orange-fanta.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_orange_fanta.setIcon(icon33)
        self.btn_orange_fanta.setIconSize(QSize(64, 64))

        self.verticalLayout_66.addWidget(self.btn_orange_fanta)

        self.label_60 = QLabel(self.frame_73)
        self.label_60.setObjectName(u"label_60")

        self.verticalLayout_66.addWidget(self.label_60)


        self.gridLayout_8.addWidget(self.frame_73, 1, 0, 1, 1)


        self.verticalLayout_27.addWidget(self.frame_19)

        self.label_13 = QLabel(self.pg_sodas)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"background-color: rgb(255, 78, 78);\n"
"padding: 3px;")

        self.verticalLayout_27.addWidget(self.label_13)

        self.ProductTypes.addWidget(self.pg_sodas)
        self.pg_specials = QWidget()
        self.pg_specials.setObjectName(u"pg_specials")
        self.verticalLayout_28 = QVBoxLayout(self.pg_specials)
        self.verticalLayout_28.setSpacing(3)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.pg_specials)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy2.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy2)
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_20)
        self.gridLayout_9.setSpacing(3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(3, 3, 3, 3)
        self.frame_74 = QFrame(self.frame_20)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_74)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.btn_hot_dog = QPushButton(self.frame_74)
        self.btn_hot_dog.setObjectName(u"btn_hot_dog")
        sizePolicy1.setHeightForWidth(self.btn_hot_dog.sizePolicy().hasHeightForWidth())
        self.btn_hot_dog.setSizePolicy(sizePolicy1)
        self.btn_hot_dog.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_hot_dog.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon34 = QIcon()
        icon34.addFile(u":/icons/assets/hot-dog.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_hot_dog.setIcon(icon34)
        self.btn_hot_dog.setIconSize(QSize(64, 64))

        self.verticalLayout_70.addWidget(self.btn_hot_dog)

        self.label_61 = QLabel(self.frame_74)
        self.label_61.setObjectName(u"label_61")

        self.verticalLayout_70.addWidget(self.label_61)


        self.gridLayout_9.addWidget(self.frame_74, 0, 0, 1, 1)

        self.frame_75 = QFrame(self.frame_20)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_75)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.btn_pastel = QPushButton(self.frame_75)
        self.btn_pastel.setObjectName(u"btn_pastel")
        sizePolicy1.setHeightForWidth(self.btn_pastel.sizePolicy().hasHeightForWidth())
        self.btn_pastel.setSizePolicy(sizePolicy1)
        self.btn_pastel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_pastel.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon35 = QIcon()
        icon35.addFile(u":/icons/assets/pastel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_pastel.setIcon(icon35)
        self.btn_pastel.setIconSize(QSize(64, 64))

        self.verticalLayout_71.addWidget(self.btn_pastel)

        self.label_62 = QLabel(self.frame_75)
        self.label_62.setObjectName(u"label_62")

        self.verticalLayout_71.addWidget(self.label_62)


        self.gridLayout_9.addWidget(self.frame_75, 0, 1, 1, 1)


        self.verticalLayout_28.addWidget(self.frame_20)

        self.label_14 = QLabel(self.pg_specials)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"background-color: rgb(255, 78, 78);\n"
"padding: 3px;")

        self.verticalLayout_28.addWidget(self.label_14)

        self.ProductTypes.addWidget(self.pg_specials)

        self.verticalLayout_22.addWidget(self.ProductTypes)


        self.verticalLayout_18.addWidget(self.frame_12)


        self.gridLayout_20.addWidget(self.frame_9, 1, 1, 1, 1)

        self.frame = QFrame(self.frame_7)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 200))
        self.frame.setBaseSize(QSize(0, 0))
        self.frame.setStyleSheet(u"QPushButton{\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame)
        self.verticalLayout_19.setSpacing(3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgb(63, 107, 235);\n"
"padding: 3px;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_3)

        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy2.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy2)
        self.frame_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_13)
        self.gridLayout_4.setSpacing(3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(3, 3, 3, 3)
        self.frame_47 = QFrame(self.frame_13)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_47)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.btn_snacks = QPushButton(self.frame_47)
        self.btn_snacks.setObjectName(u"btn_snacks")
        sizePolicy1.setHeightForWidth(self.btn_snacks.sizePolicy().hasHeightForWidth())
        self.btn_snacks.setSizePolicy(sizePolicy1)
        self.btn_snacks.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_snacks.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon36 = QIcon()
        icon36.addFile(u":/icons/assets/snacks.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_snacks.setIcon(icon36)
        self.btn_snacks.setIconSize(QSize(64, 64))

        self.verticalLayout_29.addWidget(self.btn_snacks)

        self.label_35 = QLabel(self.frame_47)
        self.label_35.setObjectName(u"label_35")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setBold(True)
        self.label_35.setFont(font1)
        self.label_35.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_29.addWidget(self.label_35)


        self.gridLayout_4.addWidget(self.frame_47, 0, 0, 1, 1)

        self.frame_49 = QFrame(self.frame_13)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_49)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.btn_drinks = QPushButton(self.frame_49)
        self.btn_drinks.setObjectName(u"btn_drinks")
        sizePolicy1.setHeightForWidth(self.btn_drinks.sizePolicy().hasHeightForWidth())
        self.btn_drinks.setSizePolicy(sizePolicy1)
        self.btn_drinks.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_drinks.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon37 = QIcon()
        icon37.addFile(u":/icons/assets/drinks.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_drinks.setIcon(icon37)
        self.btn_drinks.setIconSize(QSize(64, 64))

        self.verticalLayout_44.addWidget(self.btn_drinks)

        self.label_37 = QLabel(self.frame_49)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font1)
        self.label_37.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_44.addWidget(self.label_37)


        self.gridLayout_4.addWidget(self.frame_49, 0, 1, 1, 1)

        self.frame_51 = QFrame(self.frame_13)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_51)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.btn_sandwiches = QPushButton(self.frame_51)
        self.btn_sandwiches.setObjectName(u"btn_sandwiches")
        sizePolicy1.setHeightForWidth(self.btn_sandwiches.sizePolicy().hasHeightForWidth())
        self.btn_sandwiches.setSizePolicy(sizePolicy1)
        self.btn_sandwiches.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_sandwiches.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon38 = QIcon()
        icon38.addFile(u":/icons/assets/sandwiches.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_sandwiches.setIcon(icon38)
        self.btn_sandwiches.setIconSize(QSize(64, 64))

        self.verticalLayout_46.addWidget(self.btn_sandwiches)

        self.label_39 = QLabel(self.frame_51)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font1)
        self.label_39.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_46.addWidget(self.label_39)


        self.gridLayout_4.addWidget(self.frame_51, 0, 2, 1, 1)

        self.frame_52 = QFrame(self.frame_13)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_52)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.btn_sweets = QPushButton(self.frame_52)
        self.btn_sweets.setObjectName(u"btn_sweets")
        sizePolicy1.setHeightForWidth(self.btn_sweets.sizePolicy().hasHeightForWidth())
        self.btn_sweets.setSizePolicy(sizePolicy1)
        self.btn_sweets.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_sweets.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon39 = QIcon()
        icon39.addFile(u":/icons/assets/sweets.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_sweets.setIcon(icon39)
        self.btn_sweets.setIconSize(QSize(64, 64))

        self.verticalLayout_48.addWidget(self.btn_sweets)

        self.label_41 = QLabel(self.frame_52)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font1)
        self.label_41.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_48.addWidget(self.label_41)


        self.gridLayout_4.addWidget(self.frame_52, 0, 3, 1, 1)

        self.frame_48 = QFrame(self.frame_13)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_48)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.btn_sodas = QPushButton(self.frame_48)
        self.btn_sodas.setObjectName(u"btn_sodas")
        sizePolicy1.setHeightForWidth(self.btn_sodas.sizePolicy().hasHeightForWidth())
        self.btn_sodas.setSizePolicy(sizePolicy1)
        self.btn_sodas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_sodas.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon40 = QIcon()
        icon40.addFile(u":/icons/assets/sodas.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_sodas.setIcon(icon40)
        self.btn_sodas.setIconSize(QSize(64, 64))

        self.verticalLayout_36.addWidget(self.btn_sodas)

        self.label_36 = QLabel(self.frame_48)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font1)
        self.label_36.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_36.addWidget(self.label_36)


        self.gridLayout_4.addWidget(self.frame_48, 1, 0, 1, 1)

        self.frame_50 = QFrame(self.frame_13)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_50)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.btn_specials = QPushButton(self.frame_50)
        self.btn_specials.setObjectName(u"btn_specials")
        sizePolicy1.setHeightForWidth(self.btn_specials.sizePolicy().hasHeightForWidth())
        self.btn_specials.setSizePolicy(sizePolicy1)
        self.btn_specials.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_specials.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon41 = QIcon()
        icon41.addFile(u":/icons/assets/specials.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_specials.setIcon(icon41)
        self.btn_specials.setIconSize(QSize(64, 64))

        self.verticalLayout_45.addWidget(self.btn_specials)

        self.label_38 = QLabel(self.frame_50)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font1)
        self.label_38.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_45.addWidget(self.label_38)


        self.gridLayout_4.addWidget(self.frame_50, 1, 1, 1, 1)

        self.frame_53 = QFrame(self.frame_13)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_53)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.btn_products_home = QPushButton(self.frame_53)
        self.btn_products_home.setObjectName(u"btn_products_home")
        sizePolicy1.setHeightForWidth(self.btn_products_home.sizePolicy().hasHeightForWidth())
        self.btn_products_home.setSizePolicy(sizePolicy1)
        self.btn_products_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_products_home.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        icon42 = QIcon()
        icon42.addFile(u":/icons/assets/canteen-logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_products_home.setIcon(icon42)
        self.btn_products_home.setIconSize(QSize(64, 64))

        self.verticalLayout_47.addWidget(self.btn_products_home)

        self.label_40 = QLabel(self.frame_53)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font1)
        self.label_40.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_47.addWidget(self.label_40)


        self.gridLayout_4.addWidget(self.frame_53, 1, 2, 1, 1)


        self.verticalLayout_19.addWidget(self.frame_13)

        self.frame_13.raise_()
        self.label_3.raise_()

        self.gridLayout_20.addWidget(self.frame, 0, 0, 1, 2)


        self.horizontalLayout_6.addWidget(self.frame_7)


        self.gridLayout_19.addWidget(self.frame_5, 1, 0, 1, 3)

        self.lineEdit = QLineEdit(self.pg_order)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy7)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(11)
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)

        self.gridLayout_19.addWidget(self.lineEdit, 0, 2, 1, 1)

        self.Pages.addWidget(self.pg_order)
        self.pg_products = QWidget()
        self.pg_products.setObjectName(u"pg_products")
        self.pg_products.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.pg_products)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_8 = QLabel(self.pg_products)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 70))

        self.verticalLayout_12.addWidget(self.label_8)

        self.frame_21 = QFrame(self.pg_products)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy2.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy2)
        self.frame_21.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"	border-radius: 3px;\n"
"}\n"
"")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_21)
        self.verticalLayout_17.setSpacing(3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_21)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"background-color: rgb(63, 107, 235);\n"
"padding: 3px;")

        self.verticalLayout_17.addWidget(self.label_9)

        self.frame_23 = QFrame(self.frame_21)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy2.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy2)
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_23)
        self.verticalLayout_43.setSpacing(3)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_37 = QFrame(self.frame_23)
        self.frame_37.setObjectName(u"frame_37")
        sizePolicy2.setHeightForWidth(self.frame_37.sizePolicy().hasHeightForWidth())
        self.frame_37.setSizePolicy(sizePolicy2)
        self.frame_37.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_37)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.btn_snacks2 = QPushButton(self.frame_37)
        self.btn_snacks2.setObjectName(u"btn_snacks2")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setBold(True)
        font3.setItalic(True)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        self.btn_snacks2.setFont(font3)
        self.btn_snacks2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_snacks2.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        self.btn_snacks2.setIcon(icon36)
        self.btn_snacks2.setIconSize(QSize(64, 64))

        self.gridLayout_16.addWidget(self.btn_snacks2, 0, 0, 1, 1)

        self.btn_drinks2 = QPushButton(self.frame_37)
        self.btn_drinks2.setObjectName(u"btn_drinks2")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setBold(True)
        font4.setItalic(True)
        self.btn_drinks2.setFont(font4)
        self.btn_drinks2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_drinks2.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        self.btn_drinks2.setIcon(icon37)
        self.btn_drinks2.setIconSize(QSize(64, 64))

        self.gridLayout_16.addWidget(self.btn_drinks2, 0, 1, 1, 1)

        self.btn_sandwiches2 = QPushButton(self.frame_37)
        self.btn_sandwiches2.setObjectName(u"btn_sandwiches2")
        self.btn_sandwiches2.setFont(font4)
        self.btn_sandwiches2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_sandwiches2.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        self.btn_sandwiches2.setIcon(icon38)
        self.btn_sandwiches2.setIconSize(QSize(64, 64))

        self.gridLayout_16.addWidget(self.btn_sandwiches2, 0, 2, 1, 1)

        self.btn_sweets2 = QPushButton(self.frame_37)
        self.btn_sweets2.setObjectName(u"btn_sweets2")
        self.btn_sweets2.setFont(font4)
        self.btn_sweets2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_sweets2.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        self.btn_sweets2.setIcon(icon39)
        self.btn_sweets2.setIconSize(QSize(64, 64))

        self.gridLayout_16.addWidget(self.btn_sweets2, 0, 3, 1, 1)

        self.btn_sodas2 = QPushButton(self.frame_37)
        self.btn_sodas2.setObjectName(u"btn_sodas2")
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setBold(True)
        font5.setItalic(True)
        font5.setKerning(True)
        self.btn_sodas2.setFont(font5)
        self.btn_sodas2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_sodas2.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        self.btn_sodas2.setIcon(icon40)
        self.btn_sodas2.setIconSize(QSize(64, 64))

        self.gridLayout_16.addWidget(self.btn_sodas2, 1, 0, 1, 1)

        self.btn_specials2 = QPushButton(self.frame_37)
        self.btn_specials2.setObjectName(u"btn_specials2")
        self.btn_specials2.setFont(font4)
        self.btn_specials2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_specials2.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        self.btn_specials2.setIcon(icon41)
        self.btn_specials2.setIconSize(QSize(64, 64))

        self.gridLayout_16.addWidget(self.btn_specials2, 1, 1, 1, 1)

        self.btn_products_home2 = QPushButton(self.frame_37)
        self.btn_products_home2.setObjectName(u"btn_products_home2")
        self.btn_products_home2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_products_home2.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(220, 182, 91);\n"
"	border-color: rgb(165, 165, 165);\n"
"}")
        self.btn_products_home2.setIcon(icon42)
        self.btn_products_home2.setIconSize(QSize(64, 64))

        self.gridLayout_16.addWidget(self.btn_products_home2, 1, 2, 1, 1)


        self.verticalLayout_43.addWidget(self.frame_37)


        self.verticalLayout_17.addWidget(self.frame_23)


        self.verticalLayout_12.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.pg_products)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy2.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy2)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_22)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_22)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"background-color: rgb(63, 107, 235);\n"
"padding: 3px;")

        self.verticalLayout_42.addWidget(self.label_15)

        self.frame_24 = QFrame(self.frame_22)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy2.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy2)
        self.frame_24.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	margin: 0px;\n"
"	padding: 0px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"	border-radius: 3px;\n"
"}\n"
"")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_24)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.ProductTypes2 = QStackedWidget(self.frame_24)
        self.ProductTypes2.setObjectName(u"ProductTypes2")
        sizePolicy6.setHeightForWidth(self.ProductTypes2.sizePolicy().hasHeightForWidth())
        self.ProductTypes2.setSizePolicy(sizePolicy6)
        self.ProductTypes2.setStyleSheet(u"QLabel {\n"
"	margin: 0px;\n"
"	padding: 0px;\n"
"	background-color: rgb(255, 78, 78);\n"
"	padding: 3px;\n"
"}\n"
"\n"
"QFrame {\n"
"	margin: 0px;\n"
"	padding: 0px;\n"
"}\n"
"")
        self.pg_products_home2 = QWidget()
        self.pg_products_home2.setObjectName(u"pg_products_home2")
        self.pg_products_home2.setStyleSheet(u"background: white url(:/icons/assets/canteen-logo-300x300.png) no-repeat center contain;")
        self.ProductTypes2.addWidget(self.pg_products_home2)
        self.pg_snacks2 = QWidget()
        self.pg_snacks2.setObjectName(u"pg_snacks2")
        self.verticalLayout_30 = QVBoxLayout(self.pg_snacks2)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_31 = QFrame(self.pg_snacks2)
        self.frame_31.setObjectName(u"frame_31")
        sizePolicy2.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy2)
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_31)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frame_45 = QFrame(self.frame_31)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_45)
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.pushButton_28 = QPushButton(self.frame_45)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setFont(font)
        self.pushButton_28.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButton_28.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}")
        self.pushButton_28.setIcon(icon15)
        self.pushButton_28.setIconSize(QSize(64, 64))

        self.verticalLayout_74.addWidget(self.pushButton_28)

        self.label_69 = QLabel(self.frame_45)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_74.addWidget(self.label_69)


        self.gridLayout_10.addWidget(self.frame_45, 0, 0, 1, 1)

        self.frame_80 = QFrame(self.frame_31)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_80)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.pushButton_29 = QPushButton(self.frame_80)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButton_29.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}")
        self.pushButton_29.setIcon(icon16)
        self.pushButton_29.setIconSize(QSize(64, 64))

        self.verticalLayout_76.addWidget(self.pushButton_29)

        self.label_71 = QLabel(self.frame_80)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_76.addWidget(self.label_71)


        self.gridLayout_10.addWidget(self.frame_80, 0, 1, 1, 1)

        self.frame_81 = QFrame(self.frame_31)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frame_81)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.pushButton_30 = QPushButton(self.frame_81)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButton_30.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}")
        self.pushButton_30.setIcon(icon17)
        self.pushButton_30.setIconSize(QSize(64, 64))

        self.verticalLayout_77.addWidget(self.pushButton_30)

        self.label_72 = QLabel(self.frame_81)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_77.addWidget(self.label_72)


        self.gridLayout_10.addWidget(self.frame_81, 0, 2, 1, 1)

        self.frame_82 = QFrame(self.frame_31)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_82)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.pushButton_31 = QPushButton(self.frame_82)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}")
        self.pushButton_31.setIcon(icon18)
        self.pushButton_31.setIconSize(QSize(64, 64))

        self.verticalLayout_78.addWidget(self.pushButton_31)

        self.label_73 = QLabel(self.frame_82)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_78.addWidget(self.label_73)


        self.gridLayout_10.addWidget(self.frame_82, 0, 3, 1, 1)

        self.frame_78 = QFrame(self.frame_31)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_78)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.pushButton_32 = QPushButton(self.frame_78)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}")
        self.pushButton_32.setIcon(icon19)
        self.pushButton_32.setIconSize(QSize(64, 64))

        self.verticalLayout_75.addWidget(self.pushButton_32)

        self.label_70 = QLabel(self.frame_78)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_75.addWidget(self.label_70)


        self.gridLayout_10.addWidget(self.frame_78, 1, 0, 1, 1)


        self.verticalLayout_30.addWidget(self.frame_31)

        self.label_22 = QLabel(self.pg_snacks2)
        self.label_22.setObjectName(u"label_22")
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setStyleSheet(u"background-color: rgb(255, 78, 78);\n"
"padding: 3px;")
        self.label_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_22.setMargin(0)

        self.verticalLayout_30.addWidget(self.label_22)

        self.ProductTypes2.addWidget(self.pg_snacks2)
        self.pg_drinks2 = QWidget()
        self.pg_drinks2.setObjectName(u"pg_drinks2")
        self.verticalLayout_37 = QVBoxLayout(self.pg_drinks2)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.frame_32 = QFrame(self.pg_drinks2)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy2.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy2)
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_32)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_79 = QFrame(self.frame_32)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.frame_79)
        self.verticalLayout_80.setSpacing(0)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.pushButton_33 = QPushButton(self.frame_79)
        self.pushButton_33.setObjectName(u"pushButton_33")
        sizePolicy1.setHeightForWidth(self.pushButton_33.sizePolicy().hasHeightForWidth())
        self.pushButton_33.setSizePolicy(sizePolicy1)
        self.pushButton_33.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}")
        self.pushButton_33.setIcon(icon20)
        self.pushButton_33.setIconSize(QSize(64, 64))

        self.verticalLayout_80.addWidget(self.pushButton_33)

        self.label_74 = QLabel(self.frame_79)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_80.addWidget(self.label_74)


        self.gridLayout_11.addWidget(self.frame_79, 0, 0, 1, 1)

        self.frame_84 = QFrame(self.frame_32)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_84)
        self.verticalLayout_81.setSpacing(0)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.pushButton_34 = QPushButton(self.frame_84)
        self.pushButton_34.setObjectName(u"pushButton_34")
        sizePolicy1.setHeightForWidth(self.pushButton_34.sizePolicy().hasHeightForWidth())
        self.pushButton_34.setSizePolicy(sizePolicy1)
        self.pushButton_34.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}")
        self.pushButton_34.setIcon(icon21)
        self.pushButton_34.setIconSize(QSize(64, 64))

        self.verticalLayout_81.addWidget(self.pushButton_34)

        self.label_76 = QLabel(self.frame_84)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_81.addWidget(self.label_76)


        self.gridLayout_11.addWidget(self.frame_84, 0, 1, 1, 1)

        self.frame_85 = QFrame(self.frame_32)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_85)
        self.verticalLayout_82.setSpacing(0)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.pushButton_35 = QPushButton(self.frame_85)
        self.pushButton_35.setObjectName(u"pushButton_35")
        sizePolicy1.setHeightForWidth(self.pushButton_35.sizePolicy().hasHeightForWidth())
        self.pushButton_35.setSizePolicy(sizePolicy1)
        self.pushButton_35.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}")
        self.pushButton_35.setIcon(icon22)
        self.pushButton_35.setIconSize(QSize(64, 64))

        self.verticalLayout_82.addWidget(self.pushButton_35)

        self.label_77 = QLabel(self.frame_85)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_82.addWidget(self.label_77)


        self.gridLayout_11.addWidget(self.frame_85, 0, 2, 1, 1)

        self.frame_83 = QFrame(self.frame_32)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.frame_83)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.pushButton_36 = QPushButton(self.frame_83)
        self.pushButton_36.setObjectName(u"pushButton_36")
        sizePolicy1.setHeightForWidth(self.pushButton_36.sizePolicy().hasHeightForWidth())
        self.pushButton_36.setSizePolicy(sizePolicy1)
        self.pushButton_36.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}")
        self.pushButton_36.setIcon(icon23)
        self.pushButton_36.setIconSize(QSize(64, 64))

        self.verticalLayout_79.addWidget(self.pushButton_36)

        self.label_75 = QLabel(self.frame_83)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_79.addWidget(self.label_75)


        self.gridLayout_11.addWidget(self.frame_83, 0, 3, 1, 1)


        self.verticalLayout_37.addWidget(self.frame_32)

        self.label_23 = QLabel(self.pg_drinks2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"background-color: rgb(255, 78, 78);\n"
"padding: 3px;")

        self.verticalLayout_37.addWidget(self.label_23)

        self.ProductTypes2.addWidget(self.pg_drinks2)
        self.pg_sandwiches2 = QWidget()
        self.pg_sandwiches2.setObjectName(u"pg_sandwiches2")
        self.verticalLayout_38 = QVBoxLayout(self.pg_sandwiches2)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.frame_33 = QFrame(self.pg_sandwiches2)
        self.frame_33.setObjectName(u"frame_33")
        sizePolicy2.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy2)
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_33)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.frame_86 = QFrame(self.frame_33)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.frame_86)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.pushButton_38 = QPushButton(self.frame_86)
        self.pushButton_38.setObjectName(u"pushButton_38")
        sizePolicy1.setHeightForWidth(self.pushButton_38.sizePolicy().hasHeightForWidth())
        self.pushButton_38.setSizePolicy(sizePolicy1)
        self.pushButton_38.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}")
        self.pushButton_38.setIcon(icon24)
        self.pushButton_38.setIconSize(QSize(64, 64))

        self.verticalLayout_83.addWidget(self.pushButton_38)

        self.label_78 = QLabel(self.frame_86)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_83.addWidget(self.label_78)


        self.gridLayout_12.addWidget(self.frame_86, 0, 0, 1, 1)

        self.frame_87 = QFrame(self.frame_33)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.frame_87)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.pushButton_37 = QPushButton(self.frame_87)
        self.pushButton_37.setObjectName(u"pushButton_37")
        sizePolicy1.setHeightForWidth(self.pushButton_37.sizePolicy().hasHeightForWidth())
        self.pushButton_37.setSizePolicy(sizePolicy1)
        self.pushButton_37.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}")
        self.pushButton_37.setIcon(icon25)
        self.pushButton_37.setIconSize(QSize(64, 64))

        self.verticalLayout_84.addWidget(self.pushButton_37)

        self.label_79 = QLabel(self.frame_87)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_84.addWidget(self.label_79)


        self.gridLayout_12.addWidget(self.frame_87, 0, 1, 1, 1)


        self.verticalLayout_38.addWidget(self.frame_33)

        self.label_24 = QLabel(self.pg_sandwiches2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"background-color: rgb(255, 78, 78);\n"
"padding: 3px;")

        self.verticalLayout_38.addWidget(self.label_24)

        self.ProductTypes2.addWidget(self.pg_sandwiches2)
        self.pg_sweets2 = QWidget()
        self.pg_sweets2.setObjectName(u"pg_sweets2")
        self.verticalLayout_39 = QVBoxLayout(self.pg_sweets2)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.frame_34 = QFrame(self.pg_sweets2)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy2.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy2)
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_34)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.frame_88 = QFrame(self.frame_34)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.frame_88)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.pushButton_39 = QPushButton(self.frame_88)
        self.pushButton_39.setObjectName(u"pushButton_39")
        sizePolicy1.setHeightForWidth(self.pushButton_39.sizePolicy().hasHeightForWidth())
        self.pushButton_39.setSizePolicy(sizePolicy1)
        self.pushButton_39.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}")
        self.pushButton_39.setIcon(icon26)
        self.pushButton_39.setIconSize(QSize(64, 64))

        self.verticalLayout_87.addWidget(self.pushButton_39)

        self.label_80 = QLabel(self.frame_88)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_87.addWidget(self.label_80)


        self.gridLayout_13.addWidget(self.frame_88, 0, 0, 1, 1)

        self.frame_89 = QFrame(self.frame_34)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_89)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.pushButton_40 = QPushButton(self.frame_89)
        self.pushButton_40.setObjectName(u"pushButton_40")
        sizePolicy1.setHeightForWidth(self.pushButton_40.sizePolicy().hasHeightForWidth())
        self.pushButton_40.setSizePolicy(sizePolicy1)
        self.pushButton_40.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}")
        self.pushButton_40.setIcon(icon27)
        self.pushButton_40.setIconSize(QSize(64, 64))

        self.verticalLayout_86.addWidget(self.pushButton_40)

        self.label_81 = QLabel(self.frame_89)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_86.addWidget(self.label_81)


        self.gridLayout_13.addWidget(self.frame_89, 0, 1, 1, 1)

        self.frame_90 = QFrame(self.frame_34)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_90)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.pushButton_41 = QPushButton(self.frame_90)
        self.pushButton_41.setObjectName(u"pushButton_41")
        sizePolicy1.setHeightForWidth(self.pushButton_41.sizePolicy().hasHeightForWidth())
        self.pushButton_41.setSizePolicy(sizePolicy1)
        self.pushButton_41.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}")
        self.pushButton_41.setIcon(icon28)
        self.pushButton_41.setIconSize(QSize(64, 64))

        self.verticalLayout_85.addWidget(self.pushButton_41)

        self.label_82 = QLabel(self.frame_90)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_85.addWidget(self.label_82)


        self.gridLayout_13.addWidget(self.frame_90, 0, 2, 1, 1)


        self.verticalLayout_39.addWidget(self.frame_34)

        self.label_25 = QLabel(self.pg_sweets2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"background-color: rgb(255, 78, 78);\n"
"padding: 3px;")

        self.verticalLayout_39.addWidget(self.label_25)

        self.ProductTypes2.addWidget(self.pg_sweets2)
        self.pg_sodas2 = QWidget()
        self.pg_sodas2.setObjectName(u"pg_sodas2")
        self.verticalLayout_40 = QVBoxLayout(self.pg_sodas2)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.frame_35 = QFrame(self.pg_sodas2)
        self.frame_35.setObjectName(u"frame_35")
        sizePolicy2.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy2)
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_35)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.frame_91 = QFrame(self.frame_35)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_91)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.pushButton_42 = QPushButton(self.frame_91)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}")
        self.pushButton_42.setIcon(icon29)
        self.pushButton_42.setIconSize(QSize(64, 64))

        self.verticalLayout_88.addWidget(self.pushButton_42)

        self.label_83 = QLabel(self.frame_91)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_88.addWidget(self.label_83)


        self.gridLayout_14.addWidget(self.frame_91, 0, 0, 1, 1)

        self.frame_92 = QFrame(self.frame_35)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.frame_92)
        self.verticalLayout_90.setSpacing(0)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.pushButton_43 = QPushButton(self.frame_92)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}")
        self.pushButton_43.setIcon(icon30)
        self.pushButton_43.setIconSize(QSize(64, 64))

        self.verticalLayout_90.addWidget(self.pushButton_43)

        self.label_84 = QLabel(self.frame_92)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_90.addWidget(self.label_84)


        self.gridLayout_14.addWidget(self.frame_92, 0, 1, 1, 1)

        self.frame_93 = QFrame(self.frame_35)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.frame_93)
        self.verticalLayout_91.setSpacing(0)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.pushButton_44 = QPushButton(self.frame_93)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}")
        self.pushButton_44.setIcon(icon31)
        self.pushButton_44.setIconSize(QSize(64, 64))

        self.verticalLayout_91.addWidget(self.pushButton_44)

        self.label_85 = QLabel(self.frame_93)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_91.addWidget(self.label_85)


        self.gridLayout_14.addWidget(self.frame_93, 0, 2, 1, 1)

        self.frame_94 = QFrame(self.frame_35)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_94)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.pushButton_45 = QPushButton(self.frame_94)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}")
        self.pushButton_45.setIcon(icon32)
        self.pushButton_45.setIconSize(QSize(64, 64))

        self.verticalLayout_92.addWidget(self.pushButton_45)

        self.label_86 = QLabel(self.frame_94)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_92.addWidget(self.label_86)


        self.gridLayout_14.addWidget(self.frame_94, 0, 3, 1, 1)

        self.frame_95 = QFrame(self.frame_35)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.frame_95)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.pushButton_46 = QPushButton(self.frame_95)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}")
        self.pushButton_46.setIcon(icon33)
        self.pushButton_46.setIconSize(QSize(64, 64))

        self.verticalLayout_89.addWidget(self.pushButton_46)

        self.label_87 = QLabel(self.frame_95)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_89.addWidget(self.label_87)


        self.gridLayout_14.addWidget(self.frame_95, 1, 0, 1, 1)


        self.verticalLayout_40.addWidget(self.frame_35)

        self.label_26 = QLabel(self.pg_sodas2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"background-color: rgb(255, 78, 78);\n"
"padding: 3px;")

        self.verticalLayout_40.addWidget(self.label_26)

        self.ProductTypes2.addWidget(self.pg_sodas2)
        self.pg_specials2 = QWidget()
        self.pg_specials2.setObjectName(u"pg_specials2")
        self.verticalLayout_41 = QVBoxLayout(self.pg_specials2)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.frame_36 = QFrame(self.pg_specials2)
        self.frame_36.setObjectName(u"frame_36")
        sizePolicy2.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy2)
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_36)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.frame_96 = QFrame(self.frame_36)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.frame_96)
        self.verticalLayout_93.setSpacing(0)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.pushButton_47 = QPushButton(self.frame_96)
        self.pushButton_47.setObjectName(u"pushButton_47")
        sizePolicy1.setHeightForWidth(self.pushButton_47.sizePolicy().hasHeightForWidth())
        self.pushButton_47.setSizePolicy(sizePolicy1)
        self.pushButton_47.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}")
        self.pushButton_47.setIcon(icon34)
        self.pushButton_47.setIconSize(QSize(64, 64))

        self.verticalLayout_93.addWidget(self.pushButton_47)

        self.label_88 = QLabel(self.frame_96)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_93.addWidget(self.label_88)


        self.gridLayout_15.addWidget(self.frame_96, 0, 0, 1, 1)

        self.frame_97 = QFrame(self.frame_36)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.frame_97)
        self.verticalLayout_94.setSpacing(0)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.pushButton_48 = QPushButton(self.frame_97)
        self.pushButton_48.setObjectName(u"pushButton_48")
        sizePolicy1.setHeightForWidth(self.pushButton_48.sizePolicy().hasHeightForWidth())
        self.pushButton_48.setSizePolicy(sizePolicy1)
        self.pushButton_48.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 214, 105);\n"
"	border-color: rgb(186, 186, 186);\n"
"}")
        self.pushButton_48.setIcon(icon35)
        self.pushButton_48.setIconSize(QSize(64, 64))

        self.verticalLayout_94.addWidget(self.pushButton_48)

        self.label_89 = QLabel(self.frame_97)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_94.addWidget(self.label_89)


        self.gridLayout_15.addWidget(self.frame_97, 0, 1, 1, 1)


        self.verticalLayout_41.addWidget(self.frame_36)

        self.label_27 = QLabel(self.pg_specials2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"background-color: rgb(255, 78, 78);\n"
"padding: 3px;")

        self.verticalLayout_41.addWidget(self.label_27)

        self.ProductTypes2.addWidget(self.pg_specials2)

        self.gridLayout_21.addWidget(self.ProductTypes2, 0, 0, 1, 1)


        self.verticalLayout_42.addWidget(self.frame_24)


        self.verticalLayout_12.addWidget(self.frame_22)

        self.Pages.addWidget(self.pg_products)
        self.pg_cash = QWidget()
        self.pg_cash.setObjectName(u"pg_cash")
        self.verticalLayout_98 = QVBoxLayout(self.pg_cash)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.tabWidget_2 = QTabWidget(self.pg_cash)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_register_2 = QWidget()
        self.tab_register_2.setObjectName(u"tab_register_2")
        self.verticalLayout_73 = QVBoxLayout(self.tab_register_2)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.frame_77 = QFrame(self.tab_register_2)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setStyleSheet(u"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.frame_77)
        self.verticalLayout_95.setSpacing(0)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.label_92 = QLabel(self.frame_77)
        self.label_92.setObjectName(u"label_92")

        self.verticalLayout_95.addWidget(self.label_92)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 7, -1, -1)
        self.tbl_cash = QTableWidget(self.frame_77)
        if (self.tbl_cash.columnCount() < 4):
            self.tbl_cash.setColumnCount(4)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbl_cash.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tbl_cash.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tbl_cash.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tbl_cash.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        self.tbl_cash.setObjectName(u"tbl_cash")
        self.tbl_cash.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: rgb(148, 148, 148);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"MS Shell Dlg2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(252, 252, 252);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_9.addWidget(self.tbl_cash)


        self.verticalLayout_95.addLayout(self.horizontalLayout_9)


        self.verticalLayout_73.addWidget(self.frame_77)

        self.tabWidget_2.addTab(self.tab_register_2, "")
        self.tab_accounts_2 = QWidget()
        self.tab_accounts_2.setObjectName(u"tab_accounts_2")
        self.verticalLayout_96 = QVBoxLayout(self.tab_accounts_2)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.label_91 = QLabel(self.tab_accounts_2)
        self.label_91.setObjectName(u"label_91")

        self.verticalLayout_96.addWidget(self.label_91)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tbl_orders = QTableWidget(self.tab_accounts_2)
        if (self.tbl_orders.columnCount() < 5):
            self.tbl_orders.setColumnCount(5)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tbl_orders.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tbl_orders.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tbl_orders.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tbl_orders.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tbl_orders.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        self.tbl_orders.setObjectName(u"tbl_orders")
        self.tbl_orders.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: rgb(148, 148, 148);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"MS Shell Dlg2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(252, 252, 252);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_8.addWidget(self.tbl_orders)


        self.verticalLayout_96.addLayout(self.horizontalLayout_8)

        self.tabWidget_2.addTab(self.tab_accounts_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_97 = QVBoxLayout(self.tab)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.label_93 = QLabel(self.tab)
        self.label_93.setObjectName(u"label_93")

        self.verticalLayout_97.addWidget(self.label_93)

        self.tbl_order_item = QTableWidget(self.tab)
        if (self.tbl_order_item.columnCount() < 3):
            self.tbl_order_item.setColumnCount(3)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tbl_order_item.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tbl_order_item.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tbl_order_item.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        self.tbl_order_item.setObjectName(u"tbl_order_item")
        self.tbl_order_item.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: rgb(148, 148, 148);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"MS Shell Dlg2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(252, 252, 252);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_97.addWidget(self.tbl_order_item)

        self.tabWidget_2.addTab(self.tab, "")

        self.verticalLayout_98.addWidget(self.tabWidget_2)

        self.Pages.addWidget(self.pg_cash)
        self.pg_about = QWidget()
        self.pg_about.setObjectName(u"pg_about")
        self.verticalLayout_72 = QVBoxLayout(self.pg_about)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.label_64 = QLabel(self.pg_about)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMaximumSize(QSize(16777215, 70))

        self.verticalLayout_72.addWidget(self.label_64)

        self.frame_76 = QFrame(self.pg_about)
        self.frame_76.setObjectName(u"frame_76")
        sizePolicy2.setHeightForWidth(self.frame_76.sizePolicy().hasHeightForWidth())
        self.frame_76.setSizePolicy(sizePolicy2)
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_76)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_67 = QLabel(self.frame_76)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout.addWidget(self.label_67, 0, 0, 1, 1)

        self.label_68 = QLabel(self.frame_76)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_68, 0, 1, 1, 1)

        self.label_33 = QLabel(self.frame_76)
        self.label_33.setObjectName(u"label_33")
        sizePolicy2.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy2)
        self.label_33.setWordWrap(True)

        self.gridLayout.addWidget(self.label_33, 1, 0, 1, 2)

        self.label_65 = QLabel(self.frame_76)
        self.label_65.setObjectName(u"label_65")
        sizePolicy2.setHeightForWidth(self.label_65.sizePolicy().hasHeightForWidth())
        self.label_65.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_65, 2, 0, 1, 1)

        self.label_66 = QLabel(self.frame_76)
        self.label_66.setObjectName(u"label_66")
        sizePolicy2.setHeightForWidth(self.label_66.sizePolicy().hasHeightForWidth())
        self.label_66.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_66, 2, 1, 1, 1)


        self.verticalLayout_72.addWidget(self.frame_76)

        self.Pages.addWidget(self.pg_about)

        self.verticalLayout_6.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        sizePolicy7.setHeightForWidth(self.footer_frame.sizePolicy().hasHeightForWidth())
        self.footer_frame.setSizePolicy(sizePolicy7)
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 9, 0, 0)

        self.verticalLayout.addWidget(self.footer_frame)

        self.label_2 = QLabel(self.main_container)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)


        self.gridLayout_22.addWidget(self.main_container, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.ProductTypes.setCurrentIndex(0)
        self.ProductTypes2.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Home</p></body></html>", None))
        self.btn_accounts.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Accounts</p></body></html>", None))
        self.btn_order.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Order</p></body></html>", None))
        self.btn_products.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Products</p></body></html>", None))
        self.btn_cash.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Tables</p></body></html>", None))
        self.btn_about.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">About</p></body></html>", None))
        self.btn_exit.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Exit</p></body></html>", None))
        self.btn_toggle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Management System</span></p></body></html>", None))
        self.lbs_cadastroConta.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">REGISTER ACCOUNT</span></p></body></html>", None))
        self.txt_value.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Added value", None))
        self.txt_phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"email", None))
        self.txt_name.setText("")
        self.txt_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.txt_cpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.btn_register.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_register), QCoreApplication.translate("MainWindow", u"Register", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">ACCOUNTS</span></p></body></html>", None))
        ___qtablewidgetitem = self.tbl_accounts.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ACCOUNT ID", None));
        ___qtablewidgetitem1 = self.tbl_accounts.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem2 = self.tbl_accounts.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem3 = self.tbl_accounts.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        ___qtablewidgetitem4 = self.tbl_accounts.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"PHONE", None));
        ___qtablewidgetitem5 = self.tbl_accounts.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"BALANCE", None));
        self.btn_update_account.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.btn_delete_account.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_accounts), QCoreApplication.translate("MainWindow", u"Accounts", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:11pt;\">P</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">ORDER</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">ORDER ITEMS</p></body></html>", None))
        ___qtablewidgetitem6 = self.tbl_selected_products.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"product", None));
        ___qtablewidgetitem7 = self.tbl_selected_products.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"quantity", None));
        self.btn_decrease_2.setText("")
        self.btn_decrease_1.setText("")
        self.btn_increase_1.setText("")
        self.btn_increase_2.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">N\u00b0 Items</span></p></body></html>", None))
        self.edit_item_quantity.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">R$</span></p></body></html>", None))
        self.edit_total_value.setText(QCoreApplication.translate("MainWindow", u"00,00", None))
        self.btn_finalize_order.setText("")
        self.btn_cancel_order.setText("")
        self.btn_delete_product.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">ACCOUNT</span></p></body></html>", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/assets/account.png\"/></p></body></html>", None))
        self.edit_account_cpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.edit_account_phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PHONE", None))
        self.edit_account_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NAME", None))
        self.edit_account_balance.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BALANCE", None))
        self.btn_confirm_account.setText(QCoreApplication.translate("MainWindow", u"confirm", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">PRODUCTS</span></p></body></html>", None))
        self.btn_coxinha.setText("")
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Coxinha</p></body></html>", None))
        self.btn_sfiha.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Sfiha /chicken</p></body></html>", None))
        self.btn_burger.setText("")
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Burguer</p></body></html>", None))
        self.btn_croissant.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Croissant</p></body></html>", None))
        self.btn_pao_de_queijo.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">P\u00e3o de Queijo</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">SNACKS</span></p></body></html>", None))
        self.btn_water.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Water</p></body></html>", None))
        self.btn_dellvale.setText("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">DellVale Juice</p></body></html>", None))
        self.btn_tea_lipton.setText("")
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Tea Lipton</p></body></html>", None))
        self.btn_tea_matte.setText("")
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Tea Matte</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">DRINKS</span></p></body></html>", None))
        self.btn_hamburger.setText("")
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Hamburger</p></body></html>", None))
        self.btn_grilled_cheese.setText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Grilled Cheese</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">SANDWICHES</span></p></body></html>", None))
        self.btn_lollipop.setText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Lollipop 7belo</p></body></html>", None))
        self.btn_candy_azedinho.setText("")
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Candy azedinho</p></body></html>", None))
        self.btn_mentos.setText("")
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Mentos</p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">SWEETS</span></p></body></html>", None))
        self.btn_coca_cola.setText("")
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Coca-cola</p></body></html>", None))
        self.btn_coca_cola_zero.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Coca zero</p></body></html>", None))
        self.btn_guarana.setText("")
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Guaran\u00e1</p></body></html>", None))
        self.btn_guarana_zero.setText("")
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Guaran\u00e1 Zero</p></body></html>", None))
        self.btn_orange_fanta.setText("")
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Orange Fanta</p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">SODAS</span></p></body></html>", None))
        self.btn_hot_dog.setText("")
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Hot-dog</p></body></html>", None))
        self.btn_pastel.setText("")
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Pastel</p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">SPECIALS</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">CATEGORIES</span></p></body></html>", None))
        self.btn_snacks.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">snacks</p></body></html>", None))
        self.btn_drinks.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">drinks</p></body></html>", None))
        self.btn_sandwiches.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">sandwiches</p></body></html>", None))
        self.btn_sweets.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">sweets</p></body></html>", None))
        self.btn_sodas.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">sodas</p></body></html>", None))
        self.btn_specials.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">specials</p></body></html>", None))
        self.btn_products_home.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">logo</p></body></html>", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"000", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">PRODUCTS</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">CATEGORIES</span></p></body></html>", None))
        self.btn_snacks2.setText(QCoreApplication.translate("MainWindow", u"snacks", None))
        self.btn_drinks2.setText(QCoreApplication.translate("MainWindow", u"drinks", None))
        self.btn_sandwiches2.setText(QCoreApplication.translate("MainWindow", u"sandwiches", None))
        self.btn_sweets2.setText(QCoreApplication.translate("MainWindow", u"sweets", None))
        self.btn_sodas2.setText(QCoreApplication.translate("MainWindow", u"sodas", None))
        self.btn_specials2.setText(QCoreApplication.translate("MainWindow", u"specials", None))
        self.btn_products_home2.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">PRODUCTS</span></p></body></html>", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"coxinha", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">R$ 7,50</span></p></body></html>", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"sfiha /chicker", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">R$ 6</span></p></body></html>", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"burger", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">R$ 8</span></p></body></html>", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"croissant", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">R$ 6,50</span></p></body></html>", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"p\u00e3o de queijo", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">R$ 5</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">SNACKS</span></p></body></html>", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"water", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">R$ 3</span></p></body></html>", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"dellvale", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">R$ 3,80</span></p></body></html>", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"tea lipton", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">R$ 3</span></p></body></html>", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"tea matte", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">R$ 2,50</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">DRINKS</span></p></body></html>", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"hamburger", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">R$ 12</span></p></body></html>", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"grilled cheese", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">R$ 5,80</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">SANDWICHES</span></p></body></html>", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"lollipop 7belo", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">R$ 1</span></p></body></html>", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"candy azedinho", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">R$ 0,50</span></p></body></html>", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"mentos", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">R$ 2,50</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">SWEETS</span></p></body></html>", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"coca-cola", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">R$ 5,50</span></p></body></html>", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"coca-cola zero", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">R$ 5</span></p></body></html>", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"guaran\u00e1", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">R$ 5</span></p></body></html>", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"guaran\u00e1 zero", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">R$ 5</span></p></body></html>", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"orange fanta", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">R$ 4,60</span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">SODAS</span></p></body></html>", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"hot-dog", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">R$ 5,50</span></p></body></html>", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"pastel", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">R$ 6</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">SPECIALS</span></p></body></html>", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">CASH REGISTERY</span></p></body></html>", None))
        ___qtablewidgetitem8 = self.tbl_cash.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CASH ID", None));
        ___qtablewidgetitem9 = self.tbl_cash.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"CASH DATE", None));
        ___qtablewidgetitem10 = self.tbl_cash.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"OPENING BALANCE", None));
        ___qtablewidgetitem11 = self.tbl_cash.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"CLOSING BALANCE", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_register_2), QCoreApplication.translate("MainWindow", u"Cash", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">ORDERS</span></p></body></html>", None))
        ___qtablewidgetitem12 = self.tbl_orders.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"ORDER ID", None));
        ___qtablewidgetitem13 = self.tbl_orders.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"ORDER DATE", None));
        ___qtablewidgetitem14 = self.tbl_orders.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"ORDER VALUE", None));
        ___qtablewidgetitem15 = self.tbl_orders.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"AMOUNT PAID", None));
        ___qtablewidgetitem16 = self.tbl_orders.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"CHANGE", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_accounts_2), QCoreApplication.translate("MainWindow", u"Orders", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">ORDER ITEM</span></p></body></html>", None))
        ___qtablewidgetitem17 = self.tbl_order_item.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"ORDER ID", None));
        ___qtablewidgetitem18 = self.tbl_order_item.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"PRODUCT", None));
        ___qtablewidgetitem19 = self.tbl_order_item.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"QUANTITY", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Order Item", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">ABOUT</span></p></body></html>", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/assets/logo-odcs.png\"/></p></body></html>", None))
    # retranslateUi

