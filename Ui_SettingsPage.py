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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_SettingsPage(object):
    def setupUi(self, SettingsPage):
        if not SettingsPage.objectName():
            SettingsPage.setObjectName(u"SettingsPage")
        SettingsPage.resize(488, 376)
        self.gridLayout = QGridLayout(SettingsPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.cancel_btn = QPushButton(SettingsPage)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout.addWidget(self.cancel_btn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.title_lbl = QLabel(SettingsPage)
        self.title_lbl.setObjectName(u"title_lbl")
        self.title_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.title_lbl)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.apply_btn = QPushButton(SettingsPage)
        self.apply_btn.setObjectName(u"apply_btn")

        self.horizontalLayout.addWidget(self.apply_btn)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.webkey_lbl = QLabel(SettingsPage)
        self.webkey_lbl.setObjectName(u"webkey_lbl")

        self.horizontalLayout_2.addWidget(self.webkey_lbl)

        self.webkey_edit = QLineEdit(SettingsPage)
        self.webkey_edit.setObjectName(u"webkey_edit")

        self.horizontalLayout_2.addWidget(self.webkey_edit)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.queue_time_lbl = QLabel(SettingsPage)
        self.queue_time_lbl.setObjectName(u"queue_time_lbl")

        self.horizontalLayout_3.addWidget(self.queue_time_lbl)

        self.queue_time_spinbox = QSpinBox(SettingsPage)
        self.queue_time_spinbox.setObjectName(u"queue_time_spinbox")

        self.horizontalLayout_3.addWidget(self.queue_time_spinbox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.promo_time_lbl = QLabel(SettingsPage)
        self.promo_time_lbl.setObjectName(u"promo_time_lbl")

        self.horizontalLayout_4.addWidget(self.promo_time_lbl)

        self.promo_time_spinbox = QSpinBox(SettingsPage)
        self.promo_time_spinbox.setObjectName(u"promo_time_spinbox")

        self.horizontalLayout_4.addWidget(self.promo_time_spinbox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(SettingsPage)

        QMetaObject.connectSlotsByName(SettingsPage)
    # setupUi

    def retranslateUi(self, SettingsPage):
        SettingsPage.setWindowTitle(QCoreApplication.translate("SettingsPage", u"Form", None))
        self.cancel_btn.setText(QCoreApplication.translate("SettingsPage", u"Cancel", None))
        self.title_lbl.setText(QCoreApplication.translate("SettingsPage", u"Settings", None))
        self.apply_btn.setText(QCoreApplication.translate("SettingsPage", u"Apply", None))
        self.webkey_lbl.setText(QCoreApplication.translate("SettingsPage", u"Web Key", None))
        self.queue_time_lbl.setText(QCoreApplication.translate("SettingsPage", u"Queue Time (sec)", None))
        self.promo_time_lbl.setText(QCoreApplication.translate("SettingsPage", u"Promo Time (sec)", None))
    # retranslateUi

