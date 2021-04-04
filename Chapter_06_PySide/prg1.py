import sys
import PySide2.QtWidgets as QtWidgets
import PySide2.QtCore as QtCore


class MyDialog(QtWidgets.QDialog):
    def __init__(self, title):
        super(MyDialog, self).__init__()
        self.setWindowTitle(title)
        self.setMinimumWidth(600)
        self.setMinimumHeight(400)
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.first_name = QtWidgets.QLineEdit('First Name')
        self.first_name.setMaximumWidth(120)
        self.last_name = QtWidgets.QLineEdit('Last Name')
        self.last_name.setMaximumWidth(120)
        self.email = QtWidgets.QLineEdit('Email')
        self.email.setMaximumWidth(120)
        self.male_rad = QtWidgets.QRadioButton('Male')
        self.male_rad.setMaximumWidth(100)
        self.female_rad = QtWidgets.QRadioButton('Female')
        self.female_rad.setMaximumWidth(100)
        self.submit_button = QtWidgets.QPushButton('Submit')
        self.cancel_button = QtWidgets.QPushButton('Cancel')

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)
        main_layout.setAlignment(QtCore.Qt.AlignTop)

        hbox_1 = QtWidgets.QHBoxLayout()
        hbox_1.setAlignment(QtCore.Qt.AlignLeft)
        hbox_2 = QtWidgets.QHBoxLayout()
        hbox_2.setAlignment(QtCore.Qt.AlignLeft)
        hbox_3 = QtWidgets.QHBoxLayout()
        hbox_3.setAlignment(QtCore.Qt.AlignLeft)

        hbox_1.addWidget(self.first_name)
        hbox_1.addWidget(self.last_name)
        main_layout.addLayout(hbox_1)

        hbox_2.addWidget(self.email)
        hbox_2.addWidget(self.male_rad)
        hbox_2.addWidget(self.female_rad)
        main_layout.addLayout(hbox_2)

        hbox_3.addWidget(self.submit_button)
        hbox_3.addWidget(self.cancel_button)
        main_layout.addLayout(hbox_3)


app = QtWidgets.QApplication(sys.argv)
dialog = MyDialog('My Dialog')
dialog.show()
sys.exit(app.exec_())
