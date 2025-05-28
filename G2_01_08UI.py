from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)
import G2_01_14rc_icon
import G2_01_15rc_pic

class Ui_SignUp(object):
    def setupUi(self, SignUp):
        if not SignUp.objectName():
            SignUp.setObjectName(u"SignUp")
        SignUp.resize(1000, 680)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SignUp.sizePolicy().hasHeightForWidth())
        SignUp.setSizePolicy(sizePolicy)
        SignUp.setMinimumSize(QSize(1000, 680))
        SignUp.setMaximumSize(QSize(1000, 680))
        self.label = QLabel(SignUp)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 741, 641))
        self.label.setStyleSheet(u"border-radius: 20px;\n"
"background-image: url(:/pics/pics/Web capture_12-7-2023_01222_.jpeg);")
        self.label_2 = QLabel(SignUp)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(660, 60, 321, 591))
        self.label_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(151, 160, 239, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 20px;\n"
"border: 2px solid raised;")
        self.label_3 = QLabel(SignUp)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(700, 100, 221, 91))
        font = QFont()
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-image: url(:/icons/icons/text-1689250808061.png);\n"
"background-color: rgba(0,0,0,0);\n"
"background-position: center;\n"
"background-repeat: no;\n"
"margin-bottom: 5px;\n"
"font-size: 30px;\n"
"\n"
"")
        self.fullname_field = QLineEdit(SignUp)
        self.fullname_field.setObjectName(u"fullname_field")
        self.fullname_field.setGeometry(QRect(700, 200, 231, 41))
        font1 = QFont()
        font1.setFamilies([u"MS Sans Serif"])
        font1.setBold(True)
        font1.setItalic(True)
        self.fullname_field.setFont(font1)
        self.fullname_field.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46,82,101,200);\n"
"color: rgb(58,99,122);\n"
"padding-bottom: 10px;\n"
"background:url(:/icons/icons/icons8-name-30.png), rgba(0,0,0,0);\n"
"background-repeat: no repeat;\n"
"margin-left: 4px;\n"
"")
        self.fullname_field.setAlignment(Qt.AlignCenter)
        self.username_field = QLineEdit(SignUp)
        self.username_field.setObjectName(u"username_field")
        self.username_field.setGeometry(QRect(700, 250, 231, 41))
        self.username_field.setFont(font1)
        self.username_field.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46,82,101,200);\n"
"color: rgb(58,99,122);\n"
"padding-bottom: 10px;\n"
"background: url(:/icons/icons/icons8-username-30.png), rgba(0,0,0,0);\n"
"background-repeat: no repeat;\n"
"margin-left: 4px;\n"
"")
        self.username_field.setAlignment(Qt.AlignCenter)
        self.email_field = QLineEdit(SignUp)
        self.email_field.setObjectName(u"email_field")
        self.email_field.setGeometry(QRect(700, 300, 231, 41))
        self.email_field.setFont(font1)
        self.email_field.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46,82,101,200);\n"
"color: rgb(58,99,122);\n"
"padding-bottom: 10px;\n"
"background: url(:/icons/icons/icons8-email-30.png), rgba(0,0,0,0);\n"
"background-repeat: no repeat;\n"
"margin-left: 4px;")
        self.email_field.setAlignment(Qt.AlignCenter)
        self.password_field = QLineEdit(SignUp)
        self.password_field.setEchoMode(QLineEdit.Password)
        self.password_field.setObjectName(u"password_field")
        self.password_field.setGeometry(QRect(700, 350, 231, 41))
        self.password_field.setFont(font1)
        self.password_field.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46,82,101,200);\n"
"color: rgb(58,99,122);\n"
"padding-bottom: 10px;\n"
"background: url(:/icons/icons/icons8-logout-30.png), rgba(0,0,0,0);\n"
"background-repeat: no repeat;\n"
"margin-left: 4px;")
        self.password_field.setAlignment(Qt.AlignCenter)
        self.phone_field = QLineEdit(SignUp)
        self.phone_field.setObjectName(u"phone_field")
        self.phone_field.setGeometry(QRect(700, 400, 231, 41))
        self.phone_field.setFont(font1)
        self.phone_field.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46,82,101,200);\n"
