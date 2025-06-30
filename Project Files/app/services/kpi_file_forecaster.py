import pandas as pd
import numpy as np

def forecast_kpi_from_file(file_path: str, months: int = 6):
    try:
        df = pd.read_csv(file_path)

        forecasts = {}

        for col in df.columns[1:]:  # Skip first column (e.g., date or month)
            data = df[col].dropna().values
            if len(data) < 2:
                forecasts[col] = "Not enough data to forecast"
                continue

            # Simple linear forecast using numpy
            x = np.arange(len(data))
            coeffs = np.polyfit(x, data, 1)  # Linear regression: degree 1
            trend = np.poly1d(coeffs)

            future_x = np.arange(len(data), len(data) + months)
            future_values = trend(future_x).tolist()

            forecasts[col] = [round(val, 2) for val in future_values]

        return forecasts

    except Exception as e:
        return {"error": str(e)}
