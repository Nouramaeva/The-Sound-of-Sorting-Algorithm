# Add reference to the location of the algorithm being used

import musicalbeeps
import random
import copy


notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


def scaleToNote(value, min_value, max_value, low=48, high=96):
    # C3 = 48   ... midi note number in a range from 0 to 127
    # C4 = 60
    # C7 = 96

    # We will normalize the value in the original range into the range of note values.
    range_max = high - low # 0 is the bottom, this will be the top of the range of notes

    input_range_max = max_value - min_value

    value_relative_to_0 = value - min_value

    value_range_percent = float(value_relative_to_0) / float(input_range_max)

    note_value = int((range_max * value_range_percent) + low)
    # We now have a note number that we can convert to a string for the beep library.

    # To figure out the correct octave value, divide by 12 and subtract 1
    note_octave = int(note_value / 12) - 1

    # Get note string in notes array based on index
    note_index = note_value % 12

    # In the notes array, the sharp is already included. Beeps needs the octave number before the sharp.
    # For example, if we want C# in octave 4, we need to have "C4#".
    # So we get the first character of the value from the array, then add the octave, then add anything that's
    #   after the first character. The [1:] slice will return an empty string if the string is only one character.
    note_string = notes[note_index][0] + str(note_octave) + notes[note_index][1:]

    return note_string
    pass


def insertionSort(arr, player, _min, _max):
    for i in range(1, len(arr)):
        key = arr[i]
        player.play_note(scaleToNote(arr[i], _min, _max), 0.05)
        #player.play_note("B", 0.00005)

        # Move elements of arr, that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            player.play_note(scaleToNote(arr[j], _min, _max), 0.05)
            #player.play_note("D", 0.00005)
            arr[j + 1] = arr[j]

            j -= 1
        arr[j + 1] = key



def main():
    _min = 1
    _max = 100
    listOfData = [random.randint(_min, _max) for i in range(5)]
    player = musicalbeeps.Player(volume=0.8, mute_output=False)

    print(listOfData)
    insertionSort(listOfData, player, _min, _max)
    print(listOfData)



if __name__ == "__main__":
    main()
