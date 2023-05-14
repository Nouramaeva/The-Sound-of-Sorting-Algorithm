notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


def scaleToNote(value: int, min_value: int, max_value: int, low: int = 48, high: int = 96):
    """
    Function to convert a numeric value scale into a musical scale.
    :param value: Number being processed
    :param min_value: Minimum value the number being processed is picked from
    :param max_value: Maximum value the number being processed is picked from
    :param low: Minimum midi note correspond to C3
    :param high: Maximum midi note correspond to c7
    :return: The note that has been scaled
    """

    range_max = high - low  # 0 is the bottom, this will be the top of the range of notes  48

    input_range_max = max_value - min_value  # 999

    value_relative_to_0 = value - min_value  # 54

    value_range_percent = float(value_relative_to_0) / float(input_range_max)  # 0.054

    note_value = int((range_max * value_range_percent) + low)
    # We now have a note number that we can convert to a string for the beep library.  50.59

    # To figure out the correct octave value, divide by 12 and subtract 1
    note_octave = int(note_value / 12) - 1  # 3

    # Get note string in notes array based on index
    note_index = note_value % 12  # 2.59

    # So we get the first character of the value from the array, then add the octave, then add anything that's
    #   after the first character. The [1:] slice will return an empty string if the string is only one character.
    note_string = notes[note_index][0] + str(note_octave) + notes[note_index][1:]
    return note_string

