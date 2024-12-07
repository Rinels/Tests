import sys
import random
from PyQt6.QtCore import QMetaObject, QCoreApplication
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLabel, QMenuBar, QStatusBar
from PyQt6.QtGui import QPainter, QColor

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(12, 520, 781, 32)
        self.pushButton.setObjectName("pushButton")
        self.label = QLabel(parent=self.centralwidget)
        self.label.setGeometry(0, 0, 801, 521)
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(0, 0, 800, 24)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Кнопка"))


class CircleDrawer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.should_draw = False
        self.pushButton.clicked.connect(self.repaintLabel)

    def repaintLabel(self):
        self.should_draw = True
        self.repaint()

    def paintEvent(self, event):
        if self.should_draw:
            painter = QPainter(self)
            painter.setPen(QColor(random.randint(0, 0xffffff)))
            painter.setBrush(QColor(random.randint(0, 0xffffff)))

            for _ in range(random.randint(2, 10)):
                radius = random.randint(10, 100)
                x = random.randint(0, self.label.width() - radius)
                y = random.randint(0, self.label.height() - radius)
                painter.drawEllipse(x, y, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = CircleDrawer()
    main_window.show()
    sys.exit(app.exec())