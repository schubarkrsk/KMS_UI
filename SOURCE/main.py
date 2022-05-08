# Инициализация библиотек
import sys
from PyQt5 import QtWidgets

# Инициализация интерфейса
from misc import appgui

# Инициализация вспомогательных скриптов
from misc import kms, writer


class KMSApplication(QtWidgets.QMainWindow, appgui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._ui_links()

    def _ui_links(self):
        self.btn_gen.clicked.connect(self.btn_gen_clicked)
        # self.btn_genval.clicked.connect(self.btn_gen_val_clicked)

    def btn_gen_clicked(self):
        serial = kms.separate_delete(self.serialNumber.text())
        activation = kms.SimpleKMS.get_activation(serial)
        textActiv = ""
        for i in activation:
            textActiv = textActiv + i + "-"
        textActiv = textActiv[:len(textActiv)-1].upper()
        self.activation.setText(textActiv)


    def btn_gen_val_clicked(self):
        value = self.spinBox.value()
        licenses = kms.SimpleKMS.generate_licenses(value)
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Select floder to save licenses")
        writer.save_in_file(licenses, directory)


def main():
    application = QtWidgets.QApplication(sys.argv)
    window = KMSApplication()
    window.show()
    application.exec()


if __name__ == "__main__":
    main()
