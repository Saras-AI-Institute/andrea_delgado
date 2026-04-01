import pandas as pd

def main():
    # Load the CSV file into a DataFrame
    df = pd.read_csv('data/health_data.csv')
    
    # Print the first 5 rows of the DataFrame
    print("First 5 rows:")
    print(df.head())
    
    # Calculate and print the number of missing values in each column
    print("\nNumber of missing values in each column:")
    print(df.isnull().sum())

if __name__ == "__main__":
    main()