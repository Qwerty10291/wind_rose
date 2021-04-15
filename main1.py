from PyQt5 import QtCore, QtGui, QtWidgets
from rose_class import RoseWidget
from db import Data
from datetime import datetime
import sqlalchemy
import sqlalchemy.sql.default_comparator

class Ui_MainWindow(object):
    def __init__(self) -> None:
        self.db = Data()
        self.records_per_sector = 1
        self.window = QtWidgets.QMainWindow()
        self.setupUi(self.window)
        self._bind_buttons()
        self._set_time_now()
        self.load_cities()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(843, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.panel = QtWidgets.QTabWidget(self.centralwidget)
        self.panel.setObjectName("panel")
        self.roze = QtWidgets.QWidget()
        self.roze.setObjectName("roze")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.roze)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.roze_image = RoseWidget(self.records_per_sector)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.roze_image.sizePolicy().hasHeightForWidth())
        self.roze_image.setSizePolicy(sizePolicy)
        self.roze_image.setMinimumSize(QtCore.QSize(600, 500))
        self.roze_image.setObjectName("roze_image")
        self.gridLayout.addWidget(self.roze_image, 0, 0, 10, 1)
        self.create_rose = QtWidgets.QPushButton(self.roze)
        self.create_rose.setObjectName("create_rose")
        self.gridLayout.addWidget(self.create_rose, 6, 1, 1, 1)
        self.date_to = QtWidgets.QDateEdit(self.roze)
        self.date_to.setObjectName("date_to")
        self.gridLayout.addWidget(self.date_to, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.roze)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.roze)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.date_from = QtWidgets.QDateEdit(self.roze)
        self.date_from.setObjectName("date_from")
        self.gridLayout.addWidget(self.date_from, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.roze)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.city_choosing = QtWidgets.QComboBox(self.roze)
        self.city_choosing.setObjectName("city_choosing")
        self.gridLayout.addWidget(self.city_choosing, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.roze)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 10, 0, 1, 2)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.panel.addTab(self.roze, "")
        self.add_city = QtWidgets.QWidget()
        self.add_city.setObjectName("add_city")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.add_city)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.city_search_name = QtWidgets.QLineEdit(self.add_city)
        self.city_search_name.setText("")
        self.city_search_name.setObjectName("city_search_name")
        self.gridLayout_2.addWidget(self.city_search_name, 0, 0, 1, 1)
        self.city_search = QtWidgets.QPushButton(self.add_city)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.city_search.sizePolicy().hasHeightForWidth())
        self.city_search.setSizePolicy(sizePolicy)
        self.city_search.setMinimumSize(QtCore.QSize(150, 0))
        self.city_search.setObjectName("city_search")
        self.gridLayout_2.addWidget(self.city_search, 0, 1, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.add_city)
        self.listWidget.setWordWrap(False)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 1, 0, 1, 2)
        self.city_add = QtWidgets.QPushButton(self.add_city)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.city_add.sizePolicy().hasHeightForWidth())
        self.city_add.setSizePolicy(sizePolicy)
        self.city_add.setMinimumSize(QtCore.QSize(200, 0))
        self.city_add.setObjectName("city_add")
        self.gridLayout_2.addWidget(self.city_add, 2, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.panel.addTab(self.add_city, "")
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.settings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hr = QtWidgets.QWidget(self.settings)
        self.hr.setObjectName("hr")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.hr)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.hr)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.del_price = QtWidgets.QSlider(self.hr)
        self.del_price.setMinimum(1)
        self.del_price.setMaximum(60)
        self.del_price.setOrientation(QtCore.Qt.Horizontal)
        self.del_price.setObjectName("del_price")
        self.horizontalLayout_4.addWidget(self.del_price)
        self.label_7 = QtWidgets.QLabel(self.hr)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.verticalLayout.addWidget(self.hr, 0, QtCore.Qt.AlignTop)
        self.save_settings = QtWidgets.QPushButton(self.settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_settings.sizePolicy().hasHeightForWidth())
        self.save_settings.setSizePolicy(sizePolicy)
        self.save_settings.setObjectName("save_settings")
        self.verticalLayout.addWidget(self.save_settings)
        self.panel.addTab(self.settings, "")
        self.verticalLayout_2.addWidget(self.panel)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.panel.setCurrentIndex(0)
        self.del_price.valueChanged['int'].connect(self.label_7.setNum)
        self.del_price.valueChanged['int'].connect(self._set_records_per_sector)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Роза ветров"))
        self.create_rose.setText(_translate("MainWindow", "Создать"))
        self.label_3.setText(_translate("MainWindow", "Дата конца измерений"))
        self.label.setText(_translate("MainWindow", "Город"))
        self.label_2.setText(_translate("MainWindow", "Дата начала измерений"))
        self.panel.setTabText(self.panel.indexOf(self.roze), _translate("MainWindow", "роза ветров"))
        self.city_search.setText(_translate("MainWindow", "Поиск"))
        self.city_add.setText(_translate("MainWindow", "Добавить в базу"))
        self.panel.setTabText(self.panel.indexOf(self.add_city), _translate("MainWindow", "добавить город"))
        self.label_6.setText(_translate("MainWindow", "Цена деления:"))
        self.label_7.setText(_translate("MainWindow", "1"))
        self.save_settings.setText(_translate("MainWindow", "Сохранить"))
        self.panel.setTabText(self.panel.indexOf(self.settings), _translate("MainWindow", "настройки"))
    
    def search_cities(self):
        self.listWidget.clear()
        name = self.city_search_name.text()
        if len(name) == 0:
            return
        self.cities = self.db.search_city(name)
        self.listWidget.addItems(map(lambda x: x['name'], self.cities))
    
    def add_cities(self):
        index = self.listWidget.currentRow()
        row = self.cities[index]
        self.db.add_city(row)
        self.listWidget.clear()
    
    def load_cities(self):
        self.loaded_cities = self.db.load_cities()
        for i in self.loaded_cities:
            self.city_choosing.addItem(i.title)
        if len(self.loaded_cities) > 0:
            self.city_choosing.setCurrentIndex(1)
    
    def load_winds(self):
        city = self.loaded_cities[self.city_choosing.currentIndex()]
        date_to = self.date_from.date()
        date_from = self.date_to.date()
        date_from = datetime(year=date_from.year(), month=date_from.month(), day=date_from.day())
        date_to = datetime(year=date_to.year(), month=date_to.month(), day=date_to.day())
        if date_from > date_to:
            self.label_5.setText('Дата начала измерений не может быть позже даты конца измерений')
            self.label_5.repaint()
            return
        self.label_5.setText('Загрузка данных. Программа зависнет на некоторое время')
        self.label_5.repaint()
        self.window.repaint()
        data = self.db.load_weather(date_from, date_to, city)
        self.label_5.setText('Загрузка завершена')
        self.roze_image.set_winds(data)

        

    
    def save_settings_func(self):
        self.records_per_sector = self.del_price.tickPosition()
        self.roze_image.set_records_per_sector(self.records_per_sector)
    
    def _bind_buttons(self):
        self.city_search.clicked.connect(self.search_cities)
        self.city_add.clicked.connect(self.add_cities)
        self.city_add.clicked.connect(self.load_cities)
        self.create_rose.clicked.connect(self.load_winds)
        self.save_settings.clicked.connect(self.save_settings_func)
    
    def _set_time_now(self):
        now = datetime.now()
        qt_now = QtCore.QDate(now.year, now.month, now.day)
        self.date_from.setDate(qt_now)
        self.date_to.setDate(qt_now)

    def _set_records_per_sector(self, num):
        self.records_per_sector = num
        self.roze_image.set_records_per_sector(self.records_per_sector)

    


if __name__ == "__main__":
    try:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        ui = Ui_MainWindow()
        ui.window.show()
        sys.exit(app.exec_())
    except Exception as msg:
        print(msg)
        input()
