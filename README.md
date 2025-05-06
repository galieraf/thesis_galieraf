# Neural Network-based Approaches for Solving Minimization Problems in Computational Mechanics

This repository contains code and experiments related to the **bachelor thesis**:

**Neural Network-based Approaches for Solving Minimization Problems in Computational Mechanics**  
**Author:** Rafael Galiev  
**Supervisor:** doc. Dr. rer. nat. Ing. Jan Valdman  
**Department of Applied Mathematics, FIT CTU in Prague**  
**Year:** 2025  
📎 [Link to the thesis – TODO]

> ⚠️ This repository is provided under a license. If you use or refer to this work, please cite the official source once published.

---

## Project Setup

### **Environment**
This project requires **Python 3.9 or later**. It is recommended to use a virtual environment to manage dependencies.

#### **Create and activate a virtual environment**
On **Windows** (PowerShell):
```powershell
python -m venv venv
venv\Scripts\activate
```
On **Linux/macOS** (bash):
```bash
python -m venv venv
source venv/bin/activate
```

### **Dependencies**
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### **PyTorch Installation**

PyTorch needs to be installed separately based on your hardware.

- For **CPU only**:
```bash
pip install torch torchvision torchaudio
```
- For **NVIDIA GPU (CUDA 11.8)**:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
- For other versions, check the official guide:  
  [PyTorch Installation](https://pytorch.org/)

---

## 📂 Datasets

To download the datasets used in this work, run:

```bash
python download_data.py
```

This will download the following files into the corresponding folders:

- `data/single_yield_data.csv`
- `data/multi_yield_data.csv`

Alternatively, you can download them manually:
- [single_yield_data.csv](https://drive.google.com/file/d/1_e_HIhL6_VV4697zhCPgb_74YUbqV30l/view?usp=sharing)
- [multi_yield_data.csv](https://drive.google.com/file/d/1V5jn_kHqSuv2Uo-Ky96eGpp1URbXB6JI/view?usp=sharing)

---

## 🗂️ Project Structure

```
bi-bap-galieraf-main/
├── README.md                  ← this file
├── requirements.txt           ← Python dependencies
├── download_data.py           ← script to download datasets
├── archive/                   ← experimental notebooks (e.g. 3D tests)
├── images/                    ← visualizations used in the thesis
│   ├── multi-yield/
│   └── single-yield/
├── multi-yield/               ← main experiments for multi-yield case
├── single-yield/              ← main experiments for single-yield case
├── data/                      ← dataset folder (populated by script)
└── ...
```

---

## 📜 License

This code is part of an academic project.  
You may use, reference, and modify it **only for research and educational purposes**.  
Commercial use is **not permitted** without explicit consent from the FIT ČVUT.

For citation or usage, please refer to the final version of the thesis once published.  
📎 [Link to the thesis – TODO]

The legal licensing terms are defined in the official **Declaration** section of the
submitted thesis, in accordance with Czech Copyright Act No. 121/2000 Coll.

---

## ✉️ Contact

If you have questions or suggestions related to this repository,  
please open an issue on GitHub.
