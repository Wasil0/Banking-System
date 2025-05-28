from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QWidget)
import G2_01_14rc_icon
import G2_01_15rc_pic

class Ui_Admin(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1000, 680)
        Form.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0.392, y1:0.836, x2:1, y2:0, stop:0 rgba(151,150,240, 255), stop:1 rgba(251, 199, 212, 255));\n"
"border-radius: 20px;\n"
"border: 2px solid;\n"
"")
        self.label_23 = QLabel(Form)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(160, 30, 751, 111))
        self.label_23.setStyleSheet(u"background-image: url(:/pics/pics/text-1689253205263.png);\n"
"background-position: center;\n"
"background-repeat: no;\n"
"padding: 10px;\n"
"margin-bottom: 5px;\n"
"font-size: 30px;\n"
"background-color: qlineargradient(spread:reflect, x1:0.471591, y1:1, x2:0.881, y2:0, stop:0 rgba(117, 129, 227, 100), stop:1 rgba(255, 255, 255, 250));\n"
"border: 4px solid rgb(255,255,255);\n"
"border-radius: 20px;")
        self.label_24 = QLabel(Form)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(270, 50, 61, 61))
        self.label_24.setStyleSheet(u"background-image: url(:/icons/icons/bank logo.JPG);\n"
"background-position: center;\n"
"border-radius: 10px;")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 121, 331))
        self.label_2.setStyleSheet(u"border: 2px solid ;\n"
"border-radius: 20px;\n"
"border-color:  rgb(228, 255, 229);\n"
"background-color: qlineargradient(spread:reflect, x1:0.102227, y1:0.802, x2:1, y2:0, stop:0 rgba(223, 141, 141, 180), stop:1 rgba(255, 255, 255, 140));")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 130, 81, 111))
        self.label_6.setStyleSheet(u"background:url(:/icons/icons/icons8-user-80.png), rgba(0,0,0,0);\n"
"background-repeat: no;\n"
"")
        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(50, 330, 51, 21))
        font = QFont()
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"background: rgba(0,0,0,0);\n"
"border:no;")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.logout_btn = QPushButton(Form)
        self.logout_btn.setObjectName(u"logout_btn")
        self.logout_btn.setGeometry(QRect(50, 280, 51, 51))
        self.logout_btn.setStyleSheet(u"QPushButton{\n"
"	background: url(:/icons/icons/icons8-logout-30.png), rgba(0,0,0,0);\n"
"	background-repeat: no;\n"
"	background-position: center;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left: 5px;\n"
"	padding-top: 8px;\n"
"	background-position: calc(100% - 10px) center;\n"
"}\n"
"")
        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(140, 140, 831, 501))
        self.label_15.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.074, y1:1, x2:0.881, y1:0, stop:0 rgba(69, 104, 220, 150), stop:1 rgba(176, 106, 179, 100));\n"
"background-position: center;\n"
"background-repeat: no;\n"
"border-radius: 20px;\n"
"border: 2px solid;\n"
"border-color:  rgb(228, 255, 229);\n"
"background-color: qlineargradient(spread:reflect, x1:0.471591, y1:1, x2:0.881, y2:0, stop:0 rgba(117, 129, 227, 180), stop:1 rgba(255, 255, 255, 200));")
        self.print_users_btn = QPushButton(Form)
        self.print_users_btn.setObjectName(u"print_users_btn")
        self.print_users_btn.setGeometry(QRect(500, 460, 121, 91))
        self.print_users_btn.setStyleSheet(u"QPushButton{\n"
"	background:url(:/icons/icons/icons8-print-80.png), rgba(0,0,0,0);\n"
"	background-repeat: no;\n"
"	background-position: center;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-position: calc(100% - 30px) bottom;\n"
"}\n"
"")
        self.checking_users_radio_btn = QRadioButton(Form)
        self.checking_users_radio_btn.setObjectName(u"checking_users_radio_btn")
        self.checking_users_radio_btn.setGeometry(QRect(230, 330, 176, 41))
        self.checking_users_radio_btn.setStyleSheet(u"background-image: url(:/icons/icons/text-1689349113209.png);\n"
"background-repeat: no;\n"
"background-position: center;\n"
"padding: 5px;")
        self.saving_users_radio_btn = QRadioButton(Form)
        self.saving_users_radio_btn.setObjectName(u"saving_users_radio_btn")
        self.saving_users_radio_btn.setGeometry(QRect(470, 330, 171, 41))
        self.saving_users_radio_btn.setStyleSheet(u"background-image: url(:/icons/icons/text-1689349121011.png);\n"
"background-repeat: no;\n"
"background-position: center;")
        self.loan_users_radio_btn = QRadioButton(Form)
        self.loan_users_radio_btn.setObjectName(u"loan_users_radio_btn")
        self.loan_users_radio_btn.setGeometry(QRect(710, 330, 171, 41))
        self.loan_users_radio_btn.setStyleSheet(u"background-image: url(:/icons/icons/text-1689349104450.png);\n"
"background-repeat: no;\n"
"background-position: center;")
        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(40, 210, 61, 31))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"background: rgba(0,0,0,0);\n"
"border:no;")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 170, 641, 81))
        font1 = QFont()
        font1.setFamilies([u"MS Sans Serif"])
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-image: url(:/icons/icons/text-1689252540047.png);\n"
"background-repeat: no;\n"
"background-position: center;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(500, 420, 121, 41))
        self.label.setStyleSheet(u"background-image: url(:/icons/icons/text-1689349860228.png);\n"
"background-repeat: no;\n"
"background-position: center;\n"
"padding: 5px;\n"
"border: no;\n"
"background-color: rgba(0,0,0,0);")
        self.close_btn = QPushButton(Form)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(930, 30, 41, 41))
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
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_2.raise_()
        self.label_6.raise_()
        self.label_12.raise_()
        self.logout_btn.raise_()
        self.label_15.raise_()
        self.checking_users_radio_btn.raise_()
        self.saving_users_radio_btn.raise_()
        self.loan_users_radio_btn.raise_()
        self.label_13.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.print_users_btn.raise_()
        self.close_btn.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_23.setText("")
        self.label_24.setText("")
        self.label_2.setText("")
        self.label_6.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"LOGOUT", None))
        self.logout_btn.setText("")
        self.label_15.setText("")
        self.print_users_btn.setText("")
        self.checking_users_radio_btn.setText("")
        self.saving_users_radio_btn.setText("")
        self.loan_users_radio_btn.setText("")
        self.label_13.setText(QCoreApplication.translate("Form", u"Admin", None))
        self.label_3.setText("")
        self.label.setText("")
        self.close_btn.setText("")
    # retranslateUi

