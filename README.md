# Neural Network-based Approaches for Solving Minimization Problems in Computational Mechanics

This repository contains code and experiments related to the **bachelor thesis**:

**Neural Network-based Approaches for Solving Minimization Problems in Computational Mechanics**  
**Author:** Rafael Galiev  
**Supervisor:** doc. Dr. rer. nat. Ing. Jan Valdman  
**Department of Applied Mathematics, FIT CTU in Prague**  
**Year:** 2025  
📎 Link to the official thesis will be added upon publication.

> ⚠️ This repository is provided under a license. If you use or refer to this work, please cite the official source once published.

---

## Project Setup

### **Environment**
This project requires [Python 3.9+](https://www.python.org/downloads/). It is recommended to use a virtual environment to manage dependencies.

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

You can also generate your own datasets or experiment with different loading conditions directly in the notebooks:

- `multi-yield/multi-yield_deformation.ipynb`
- `single-yield/single-yield_deformation.ipynb`

These notebooks allow you to modify boundary conditions and rerun the simulations to produce custom data.

---

## 🗂️ Project Structure

```
bi-bap-galieraf-main/
├── README.md                  ← this file
├── requirements.txt           ← Project dependencies
├── download_data.py           ← script to download datasets
├── images/                    ← visualizations used in the thesis
│   ├── multi-yield/
│   └── single-yield/
├── multi-yield/               ← main experiments for multi-yield case
│   ├── multi-yield_NN.ipynb   ← training notebook for the neural network
│   ├── multi-yield_deformation.ipynb← notebook for visualizing and evaluating results
│   ├── multi-yield_best_model.pkl ← trained model weights
│   ├── multi-yield_scaler_A.pkl ← fitted scaler for input A
│   ├── multi-yield_scaler_P_init.pkl← fitted scaler for initial P
│   └── multi-yield_scaler_P_target.pkl ← fitted scaler for target P
├── single-yield/              ← main experiments for single-yield case
│   ├── single-yield_NN.ipynb  ← training notebook for the neural network
│   ├── single-yield_deformation.ipynb← notebook for visualizing and evaluating results
│   ├── best_model_overall_bigger_data.pkl ← trained model weights
│   ├── scaler_A.pkl ← fitted scaler for input A
│   └── scaler_P.pkl ← fitted scaler for output P
└── data/                      ← dataset folder (populated by script)
```

---
## ▶️ Running the Notebooks

To open and run the Jupyter notebooks (`*.ipynb`) included in this project, run the following command from the root directory of the repository:

```bash
jupyter notebook
```
This will launch the Jupyter Notebook interface in your default web browser.
From there, you can navigate to any notebook (e.g., `multi-yield/multi-yield_NN.ipynb`) and execute it cell by cell.


## 📜 License

This code is part of a bachelor thesis submitted to FIT CTU in Prague.  
It is released under a free-use license, allowing anyone to use, modify, and distribute the work for any purpose, including commercial use, without restriction, as declared in the author's official thesis submission.

This permission is granted in accordance with Czech Copyright Act No. 121/2000 Coll., and Section 2373(2) of Act No. 89/2012 Coll.  
The legal terms are stated in the official **Declaration** section of the submitted thesis.

📎 The thesis will be available publicly after final submission.

---

## ✉️ Contact

If you have questions or suggestions related to this repository,  
please open an issue on GitHub.
