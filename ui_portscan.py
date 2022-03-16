from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(518, 554)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"URW Bookman L")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.lineEdit.setFont(font1)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.btn_scan = QPushButton(self.frame)
        self.btn_scan.setObjectName(u"btn_scan")

        self.horizontalLayout.addWidget(self.btn_scan)

        self.btn_stop = QPushButton(self.frame)
        self.btn_stop.setObjectName(u"btn_stop")

        self.horizontalLayout.addWidget(self.btn_stop)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.minimum = QSpinBox(self.frame_4)
        self.minimum.setObjectName(u"minimum")
        self.minimum.setMinimum(1)
        self.minimum.setMaximum(10000)

        self.horizontalLayout_2.addWidget(self.minimum)

        self.maximum = QSpinBox(self.frame_4)
        self.maximum.setObjectName(u"maximum")
        self.maximum.setMinimum(1)
        self.maximum.setMaximum(20000)

        self.horizontalLayout_2.addWidget(self.maximum)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.progressBar = QProgressBar(self.frame_5)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)

        self.verticalLayout_5.addWidget(self.progressBar)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.textBrowser = QTextBrowser(self.frame_2)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_4.addWidget(self.textBrowser)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamily(u"Noto Sans Mono")
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Port Scanning", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Port Scanning", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"www.sullinux.com", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter target www.Yourtarget.com / or Target IP", None))
        self.btn_scan.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PortScanning Devlopment By Sullinux.com", None))
    # retranslateUi

