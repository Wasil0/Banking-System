from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import G2_01_14rc_icon

class Ui_InitialMoney(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(379, 289)
        Dialog.setStyleSheet(u"border-radius: 20px;\n"
"")
        self.initial_balance_field = QLineEdit(Dialog)
        self.initial_balance_field.setObjectName(u"initial_balance_field")
        self.initial_balance_field.setGeometry(QRect(70, 140, 271, 40))
        self.initial_balance_field.setMinimumSize(QSize(0, 40))
        self.initial_balance_field.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"MS Sans Serif"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.initial_balance_field.setFont(font)
        self.initial_balance_field.setStyleSheet(u"border: 2px solid rgba(0,0,0,0);\n"
"background-image: url(:/icons/icons/icons8-cash-30.png);\n"
"background-color: rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46,82,101,200);\n"
"padding-bottom: 10px;\n"
"color: rgb(58,99,122);\n"
"border-radius: 7px;\n"
"background-repeat: no repeat;\n"
"margin-left: 4px;\n"
"")
        self.initial_balance_field.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 321, 101))
        self.label.setStyleSheet(u"background-image: url(:/icons/icons/text-1689357212140.png);\n"
"background-color: rgba(0,0,0,0);\n"
"background-position: center;\n"
"background-repeat: no;\n"
"padding: 10px;\n"
"margin-bottom: 5px;\n"
"font-size: 30px;\n"
"border: no;")
        self.create_account_btn = QPushButton(Dialog)
        self.create_account_btn.setObjectName(u"create_account_btn")
        self.create_account_btn.setGeometry(QRect(150, 210, 101, 41))
        self.create_account_btn.setStyleSheet(u"QPushButton{\n"
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
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 361, 271))
        self.label_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.074, y1:1, x2:0.881, y1:0, stop:0 rgba(69, 104, 220, 90), stop:1 rgba(156, 106, 179, 50));\n"
"border-radius: 20px;\n"
"border: 2px solid;")
        self.label_2.raise_()
        self.initial_balance_field.raise_()
        self.label.raise_()
        self.create_account_btn.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.initial_balance_field.setText("")
        self.initial_balance_field.setPlaceholderText(QCoreApplication.translate("Dialog", u"AMOUNT", None))
        self.label.setText("")
        self.create_account_btn.setText("")
        self.label_2.setText("")
    # retranslateUi

