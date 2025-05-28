from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import G2_01_15rc_pic
import G2_01_14rc_icon

class Ui_UserDashboard(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1000, 680)
        Widget.setMinimumSize(QSize(1000, 680))
        Widget.setMaximumSize(QSize(1000, 680))
        Widget.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0.392, y1:0.836, x2:1, y2:0, stop:0 rgba(151,150,240, 255), stop:1 rgba(251, 199, 212, 255));\n"
"border-radius: 20px;\n"
"border: 2px solid;\n"
"")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 981, 661))
        self.label.setStyleSheet(u"background: url(:/pics/pics/u105ro5rg8o31.jpg), rgba(0,0,0,0);\n"
"border-radius: 20px;\n"
"background-repeat: no;\n"
"")
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 80, 121, 481))
        self.label_2.setStyleSheet(u"border: 2px solid ;\n"
"border-radius: 20px;\n"
"border-color:  rgb(228, 255, 229);\n"
"background-color: qlineargradient(spread:reflect, x1:0.102227, y1:0.802, x2:1, y2:0, stop:0 rgba(223, 141, 141, 180), stop:1 rgba(255, 255, 255, 140));")
        self.label_6 = QLabel(Widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 110, 81, 91))
        self.label_6.setStyleSheet(u"background:url(:/icons/icons/icons8-user-80.png), rgba(0,0,0,0);\n"
"background-repeat: no;\n"
"")
        self.label_7 = QLabel(Widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(700, 200, 261, 391))
        self.label_7.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0.392, y1:0.836, x2:1, y2:0, stop:0 rgba(227, 182, 182, 140), stop:1 rgba(255, 255, 255, 190));\n"
"border-radius: 30px;\n"
"border: 2px solid;\n"
"border-color:  rgb(228, 255, 229);")
        self.money_transfer_btn = QPushButton(Widget)
        self.money_transfer_btn.setObjectName(u"money_transfer_btn")
        self.money_transfer_btn.setGeometry(QRect(80, 230, 51, 51))
        self.money_transfer_btn.setStyleSheet(u"QPushButton{\n"
"	background:url(:/icons/icons/icons8-transactions-40.png), rgba(0,0,0,0);\n"
"	background-repeat: no;\n"
"	background-position: center;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left: 5px;\n"
"	padding-top: 8px;\n"
"	background-position: calc(100% - 20px);\n"
"}")
        self.helpdesk_btn = QPushButton(Widget)
        self.helpdesk_btn.setObjectName(u"helpdesk_btn")
        self.helpdesk_btn.setGeometry(QRect(80, 328, 51, 51))
        self.helpdesk_btn.setStyleSheet(u"QPushButton{\n"
"	background: url(:/icons/icons/icons8-helpdesk-30.png), rgba(0,0,0,0);\n"
"	background-repeat: no;\n"
"	background-position: center;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left: 5px;\n"
"	padding-top: 8px;\n"
"	background-position: calc(100% - 20px);\n"
"}")
        self.logout_btn = QPushButton(Widget)
        self.logout_btn.setObjectName(u"logout_btn")
        self.logout_btn.setGeometry(QRect(85, 420, 51, 51))
        self.logout_btn.setStyleSheet(u"QPushButton{\n"
"	background: url(:/icons/icons/icons8-logout-30.png), rgba(0,0,0,0);\n"
"	background-repeat: no;\n"
"	background-position: center;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left: 5px;\n"
"	padding-top: 8px;\n"
"	background-position: calc(100% - 20px);\n"
"}\n"
"")
        self.amount_field = QLineEdit(Widget)
        self.amount_field.setObjectName(u"amount_field")
        self.amount_field.setGeometry(QRect(710, 370, 241, 41))
        font = QFont()
        font.setFamilies([u"MS Sans Serif"])
        font.setPointSize(14)
        font.setBold(True)
        self.amount_field.setFont(font)
        self.amount_field.setStyleSheet(u"border: 2px solid;\n"
"background-image: url(:/icons/icons/icons8-euro-money-30.png);\n"
"background-color: rgba(252, 237, 255, 70);\n"
"border-bottom-color: rgba(46,82,101,200);\n"
"color: rgb(0,0,0);\n"
"padding-bottom: 5px;\n"
"border-radius: 7px;\n"
"background-repeat: no repeat;\n"
"background-position: center left;\n"
"padding-left: 30px;\n"
"")
        self.amount_field.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.deposit_btn = QPushButton(Widget)
        self.deposit_btn.setObjectName(u"deposit_btn")
        self.deposit_btn.setGeometry(QRect(760, 450, 51, 51))
        self.deposit_btn.setStyleSheet(u"QPushButton{\n"
"	background: url(:/icons/icons/icons8-deposit-30.png), rgba(0,0,0,0);\n"
"	background-repeat: no;\n"
"	background-position: center;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left: 5px;\n"
"	padding-top: 8px;\n"
"	background-position: calc(100% - 20px);\n"
"}\n"
"")
        self.withdraw_btn = QPushButton(Widget)
        self.withdraw_btn.setObjectName(u"withdraw_btn")
        self.withdraw_btn.setGeometry(QRect(860, 450, 51, 51))
        self.withdraw_btn.setStyleSheet(u"\n"
"QPushButton{\n"
"	background: url(:/icons/icons/icons8-withdraw-30.png), rgba(0,0,0,0);\n"
"	background-repeat: no;\n"
"	background-position: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left: 5px;\n"
"	padding-top: 8px;\n"
"	background-position: calc(100% - 20px);\n"
"}\n"
"")
        self.label_12 = QLabel(Widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(85, 470, 51, 21))
        font1 = QFont()
        font1.setBold(True)
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"background: rgba(0,0,0,0);\n"
"border:no;")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(Widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(60, 280, 91, 21))
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"background: rgba(0,0,0,0);\n"
"border:no;")
        self.label_15 = QLabel(Widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(170, 110, 521, 551))
        self.label_15.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.074, y1:1, x2:0.881, y1:0, stop:0 rgba(69, 104, 220, 150), stop:1 rgba(176, 106, 179, 100));\n"
