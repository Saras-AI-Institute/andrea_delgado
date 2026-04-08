from modules.processor import load_data, calculate_recovery_score
df = load_data()
df = calculate_recovery_score(df)
print(df[['Date', 'Sleep_Hours', 'Heart_Rate_bpm', 'Steps', 'Recovery_Score']].head(10))