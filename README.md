# TurboStress Power Model Fitter

This script fits a polynomial model to CPU power usage data from TurboStress benchmark CSV files.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/nadnein/turbostress-modeling.git
cd turbostress-modeling
```

### 2. Set Up a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies
Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Run the script

```bash
python fit_model.py <csv_file> [--degree DEGREE]
```

- `<csv_file>`: Path to the CSV file (e.g. `data/ts-readings.csv`)
- `--degree`, `-d`: (Optional) Degree of the polynomial (default: 1)

## 🧪 Example

```bash
python fit_model.py data/ts-readings.csv --degree 2
```

Output:

```
Fitted polynomial coefficients (highest degree first):
[-0.02332, 4.42125, 51.32497]
```
