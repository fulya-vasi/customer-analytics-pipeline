# AI-based Anomaly Detection for Sensor Data

## Project Overview
This project simulates sensor data from an infrastructure monitoring system and applies anomaly detection using Python and machine learning.

The goal is to demonstrate a simple end-to-end data workflow:
- data generation
- data processing
- anomaly detection
- export of processed results

## Technologies
- Python
- pandas
- numpy
- scikit-learn

## Workflow
1. Simulate normal sensor readings (temperature and pressure)
2. Inject artificial anomalies
3. Detect anomalies using Isolation Forest
4. Save the processed data as a CSV file

## Output
The output file is stored in:

`data/output.csv`

The column `anomaly` contains:
- `1` = normal value
- `-1` = anomaly

## Run the project
```bash
pip install -r requirements.txt
python main.py


