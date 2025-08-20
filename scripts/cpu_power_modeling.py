import numpy as np

def read_turbostress_ts(filename):
    with open(filename, 'r') as f:
        data = f.readlines()

    # CPU power readings from lines 2–12 (index 1–11), column 4 (index 3)
    y_vals = [float(data[i].strip().split(',')[3]) for i in range(1, 12)]

    # Corresponding load levels: 0%, 10%, ..., 100%
    x_vals = list(range(0, 110, 10))

    return x_vals, y_vals

def fit_polynomial_model(x, y, degree):
    coeffs = np.polyfit(x, y, degree)
    model = np.poly1d(coeffs)

    print(f"\nFitted polynomial coefficients (degree {degree}, highest degree first):")
    print([round(float(c), 5) for c in coeffs])

    return model

