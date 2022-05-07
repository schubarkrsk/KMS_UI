# Инициализация библиотек
import sys
from PyQt5 import QtWidgets

# Инициализация интерфейса
from misc import appgui

# Инициализация вспомогательных скриптов
from misc import gui_descriptor, writer


class KMSApplication(QtWidgets.QMainWindow, appgui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    application = QtWidgets.QApplication(sys.argv)
    window = KMSApplication()
    window.show()
    application.exec()


if __name__ == "__main__":
    main()
