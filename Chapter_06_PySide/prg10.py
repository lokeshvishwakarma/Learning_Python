import os
import sys

import PySide2.QtGui as QtGui
import PySide2.QtCore as QtCore
import PySide2.QtWidgets as QtWidgets


class FileEdit(QtWidgets.QLineEdit):
    def __init__(self, parent):
        super(FileEdit, self).__init__(parent)
        self.setDragEnabled(True)

    def dragEnterEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dropEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            # for some reason, this doubles up the intro slash
            filepath = str(urls[0].path())[1:]
            self.setText(filepath)


class QLineEditDropHandler(QtCore.QObject):
    def eventFilter(self, watched, event):
        if event.type() == QtCore.QEvent.DragEnter:
            data = event.mimeData()
            urls = data.urls()
            if urls and urls[0].scheme() == 'file':
                event.acceptProposedAction()

        if event.type() == QtCore.QEvent.DragMove:
            data = event.mimeData()
            urls = data.urls()
            if urls and urls[0].scheme() == 'file':
                event.acceptProposedAction()

        if event.type() == QtCore.QEvent.Drop:
            data = event.mimeData()
            urls = data.urls()
            if urls and urls[0].scheme() == 'file':
                filepath = str(urls[0].path())[1:]
                watched.setText(filepath)
                return True
        return super().eventFilter(watched, event)


class MyDialog(QtWidgets.QWidget):
    def __init__(self, title):
        super(MyDialog, self).__init__()
        self.setWindowTitle(title)
        self.setMinimumWidth(600)
        self.setMinimumHeight(200)
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.installEventFilter(QLineEditDropHandler(self.line_edit))

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)
        main_layout.setAlignment(QtCore.Qt.AlignTop)

        vbox_1 = QtWidgets.QVBoxLayout()
        vbox_1.addWidget(self.line_edit)
        main_layout.addLayout(vbox_1)
        # connections


app = QtWidgets.QApplication(sys.argv)
dialog = MyDialog('My Dialog')
dialog.show()
sys.exit(app.exec_())
