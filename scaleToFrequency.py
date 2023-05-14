import math
from scaleToNote import scaleToNote
from random import randint

def note_to_frequency(note):
    """
    Converts a note name (e.g. "A4", "C#3") to the corresponding frequency.

    Parameters: c3#
        note (str): The note name to convert.

    Returns:
        float: The frequency corresponding to the note.
    """
    notes = {
        "C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5,
        "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11
    }
    if note[-1] == "#":
        octave = int(note[1:-1])
    else:
        octave = int(note[1:])
    #print(note)
    #print(octave)
    note_name = note[0]
    if note[-1] == "#":
        note_name += "#"
    #print(note_name)

    semitones = 12 * (octave - 4) + notes[note_name]
    return 440 * math.pow(2, semitones / 12)

if __name__ == "__main__":
    #x = [randint(1, 1000) for _ in range(10)]
    x = [850, 471, 503, 489, 642, 274, 126, 501, 889, 269]
    print(x)
    #scaleToNote(x[2], 1, 100)
    #print(note_to_frequency('G#3'))
    for i in range(len(x) - 1):
        t = scaleToNote(x[i], 1, 100)
        #print(t)
        print(note_to_frequency(t))


    assert(note_to_frequency("A38#") == 13468860621783.02)
    assert(note_to_frequency("D23") == 258937088.24897102)
