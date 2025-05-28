from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)
import G2_01_14rc_icon

class Ui_MoneyTransfer(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(438, 400)
        Dialog.setStyleSheet(u"border-radius: 20px;\n"
"")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 421, 381))
        self.label_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.074, y1:1, x2:0.881, y1:0, stop:0 rgba(69, 104, 220, 90), stop:1 rgba(156, 106, 179, 50));\n"
"border-radius: 20px;\n"
"border: 2px solid;")
        self.receiver_username_field = QLineEdit(Dialog)
        self.receiver_username_field.setObjectName(u"receiver_username_field")
        self.receiver_username_field.setGeometry(QRect(100, 120, 241, 40))
        self.receiver_username_field.setMinimumSize(QSize(0, 40))
        self.receiver_username_field.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"MS Sans Serif"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.receiver_username_field.setFont(font)
        self.receiver_username_field.setStyleSheet(u"border: 2px solid rgba(0,0,0,0);\n"
"background-image: url(:/icons/icons/icons8-name-30.png);\n"
"background-color: rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46,82,101,200);\n"
"padding-bottom: 10px;\n"
"color: rgb(58,99,122);\n"
"border-radius: 7px;\n"
"background-repeat: no repeat;\n"
"margin-left: 4px;\n"
"")
        self.receiver_username_field.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.receiver_account_id_field = QLineEdit(Dialog)
        self.receiver_account_id_field.setObjectName(u"receiver_account_id_field")
        self.receiver_account_id_field.setGeometry(QRect(100, 170, 241, 40))
        self.receiver_account_id_field.setMinimumSize(QSize(0, 40))
        self.receiver_account_id_field.setMaximumSize(QSize(16777215, 16777215))
        self.receiver_account_id_field.setFont(font)
        self.receiver_account_id_field.setStyleSheet(u"border: 2px solid rgba(0,0,0,0);\n"
"background-image: url(:/icons/icons/icons8-id-30.png);\n"
"background-color: rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46,82,101,200);\n"
"padding-bottom: 10px;\n"
"color: rgb(58,99,122);\n"
"border-radius: 7px;\n"
"background-repeat: no repeat;\n"
"margin-left: 4px;\n"
"")
        self.receiver_account_id_field.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.transfer_amount_field = QLineEdit(Dialog)
        self.transfer_amount_field.setObjectName(u"transfer_amount_field")
        self.transfer_amount_field.setGeometry(QRect(100, 220, 241, 40))
        self.transfer_amount_field.setMinimumSize(QSize(0, 40))
        self.transfer_amount_field.setMaximumSize(QSize(16777215, 16777215))
        self.transfer_amount_field.setFont(font)
        self.transfer_amount_field.setStyleSheet(u"border: 2px solid rgba(0,0,0,0);\n"
"background-image: url(:/icons/icons/icons8-cash-30.png);\n"
"background-color: rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46,82,101,200);\n"
"padding-bottom: 10px;\n"
"color: rgb(58,99,122);\n"
"border-radius: 7px;\n"
"background-repeat: no repeat;\n"
"margin-left: 4px;\n"
"")
        self.transfer_amount_field.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.tranfer_money_btn = QPushButton(Dialog)
        self.tranfer_money_btn.setObjectName(u"tranfer_money_btn")
        self.tranfer_money_btn.setGeometry(QRect(150, 330, 151, 41))
        self.tranfer_money_btn.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/icons/icons8-arrow-right-30.png);\n"
"background-color: rgba(0,0,0,0);\n"
"background-position: center;\n"
"background-repeat: no;\n"
"padding: 10px;\n"
"border: 2px solid;\n"
"margin-bottom: 5px;\n"
"font-size: 30px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-left: 5px;\n"
"	padding-top: 8px;\n"
"	background-color: rgba(255,107,107,255);\n"
"	background-position: calc(100% - 25px) center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255,107,107,255);\n"
"	opacity: 0.4;\n"
"}\n"
"\n"
"\n"
"")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 20, 321, 101))
        self.label.setStyleSheet(u"background-image: url(:/icons/icons/text-1689358416197.png);\n"
"background-color: rgba(0,0,0,0);\n"
"background-position: center;\n"
"background-repeat: no;\n"
"padding: 10px;\n"
"margin-bottom: 5px;\n"
"font-size: 30px;\n"
"border: no;")
        self.receiver_account_type_comboBox = QComboBox(Dialog)
        self.receiver_account_type_comboBox.addItem("")
        self.receiver_account_type_comboBox.addItem("")
        self.receiver_account_type_comboBox.addItem("")
        self.receiver_account_type_comboBox.setObjectName(u"receiver_account_type_comboBox")
        self.receiver_account_type_comboBox.setGeometry(QRect(90, 280, 131, 31))
        font1 = QFont()
        font1.setFamilies([u"MS Sans Serif"])
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setItalic(True)
        self.receiver_account_type_comboBox.setFont(font1)
        self.receiver_account_type_comboBox.setStyleSheet(u"border-radius: 5px;\n"
"background: rgba(0,0,0,0);\n"
"color: rgb(10,117,122);\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText("")
        self.receiver_username_field.setText("")
        self.receiver_username_field.setPlaceholderText(QCoreApplication.translate("Dialog", u"USERNAME", None))
        self.receiver_account_id_field.setText("")
        self.receiver_account_id_field.setPlaceholderText(QCoreApplication.translate("Dialog", u"ACCOUNT ID", None))
        self.transfer_amount_field.setText("")
        self.transfer_amount_field.setPlaceholderText(QCoreApplication.translate("Dialog", u"AMOUNT", None))
        self.tranfer_money_btn.setText("")
        self.label.setText("")
        self.receiver_account_type_comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"ACCOUNT TYPE", None))
        self.receiver_account_type_comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"CheckingAccountUsers", None))
        self.receiver_account_type_comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"SavingAccountUsers", None))
        
        self.receiver_account_type_comboBox.setCurrentText(QCoreApplication.translate("Dialog", u"ACCOUNT TYPE", None))
    # retranslateUi

