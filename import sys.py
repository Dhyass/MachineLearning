import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QFont
import math
import time

class HorlogeAnalogique(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Horloge Analogique")
        self.setGeometry(200, 200, 400, 400)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)  # Met à jour l'horloge toutes les 1000 ms (1 seconde)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)

        # Obtenir l'heure actuelle
        current_time = time.localtime()
        hour = current_time.tm_hour % 12
        minute = current_time.tm_min
        second = current_time.tm_sec

        # Dessiner le cadran de l'horloge
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white))
        painter.drawEllipse(50, 50, 300, 300)

        # Dessiner les aiguilles des heures, des minutes et des secondes
        self.draw_hand(painter, hour * 30 + minute * 0.5, 100, Qt.black, 6)
        self.draw_hand(painter, minute * 6 + second * 0.1, 150, Qt.blue, 4)
        self.draw_hand(painter, second * 6, 150, Qt.red, 2)

        # Dessiner les nombres correspondants aux heures
        font = QFont()
        font.setPointSize(16)
        painter.setFont(font)
        for h in range(1, 13):
            angle = -(h * 30) + 60  # Décalage de 60 degrés pour placer les chiffres au bon endroit
            x = 200 + 150 * math.cos(math.radians(angle))
            y = 200 - 150 * math.sin(math.radians(angle))
            painter.drawText(int(x) - 10, int(y) + 10, str(h))

    def draw_hand(self, painter, angle, length, color, width):
        painter.save()
        painter.setPen(QPen(color, width, Qt.SolidLine))
        painter.translate(200, 200)  # Déplacer l'origine au centre
        painter.rotate(-90)  # Tourner pour que 0 degré soit à midi
        painter.rotate(angle)  # Tourner à l'angle approprié
        painter.drawLine(0, 0, length, 0)  # Dessiner l'aiguille
        painter.restore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    horloge = HorlogeAnalogique()
    horloge.show()
    sys.exit(app.exec_())
