
import pandas as pd

def load_data(filepath):
    """
    Load the dataset into a pandas DataFrame.
    """
    df = pd.read_csv(filepath)
    return df

def check_missing_values(df):
    """
    TODO : Check for missing values in the DataFrame.
    """
    print("Missing Values:\n", missing)

def generate_summary_statistics(df):
    """
    TODO : Generate summary statistics for key variables.
    """
    print("Summary Statistics:\n", summary)

def main():
    # Load data
    df = load_data('data/bank_churn.csv')
    
    # TODO : Check for missing values by calling it's function
    
    # TODO : Generate summary statistics by calling it's function

if __name__ == "__main__":
    main()


