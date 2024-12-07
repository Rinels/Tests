import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPainter, QColor


class CircleDrawer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Git и окружности.ui', self)
        self.should_draw = False
        self.pushButton.clicked.connect(self.repaintLabel)

    def repaintLabel(self):
        self.should_draw = True
        self.repaint()

    def paintEvent(self, event):
        if self.should_draw:
            painter = QPainter(self)
            painter.setPen(QColor('#ffff00'))
            painter.setBrush(QColor('#ffff00'))

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