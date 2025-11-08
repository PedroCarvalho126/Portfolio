# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Principal.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(824, 893)
        MainWindow.setStyleSheet(u"background-color: #FAF3B0;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 802, 731))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(800, 70))
        self.label.setMaximumSize(QSize(800, 70))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(32)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label.setContextMenuPolicy(Qt.PreventContextMenu)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"color: black;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.Titulo = QLineEdit(self.verticalLayoutWidget)
        self.Titulo.setObjectName(u"Titulo")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(16)
        self.Titulo.setFont(font1)
        self.Titulo.setContextMenuPolicy(Qt.PreventContextMenu)
        self.Titulo.setStyleSheet(u"border: 2px solid #2980b9;\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"color: black;")

        self.verticalLayout.addWidget(self.Titulo)

        self.Descricao = QTextEdit(self.verticalLayoutWidget)
        self.Descricao.setObjectName(u"Descricao")
        self.Descricao.setEnabled(True)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(25)
        self.Descricao.setFont(font2)
        self.Descricao.viewport().setProperty("cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.Descricao.setStyleSheet(u"border: 2px solid #2980b9;\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"color: black;\n"
"")

        self.verticalLayout.addWidget(self.Descricao)

        self.Adicionar = QPushButton(self.verticalLayoutWidget)
        self.Adicionar.setObjectName(u"Adicionar")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(20)
        self.Adicionar.setFont(font3)
        self.Adicionar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Adicionar.setStyleSheet(u"border: 2px solid #2980b9;\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"background-color: #00FF7F	;\n"
"color: white;\n"
"")

        self.verticalLayout.addWidget(self.Adicionar)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"border: 2px solid #2980b9;\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"background-color: #FF0000	;\n"
"color: white;")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.Adicionar.raise_()
        self.pushButton_2.raise_()
        self.Titulo.raise_()
        self.Descricao.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Controle De Tarefas", None))
        self.Titulo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Titulo da Tarefa:", None))
        self.Descricao.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o:", None))
        self.Adicionar.setText(QCoreApplication.translate("MainWindow", u"Adicionar Tarefa", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Excluir Tarefa", None))
    # retranslateUi

