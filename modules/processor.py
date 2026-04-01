import pandas as pd
from datetime import datetime

# Function to load and clean health data

def load_data():
    # Step 1: Read the CSV file into a DataFrame
    df = pd.read_csv('data/health_data.csv')
    
    # Step 2: Handle missing values intelligently
    # Fill missing 'Steps' with median
    df['Steps'].fillna(df['Steps'].median(), inplace=True)
    
    # Fill missing 'Sleep_Hours' with 7.0
    df['Sleep_Hours'].fillna(7.0, inplace=True)
    
    # Fill missing 'Heart_Rate_bpm' with 68
    df['Heart_Rate_bpm'].fillna(68, inplace=True)
    
    # Fill missing values in other columns with their median
    for column in ['Calories_Burned', 'Active_Minutes']:
        df[column].fillna(df[column].median(), inplace=True)
    
    # Step 3: Convert the 'Date' column to datetime objects
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Step 4: Return the cleaned DataFrame
    return df

# Function to calculate the recovery score for each record in the DataFrame

def calculate_recovery_score(df):
    # Step through each row to calculate the recovery score based on given metrics
    def calculate_score(row):
        score = 50  # Base score set at midpoint (50)

        # Adjust score based on Sleep_Hours
        if row['Sleep_Hours'] >= 7:
            score += 30  # Good sleep significantly boosts recovery
        elif row['Sleep_Hours'] < 6:
            score -= 20  # Poor sleep reduces recovery score

        # Adjust score based on Heart_Rate_bpm
        if row['Heart_Rate_bpm'] < 60:
            score += 10  # Lower heart rate improves recovery
        elif row['Heart_Rate_bpm'] > 80:
            score -= 10  # Higher heart rate may indicate stress

        # Adjust score based on Steps
        if row['Steps'] > 10000:
            score -= 5  # Very high activity may reduce recovery due to strain
        elif row['Steps'] < 5000:
            score -= 5  # Low activity may also not be ideal

        # Ensure the score is within 0 to 100
        return max(0, min(score, 100))

    # Apply the calculated score to each row and create a new column
    df['Recovery_Score'] = df.apply(calculate_score, axis=1)

    return df

# Add any additional helper functions or constants above