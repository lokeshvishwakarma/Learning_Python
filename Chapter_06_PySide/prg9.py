import sys
import PySide2.QtWidgets as QtWidgets
import PySide2.QtGui as QtGui
import PySide2.QtCore as QtCore


class ListDataDialog(QtWidgets.QWidget):
    def __init__(self):
        super(ListDataDialog, self).__init__()
        self.setMinimumWidth(600)
        self.setMinimumHeight(200)
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.my_list_wdg = QtWidgets.QListWidget()
        self.my_list_wdg.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.my_list_wdg.addItems(['Item 1', 'Item 2', 'Item 3', 'Item 4'])
        self.my_list_wdg.installEventFilter(self)

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)
        main_layout.setAlignment(QtCore.Qt.AlignTop)

        vbox_1 = QtWidgets.QVBoxLayout()
        vbox_1.addWidget(self.my_list_wdg)
        main_layout.addLayout(vbox_1)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.ContextMenu and source is self.my_list_wdg:
            menu = QtWidgets.QMenu()
            menu.addAction('Action 1')
            menu.addAction('Action 2')
            menu.addAction('Action 3')

            if menu.exec_(event.globalPos()):
                item = source.itemAt(event.pos())
                row = self.my_list_wdg.row(item)
                self.my_list_wdg.takeItem(row)
                print(item.text())
            return True
        return super().eventFilter(source, event)


app = QtWidgets.QApplication(sys.argv)
ex = ListDataDialog()
ex.show()
sys.exit(app.exec_())
