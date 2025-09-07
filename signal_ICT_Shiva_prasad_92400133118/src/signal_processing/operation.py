import numpy as np
import matplotlib.pyplot as plt

def time_shift(signal, k):
    """
    Shifts the signal by k units.
    Positive k → right shift
    Negative k → left shift
    """
    shifted = np.roll(signal, k)
    return shifted

def time_scale(signal, k):
    """
    Scales the signal in time.
    For discrete signals, this is done by stretching/compressing the index.
    """
    n = np.arange(len(signal))
    scaled = signal[::k] if k > 0 else signal
    return scaled

def signal_addition(signal1, signal2):
    """
    Adds two signals point-wise.
    """
    min_len = min(len(signal1), len(signal2))
    return signal1[:min_len] + signal2[:min_len]

def signal_multiplication(signal1, signal2):
    """
    Multiplies two signals point-wise.
    """
    min_len = min(len(signal1), len(signal2))
    return signal1[:min_len] * signal2[:min_len]
