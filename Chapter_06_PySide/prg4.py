import json
import sys

from PySide2 import QtWidgets
from PySide2 import QtCore

with open('countries_states.json', 'r') as db_file:
    database = json.load(db_file)


class CountryDialog(QtWidgets.QWidget):
    def __init__(self):
        super(CountryDialog, self).__init__()
        self.setMinimumWidth(300)
        self.setMinimumHeight(100)
        self.create_widgets()
        self.create_layout()
        self.populate_countries()

    def create_widgets(self):
        self.country_lbl = QtWidgets.QLabel('Country')
        self.state_lbl = QtWidgets.QLabel('State')
        self.country_cbx = QtWidgets.QComboBox()
        self.state_cbx = QtWidgets.QComboBox()

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)
        main_layout.setAlignment(QtCore.Qt.AlignTop)

        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.country_lbl)
        hbox.addWidget(self.country_cbx)
        hbox.addWidget(self.state_lbl)
        hbox.addWidget(self.state_cbx)

        main_layout.addLayout(hbox)

        # connections
        self.country_cbx.currentIndexChanged.connect(self.populate_states)

    def populate_countries(self):
        countries = [x for x in database]
        self.country_cbx.addItems(countries)

    def populate_states(self):
        self.state_cbx.clear()
        for k, v in database.items():
            if k == self.country_cbx.currentText():
                self.state_cbx.addItems(v)


app = QtWidgets.QApplication(sys.argv)
dialog = CountryDialog()
dialog.show()
sys.exit(app.exec_())
