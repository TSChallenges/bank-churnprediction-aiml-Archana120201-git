import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

def visualize_distributions(df):
    """
    Visualize distributions of age, balance, credit_score, and estimated_salary,
    and save each plot as a separate PNG file.
    """
    # Age distribution
    plt.figure(figsize=(6, 4))
    sns.histplot(df['age'], kde=True)
    plt.title('Age Distribution')
    plt.savefig('age_distribution.png')
    plt.close()  # Close the figure to ensure no overlap with the next plot

    # Balance distribution
    plt.figure(figsize=(6, 4))
    sns.histplot(df['balance'], kde=True)
    plt.title('Balance Distribution')
    plt.savefig('balance_distribution.png')
    plt.close()  # Close the figure to ensure no overlap with the next plot

    # Credit score distribution
    plt.figure(figsize=(6, 4))
    sns.histplot(df['credit_score'], kde=True)
    plt.title('Credit Score Distribution')
    plt.savefig('credit_score_distribution.png')
    plt.close()  # Close the figure to ensure no overlap with the next plot

    # Estimated salary distribution
    plt.figure(figsize=(6, 4))
    sns.histplot(df['estimated_salary'], kde=True)
    plt.title('Estimated Salary Distribution')
    plt.savefig('estimated_salary_distribution.png')
    plt.close()  # Close the figure to ensure no overlap with the next plot

def main():
    # Load data
    df = load_data('data/bank_churn.csv')
    
    # Check for missing values
    check_missing_values(df)
    
    # Generate summary statistics
    generate_summary_statistics(df)
    
    # Visualize distributions and save the plots
    visualize_distributions(df)

if __name__ == "__main__":
    main()

