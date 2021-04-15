from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from rose_class import RoseWidget
from weather_api import WeatherApi


class Ui_MainWindow(object):
    def __init__(self) -> None:
        self.weather = WeatherApi()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.panel = QtWidgets.QTabWidget(self.centralwidget)
        self.panel.setObjectName("panel")
        self.roze = QtWidgets.QWidget()
        self.roze.setObjectName("roze")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.roze)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.roze)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.city_choosing = QtWidgets.QComboBox(self.roze)
        self.city_choosing.setObjectName("city_choosing")
        self.city_choosing.addItem("")
        self.gridLayout.addWidget(self.city_choosing, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.roze)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        day_now, mouth_now, year_now = datetime.now().day, datetime.now().month, datetime.now().year

        self.date_from = QtWidgets.QDateEdit(self.roze)
        self.date_from.setDate(QtCore.QDate(year_now, mouth_now, day_now))
        self.date_from.setMaximumDate(QtCore.QDate(year_now, mouth_now, day_now))
        self.date_from.setObjectName("date_from")
        self.gridLayout.addWidget(self.date_from, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.roze)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)
        self.date_to = QtWidgets.QDateEdit(self.roze)
        self.date_to.setDate(QtCore.QDate(year_now, mouth_now, day_now))
        self.date_to.setMaximumDate(QtCore.QDate(year_now, mouth_now, day_now))
        self.date_to.setObjectName("date_to")
        self.gridLayout.addWidget(self.date_to, 5, 1, 1, 1)
        self.create_rose = QtWidgets.QPushButton(self.roze)
        self.create_rose.setObjectName("create_rose")
        self.gridLayout.addWidget(self.create_rose, 6, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.roze)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 1, 1, 1)
        self.file_name = QtWidgets.QLineEdit(self.roze)
        self.file_name.setObjectName("file_name")
        self.gridLayout.addWidget(self.file_name, 8, 1, 1, 1)
        self.save_file = QtWidgets.QPushButton(self.roze)
        self.save_file.setObjectName("save_file")
        self.gridLayout.addWidget(self.save_file, 9, 1, 1, 1)
        self.roze_image = RoseWidget()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.roze_image.sizePolicy().hasHeightForWidth())
        self.roze_image.setSizePolicy(sizePolicy)
        self.roze_image.setMinimumSize(QtCore.QSize(400, 300))
        self.roze_image.setObjectName("roze_image")
        self.gridLayout.addWidget(self.roze_image, 0, 0, 10, 1)
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
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.city_search.sizePolicy().hasHeightForWidth())
        self.city_search.setSizePolicy(sizePolicy)
        self.city_search.setMinimumSize(QtCore.QSize(150, 0))
        self.city_search.setObjectName("city_search")
        self.gridLayout_2.addWidget(self.city_search, 0, 1, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.add_city)
        self.listWidget.setGridSize(QtCore.QSize(0, 0))
        self.listWidget.setWordWrap(False)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 1, 0, 1, 2)
        self.city_add = QtWidgets.QPushButton(self.add_city)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.city_add.sizePolicy().hasHeightForWidth())
        self.city_add.setSizePolicy(sizePolicy)
        self.city_add.setMinimumSize(QtCore.QSize(200, 0))
        self.city_add.setObjectName("city_add")
        self.gridLayout_2.addWidget(
            self.city_add, 2, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.panel.addTab(self.add_city, "")
        self.horizontalLayout.addWidget(self.panel)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.panel.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Роза ветров"))
        self.label.setText(_translate("MainWindow", "Город"))
        self.city_choosing.setItemText(0, _translate("MainWindow", "тест"))
        self.label_2.setText(_translate("MainWindow", "Дата начала измерений"))
        self.label_3.setText(_translate("MainWindow", "Дата конца измерений"))
        self.create_rose.setText(_translate("MainWindow", "Создать"))
        self.label_4.setText(_translate("MainWindow", "Имя файла"))
        self.save_file.setText(_translate("MainWindow", "Сохранить"))
        self.panel.setTabText(self.panel.indexOf(
            self.roze), _translate("MainWindow", "роза ветров"))
        self.city_search.setText(_translate("MainWindow", "Поиск"))
        self.city_add.setText(_translate("MainWindow", "Добавить в базу"))
        self.panel.setTabText(self.panel.indexOf(
            self.add_city), _translate("MainWindow", "добавить город"))
    
    def bind_cuttons(self):
        self.create_rose.clicked.connect(self.set_weather)
    
    def set_weather(self):
        date_to = self.date_from.date().toString('dd.MM.yyyy')
        date_from = self.date_to.date().toString('dd.MM.yyyy')
        date_from = datetime.strptime(date_from, '%d.%m.%Y')
        date_to = datetime.strptime(date_to, '%d.%m.%Y')
        
        if date_from > date_to:
            return
        
        data = self.weather.get_wind_during_date('https://www.worldweatheronline.com/kazan-weather-history/tatarstan/ru.aspx',
                                                 date_from, date_to)
        print(data)
        self.roze_image.set_winds(data)
    
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.bind_cuttons()
    MainWindow.show()
    sys.exit(app.exec_())
