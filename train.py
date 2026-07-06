import os
import numpy as np
import pandas as pd

def generate_flood_dataset(filename="dataset/flood_data.csv", num_samples=5000, random_seed=42):
    np.random.seed(random_seed)
    
    # 1. Generate meteorological features with realistic distributions
    # Annual Rainfall: 1000mm to 4500mm
    annual_rainfall = np.random.uniform(1000, 4500, num_samples)
    
    # Seasonal Rainfall (Monsoon/Spring rain): highly correlated with annual rainfall (roughly 30-70% of annual)
    seasonal_rainfall = annual_rainfall * np.random.uniform(0.3, 0.7, num_samples)
    
    # Cloud Cover: 10% to 100%
    cloud_cover = np.random.uniform(10, 100, num_samples)
    
    # Humidity: 30% to 100% (high cloud cover generally correlates with higher humidity)
    humidity = np.clip(cloud_cover * 0.8 + np.random.normal(15, 10, num_samples), 30, 100)
    
    # Temperature: 10°C to 45°C (higher rain/clouds tend to slightly cool down temperature)
    temperature = np.clip(35 - (cloud_cover * 0.15) + np.random.uniform(-5, 10, num_samples), 10, 45)
    
    # Visibility: 1km to 15km (heavy clouds and humidity decrease visibility)
    visibility = np.clip(15 - (humidity * 0.1) - (cloud_cover * 0.05) + np.random.uniform(-1, 2, num_samples), 1, 15)
    
    # Pressure: 980 hPa to 1030 hPa (low pressure triggers storm/precipitation)
    pressure = np.clip(1013 - (cloud_cover * 0.25) + np.random.normal(0, 5, num_samples), 980, 1030)
    
    # Wind Speed: 0 km/h to 80 km/h
    wind_speed = np.random.exponential(15, num_samples)
    wind_speed = np.clip(wind_speed + (1030 - pressure) * 0.4, 0, 80)
    
    # River Level: 0.5m to 8.0m (highly dependent on seasonal rainfall and soil saturation)
    river_level = np.clip(0.5 + (seasonal_rainfall / 300) + np.random.normal(1, 0.5, num_samples), 0.5, 8.0)
    
    # Soil Moisture: 10% to 90% (highly saturated if heavy seasonal rainfall and high humidity)
    soil_moisture = np.clip((seasonal_rainfall / 1500) * 60 + humidity * 0.3 + np.random.normal(5, 5, num_samples), 10, 90)
    
    # 2. Formulate Flood Risk Probability (weighted physical model)
    # Normed inputs (0 to 1 scaling for logic weightings)
    norm_annual = (annual_rainfall - 1000) / 3500
    norm_seasonal = (seasonal_rainfall - 200) / 1300
    norm_clouds = cloud_cover / 100
    norm_humidity = humidity / 100
    norm_low_pressure = (1030 - pressure) / 50
    norm_river = (river_level - 0.5) / 7.5
    norm_soil = soil_moisture / 90
    
    # Weighted score calculation
    flood_score = (
        0.20 * norm_annual +
        0.25 * norm_seasonal +
        0.05 * norm_clouds +
        0.05 * norm_humidity +
        0.10 * norm_low_pressure +
        0.25 * norm_river +
        0.10 * norm_soil
    )
    
    # Add random anomaly noise (to keep ML metrics realistic)
    noise = np.random.normal(0, 0.02, num_samples)
    final_score = flood_score + noise
    
    # Predict flood based on threshold (e.g. > 0.50 triggers a flood event)
    flood_occurrence = (final_score > 0.50).astype(int)
    
    # Create DataFrame
    df = pd.DataFrame({
        "Annual_Rainfall": np.round(annual_rainfall, 1),
        "Seasonal_Rainfall": np.round(seasonal_rainfall, 1),
        "Cloud_Cover": np.round(cloud_cover, 1),
        "Humidity": np.round(humidity, 1),
        "Temperature": np.round(temperature, 1),
        "Visibility": np.round(visibility, 1),
        "Pressure": np.round(pressure, 1),
        "Wind_Speed": np.round(wind_speed, 1),
        "River_Level": np.round(river_level, 2),
        "Soil_Moisture": np.round(soil_moisture, 1),
        "Flood": flood_occurrence
    })
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Save to CSV
    df.to_csv(filename, index=False)
    print(f"Dataset successfully created at {filename} with {num_samples} samples.")
    print(f"Flood occurrence distribution:\n{df['Flood'].value_counts(normalize=True)}")

if __name__ == "__main__":
    generate_flood_dataset()
