# app/services/anomaly_file_checker.py

import pandas as pd
import numpy as np

def detect_anomalies(file_path: str, threshold: float = 2.0):
    try:
        df = pd.read_csv(file_path)

        results = {}
        for col in df.columns[1:]:  # skip first column (like 'Month' or 'Year')
            values = df[col].dropna()
            mean = np.mean(values)
            std = np.std(values)

            anomalies = []
            for idx, val in enumerate(values):
                z_score = (val - mean) / std if std > 0 else 0
                if abs(z_score) > threshold:
                    anomalies.append((df.iloc[idx, 0], val))  # get month/year and value

            results[col] = anomalies if anomalies else "No anomalies"

        return results

    except Exception as e:
        return {"error": str(e)}
