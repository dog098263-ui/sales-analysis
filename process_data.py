import pandas as pd
import numpy as np
import os

def process_and_split_data():
    file_path = "/Users/meow/.gemini/antigravity/scratch/powerbi_portfolio/Online Retail.xlsx"
    output_dir = "/Users/meow/.gemini/antigravity/scratch/powerbi_portfolio/clean_data"
    os.makedirs(output_dir, exist_ok=True)
    
    print("Loading raw Excel data...")
    df = pd.read_excel(file_path)
    print(f"Data loaded. Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    
    # 1. Inspect anomalies and prepare columns
    # Normalize strings
    df['StockCode'] = df['StockCode'].astype(str).str.strip().str.upper()
    df['Description'] = df['Description'].astype(str).str.strip()
    df['InvoiceNo'] = df['InvoiceNo'].astype(str).str.strip()
    
    # Identify returns/cancellations
    df['IsCancelled'] = df['InvoiceNo'].str.startswith('C') | (df['Quantity'] < 0)
    
    # 2. Build DimGeography
    print("Creating DimGeography...")
    countries = df['Country'].unique()
    geo_data = []
    
    # Map countries to regions/continents to enrich the portfolio data
    europe = ['United Kingdom', 'France', 'Germany', 'EIRE', 'Spain', 'Netherlands', 'Belgium', 'Switzerland', 
              'Portugal', 'Norway', 'Italy', 'Channel Islands', 'Finland', 'Cyprus', 'Sweden', 'Austria', 
              'Denmark', 'Poland', 'GREECE', 'Italy', 'Lithuania', 'European Community', 'Iceland', 'Malta', 'Czech Republic']
    asia = ['Japan', 'Singapore', 'Hong Kong', 'Israel', 'Bahrain', 'United Arab Emirates', 'Saudi Arabia', 'Lebanon']
    americas = ['USA', 'Canada', 'Brazil']
    oceania = ['Australia']
    
    for country in countries:
        if country in europe:
            region = "Europe"
        elif country in asia:
            region = "Asia"
        elif country in americas:
            region = "Americas"
        elif country in oceania:
            region = "Oceania"
        else:
            region = "Other"
        geo_data.append({"Country": country, "Region": region})
        
    df_geo = pd.DataFrame(geo_data)
    df_geo.to_csv(os.path.join(output_dir, "dim_geography.csv"), index=False)
    print(f"DimGeography saved: {df_geo.shape[0]} rows")

    # 3. Build DimProduct
    print("Creating DimProduct...")
    # Products can have multiple descriptions or empty descriptions. We group by StockCode and choose the most common non-empty description.
    product_desc = df.dropna(subset=['Description']).groupby('StockCode')['Description'].agg(lambda x: x.value_counts().index[0] if not x.empty else "Unknown Product").reset_index()
    
    # For StockCodes with no description at all in the whole dataset, map to "Unknown Description"
    all_stock_codes = pd.DataFrame({"StockCode": df['StockCode'].unique()})
    df_product = pd.merge(all_stock_codes, product_desc, on='StockCode', how='left').fillna("Unknown Product")
    
    # Filter out empty or space stock codes
    df_product = df_product[df_product['StockCode'] != '']
    df_product.to_csv(os.path.join(output_dir, "dim_products.csv"), index=False)
    print(f"DimProduct saved: {df_product.shape[0]} rows")

    # 4. Build DimCustomer
    print("Creating DimCustomer...")
    # Customers: unique CustomerID. Group by CustomerID and get their Country.
    # Note: Many customer IDs are NaN. We will handle them as a single guest customer -1.
    df_customers = df.dropna(subset=['CustomerID']).copy()
    df_customers['CustomerID'] = df_customers['CustomerID'].astype(int)
    
    customer_mapping = df_customers.groupby('CustomerID')['Country'].last().reset_index()
    
    # Add Guest Checkout customer
    guest_row = pd.DataFrame([{"CustomerID": -1, "Country": "United Kingdom"}])
    df_customer_final = pd.concat([customer_mapping, guest_row], ignore_index=True)
    df_customer_final.to_csv(os.path.join(output_dir, "dim_customers.csv"), index=False)
    print(f"DimCustomer saved: {df_customer_final.shape[0]} rows")

    # 5. Build FactSales
    print("Creating FactSales...")
    # Fill NaN CustomerIDs with -1 (Guest checkout)
    df_fact = df.copy()
    df_fact['CustomerID'] = df_fact['CustomerID'].fillna(-1).astype(int)
    
    # Calculate LineTotal / SalesAmount
    df_fact['SalesAmount'] = df_fact['Quantity'] * df_fact['UnitPrice']
    
    # Keep only relevant columns for Fact table
    # Columns: InvoiceNo, StockCode, CustomerID, InvoiceDate, Quantity, UnitPrice, SalesAmount, IsCancelled, Country (to link with Geography)
    df_fact_final = df_fact[['InvoiceNo', 'StockCode', 'CustomerID', 'InvoiceDate', 'Quantity', 'UnitPrice', 'SalesAmount', 'IsCancelled', 'Country']]
    
    df_fact_final.to_csv(os.path.join(output_dir, "fact_sales.csv"), index=False)
    print(f"FactSales saved: {df_fact_final.shape[0]} rows")
    
    print("\nData splitting and cleaning completed successfully!")
    print(f"Clean files exported to: {output_dir}")

if __name__ == "__main__":
    process_and_split_data()
