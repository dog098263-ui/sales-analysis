import sys
import os

def check_and_install_dependencies():
    # Try importing pandas and openpyxl
    try:
        import pandas
        import openpyxl
        print("Pandas and openpyxl are already installed.")
    except ImportError:
        print("Installing pandas and openpyxl...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas", "openpyxl"])

def analyze_excel():
    import pandas as pd
    file_path = "/Users/meow/.gemini/antigravity/scratch/powerbi_portfolio/Online Retail.xlsx"
    
    print(f"Reading file: {file_path}")
    
    # Load Excel file (this might take a few seconds as it is ~23MB)
    xls = pd.ExcelFile(file_path)
    print(f"Sheet names: {xls.sheet_names}")
    
    for sheet_name in xls.sheet_names:
        print(f"\n--- Analysis for Sheet: {sheet_name} ---")
        df = pd.read_excel(xls, sheet_name)
        print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
        
        print("\nColumns and Data Types:")
        print(df.dtypes)
        
        print("\nNull Values per Column:")
        print(df.isnull().sum())
        
        print("\nUnique Values per Column:")
        for col in df.columns:
            print(f"  {col}: {df[col].nunique()} unique values")
            
        print("\nFirst 5 rows:")
        print(df.head())
        
        # Simple statistics for numeric columns
        print("\nDescriptive Statistics:")
        print(df.describe(include='all', datetime_is_numeric=True))

if __name__ == "__main__":
    check_and_install_dependencies()
    analyze_excel()
