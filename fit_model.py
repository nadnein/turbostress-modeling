import numpy as np
import argparse

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

    print("\nFitted polynomial coefficients (highest degree first):")
    print([round(float(c), 5) for c in coeffs])

    return model

def main():
    parser = argparse.ArgumentParser(description="Fit a polynomial model to TurboStress power data.")
    parser.add_argument("csv_file", help="Path to the TurboStress CSV file")
    parser.add_argument(
        "-d", "--degree", type=int, default=1,
        help="Degree of the polynomial to fit (default: 1 for linear)"
    )

    args = parser.parse_args()

    x, y = read_turbostress_ts(args.csv_file)
    fit_polynomial_model(x, y, args.degree)

if __name__ == '__main__':
    main()
