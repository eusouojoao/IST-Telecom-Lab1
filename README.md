# IST-Telecom-Lab1 2022/2023 | [LAB 1 - FM stereo](LAB_1_2022.pdf)

## Overview 
This project focuses on designing an FM stereo demodulator to recover a stereo audio signal. The FM stereo signal consists of two audio channels: left (L) and right (R), transmitted using frequency multiplexing as L+R (sum) and L-R (difference) signals.

## FM Stereo Demodulator Structure
The FM stereo demodulator comprises the following stages:

- FM Demodulation: Demodulate the FM signal using GNU Radio blocks like Quadrature Demod or Frequency Demod.

- Filtering: Apply low-pass filters to remove high-frequency components introduced during demodulation.

- Channel Separation: Separate left and right channels based on the L-R and L+R signals using a process described in [1], Chapter 4, Section 4.9.

- Indication of Stereo Format: Determine stereo format by analyzing the separated audio channels, detecting the presence of the L-R signal.

## Relevant Aspects for Stereo FM Demodulation
Design considerations include:

- Spectral Characteristics: Compare pre-modulation spectral characteristics of stereo and monophonic audio signals for appropriate filtering and channel separation.

- Obtaining Audio Channels: Study the laboratory guide for obtaining left and right audio channels in the stereo demodulator.

- Demodulated Signal Bandwidth: Pay attention to the demodulated signal's bandwidth for audio quality and stereo channel separation.

## References
[1] Simon Haykin and Michael Moher - Introduction to Analog and Digital Communications, 2nd Ed. (2007) - Wiley
