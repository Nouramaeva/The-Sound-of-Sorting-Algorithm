import random

import musicalbeeps

from scaleToNote import *
import toneFile
import scaleToFrequency
import Spectogram


def bubble_sort(a_list, player, _min, _max):
    """
    This function sorts a list of numbers using the bubble sort method and scale the number to a midi note

    :param a_list: the list containing the values that we want to sort
    :param _min: Minimum value the number being processed is picked from
    :param _max: Maximum value the number being processed is picked from
    :param player: play the note at a certain position
    :return: the list sorted using bubble sort with corresponding notes one at the time
    """
    t = toneFile.ToneFile("test.wav")
    n = len(a_list)
    for i in range(n - 1):  # number of passes to guarantee the list is sorted
        swapped = False
        for j in range(n - 1):  # running through the elements of the list
            if a_list[j] > a_list[j + 1]:
                swapped = True
                player.play_note(scaleToNote(a_list[j], _min, _max), 0.05)
                t.addToneByFrequency(scaleToFrequency.note_to_frequency(scaleToNote(a_list[j], _min, _max)), 50)

                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
        player.play_note(scaleToNote(a_list[j], _min, _max), 0.05)
        t.addToneByFrequency(scaleToFrequency.note_to_frequency(scaleToNote(a_list[j], _min, _max)), 50)

        if not swapped:
            break
    t.write()
    Spectogram.generate_spectogram('test.wav')
    return a_list


def heapify(arr, n, i):
    """
    This function heapify a subtree rooted with node i which is
    an index in arr[] with n as a size of the heap.

    :param arr: array to sort
    :param n: the size of the heap
    :param i: an index of the array
    :return: a heapify array

    """
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root

    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap

        # Heapify the root.

        heapify(arr, n, largest)


# The main function to sort an array of given size

def heapSort(a_list, player, _min, _max):
    """
    This function sorts a list of numbers using the heap sort method and scale the number to a midi note

    Sorting algorithm that does ...
    :param a_list: the list containing the values that we want to sort
    :param _min: Minimum value the number being processed is picked from
    :param _max: Maximum value the number being processed is picked from
    :param player: play the note at a certain position
    :return: the list sorted using heap sort with corresponding notes one at the time

    """
    n = len(a_list)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    t = toneFile.ToneFile("test.wav")
    for i in range(n // 2 - 1, -1, -1):
        player.play_note(scaleToNote(a_list[i], _min, _max), 0.05)
        t.addToneByFrequency(scaleToFrequency.note_to_frequency(scaleToNote(a_list[i], _min, _max)), 50)
        heapify(a_list, n, i)

    # One by one extract elements

    for i in range(n - 1, 0, -1):
        (a_list[i], a_list[0]) = (a_list[0], a_list[i])  # swap
        player.play_note(scaleToNote(a_list[i], _min, _max), 0.05)
        t.addToneByFrequency(scaleToFrequency.note_to_frequency(scaleToNote(a_list[i], _min, _max)), 50)
        heapify(a_list, i, 0)

    t.write()
    Spectogram.generate_spectogram('test.wav')
    return a_list


def insertion_sort(arr, player, _min, _max):
    """
    This function sorts a list of numbers using the insertion sort method and scale the number to a midi note
    :param arr: the list containing the values that we want to sort
    :param _min: Minimum value the number being processed is picked from
    :param _max: Maximum value the number being processed is picked from
    :param player: play the note at a certain position
    :return: the list sorted using insertion sort with corresponding notes one at the time
    """
    t = toneFile.ToneFile("test.wav")
    for i in range(1, len(arr)):
        key = arr[i]
        player.play_note(scaleToNote(arr[i], _min, _max), 0.05)
        t.addToneByFrequency(scaleToFrequency.note_to_frequency(scaleToNote(arr[i], _min, _max)), 50)

        # Move elements of arr, that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            player.play_note(scaleToNote(arr[j], _min, _max), 0.05)
            t.addToneByFrequency(scaleToFrequency.note_to_frequency(scaleToNote(arr[j], _min, _max)), 50)
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    t.write()
    Spectogram.generate_spectogram('test.wav')
    return arr


def mergeSort(a_list, player, _min, _max):
    """
    This function sorts a list of numbers using the merge sort method and scale the number to a midi note.

    :param a_list: the list containing the values that we want to sort
    :param _min: Minimum value the number being processed is picked from
    :param _max: Maximum value the number being processed is picked from
    :param player: play the note at a certain position
    :return: the list sorted using merge sort with corresponding notes one at the time
    """
    t = toneFile.ToneFile("test.wav")
    if len(a_list) > 1:

        mid = len(a_list) // 2
        player.play_note(scaleToNote(a_list[mid], _min, _max), 0.05)  # play at the index of the mid point
        t.addToneByFrequency(scaleToFrequency.note_to_frequency(scaleToNote(a_list[mid], _min, _max)), 50)
        left = a_list[:mid]
        right = a_list[mid:]

        # Recursive call on each half
        mergeSort(left, player, _min, _max)
        mergeSort(right, player, _min, _max)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # The value from the left half has been used
                a_list[k] = left[i]
                player.play_note(scaleToNote(left[i], _min, _max), 0.08)
                t.addToneByFrequency(scaleToFrequency.note_to_frequency(scaleToNote(left[i], _min, _max)), 50)
                # Move the iterator forward
                i += 1
            else:
                a_list[k] = right[j]
                player.play_note(scaleToNote(right[j], _min, _max), 0.06)
                t.addToneByFrequency(scaleToFrequency.note_to_frequency(scaleToNote(right[j], _min, _max)), 50)
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            a_list[k] = left[i]
            player.play_note(scaleToNote(left[i], _min, _max), 0.08)
            t.addToneByFrequency(scaleToFrequency.note_to_frequency(scaleToNote(left[i], _min, _max)), 50)
            i += 1
            k += 1

        while j < len(right):
            a_list[k] = right[j]
            player.play_note(scaleToNote(right[j], _min, _max), 0.06)
            t.addToneByFrequency(scaleToFrequency.note_to_frequency(scaleToNote(right[j], _min, _max)), 50)
            j += 1
            k += 1

    t.write()
    Spectogram.generate_spectogram('test.wav')
    return a_list