"background-position: center;\n"
"background-repeat: no;\n"
"border-radius: 20px;\n"
"border: 2px solid;\n"
"border-color:  rgb(228, 255, 229);\n"
"background-color: qlineargradient(spread:reflect, x1:0.471591, y1:1, x2:0.881, y2:0, stop:0 rgba(117, 129, 227, 180), stop:1 rgba(255, 255, 255, 200));")
        self.label_16 = QLabel(Widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(750, 500, 71, 21))
        self.label_16.setFont(font1)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_17 = QLabel(Widget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(850, 500, 81, 21))
        self.label_17.setFont(font1)
        self.label_17.setAlignment(Qt.AlignCenter)
        self.username_lbl = QLabel(Widget)
        self.username_lbl.setObjectName(u"username_lbl")
        self.username_lbl.setGeometry(QRect(400, 200, 251, 41))
        font2 = QFont()
        font2.setFamilies([u"MS Sans Serif"])
        font2.setPointSize(22)
        font2.setBold(True)
        font2.setItalic(True)
        self.username_lbl.setFont(font2)
        self.username_lbl.setAlignment(Qt.AlignCenter)
        self.balance_lbl = QLabel(Widget)
        self.balance_lbl.setObjectName(u"balance_lbl")
        self.balance_lbl.setGeometry(QRect(220, 310, 411, 41))
        font3 = QFont()
        font3.setFamilies([u"MS Sans Serif"])
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setItalic(True)
        self.balance_lbl.setFont(font3)
        self.balance_lbl.setStyleSheet(u"color: rgb(10,117,122);\n"
"color: rgb(255, 210, 210);\n"
"color: rgb(255, 166, 168);\n"
"background: rgba(0,0,0,0);\n"
"border:no;")
        self.account_number_lbl = QLabel(Widget)
        self.account_number_lbl.setObjectName(u"account_number_lbl")
        self.account_number_lbl.setGeometry(QRect(220, 260, 411, 41))
        self.account_number_lbl.setFont(font3)
        self.account_number_lbl.setStyleSheet(u"color: rgb(10,117,122);\n"
"color: rgb(255, 210, 210);\n"
"color: rgb(255, 166, 168);\n"
"background: rgba(0,0,0,0);\n"
"border:no;")
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 120, 401, 81))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"background-image: url(:/icons/icons/text-1689252540047.png);\n"
"background-repeat: no;\n"
"background-position: center;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(Widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(70, 378, 71, 16))
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"background: rgba(0,0,0,0);\n"
"border:no;")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.show_transactions_btn = QPushButton(Widget)
        self.show_transactions_btn.setObjectName(u"show_transactions_btn")
        self.show_transactions_btn.setGeometry(QRect(350, 460, 191, 191))
        self.show_transactions_btn.setStyleSheet(u"QPushButton{\n"
"	background: url(:/pics/pics/icons8-synchronize-200.png), rgba(0,0,0,0);\n"
"	background-repeat: no;\n"
"	background-position: center;\n"
"	background-color: rgba(0,0,0,0);\n"
"	border:no;\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left: 5px;\n"
"	padding-top: 8px;\n"
"	background-position: calc(100% - 10px) center;\n"
"}\n"
"")
        self.label_11 = QLabel(Widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(300, 530, 301, 51))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setItalic(True)
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"background-image: url(:/icons/icons/text-1689252575884.png);\n"
"background-repeat: no;\n"
"background-position: center;")
        self.different_balance_scheme_lbl = QLabel(Widget)
        self.different_balance_scheme_lbl.setObjectName(u"different_balance_scheme_lbl")
        self.different_balance_scheme_lbl.setGeometry(QRect(220, 360, 411, 41))
        self.different_balance_scheme_lbl.setFont(font3)
        self.different_balance_scheme_lbl.setStyleSheet(u"color: rgb(10,117,122);\n"
"color: rgb(255, 210, 210);\n"
"color: rgb(255, 166, 168);\n"
"background: rgba(0,0,0,0);\n"
"border:no;")
        self.time_period_lbl = QLabel(Widget)
        self.time_period_lbl.setObjectName(u"time_period_lbl")
        self.time_period_lbl.setGeometry(QRect(220, 410, 411, 41))
        self.time_period_lbl.setFont(font3)
        self.time_period_lbl.setStyleSheet(u"color: rgb(10,117,122);\n"
"color: rgb(255, 210, 210);\n"
"color: rgb(255, 166, 168);\n"
"background: rgba(0,0,0,0);\n"
"border:no;")
        self.account_type_lbl = QLabel(Widget)
        self.account_type_lbl.setObjectName(u"account_type_lbl")
        self.account_type_lbl.setGeometry(QRect(710, 270, 241, 51))
        font5 = QFont()
        font5.setFamilies([u"MS Sans Serif"])
        font5.setPointSize(16)
        font5.setBold(True)
        font5.setItalic(True)
        font5.setKerning(True)
        self.account_type_lbl.setFont(font5)
        self.account_type_lbl.setAlignment(Qt.AlignCenter)
        self.label_23 = QLabel(Widget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(180, 20, 671, 91))
        self.label_23.setStyleSheet(u"background-image: url(:/pics/pics/text-1689253205263.png);\n"
"background-position: center;\n"
"background-repeat: no;\n"
"padding: 10px;\n"
"margin-bottom: 5px;\n"
"font-size: 30px;\n"
"background-color: qlineargradient(spread:reflect, x1:0.471591, y1:1, x2:0.881, y2:0, stop:0 rgba(117, 129, 227, 100), stop:1 rgba(255, 255, 255, 250));\n"
"border: 4px solid rgb(255,255,255);\n"
"border-radius: 20px;")
        self.label_24 = QLabel(Widget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(270, 30, 61, 61))
        self.label_24.setStyleSheet(u"background-image: url(:/icons/icons/bank logo.JPG);\n"
"background-position: center;\n"
"border-radius: 10px;")
        self.close_btn = QPushButton(Widget)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(930, 20, 41, 41))
        self.close_btn.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/icons/icons8-close-40.png);\n"
