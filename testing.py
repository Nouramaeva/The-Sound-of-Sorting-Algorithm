import unittest

from scaleToNote import scaleToNote
from sortingAlgorithm import bubble_sort, mergeSort, insertion_sort, heapSort
import musicalbeeps


class TestMyMethods(unittest.TestCase):

    def test_mergesort(self):
        player = musicalbeeps.Player(volume=0.8, mute_output=False)
        self.assertEqual(mergeSort([6, 8, 4, 3, 2, 1], player, 1, 1000), [1, 2, 3, 4, 6, 8])
        self.assertEqual(mergeSort([6, 8, 4, 3, 2, 1], player, 90, 700), [1, 2, 3, 4, 6, 8])

    def test_heapsort(self):
        player = musicalbeeps.Player(volume=0.8, mute_output=False)
        self.assertEqual(heapSort([6, 8, 4, 3, 2, 1], player, 1, 1000), [1, 2, 3, 4, 6, 8])
        self.assertEqual(heapSort([6, 8, 4, 10, 2, 1, 11], player, 0, 999), [1, 2, 4, 6, 8, 10, 11])
        # self.assertEqual()

    def test_insertion(self):
        player = musicalbeeps.Player(volume=0.8, mute_output=False)
        self.assertEqual(insertion_sort([6, 8, 4, 3, 2, 1], player, 1, 1000), [1, 2, 3, 4, 6, 8])
        self.assertEqual(insertion_sort([6, 8, 4, 10, 2, 1, 11], player, 12, 999), [1, 2, 4, 6, 8, 10, 11])

    def test_bubble(self):
        player = musicalbeeps.Player(volume=0.8, mute_output=False)
        self.assertEqual(bubble_sort([6, 8, 4, 3, 2, 1], player, 1, 1000), [1, 2, 3, 4, 6, 8])
        self.assertEqual(bubble_sort([6, 8, 4, 10, 2, 1, 11], player, 80, 999), [1, 2, 4, 6, 8, 10, 11])

    def test_scaleToNote(self):
        self.assertEqual(scaleToNote(48, 0, 127, 0, 127), 'C3')
        self.assertEqual(scaleToNote(55, 0, 127, 0, 127), 'G3')
        self.assertEqual(scaleToNote(65, 0, 1000, 63, 96), 'F4')
        self.assertEqual(scaleToNote(86, 20, 500, 63, 96), 'G4')
        self.assertEqual(scaleToNote(101, 100, 800, 90, 127), 'F6#')
        self.assertEqual(scaleToNote(200, 98, 990, 60, 96), 'E4')


if __name__ == '__main__':
    unittest.main()
