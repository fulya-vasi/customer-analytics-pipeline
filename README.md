# Data Anomaly Detection Pipeline (Python)

## Context

This project is inspired by my Bachelor thesis on AI-based anomaly detection in critical infrastructure systems (e.g., water supply and SCADA systems).  
It demonstrates a simplified prototype of how anomalies in sensor data can be detected using machine learning.

## Overview

This project simulates sensor data (e.g. temperature and pressure) and detects anomalies using a machine learning model.

It reflects a simple end-to-end data pipeline from data ingestion to anomaly detection and export.

The implementation focuses on clean and modular Python code as well as reproducible data processing.

This pipeline demonstrates a simplified ETL-like workflow and can be extended to ingest real data from APIs or databases.

## Data Pipeline

<img src="images/pipeline-diagram.png" width="900">

## Technologies

- Python
- pandas
- numpy
- scikit-learn
- matplotlib

## What it does

- Generates synthetic sensor data
- Injects artificial anomalies
- Applies anomaly detection using Isolation Forest
- Visualizes the results
- Exports processed data to CSV

## Output

The results are stored in:

`data/output.csv`

The column `anomaly` contains:
- `1` = normal value  
- `-1` = anomaly  

## Example Output

### Visualization
<img src="images/anomaly-plot.png" alt="Anomaly Plot" width="400">

### Console Output
<img src="images/output-console.png" alt="Console Output" width="400">

## Run the project

```bash
pip install -r requirements.txt
python main.py
