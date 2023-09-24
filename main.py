import sys
from PyQt6.QtWidgets import QMessageBox,QApplication,QWidget,QMenu,QPushButton,QMainWindow
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit,
        QTextEdit, QGridLayout, QApplication,QPushButton)
from PyQt6.QtGui import QPixmap
from qt_material import apply_stylesheet
# import qtawesome as qta
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.center()
    
    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件')

        impMenu = QMenu('导入数据', self)
        impAct = QAction('导入', self)
        impMenu.addAction(impAct)

        newAct = QAction('获得数据', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        title = QLabel('网址')
        author = QLabel('博主')
        review = QLabel('结果')
        pixmap = QPixmap('day07/weibo/data/帖子热度统计.png')

        # review.setPixmap(pixmap)
        # review.setScaledContents(True)
        
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()
        string=titleEdit.text()
        reviewEdit.append('<img src=day07/weibo/data/帖子热度统计.png>')
        button=QPushButton("提交")
        button.clicked.connect(self.buttonClicked)
        button.setObjectName(str(string));
        grid = QGridLayout()
        grid.setSpacing(10)
        print(string)
        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)
        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
        grid.addWidget(button,3,1)
        grid.addWidget(review, 4, 0)
        grid.addWidget(reviewEdit, 4, 1, 5, 1)
        widget=QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)
        self.statusBar()
        self.setGeometry(300, 300, 350, 300)
        self.resize(900,650)
        self.setWindowTitle('微博数据分析')
        self.show()
    
    def closeEvent(self,event):
        reply = QMessageBox.question(self,'Message',"你确定要退出吗？",QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def buttonClicked(self):
        sender = self.sender()
        msg = f'{sender.text()} was pressed'
        self.statusBar().showMessage(msg)

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.center())

def main():
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='light_blue.xml')
    # w = QWidget()
    # w.resize(250,200)
    # w.move(300,300)
    # w.setWindowTitle('hello')
    # w.show()
    ex = Example()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()