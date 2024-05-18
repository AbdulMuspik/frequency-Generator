import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

def generate_frequency(frequency, duration, sampling_rate):
    t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
    signal = np.sin(2 * np.pi * frequency * t)
    return t, signal

def play_sound(signal, sampling_rate):
    sd.play(signal, samplerate=sampling_rate)
    sd.wait()

def plot_waveform(t, signal, frequency):
    plt.figure(figsize=(10, 4))
    plt.plot(t, signal)
    plt.title(f"Sine Wave of {frequency} Hz")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

def main():
    frequency = float(input("Enter frequency in Hz: "))
    duration = float(input("Enter duration in seconds: "))
    sampling_rate = 44100  # CD quality sampling rate
    t, signal = generate_frequency(frequency, duration, sampling_rate)
    plot_waveform(t, signal, frequency)
    play_sound(signal, sampling_rate)

if __name__ == "__main__":
    main()