"color: rgb(58,99,122);\n"
"padding-bottom: 10px;\n"
"background: url(:/icons/icons/icons8-phone-30.png), rgba(0,0,0,0);\n"
"background-repeat: no repeat;\n"
"margin-left: 4px;")
        self.phone_field.setAlignment(Qt.AlignCenter)
        self.account_type_comboBox = QComboBox(SignUp)
        self.account_type_comboBox.addItem("")
        self.account_type_comboBox.addItem("")
        self.account_type_comboBox.addItem("")
        self.account_type_comboBox.addItem("")
        self.account_type_comboBox.setObjectName(u"account_type_comboBox")
        self.account_type_comboBox.setGeometry(QRect(800, 463, 141, 31))
        font2 = QFont()
        font2.setFamilies([u"MS Sans Serif"])
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setItalic(True)
        self.account_type_comboBox.setFont(font2)
        self.account_type_comboBox.setStyleSheet(u"border-radius: 5px;\n"
"background: rgba(0,0,0,0);\n"
"color: rgb(10,117,122);\n"
"")
        self.checkBox = QCheckBox(SignUp)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(690, 510, 241, 41))
        self.checkBox.setStyleSheet("Background-color: rgba(0,0,0,0);")
        font3 = QFont()
        font3.setPointSize(7)
        font3.setBold(True)
        self.checkBox.setFont(font3)
        self.sign_up_btn = QPushButton(SignUp)
        self.sign_up_btn.setObjectName(u"sign_up_btn")
        self.sign_up_btn.setGeometry(QRect(780, 580, 121, 41))
        self.sign_up_btn.setFont(font1)
        self.sign_up_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(162, 153, 255, 255);\n"
"	color: rgba(58,70,122,255);\n"
"	border-radius: 7px;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-left: 5px;\n"
"	padding-top: 8px;\n"
"	background-color: rgba(255,107,107,255);\n"
"	background-position: calc(100% - 10px) center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(165, 153, 255, 150);\n"
"}")
        self.back_btn = QPushButton(SignUp)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(680, 70, 41, 41))
        self.back_btn.setStyleSheet(u"QPushButton{\n"
"	background: url(:/icons/icons/icons8-left-30.png), rgba(0,0,0,0);\n"
"	background-repeat: no repeat;\n"
"	border: 2px solid;\n"
"	margin-top: 5px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left: 5px;\n"
"	padding-top: 8px;\n"
"	background-color: rgba(255,107,107,255);\n"
"	background-position: calc(100% - 10px) center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(165, 153, 255, 150);\n"
"}")
        self.label_4 = QLabel(SignUp)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(700, 530, 261, 31))
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet("Background-color: rgba(0,0,0,0);")
        self.label_5 = QLabel(SignUp)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 40, 551, 101))
        self.label_5.setStyleSheet(u"background-image: url(:/icons/icons/text-1689250023909.png);\n"
"background-color: rgba(0,0,0,0);\n"
"background-position: center;\n"
"background-repeat: no;\n"
"padding: 10px;\n"
"margin-bottom: 5px;\n"
"font-size: 30px;\n"
"")
        self.close_btn = QPushButton(SignUp)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(950, 10, 41, 41))
        self.close_btn.setStyleSheet(u"background-image: url(:/icons/icons/icons8-close-40.png);\n"
"border: 1px solid red;\n"
"border-radius: 4px;")

        self.retranslateUi(SignUp)

        QMetaObject.connectSlotsByName(SignUp)
    # setupUi

    def retranslateUi(self, SignUp):
        SignUp.setWindowTitle(QCoreApplication.translate("SignUp", u"SignUp", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.fullname_field.setPlaceholderText(QCoreApplication.translate("SignUp", u"FULL NAME", None))
        self.username_field.setPlaceholderText(QCoreApplication.translate("SignUp", u"USERNAME", None))
        self.email_field.setPlaceholderText(QCoreApplication.translate("SignUp", u"EMAIL", None))
        self.password_field.setPlaceholderText(QCoreApplication.translate("SignUp", u"PASSWORD", None))
        self.phone_field.setPlaceholderText(QCoreApplication.translate("SignUp", u"PHONE NUMBER", None))
        self.account_type_comboBox.setItemText(0, QCoreApplication.translate("SignUp", u"ACCOUNT TYPE", None))
        self.account_type_comboBox.setItemText(1, QCoreApplication.translate("SignUp", u"CHECKING ACCOUNT", None))
        self.account_type_comboBox.setItemText(2, QCoreApplication.translate("SignUp", u"SAVINGS ACCOUNT", None))
        self.account_type_comboBox.setItemText(3, QCoreApplication.translate("SignUp", u"LOAN ACCOUNT", None))

        self.account_type_comboBox.setCurrentText(QCoreApplication.translate("SignUp", u"ACCOUNT TYPE", None))
        self.checkBox.setText(QCoreApplication.translate("SignUp", u"I AGREE THAT ALL THE DETAILS ABOVE", None))
        self.sign_up_btn.setText(QCoreApplication.translate("SignUp", u"SIGN UP", None))
        self.back_btn.setText("")
        self.label_4.setText(QCoreApplication.translate("SignUp", u"ARE CORRECT AND HENCE CANNOT BE CHANGED.", None))
        self.label_5.setText("")
        self.close_btn.setText("")
    # retranslateUi

