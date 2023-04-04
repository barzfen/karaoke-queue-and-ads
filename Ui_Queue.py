# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Queue.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
    QLabel, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Queue(object):
    def setupUi(self, Queue):
        if not Queue.objectName():
            Queue.setObjectName(u"Queue")
        Queue.resize(1038, 699)
        self.gridLayout = QGridLayout(Queue)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.banner = QLabel(Queue)
        self.banner.setObjectName(u"banner")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.banner.sizePolicy().hasHeightForWidth())
        self.banner.setSizePolicy(sizePolicy)
        self.banner.setMinimumSize(QSize(0, 60))
        self.banner.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.banner)

        self.bio = QLabel(Queue)
        self.bio.setObjectName(u"bio")
        sizePolicy.setHeightForWidth(self.bio.sizePolicy().hasHeightForWidth())
        self.bio.setSizePolicy(sizePolicy)
        self.bio.setMinimumSize(QSize(0, 80))
        self.bio.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.bio)

        self.queue_table = QTableWidget(Queue)
        if (self.queue_table.columnCount() < 3):
            self.queue_table.setColumnCount(3)
        self.queue_table.setObjectName(u"queue_table")
        self.queue_table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.queue_table.setColumnCount(3)

        self.verticalLayout.addWidget(self.queue_table)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Queue)

        QMetaObject.connectSlotsByName(Queue)
    # setupUi

    def retranslateUi(self, Queue):
        Queue.setWindowTitle(QCoreApplication.translate("Queue", u"Form", None))
        self.banner.setText(QCoreApplication.translate("Queue", u"Placeholder for Banner", None))
        self.bio.setText(QCoreApplication.translate("Queue", u"Place holder for current singer with BIO.", None))
    # retranslateUi

