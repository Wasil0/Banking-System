from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)
import G2_01_14rc_icon
import G2_01_15rc_pic

class Ui_SignIn(object):
    def setupUi(self, StartingScreen):
        if not StartingScreen.objectName():
            StartingScreen.setObjectName(u"StartingScreen")
        StartingScreen.resize(1000, 680)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StartingScreen.sizePolicy().hasHeightForWidth())
        StartingScreen.setSizePolicy(sizePolicy)
        StartingScreen.setMinimumSize(QSize(1000, 680))
        StartingScreen.setMaximumSize(QSize(1000, 700))
        StartingScreen.setStyleSheet(u"background-color: rgba(255,255,255,255);\n"
"border-radius: 30px;")
        self.centralwidget = QWidget(StartingScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(1000, 700))
        self.centralwidget.setMaximumSize(QSize(1000, 700))
        self.centralwidget.setStyleSheet(u"")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(20, 50, 241, 601))
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.074, y1:1, x2:0.881, y1:0, stop:0 rgba(69, 104, 220, 200), stop:1 rgba(176, 106, 179, 150));\n"
"border-radius: 20px;\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.password_field = QLineEdit(self.frame_4)
        self.password_field.setObjectName(u"password_field")
        self.password_field.setGeometry(QRect(20, 340, 201, 40))
        self.password_field.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setFamilies([u"MS Sans Serif"])
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.password_field.setFont(font)
        self.password_field.setStyleSheet(u"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46,82,101,200);\n"
"color: rgb(172,61,221);\n"
"padding-bottom: 10px;\n"
"border-radius: 7px;\n"
"margin-left: 4px;\n"
"background: url(:/icons/icons/icons8-password-30.png), rgba(0,0,0,0);\n"
"background-repeat: no repeat;")
        self.password_field.setEchoMode(QLineEdit.Password)
        self.password_field.setAlignment(Qt.AlignCenter)
        self.username_field = QLineEdit(self.frame_4)
        self.username_field.setObjectName(u"username_field")
        self.username_field.setGeometry(QRect(20, 270, 201, 40))
        self.username_field.setMinimumSize(QSize(0, 40))
        self.username_field.setMaximumSize(QSize(16777215, 16777215))
        self.username_field.setFont(font)
        self.username_field.setStyleSheet(u"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46,82,101,200);\n"
"padding-bottom: 10px;\n"
"color: rgb(172,61,221);\n"
"border-radius: 7px;\n"
"background: url(:/icons/icons/icons8-username-30.png), rgba(0,0,0,0);\n"
"background-repeat: no repeat;\n"
"margin-left: 4px;")
        self.username_field.setAlignment(Qt.AlignCenter)
        self.login_btn = QPushButton(self.frame_4)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(40, 470, 161, 34))
        self.login_btn.setMinimumSize(QSize(0, 0))
        self.login_btn.setMaximumSize(QSize(180, 35))
        font1 = QFont()
        font1.setFamilies([u"MS Sans Serif"])
        font1.setBold(True)
        font1.setItalic(True)
        self.login_btn.setFont(font1)
        self.login_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(95,98,112,255);\n"
"	color: rgb(10,117,122);\n"
"	border-radius: 15px;\n"
"	background: url(:/icons/icons/icons8-logout-30.png), rgba(0,0,0,0);\n"
"	background-repeat: no repeat;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-left: 5px;\n"
"	padding-top: 8px;\n"
"	background-color: rgba(255,107,107,255);\n"
"	background-position: calc(100% - 10px) center right;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255,180,107,255);\n"
"}")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 130, 171, 141))
        self.label_5.setMaximumSize(QSize(16777215, 160))
        font2 = QFont()
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"background-image: url(:/icons/icons/text-1689249873503.png);\n"
"background-position: center;\n"
"background-repeat: no;\n"
"padding: 10px;\n"
"margin-bottom: 5px;\n"
"font-size: 30px;\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.register_btn = QPushButton(self.frame_4)
        self.register_btn.setObjectName(u"register_btn")
        self.register_btn.setGeometry(QRect(10, 540, 231, 31))
        self.register_btn.setMinimumSize(QSize(50, 28))
        font3 = QFont()
        font3.setFamilies([u"MS Sans Serif"])
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(True)
        self.register_btn.setFont(font3)
        self.register_btn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(10,117,122);\n"
