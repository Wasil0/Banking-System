from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QProgressBar,
    QSizePolicy, QWidget)
import G2_01_15rc_pic
import G2_01_14rc_icon

class Ui_SplashWindow(object):
    def setupUi(self, StartingWindow:QMainWindow):
        if not StartingWindow.objectName():
            StartingWindow.setObjectName(u"StartingWindow")
        StartingWindow.resize(844, 502)
        StartingWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        StartingWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(StartingWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-80, -50, 1171, 761))
        self.label.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0.392, y1:0.836, x2:1, y2:0, stop:0 rgba(151,150,240, 255), stop:1 rgba(251, 199, 212, 255));\n"
"border-radius: 20px;\n"
"border: 2px solid;\n"
"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 811, 481))
        self.label_3.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0.392, y1:0.836, x2:1, y2:0, stop:0 rgba(151,150,240, 150), stop:1 rgba(251, 199, 212, 255));\n"
"border-radius: 20px;\n"
"border: 2px solid;\n"
"")
        self.dump = QLabel(self.centralwidget)
        self.dump.setObjectName(u"dump")
        self.dump.setGeometry(QRect(380, 420, 91, 21))
        font = QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.dump.setFont(font)
        self.dump.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 50, 651, 311))
        self.label_2.setStyleSheet(u"background-image: url(:/pics/pics/Stating Logo.JPG);\n"
"background-position: center;\n"
"background-repeat: no;\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(255,255,255);")
        self.Watermark = QLabel(self.centralwidget)
        self.Watermark.setObjectName(u"Watermark")
        self.Watermark.setGeometry(QRect(680, 460, 131, 21))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.Watermark.setFont(font1)
        self.AppLoadingBar = QProgressBar(self.centralwidget)
        self.AppLoadingBar.setObjectName(u"AppLoadingBar")
        self.AppLoadingBar.setGeometry(QRect(70, 390, 711, 23))
        font2 = QFont()
        font2.setFamilies([u"UI 10 20"])
        font2.setBold(True)
        font2.setItalic(False)
        self.AppLoadingBar.setFont(font2)
        self.AppLoadingBar.setLayoutDirection(Qt.LeftToRight)
        self.AppLoadingBar.setStyleSheet(u"QProgressBar{\n"
"	border-radius : 10px;\n"
"	background-color : rgba(192, 62, 155, 139);\n"
"	color: rgba(196,162,255, 255);\n"
"	border : 3px solid;\n"
"	font : Bold Segoe UI Italic 20;\n"
"	text-align : center;\n"
"	\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius : 5px;\n"
"	background-color : rgba(142, 18, 79, 90);\n"
"}")
        self.AppLoadingBar.setValue(74)
        StartingWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartingWindow)

        QMetaObject.connectSlotsByName(StartingWindow)
    # setupUi

    def retranslateUi(self, StartingWindow):
        StartingWindow.setWindowTitle(QCoreApplication.translate("StartingWindow", u"StartingWindow", None))
        self.label.setText("")
        self.label_3.setText("")
        self.dump.setText(QCoreApplication.translate("StartingWindow", u"Loading...", None))
        self.label_2.setText("")
        self.Watermark.setText(QCoreApplication.translate("StartingWindow", u"Created By Asta", None))
    # retranslateUi

