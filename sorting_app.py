import os
import sys

sys.dont_write_bytecode = True  # noqa: E402
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))  # noqa: E402

from PySide6.QtUiTools import loadUiType

from PySide6.QtCore import (
    QCoreApplication,
    Qt,
    Slot
)

from PySide6.QtWidgets import (
    QApplication,
    QMessageBox
)

import listswrapper as ls

UIsPath = "ui/"

mainUIfilePath = UIsPath + "MainWindow.ui"
Form, Base = loadUiType(os.path.join(sys.path[1], mainUIfilePath))


class MainWindow(Form, Base):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.__activeList = []
        self.lcbSortingAlgo.addItem(ls.SortingAlgo.Bubble.name + " (Slow)")
        self.lcbSortingAlgo.addItem(ls.SortingAlgo.Selection.name + " (Slow)")
        self.lcbSortingAlgo.addItem(ls.SortingAlgo.Insertion.name + " (Slow)")
        self.lcbSortingAlgo.addItem(ls.SortingAlgo.Heap.name)
        self.lcbSortingAlgo.addItem(ls.SortingAlgo.Merge.name)
        self.lcbSortingAlgo.addItem(ls.SortingAlgo.Quick.name)
        self.update_list()

    @property
    def activeList(self):
        return self.__activeList

    @activeList.setter
    def activeList(self, value):
        self.__activeList = value
        self.update_list()

    def update_list(self):
        self.lwNumberList.clear()
        if len(self.activeList) == 0:
            self.leCount.setText("0")
            self.leSum.setText("0")
            self.leAMean.setText("0")
            self.leMax.setText("0")
            self.leMin.setText("0")
            return
        for i in self.activeList:
            self.lwNumberList.addItem(str(i))
        self.leCount.setText(str(len(self.activeList)))
        self.leSum.setText(str(sum(self.activeList)))
        self.leAMean.setText(str(ls.arithmetic_mean(self.activeList)))
        self.leMax.setText(str(max(self.activeList)))
        self.leMin.setText(str(min(self.activeList)))

    @Slot()
    def on_btnRegenerateList_clicked(self):
        self.activeList = ls.generate_random_list(self.sbCount.value(), self.sbMin.value(), self.sbMax.value())

    @Slot()
    def on_btnSort_clicked(self):
        run = True
        if len(self.activeList) > 5000 and self.lcbSortingAlgo.currentIndex() < 3:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setText("Are you sure you want to sort this large of a list with an algorithm this slow?")
            msgBox.setInformativeText("Do you want to cary on?")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if msgBox.exec() == QMessageBox.StandardButton.No:
                run = False

        if run:
            self.activeList = ls.sort_list(self.activeList, self.lcbSortingAlgo.currentIndex() + 1)
            if self.cbReverse.isChecked():
                self.activeList = self.activeList[::-1]


if __name__ == "__main__":
    os.environ['PYSIDE_DESIGNER_PLUGINS'] = "."
    os.environ["QT_LOGGING_RULES"] = '*.debug=false;qt.pysideplugin=false'

    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    os.chdir(sys.path[1])
    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())
