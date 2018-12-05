from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

import ui_test

class MainForm(QMainWindow):
    def __init__(self, parent=None):
        super(MainForm,self).__init__(parent)
        self.ui = ui_test.Ui_MainWindow()
        self.ui.setupUi(self)

'''
def closeEvent(self, event):
        reply = QMessageBox.question(self, '关闭', '确认退出吗？', QMessageBox.StandardButtons(
            QMessageBox.Yes|QMessageBox.No))
        if reply:
            event.accept()
        else:
            event.ignore()
'''

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.exit(app.exec_())