import sys
import PySide2.QtWidgets as QtWidgets
import PySide2.QtCore as QtCore


class MyDialog(QtWidgets.QWidget):
    def __init__(self):
        super(MyDialog, self).__init__()
        self.setMinimumHeight(500)
        self.setMinimumWidth(800)
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.radio1 = QtWidgets.QRadioButton('1')
        self.radio2 = QtWidgets.QRadioButton('2')
        self.radio3 = QtWidgets.QRadioButton('3')
        self.radio4 = QtWidgets.QRadioButton('4')
        self.radio5 = QtWidgets.QRadioButton('5')
        self.radio6 = QtWidgets.QRadioButton('6')

        self.menubar = QtWidgets.QMenuBar()
        self.file_menu = self.menubar.addMenu('File')
        self.edit_menu = self.menubar.addMenu('Edit')
        self.help_menu = self.menubar.addMenu('Help')

        new = QtWidgets.QAction('New', self.file_menu)
        save = QtWidgets.QAction('Save', self.file_menu)
        save.setShortcut('Ctrl+S')
        exit = QtWidgets.QAction('Exit', self.file_menu)

        self.file_menu.addAction(new)
        self.file_menu.addAction(save)
        self.file_menu.addSeparator()
        self.file_menu.addAction(exit)

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)
        main_layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

        grp_box1 = QtWidgets.QGroupBox()
        grp_box2 = QtWidgets.QGroupBox()

        vbox1 = QtWidgets.QVBoxLayout()
        vbox1.addWidget(self.radio1)
        vbox1.addWidget(self.radio2)
        vbox1.addWidget(self.radio3)

        vbox2 = QtWidgets.QVBoxLayout()
        vbox2.addWidget(self.radio4)
        vbox2.addWidget(self.radio5)
        vbox2.addWidget(self.radio6)

        grp_box1.setLayout(vbox1)
        grp_box1.setTitle('Menu 1')
        grp_box2.setLayout(vbox2)
        grp_box2.setTitle('Menu 2')

        main_layout.setMenuBar(self.menubar)
        main_layout.addWidget(grp_box1)
        main_layout.addWidget(grp_box2)

        # conections
        self.file_menu.triggered[QtWidgets.QAction].connect(self.menu_trigger)

    def menu_trigger(self, action):
        print(action.text())


app = QtWidgets.QApplication(sys.argv)
mydialog = MyDialog()
mydialog.show()
app.exec_()
