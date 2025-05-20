# Network Anomaly Detection

This repository contains the implementation of a Network Anomaly Detection system that utilizes genetic algorithms for feature selection combined with machine learning techniques to enhance detection accuracy.

## Abstract

This study explores the efficiency of genetic algorithms for feature selection in network anomaly detection systems, combined with machine learning techniques to enhance detection accuracy. The focus is on identifying optimal feature subsets contributing to high classification accuracy in a network environment dataset. The findings demonstrate significant improvements in detection rates, emphasizing the potential of integrating genetic algorithms with machine learning for network security applications.

## Dataset

The dataset used in this project can be accessed from the following Google Drive link:
[Network Anomaly Detection Dataset](https://drive.google.com/drive/folders/1uTOQfcwVl-RJFKgN79CyAcoUktAsLoF4?usp=sharing)

The dataset contains two files:
- ACI-IoT-fulldata.xlsx (387.6 MB)
- ACI-IoT.xlsx (273.1 MB)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Network_Anomaly_Detection.git
cd Network_Anomaly_Detection
```

2. Create a virtual environment (recommended):
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running Locally

1. Download the dataset from the provided Google Drive link
2. Place the dataset file `ACI-IoT.xlsx` in the project directory
3. Modify the file path in the code:
   - Open `network_anomaly_detection(genetic_algorithm).py`
   - Replace the Google Drive path with your local path:
   ```python
   # Change this line:
   file_path = '/content/drive/MyDrive/Network_Anomaly_Detection/ACI-IoT.xlsx'
   # To:
   file_path = 'ACI-IoT.xlsx'  # or the full path to your file
   ```
4. Remove or comment out the Google Colab specific code:
   ```python
   # Remove or comment these lines:
   # from google.colab import drive
   # drive.mount('/content/drive')
   ```
5. Run the script:
```bash
python network_anomaly_detection\(genetic_algorithm\).py
```

### Running in Google Colab

1. Upload the code file to Google Colab
2. Upload the dataset to your Google Drive
3. Mount your Google Drive in Colab
4. Run the code as is

## Project Structure

```
Network_Anomaly_Detection/
├── data/                  # Directory for dataset files
├── network_anomaly_detection(genetic_algorithm).py  # Main code file
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## Requirements

The project requires Python 3.7+ and the following main dependencies:
- numpy
- pandas
- scikit-learn
- matplotlib
- seaborn
- openpyxl
- deap

For a complete list of dependencies, please refer to the `requirements.txt` file.

## Citation

If you use this code in your research, please cite our paper:

```
https://doi.org/10.5281/zenodo.15412033
```

## Contact

For any questions or suggestions, please feel free to open an issue in this repository. 
