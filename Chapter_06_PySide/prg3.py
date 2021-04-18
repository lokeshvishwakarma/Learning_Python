import sys
import PySide2.QtWidgets as QtWidgets
import PySide2.QtGui as QtGui
import PySide2.QtCore as QtCore


class MyDialog(QtWidgets.QWidget):
    def __init__(self, title):
        super(MyDialog, self).__init__()
        self.setWindowTitle(title)
        self.setMinimumWidth(300)
        self.setMinimumHeight(100)
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.submit_button = QtWidgets.QPushButton('Submit')
        self.delete_button = QtWidgets.QPushButton('Delete')

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)
        main_layout.setAlignment(QtCore.Qt.AlignTop)

        vbox_1 = QtWidgets.QVBoxLayout()
        vbox_1.addWidget(self.submit_button)
        vbox_1.addWidget(self.delete_button)
        main_layout.addLayout(vbox_1)

        # connections
        self.submit_button.clicked.connect(self.submit_pressed)
        self.delete_button.clicked.connect(self.delete_pressed)

    def submit_pressed(self):
        msg_box = MessageBox('Submit')
        msg_box.exec_()

    def delete_pressed(self):
        msg_box = MessageBox('Delete')
        msg_box.exec_()


class MessageBox(QtWidgets.QDialog):
    def __init__(self, text):
        super(MessageBox, self).__init__()
        self.setMinimumWidth(300)
        self.setMinimumHeight(100)
        self.create_widgets(text)
        self.create_layout()

    def create_widgets(self,text):
        msg = "Pressed {} button.".format(text)
        self.label = QtWidgets.QLabel(msg)

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)
        main_layout.setAlignment(QtCore.Qt.AlignTop)
        main_layout.addWidget(self.label)


app = QtWidgets.QApplication(sys.argv)
dialog = MyDialog('My Dialog')
dialog.show()
sys.exit(app.exec_())
