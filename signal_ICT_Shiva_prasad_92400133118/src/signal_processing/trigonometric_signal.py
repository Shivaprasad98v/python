import numpy as np
import matplotlib.pyplot as plt

def sine_wave(A, f, phi, t):
    signal = A * np.sin(2 * np.pi * f * t + phi)
    plt.plot(t, signal)
    plt.title('Sine Wave')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()
    return signal

def cosine_wave(A, f, phi, t):
    signal = A * np.cos(2 * np.pi * f * t + phi)
    plt.plot(t, signal)
    plt.title('Cosine Wave')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()
    return signal

def exponential_signal(A, a, t):
    signal = A * np.exp(a * t)
    plt.plot(t, signal)
    plt.title('Exponential Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()
    return signal

A = 1          
f = 1          
phi = 0        
t = np.linspace(0, 1, 100)  

sine_wave(A, f, phi, t)
cosine_wave(A, f, phi, t)
exponential_signal(A, 1, t)
