# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'designermaBWHz.ui'
##
# Created by: Qt User Interface Compiler version 6.7.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

import sys


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 300)
        Form.setToolTipDuration(8)
        self.pbQuit = QPushButton(Form)
        self.pbQuit.setObjectName(u"pbQuit")
        self.pbQuit.setGeometry(QRect(290, 50, 88, 26))
        self.pbQuit.setToolTipDuration(-2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate(
            "Form", u"Designer Example With Copied", None))
        self.pbQuit.setText(QCoreApplication.translate("Form", u"Exit", None))
    # retranslateUi


app = QApplication(sys.argv)
window = QWidget()
form = Ui_Form()
form.setupUi(window)

window.show()
sys.exit(app.exec())
