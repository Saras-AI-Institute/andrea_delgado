import pandas as pd
import numpy as np
from numpy.random import default_rng

# Set random seed for reproducibility
rng = default_rng(42)

# Generate 365 dates starting from 2025-01-01
start_date = pd.to_datetime('2025-01-01')
dates = pd.date_range(start_date, periods=365)

# Generate Steps
steps_mean, steps_std_dev = 8500, 2500
steps = rng.normal(steps_mean, steps_std_dev, 365)
steps = np.clip(steps, 3000, 18000)

# Generate Sleep Hours
sleep_mean, sleep_std_dev = 7.2, 1.0
sleep_hours = rng.normal(sleep_mean, sleep_std_dev, 365)
sleep_hours = np.clip(sleep_hours, 4.5, 9.5)

# Generate Heart Rate
hr_mean, hr_std_dev = 68, 12
heart_rate = rng.normal(hr_mean, hr_std_dev, 365)
heart_rate = np.clip(heart_rate, 48, 110)

# Generate Calories Burned
calories_min, calories_max = 1800, 4200
calories_burned = rng.integers(calories_min, calories_max, 365)

# Generate Active Minutes
active_minutes_min, active_minutes_max = 20, 180
active_minutes = rng.integers(active_minutes_min, active_minutes_max, 365)

# Create DataFrame
fitness_data = pd.DataFrame({
    'Date': dates,
    'Steps': steps,
    'Sleep_Hours': sleep_hours,
    'Heart_Rate_bpm': heart_rate,
    'Calories_Burned': calories_burned,
    'Active_Minutes': active_minutes
})

# Introduce 5% missing values randomly in each column
for column in fitness_data.columns[1:]:  # Skip the 'Date' column
    fitness_data.loc[rng.choice(fitness_data.index, size=int(365 * 0.05), replace=False), column] = np.nan

# Save the DataFrame to a CSV file
fitness_data.to_csv('data/health_data.csv', index=False)
