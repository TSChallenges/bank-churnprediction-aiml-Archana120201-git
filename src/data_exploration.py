
import pandas as pd

def load_data(filepath):
    """
    Load the dataset into a pandas DataFrame.
    """
    df = pd.read_csv(filepath)
    return df

def check_missing_values(df):
    """
    Check for missing values in the DataFrame.
    """
    missing = df.isnull().sum()
    print("Missing Values:\n", missing)

def generate_summary_statistics(df):
    """
    Generate summary statistics for key variables.
    """
    summary = df.describe()
    print("Summary Statistics:\n", summary)

def main():
    # Load data
    df = load_data('data/bank_churn.csv')
    
    # Check for missing values
    check_missing_values(df)
    
    # Generate summary statistics
    generate_summary_statistics(df)

if __name__ == "__main__":
    main()


