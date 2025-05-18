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

1. Download the dataset from the provided Google Drive link
2. Place the dataset files in the appropriate directory
3. Run the main script:
```bash
python main.py
```

## Project Structure

```
Network_Anomaly_Detection/
├── data/                  # Directory for dataset files
├── src/                   # Source code
├── requirements.txt       # Project dependencies
├── README.md             # Project documentation
└── main.py               # Main execution script
```

## Requirements

The project requires Python 3.7+ and the following main dependencies:
- numpy
- pandas
- scikit-learn
- matplotlib
- seaborn

For a complete list of dependencies, please refer to the `requirements.txt` file.

## Citation

If you use this code in your research, please cite our paper:

```
@article{network_anomaly_detection,
  title={Network Anomaly Detection},
  author={Your Name},
  journal={Journal Name},
  year={2024}
}
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any questions or suggestions, please feel free to open an issue in this repository. 
