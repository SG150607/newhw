import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 570, 450)
        self.setWindowTitle('Git и случайные окружности')

        self.check_button = QPushButton(self)
        self.check_button.setText('Нарисовать')
        self.check_button.setGeometry(220, 340, 115, 40)
        self.draw_circle = False
        self.check_button.clicked.connect(self.draw)

    def paintEvent(self, event):
        if self.draw_circle:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw(self):
        self.draw_circle = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        sizee = random.randint(10, 100)
        qp.drawEllipse(random.randint(0, 570), random.randint(0, 450), sizee, sizee)
        self.draw_circle = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
