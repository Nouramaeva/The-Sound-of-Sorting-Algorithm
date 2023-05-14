import sys
import random
import musicalbeeps
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton

from sortingAlgorithm import bubble_sort, mergeSort, insertion_sort, heapSort


class SortVisualization(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(50, 50, 715, 250)
        self.setWindowTitle("Sort Visualization")

        self.initUI()

    def initUI(self):
        self.sort_dropdown = QComboBox(self)
        self.sort_dropdown.setGeometry(50, 50, 200, 30)
        self.sort_dropdown.addItems(["Insertion sort", "Bubble sort", "Merge sort", "Heap sort"])

        self.vis_dropdown = QComboBox(self)
        self.vis_dropdown.setGeometry(300, 50, 200, 30)
        self.vis_dropdown.addItems(["Spectogram"])

        self.ok_button = QPushButton("OK", self)
        self.ok_button.setGeometry(550, 50, 100, 30)
        self.ok_button.clicked.connect(self.perform_action)

    def perform_action(self):
        _min = 1
        _max = 1000
        total = 20

        listOfData = [random.randint(_min, _max) for i in range(total)]
        print(listOfData)
        player = musicalbeeps.Player(volume=0.8, mute_output=False)

        selected_option = self.sort_dropdown.currentText()
        selected_option2 = self.vis_dropdown.currentText()

        if selected_option == "Insertion sort" and selected_option2 == "Spectogram":
            # perform action for insertion sort
            insertion_sort(listOfData, player, _min, _max)


        elif selected_option == "Bubble sort" and selected_option2 == "Spectogram":
            # perform action for bubble sort
            bubble_sort(listOfData, player, _min, _max)


        elif selected_option == "Merge sort" and selected_option2 == "Spectogram":
            # perform action for merge sort
            mergeSort(listOfData, player, _min, _max)


        elif selected_option == "Heap sort" and selected_option2 == "Spectogram":
            # perform action for heap sort
            heapSort(listOfData, player, _min, _max)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SortVisualization()
    ex.show()
    sys.exit(app.exec_())
