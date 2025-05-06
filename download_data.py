import gdown
import os

# Dictionary mapping destination paths to Google Drive file IDs
files = {
    "data/single_yield_data.csv": "1_e_HIhL6_VV4697zhCPgb_74YUbqV30l",
    "data/multi_yield_data.csv": "1V5jn_kHqSuv2Uo-Ky96eGpp1URbXB6JI",
}

for output_path, file_id in files.items():
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    url = f"https://drive.google.com/uc?id={file_id}"
    print(f"Downloading {output_path}...")
    gdown.download(url, output_path, quiet=False)
