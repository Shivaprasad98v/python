import numpy as np
import matplotlib.pyplot as plt

from unitary_signal import unit_step, unit_impulse, ramp_signal
from trigonometric_signal import sine_wave, cosine_wave
from operation import time_shift, signal_addition, signal_multiplication

# Task 1: Generate and plot a unit step and unit impulse of length 20
n = np.arange(-10, 10)
u = unit_step(n)
delta = unit_impulse(n)

# Task 2: Generate a sine wave (A=2, f=5Hz, phi=0, t=0..1s)
t = np.linspace(0, 1, 500)
sine = sine_wave(2, 5, 0, t)

# Task 3: Time shifting the sine wave by +5 units
shifted_sine = time_shift(sine, 5)
plt.plot(t, sine, label="Original Sine")
plt.plot(t, shifted_sine, label="Shifted Sine (+5)")
plt.title("Time Shifted Sine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

# Task 4: Addition of unit step and ramp signal
ramp = ramp_signal(n)
added = signal_addition(u, ramp)
plt.stem(n[:len(added)], added, basefmt=" ")
plt.title("Addition of Unit Step and Ramp Signal")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# Task 5: Multiply sine and cosine waves of same frequency
cosine = cosine_wave(2, 5, 0, t)
product = signal_multiplication(sine, cosine)
plt.plot(t[:len(product)], product)
plt.title("Multiplication of Sine and Cosine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
