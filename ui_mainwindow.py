# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(990, 900)
        MainWindow.setStyleSheet(u"QWidget#MainWindow {\n"
"	background-color: #F0F0F0;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(14)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.ownValuesTable = QTableWidget(self.centralwidget)
        if (self.ownValuesTable.columnCount() < 2):
            self.ownValuesTable.setColumnCount(2)
        brush = QBrush(QColor(0, 178, 238, 255))
        brush.setStyle(Qt.SolidPattern)
        font1 = QFont()
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        __qtablewidgetitem.setFont(font1);
        __qtablewidgetitem.setBackground(QColor(230, 230, 230));
        __qtablewidgetitem.setForeground(brush);
        self.ownValuesTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        __qtablewidgetitem1.setFont(font1);
        __qtablewidgetitem1.setBackground(QColor(230, 230, 230));
        __qtablewidgetitem1.setForeground(brush);
        self.ownValuesTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.ownValuesTable.rowCount() < 5):
            self.ownValuesTable.setRowCount(5)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.ownValuesTable.setItem(0, 0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.ownValuesTable.setItem(0, 1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.ownValuesTable.setItem(1, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.ownValuesTable.setItem(1, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.ownValuesTable.setItem(2, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.ownValuesTable.setItem(2, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.ownValuesTable.setItem(3, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.ownValuesTable.setItem(3, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.ownValuesTable.setItem(4, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.ownValuesTable.setItem(4, 1, __qtablewidgetitem11)
        self.ownValuesTable.setObjectName(u"ownValuesTable")
        self.ownValuesTable.setMinimumSize(QSize(0, 204))
        self.ownValuesTable.setMaximumSize(QSize(230, 16777215))
        self.ownValuesTable.setAlternatingRowColors(True)
        self.ownValuesTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ownValuesTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ownValuesTable.setShowGrid(False)
        self.ownValuesTable.setRowCount(5)

        self.gridLayout.addWidget(self.ownValuesTable, 3, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.minRange = QSpinBox(self.centralwidget)
        self.minRange.setObjectName(u"minRange")
        self.minRange.setAccelerated(True)
        self.minRange.setMinimum(1)
        self.minRange.setMaximum(1000)
        self.minRange.setSingleStep(5)
        self.minRange.setValue(59)

        self.gridLayout_3.addWidget(self.minRange, 0, 1, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_7, 0, 2, 1, 1)

        self.maxRange = QSpinBox(self.centralwidget)
        self.maxRange.setObjectName(u"maxRange")
        self.maxRange.setAccelerated(True)
        self.maxRange.setMinimum(1)
        self.maxRange.setMaximum(1000)
        self.maxRange.setValue(100)

        self.gridLayout_3.addWidget(self.maxRange, 0, 3, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 5, 0, 1, 1)

        self.datasetTable = QTableWidget(self.centralwidget)
        if (self.datasetTable.columnCount() < 2):
            self.datasetTable.setColumnCount(2)
        brush1 = QBrush(QColor(50, 205, 50, 255))
        brush1.setStyle(Qt.SolidPattern)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        __qtablewidgetitem12.setFont(font1);
        __qtablewidgetitem12.setBackground(QColor(230, 230, 230));
        __qtablewidgetitem12.setForeground(brush1);
        self.datasetTable.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        __qtablewidgetitem13.setFont(font1);
        __qtablewidgetitem13.setBackground(QColor(230, 230, 230));
        __qtablewidgetitem13.setForeground(brush1);
        self.datasetTable.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        if (self.datasetTable.rowCount() < 9):
            self.datasetTable.setRowCount(9)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.datasetTable.setItem(0, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.datasetTable.setItem(0, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.datasetTable.setItem(1, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.datasetTable.setItem(1, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.datasetTable.setItem(2, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.datasetTable.setItem(2, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.datasetTable.setItem(3, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.datasetTable.setItem(3, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.datasetTable.setItem(4, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.datasetTable.setItem(4, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.datasetTable.setItem(5, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.datasetTable.setItem(5, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.datasetTable.setItem(6, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.datasetTable.setItem(6, 1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.datasetTable.setItem(7, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.datasetTable.setItem(7, 1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.datasetTable.setItem(8, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.datasetTable.setItem(8, 1, __qtablewidgetitem31)
        self.datasetTable.setObjectName(u"datasetTable")
        self.datasetTable.setMinimumSize(QSize(0, 325))
        self.datasetTable.setMaximumSize(QSize(230, 16777215))
        self.datasetTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.datasetTable.setAlternatingRowColors(True)
        self.datasetTable.setSelectionMode(QAbstractItemView.NoSelection)
        self.datasetTable.setShowGrid(False)
        self.datasetTable.setRowCount(9)

        self.gridLayout.addWidget(self.datasetTable, 1, 0, 1, 1)

        self.generateAdvertising = QPushButton(self.centralwidget)
        self.generateAdvertising.setObjectName(u"generateAdvertising")

        self.gridLayout.addWidget(self.generateAdvertising, 4, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setTextFormat(Qt.RichText)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 2)

        self.plotHolder = QWidget(self.centralwidget)
        self.plotHolder.setObjectName(u"plotHolder")
        self.gridLayout_2 = QGridLayout(self.plotHolder)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.resultsLabel = QLabel(self.plotHolder)
        self.resultsLabel.setObjectName(u"resultsLabel")
        self.resultsLabel.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setFamilies([u"Cambria"])
        font2.setPointSize(14)
        self.resultsLabel.setFont(font2)
        self.resultsLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.resultsLabel, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.plotHolder, 1, 1, 5, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Simple Linear Regresion - Benetton Case", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Data Set del Caso Benetton\n"
"(Sales & Advertising)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1fico", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Valores ingresados", None))
        ___qtablewidgetitem = self.ownValuesTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Sales\n"
"(Million\n"
"Euro)", None));
        ___qtablewidgetitem1 = self.ownValuesTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Advertising\n"
"(Million Euro)", None));

        __sortingEnabled = self.ownValuesTable.isSortingEnabled()
        self.ownValuesTable.setSortingEnabled(False)
        self.ownValuesTable.setSortingEnabled(__sortingEnabled)

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Rango: ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u" - ", None))
        ___qtablewidgetitem2 = self.datasetTable.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Sales\n"
"(Million\n"
"Euro) (Y)", None));
        ___qtablewidgetitem3 = self.datasetTable.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Advertising\n"
"(Million Euro) (X)", None));

        __sortingEnabled1 = self.datasetTable.isSortingEnabled()
        self.datasetTable.setSortingEnabled(False)
        ___qtablewidgetitem4 = self.datasetTable.item(0, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"651", None));
        ___qtablewidgetitem5 = self.datasetTable.item(0, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"23", None));
        ___qtablewidgetitem6 = self.datasetTable.item(1, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"762", None));
        ___qtablewidgetitem7 = self.datasetTable.item(1, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"26", None));
        ___qtablewidgetitem8 = self.datasetTable.item(2, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"856", None));
        ___qtablewidgetitem9 = self.datasetTable.item(2, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"30", None));
        ___qtablewidgetitem10 = self.datasetTable.item(3, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"1,063", None));
        ___qtablewidgetitem11 = self.datasetTable.item(3, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"34", None));
        ___qtablewidgetitem12 = self.datasetTable.item(4, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"1,190", None));
        ___qtablewidgetitem13 = self.datasetTable.item(4, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"43", None));
        ___qtablewidgetitem14 = self.datasetTable.item(5, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"1,298", None));
        ___qtablewidgetitem15 = self.datasetTable.item(5, 1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"48", None));
        ___qtablewidgetitem16 = self.datasetTable.item(6, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"1,421", None));
        ___qtablewidgetitem17 = self.datasetTable.item(6, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"52", None));
        ___qtablewidgetitem18 = self.datasetTable.item(7, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"1,440", None));
        ___qtablewidgetitem19 = self.datasetTable.item(7, 1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"57", None));
        ___qtablewidgetitem20 = self.datasetTable.item(8, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"1,518", None));
        ___qtablewidgetitem21 = self.datasetTable.item(8, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"58", None));
        self.datasetTable.setSortingEnabled(__sortingEnabled1)

        self.generateAdvertising.setText(QCoreApplication.translate("MainWindow", u"Generar Advertising Aleatoriamente", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Fuente: <a href=\"https://www.displayr.com/what-is-linear-regression/\">https://www.displayr.com/what-is-linear-regression/</a>", None))
        self.resultsLabel.setText(QCoreApplication.translate("MainWindow", u"\u03b2\u2081 = , \u03b2\u2080 = ", None))
    # retranslateUi