"	background: url(:/icons/icons/icons8-register-30.png), rgba(0,0,0,0);\n"
"	background-repeat: no repeat;\n"
"	margin-left: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color: rgb(87,190,255);\n"
"}")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 50, 111, 131))
        self.label.setStyleSheet(u"background-image: url(:/icons/icons/icons8-user-65.png);\n"
"background-position: center;\n"
"background-repeat: no;\n"
"background-color: rgba(0,0,0,0);")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 241, 601))
        self.label_4.setStyleSheet(u"border: 2px solid;\n"
"border-radius: 20px;\n"
"background: rgba(0,0,0,0);")
        self.account_type_comboBox = QComboBox(self.frame_4)
        self.account_type_comboBox.addItem("")
        self.account_type_comboBox.addItem("")
        self.account_type_comboBox.addItem("")
        self.account_type_comboBox.addItem("")
        self.account_type_comboBox.setObjectName(u"account_type_comboBox")
        self.account_type_comboBox.setGeometry(QRect(70, 410, 131, 31))
        font4 = QFont()
        font4.setFamilies([u"MS Sans Serif"])
        font4.setPointSize(9)
        font4.setBold(True)
        font4.setItalic(True)
        self.account_type_comboBox.setFont(font4)
        self.account_type_comboBox.setStyleSheet(u"border-radius: 5px;\n"
"background: rgba(0,0,0,0);\n"
"color: rgb(10,117,122);\n"
"")
        self.label_4.raise_()
        self.password_field.raise_()
        self.username_field.raise_()
        self.login_btn.raise_()
        self.label_5.raise_()
        self.register_btn.raise_()
        self.label.raise_()
        self.account_type_comboBox.raise_()
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 30, 721, 651))
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(u"background-image: url(:/pics/pics/Web capture_12-7-2023_01222_.jpeg);\n"
"background-repeat: no;\n"
"color:  rgba(255,107,107,255);\n"
"border-radius: 30px;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 50, 551, 101))
        self.label_2.setStyleSheet(u"background-image: url(:/icons/icons/text-1689250023909.png);\n"
"background-color: rgba(0,0,0,0);\n"
"background-position: center;\n"
"background-repeat: no;\n"
"padding: 10px;\n"
"margin-bottom: 5px;\n"
"font-size: 30px;\n"
"")
        self.close_btn = QPushButton(self.centralwidget)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(950, 20, 41, 41))
        self.close_btn.setStyleSheet(u"background-image: url(:/icons/icons/icons8-close-40.png);\n"
"border: 1px solid red;\n"
"border-radius: 4px;")
        StartingScreen.setCentralWidget(self.centralwidget)
        self.label_3.raise_()
        self.frame_4.raise_()
        self.label_2.raise_()
        self.close_btn.raise_()

        self.retranslateUi(StartingScreen)

        QMetaObject.connectSlotsByName(StartingScreen)
    # setupUi

    def retranslateUi(self, StartingScreen):
        StartingScreen.setWindowTitle(QCoreApplication.translate("StartingScreen", u"StartingScreen", None))
        self.password_field.setText("")
        self.password_field.setPlaceholderText(QCoreApplication.translate("StartingScreen", u"PASSWORD", None))
        self.username_field.setText("")
        self.username_field.setPlaceholderText(QCoreApplication.translate("StartingScreen", u"USERNAME", None))
        self.login_btn.setText(QCoreApplication.translate("StartingScreen", u"SIGN IN", None))
        self.label_5.setText("")
        self.register_btn.setText(QCoreApplication.translate("StartingScreen", u"Not A User? Register Now", None))
        self.label.setText("")
        self.label_4.setText("")
        self.account_type_comboBox.setItemText(0, QCoreApplication.translate("StartingScreen", u"ACCOUNT TYPE", None))
        self.account_type_comboBox.setItemText(1, QCoreApplication.translate("StartingScreen", u"CHECKING ACCOUNT", None))
        self.account_type_comboBox.setItemText(2, QCoreApplication.translate("StartingScreen", u"SAVINGS ACCOUNT", None))
        self.account_type_comboBox.setItemText(3, QCoreApplication.translate("StartingScreen", u"LOAN ACCOUNT", None))

        self.account_type_comboBox.setCurrentText(QCoreApplication.translate("StartingScreen", u"ACCOUNT TYPE", None))
        self.label_3.setText("")
        self.label_2.setText("")
        self.close_btn.setText("")
    # retranslateUi

