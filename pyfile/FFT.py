import cmath
from typing import List

def fft(x: List[complex]) -> List[complex]:
    """
    Recursive Cooley-Tukey FFT Algorithm.
    
    Args:
        x (List[complex]): Input sequence of complex numbers.
                          Length must be a power of 2.
    
    Returns:
        List[complex]: Frequency domain representation (complex spectrum).
    """
    n: int = len(x)
    if n == 1:
        return x

    # Divide: even and odd elements
    X_even: List[complex] = fft(x[0::2])
    X_odd: List[complex] = fft(x[1::2])

    # Twiddle factors (complex roots of unity)
    factor: List[complex] = [
        cmath.exp(-2j * cmath.pi * k / n) * X_odd[k]
        for k in range(n // 2)
    ]

    # Combine results
    return [X_even[k] + factor[k] for k in range(n // 2)] + \
           [X_even[k] - factor[k] for k in range(n // 2)]


if __name__ == "__main__":
    # Example input: real values as complex numbers
    signal: List[complex] = [complex(s, 0) for s in [0, 1, 2, 3, 4, 3, 2, 1]]

    spectrum: List[complex] = fft(signal)

    print("Input signal:", signal)
    print("FFT result (frequency components):")
    for freq in spectrum:
        print(freq)
