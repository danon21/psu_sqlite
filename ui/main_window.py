from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QComboBox, QPushButton, QTableView, QScrollBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 640, 480)
        self.setWindowTitle("Отчет \"Окраска автомобилей\"")
        self.setWindowIcon(QIcon("C:/Users/danon/Pictures/pop-cat-icons/Pop Cat icons/Pop cat closed.ico"))
        
        self.centralwidget = QWidget(self)
        
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(9, 10, 621, 31)
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        
        self.comboBox = QComboBox(self.horizontalLayoutWidget)
        self.horizontalLayout.addWidget(self.comboBox)
        
        self.pushButton = QPushButton("Собрать отчет", self.horizontalLayoutWidget)
        self.horizontalLayout.addWidget(self.pushButton)
        
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(10, 50, 621, 421)
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        
        self.tableView = QTableView(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.addWidget(self.tableView)
        
        self.verticalScrollBar = QScrollBar(Qt.Vertical, self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.addWidget(self.verticalScrollBar)
        
        self.setCentralWidget(self.centralwidget)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
