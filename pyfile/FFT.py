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

    # Divide
    X_even: List[complex] = fft(x[0::2])
    X_odd: List[complex] = fft(x[1::2])

    # Twiddle factors (roots of unity)
    factor: List[complex] = [
        cmath.exp(-2j * cmath.pi * k / n) * X_odd[k]
        for k in range(n // 2)
    ]

    # Combine
    return [X_even[k] + factor[k] for k in range(n // 2)] + \
           [X_even[k] - factor[k] for k in range(n // 2)]


def ifft(X: List[complex]) -> List[complex]:
    """
    Inverse FFT (Cooley-Tukey).
    
    Args:
        X (List[complex]): Frequency domain data (length must be power of 2).
    
    Returns:
        List[complex]: Time domain sequence reconstructed from the spectrum.
    """
    n: int = len(X)
    if n == 1:
        return X

    # Divide
    X_even: List[complex] = ifft(X[0::2])
    X_odd: List[complex] = ifft(X[1::2])

    # Twiddle factors (note the sign flip vs FFT)
    factor: List[complex] = [
        cmath.exp(2j * cmath.pi * k / n) * X_odd[k]
        for k in range(n // 2)
    ]

    # Combine (and scale by 1/n at the top level)
    return [X_even[k] + factor[k] for k in range(n // 2)] + \
           [X_even[k] - factor[k] for k in range(n // 2)]


if __name__ == "__main__":
    # Example: 8-point signal
    signal: List[complex] = [complex(s, 0) for s in [0, 1, 2, 3, 4, 3, 2, 1]]

    # FFT
    spectrum: List[complex] = fft(signal)
    print("FFT result:")
    print(spectrum)

    # IFFT (scale by 1/n)
    n: int = len(spectrum)
    recovered: List[complex] = [val / n for val in ifft(spectrum)]
    print("\nRecovered signal (after IFFT):")
    print(recovered)
