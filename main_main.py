import sys
import random

from PyQt5 import uic

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()
        self.draw_flag = False

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Рисование')
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.draw_flag = True
        self.update()

    def paintEvent(self, event):
        if not self.draw_flag:
            return
        self.draw_flag = False
        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)
        qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        radius = random.randint(1, 300)
        qp.drawEllipse(100, 100, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