"background-color: rgba(0,0,0,0);\n"
"border: 1px solid red;\n"
"border-radius: 4px;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-left: 5px;\n"
"	padding-top: 8px;\n"
"	background-position: calc(100% - 20px);\n"
"}")

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.money_transfer_btn.setText("")
        self.helpdesk_btn.setText("")
        self.logout_btn.setText("")
        self.amount_field.setPlaceholderText(QCoreApplication.translate("Widget", u"$", None))
        self.deposit_btn.setText("")
        self.withdraw_btn.setText("")
        self.label_12.setText(QCoreApplication.translate("Widget", u"LOGOUT", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"Money Transfer", None))
        self.label_15.setText("")
        self.label_16.setText(QCoreApplication.translate("Widget", u"DEPOSIT", None))
        self.label_17.setText(QCoreApplication.translate("Widget", u"WITHDRAW", None))
        self.username_lbl.setText(QCoreApplication.translate("Widget", u"ASTA", None))
        self.balance_lbl.setText(QCoreApplication.translate("Widget", u"BALANCE : $", None))
        self.account_number_lbl.setText(QCoreApplication.translate("Widget", u"ACCOUNT NUMBER : ", None))
        self.label_3.setText("")
        self.label_10.setText(QCoreApplication.translate("Widget", u"HELPDESK", None))
        self.show_transactions_btn.setText("")
        self.label_11.setText("")
        self.different_balance_scheme_lbl.setText(QCoreApplication.translate("Widget", u"OVERDRAFT :", None))
        self.time_period_lbl.setText(QCoreApplication.translate("Widget", u"RETURN PERIOD :", None))
        self.account_type_lbl.setText(QCoreApplication.translate("Widget", u"Checking Account", None))
        self.label_23.setText("")
        self.label_24.setText("")
        self.close_btn.setText("")
    # retranslateUi

