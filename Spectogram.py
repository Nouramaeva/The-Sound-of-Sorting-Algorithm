import wave
import numpy as np
import matplotlib.pyplot as plt


def generate_spectogram(filename):
    """
    This filename generates a waveform for each sorting algorithm selected.
    :param filename: the filename to be graphed
    :return: a waveform of a certain file

    """
    # Open the WAV file
    wav_file = wave.open(filename, 'r')

    # Get the audio data as a raw byte stream
    audio_bytes = wav_file.readframes(-1)

    # Convert the raw bytes to a NumPy array of samples
    audio_samples = np.frombuffer(audio_bytes, dtype=np.int16)

    # Get the audio sample rate
    sample_rate = wav_file.getframerate()

    # Close the WAV file
    wav_file.close()

    # Calculate the duration of the audio in seconds
    duration = len(audio_samples) / float(sample_rate)

    # Generate the time axis for the waveform plot
    time_axis = np.linspace(0, duration, len(audio_samples))

    # Plot the waveform
    # plt.plot(time_axis, audio_samples)
    plt.specgram(audio_samples, cmap="rainbow")
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Spectrogram of {}'.format(filename))
    plt.show()
