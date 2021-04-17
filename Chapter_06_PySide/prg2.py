import sys
import PySide2.QtWidgets as QtWidgets
import PySide2.QtGui as QtGui
import PySide2.QtCore as QtCore
import os

curr_dir = os.path.dirname(__file__)
icons_path = os.path.join(curr_dir, 'icons')

students = ['loki', 'sunil', 'datta']


class Account:
    def __init__(self, account_no, account_balance):
        self.account_no = account_no
        self.account_balance = account_balance

    def __repr__(self):
        return "Account No: {}, Balance: {}".format(self.account_no, self.account_balance)


acc1 = Account(1, 5000)
acc2 = Account(2, 5000)
acc3 = Account(3, 5000)
acc4 = Account(4, 5000)
acc5 = Account(4, 5000)
acc6 = Account(4, 5000)
acc7 = Account(4, 5000)
acc8 = Account(4, 5000)
acc9 = Account(4, 5000)
acc10 = Account(4, 5000)
acc11 = Account(4, 5000)
acc12 = Account(4, 5000)

accounts_list = [acc1, acc2, acc3, acc4,
                 acc5, acc6, acc7, acc8,
                 acc9, acc10, acc11, acc12,
                 ]


class MyDialog(QtWidgets.QWidget):
    def __init__(self, title):
        super(MyDialog, self).__init__()
        self.setWindowTitle(title)
        self.setMinimumWidth(600)
        self.setMinimumHeight(200)
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        submit_img = os.path.join(icons_path, 'deadline.png')
        self.submit_icon = QtGui.QIcon(submit_img)
        self.submit_button = QtWidgets.QPushButton('Submit')
        self.submit_button.setIcon(self.submit_icon)
        self.delete_button = QtWidgets.QPushButton('Delete')

        self.my_list_wdg = QtWidgets.QListWidget()
        self.my_list_wdg.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)
        main_layout.setAlignment(QtCore.Qt.AlignTop)

        vbox_1 = QtWidgets.QVBoxLayout()
        vbox_1.addWidget(self.submit_button)
        vbox_1.addWidget(self.delete_button)
        vbox_1.addWidget(self.my_list_wdg)
        main_layout.addLayout(vbox_1)

        # connections
        # self.submit_button.clicked.connect(self.populate_student_data)
        self.submit_button.clicked.connect(self.populate_account_data)
        self.delete_button.clicked.connect(self.delete_selected)

    def populate_student_data(self):
        # for student in students:
        #     self.my_list_wdg.addItem(student)
        self.my_list_wdg.addItems(students)

    def populate_account_data(self):
        for account in accounts_list:
            self.my_list_wdg.addItem(str(account))

    def delete_selected(self):
        for item in self.my_list_wdg.selectedItems():
            row = self.my_list_wdg.row(item)
            self.my_list_wdg.takeItem(row)


app = QtWidgets.QApplication(sys.argv)
dialog = MyDialog('My Dialog')
dialog.show()
sys.exit(app.exec_())
