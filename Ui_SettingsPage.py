# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsPage.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_SettingsPage(object):
    def setupUi(self, SettingsPage):
        if not SettingsPage.objectName():
            SettingsPage.setObjectName(u"SettingsPage")
        SettingsPage.resize(584, 409)
        self.gridLayout = QGridLayout(SettingsPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_lbl = QLabel(SettingsPage)
        self.title_lbl.setObjectName(u"title_lbl")
        self.title_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_lbl)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.apply_btn = QPushButton(SettingsPage)
        self.apply_btn.setObjectName(u"apply_btn")

        self.horizontalLayout.addWidget(self.apply_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(SettingsPage)

        QMetaObject.connectSlotsByName(SettingsPage)
    # setupUi

    def retranslateUi(self, SettingsPage):
        SettingsPage.setWindowTitle(QCoreApplication.translate("SettingsPage", u"Form", None))
        self.title_lbl.setText(QCoreApplication.translate("SettingsPage", u"Settings", None))
        self.apply_btn.setText(QCoreApplication.translate("SettingsPage", u"Apply", None))
    # retranslateUi

