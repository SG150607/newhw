import random
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from UI import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Git и случайные окружности')
        self.draw_circle = False
        self.pushButton.clicked.connect(self.draw)

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
