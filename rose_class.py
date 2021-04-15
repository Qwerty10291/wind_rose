from PyQt5.QtCore import QObject, QPoint, QRect, Qt
from PyQt5.QtGui import QBrush, QPainter, QFont, QColor, QPen
from PyQt5.QtWidgets import QLabel, QWidget

import math

class RoseWidget(QWidget):
    def __init__(self, del_price) -> None:
        super().__init__()
        self.winds_direction = {
            'N': 0, 'NNE': 25, 'NE': 45, 'ENE': 65, 'E': 90,
            'ESE': 115, 'SE': 135, 'SSE': 155, 'S': 180,
            'SSW': 205, 'SW': 225, 'WSW': 245, 'W': 270,
            'WNW': 295, 'NW': 320, 'NNW': 345
        }
        self.winds = {
            'N': 0, 'NNE': 0, 'NE': 0, 'ENE': 0, 'E': 0,
            'ESE': 0, 'SE': 0, 'SSE': 0, 'S': 0,
            'SSW': 0, 'SW': 0, 'WSW': 0, 'W': 0,
            'WNW': 0, 'NW': 0, 'NNW': 0
        }
        self.winds_count = 0
        self.circle_color = QColor(0, 0, 0)
        self.polygon_color = QColor(0, 0, 225, 125)
        self.text_color = QColor(15, 15, 15)

        self.records_per_sector = del_price


    def set_winds(self, winds:list[str]) -> None:
        max_wind = 0
        for i in self.winds.keys():
            self.winds[i] = 0
        
        for i in winds:
            self.winds[i] += 1
            if self.winds[i] > max_wind:
                max_wind = self.winds[i]
        self.winds_count = max_wind
        self.repaint()
    
    def set_records_per_sector(self, num:int):
        if num > self.winds_count:
            return
        self.records_per_sector = num
        self.repaint()
    
    def draw_sectors(self, qp:QPainter, center, radius) -> int:
        qp.setFont(QFont('Serif', 8, QFont.Bold))
        sector_radius = int(radius / (self.winds_count / self.records_per_sector))
        qp.setPen(QPen(self.circle_color, 2, Qt.SolidLine))
        sectors = int(radius / sector_radius)
        for i in range(1, sectors + 1):
            qp.drawEllipse(center[0] - sector_radius * i, center[1] - sector_radius * i,
                            sector_radius * i * 2, sector_radius * i * 2)
            qp.drawText(center[0] + 2, center[1] - sector_radius * i + 10, str(i * self.records_per_sector))
        if self.winds_count % self.records_per_sector != 0:
            sub = self.winds_count % self.records_per_sector
            radius = sectors * sector_radius + (int(sector_radius / self.records_per_sector) * sub)
            qp.drawEllipse(QPoint(center[0], center[1]), radius, radius)
            qp.drawText(center[0], center[1] - radius + 10, str(self.winds_count))
        return sector_radius
    
    def draw_directions(self, qp:QPainter, center, radius:int):
        qp.setPen(QPen(self.polygon_color, 2, Qt.SolidLine))
        font = QFont('Serif', 11, QFont.Bold)
        qp.setFont(font)
        for wind, deg in self.winds_direction.items():
            a = int(-radius * math.sin(math.radians(deg)))
            b = int(-radius * math.cos(math.radians(deg)))
            qp.drawLine(center[0], center[1], center[0] + a, center[1] + b)
            qp.drawText(center[0] + a + a // 20, center[1] + b + b // 20, wind)
    
    def draw_center(self, qp:QPainter, center, sector):
        qp.setBrush(QBrush(self.polygon_color))
        dotes = []
        record_rad = int(sector / self.records_per_sector)
        for dir, num in self.winds.items():
            radius = record_rad * num
            a = int(-radius * math.sin(math.radians(self.winds_direction[dir])))
            b = int(-radius * math.cos(math.radians(self.winds_direction[dir])))
            dotes.append(QPoint(center[0] + a, center[1] + b))
        qp.drawPolygon(*dotes)

    
    def draw(self, qp:QPainter):
        size = self.size()
        w, h = size.width(), size.height()
        center = [w // 2, h // 2]
        radius = h // 2 - h // 15
        if self.winds_count == 0:
            qp.fillRect(0, 0, w, h, QColor(255, 255, 255))
            return
        font = QFont('Serif', 8, QFont.Light)
        qp.setFont(font)

        qp.fillRect(0, 0, w, h, QColor(255, 255, 255))

        sector = self.draw_sectors(qp, center, radius)
        self.draw_directions(qp, center, radius)
        self.draw_center(qp, center, sector)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()
    
