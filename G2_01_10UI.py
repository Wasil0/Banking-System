from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget, QAbstractItemView)
import G2_01_14rc_icon
import G2_01_15rc_pic

class Ui_Transactions(object):
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
        self.label_23.setGeometry(QRect(170, 20, 711, 111))
        self.label_23.setStyleSheet(u"background-image: url(:/pics/pics/text-1689253205263.png);\n"
"background-position: center;\n"
"background-repeat: no;\n"
"padding: 10px;\n"
"margin-bottom: 5px;\n"
"font-size: 30px;\n"
"background-color: qlineargradient(spread:reflect, x1:0.471591, y1:1, x2:0.881, y2:0, stop:0 rgba(117, 129, 227, 100), stop:1 rgba(255, 255, 255, 250));\n"
"border: 4px solid rgb(255,255,255);\n"
"border-radius: 20px;")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 101, 171))
        self.label_3.setStyleSheet(u"border: 2px solid ;\n"
"border-radius: 20px;\n"
"border-color:  rgb(228, 255, 229);\n"
"background-color: qlineargradient(spread:reflect, x1:0.102227, y1:0.802, x2:1, y2:0, stop:0 rgba(223, 141, 141, 180), stop:1 rgba(255, 255, 255, 140));")
        self.label_24 = QLabel(Form)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(260, 40, 61, 61))
        self.label_24.setStyleSheet(u"background-image: url(:/icons/icons/bank logo.JPG);\n"
"background-position: center;\n"
"background-repeat:no;\n"
"border-radius: 10px;")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 80, 81, 91))
        self.label_6.setStyleSheet(u"background:url(:/icons/icons/icons8-user-80.png), rgba(0,0,0,0);\n"
"background-repeat: no;\n"
"\n"
"")
        self.back_to_userdashboard_btn = QPushButton(Form)
        self.back_to_userdashboard_btn.setObjectName(u"back_to_userdashboard_btn")
        self.back_to_userdashboard_btn.setGeometry(QRect(50, 20, 41, 41))
        self.back_to_userdashboard_btn.setStyleSheet(u"background-image: url(:/icons/icons/icons8-left-30.png);\n"
"background-position: center;\n"
"background-repeat:no;\n"
"border-radius: 10px;")
        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget.setColumnWidth(0, 180)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setColumnWidth(1, 180)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setColumnWidth(2, 180)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setColumnWidth(3, 180)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setColumnWidth(4, 180)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setColumnWidth(5, 180)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setColumnWidth(6, 180)

        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(40, 190, 941, 461))
        font = QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(u"border-radius: 0px;")
        self.tableWidget.setSortingEnabled(False)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 130, 411, 51))
        self.label.setStyleSheet(u"background-image: url(:/icons/icons/text-1689354793688.png);\n"
"background-position: center;\n"
"background-repeat: no;\n"
"padding: 10px;\n"
"margin-bottom: 5px;\n"
"font-size: 30px;\n"
"background-color: qlineargradient(spread:reflect, x1:0.471591, y1:1, x2:0.881, y2:0, stop:0 rgba(117, 129, 227, 100), stop:1 rgba(255, 255, 255, 250));\n"
"border: 4px solid rgb(255,255,255);\n"
"border-radius: 20px;")
        self.close_btn = QPushButton(Form)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(940, 10, 41, 41))
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

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_23.setText("")
        self.label_3.setText("")
        self.label_24.setText("")
        self.label_6.setText("")
        self.back_to_userdashboard_btn.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"SenderID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Sender", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"OperationType", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Amount", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"ReceiverID", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Receiver", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Date", None));
        self.label.setText("")
        self.close_btn.setText("")
    # retranslateUi

