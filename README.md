# nf-co2footprint Benchmarking 🌱

This repository provides tools and workflows for **evaluation and benchmarking** of the [nf-co2footprint Nextflow plugin](https://nextflow-io.github.io/nf-co2footprint/).  
The plugin estimates the CO₂ footprint of Nextflow pipeline runs.  
Here we compare its estimates against **real wattmeter measurements** to assess accuracy and provide insights for sustainable computing.

---

## 📂 Repository Structure

```
nfco2footprint-benchmarking/
├── data/                # Input data (plugin outputs, wattmeter logs, idle measurements)
├── notebooks/           # Jupyter notebooks for analysis & plotting
├── scripts/             # Reusable Python scripts (modeling, parsing, plotting)
├── results/             # Generated plots, tables, statistics
└── README.md            # This file
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/nfco2footprint-benchmarking.git
cd nfco2footprint-benchmarking
```

### 2. Set Up a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🧪 Workflow

### 1. Idle Power Measurement
- Plug the server into a wattmeter (e.g. Voltcraft SEM6000)  
- Record average **idle power (W)** over 30–60 minutes  

### 2. Pipeline Runs
- Execute pipelines with `nf-co2footprint` enabled  
- Record both plugin output (`e_nfco2footprint`) and wattmeter data (`e_wattmeter`)  

### 3. Baseline Correction
- Correct wattmeter readings by subtracting idle energy:

$$
E_\text{pipeline} = E_\text{measured} - (P_\text{idle} \times t)
$$

### 4. Benchmarking & Visualization
- Store results in a single CSV with columns:

```
pipeline, revision, dataset, cpu_model, trial,
e_nfco2footprint (Wh), e_wattmeter_raw (Wh),
idle_power (W), runtime (h), e_wattmeter_corrected (Wh)
```

- Use provided notebooks and plotting scripts to create **boxplots** and compare plugin vs. wattmeter results  

---

## 📄 License

MIT License (or whichever license you choose).
