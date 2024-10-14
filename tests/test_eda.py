# tests/test_eda.py

import pytest
import os
import pandas as pd
import matplotlib.pyplot as plt
from src.eda import load_data, check_missing_values, generate_summary_statistics, visualize_distributions

def test_load_data():
    df = load_data('data/bank_churn.csv')
    assert isinstance(df, pd.DataFrame), "Data should be loaded into a pandas DataFrame"
    assert not df.empty, "DataFrame should not be empty"

def test_missing_values():
    df = load_data('data/bank_churn.csv')
    # You can call the actual function to test
    check_missing_values(df)
    missing = df.isnull().sum()
    assert missing.sum() == 0, "There should be no missing values in the dataset"

def test_summary_statistics():
    df = load_data('data/bank_churn.csv')
    summary = df.describe()
    # Check if key columns exist in the original DataFrame
    assert 'age' in df.columns, "DataFrame should include 'Age' column"
    assert 'balance' in df.columns, "DataFrame should include 'Balance' column"

def test_visualizations():
    df = load_data('data/bank_churn.csv')
    # Test if the visualize_distributions function runs without errors
    try:
        visualize_distributions(df)
    except Exception as e:
        pytest.fail(f"Visualization failed with exception: {e}")
    
    # Check if the image files are created as expected
    assert os.path.exists('age_distribution.png'), "Age distribution plot not saved."
    assert os.path.exists('balance_distribution.png'), "Balance distribution plot not saved."
    assert os.path.exists('credit_score_distribution.png'), "Credit score distribution plot not saved."
    assert os.path.exists('estimated_salary_distribution.png'), "Estimated salary distribution plot not saved."
