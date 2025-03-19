from PySide6 import QtCore, QtGui, QtWidgets
from detectWindow import Ui_MainWindow


class run_Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.select_file.clicked.connect(self.choose_file)
        # self.setSizePolicy(
        #     QtWidgets.QSizePolicy.horizontalPo,  # 水平策略
        #     QtWidgets.QSizePolicy.verticalPolicy()  # 垂直策略
        # )
    def choose_file(self):
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Image File", "", "Image files (*.jpg *.png)")
        self.img_path.setText(filepath)
        if filepath.split('.')[-1] in ['jpg', 'png']:
            self.show_img()
    def show_img(self):
        img_path = self.img_path.text()
        self.img = QtGui.QPixmap(img_path)
        self.show_label.setPixmap(self.img)
        self.show_label.show()
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = run_Window()
    window.show()
    sys.exit(app.exec_())