# Import the necessary modules
import numpy as np
import matplotlib.pyplot as plt

"""1. unitary_signals.py
This module contains functions for generating foundational discrete-time signals. All functions return a NumPy array representing the signal and automatically plot the generated signal using matplotlib.

Function	Description
unit_step(n)	Generates a unit step signal, defined as 1 for nge0 and 0 otherwise.
unit_impulse(n)	Generates a unit impulse (or delta) signal, which is 1 at n=0 and 0 for all other values of n.
ramp_signal(n)	Generates a ramp signal, where the value of the signal is equal to n for n
ge0 and 0 otherwise.
from unitary_signals import unit_step, unit_impulse, ramp_signal
from trigonometric_signals import sine_wave, exponential_signal
from operations import time_shift, signal_addition """

#trigonometric_signals.py:
"""This module focuses on generating continuous-time trigonometric and exponential signals.
sine_wave(A, f, phi, t)	Generates a sine wave with amplitude A, frequency f, phase phi, and a time vector t. The signal is given by A sin(2 pift+ phi).
cosine_wave(A, f, phi, t)	Generates a cosine wave with amplitude A, frequency f, phase phi, and a time vector t. The signal is given by A cos(2pift+phi).
exponential_signal(A, a, t)	Generates a real exponential signal of the form Ae  at
  with amplitude A, exponent a, and a time vector t."""

  """# operations.py
This module provides functions for performing common signal manipulations.

Function	Description
time_shift(signal, k)	Shifts a signal by k units. A positive k shifts the signal to the right (delay), while a negative k shifts it to the left (advance).
time_scale(signal, k)	Scales the time axis of a signal by a factor k. If k1, the signal is compressed; if $0 \< k \< 1$, it's expanded.
signal_addition(signal1, signal2)	Performs element-wise addition of two signals, ensuring they have compatible dimensions.
signal_multiplication(signal1, signal2)	Performs element-wise multiplication of two signals, ensuring they have compatible dimensions.

# Example 1: Generate and plot a unit step signal
n = np.arange(-5, 10)
unit_step(n)

# Example 2: Generate a sine wave
t = np.linspace(0, 2 * np.pi, 100)
sine_wave_signal = sine_wave(A=5, f=1, phi=0, t=t)

# Example 3: Perform signal operations
# Generate two signals
signal1 = exponential_signal(A=1, a=-0.5, t=t)
signal2 = exponential_signal(A=1, a=-0.2, t=t)

# Add them together
summed_signal = signal_addition(signal1, signal2)

# Shift one of the signals
shifted_signal = time_shift(signal1, k=10)

# Plot the results
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, summed_signal)
plt.title('Sum of Two Exponential Signals')
plt.grid(True)
plt.subplot(2, 1, 2)
plt.plot(t, shifted_signal)
plt.title('Time-Shifted Signal')
plt.grid(True)
plt.tight_layout()
plt.show()