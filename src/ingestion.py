# src/ingestion.py
"""
Landing Layer Ingestion Script
Purpose: Load raw data and save it into Landing Layer
"""

import pandas as pd
import os
from datetime import datetime

def ingest_customer_data():
    """Ingest raw data into Landing Layer"""
    
    print("🚀 Starting Data Ingestion Process...")

    # ================== CONFIGURATION ==================
    raw_file_path = r'C:\Users\hardy\telecom_customer_churn_project\data\raw\telecomdata.csv'
    landing_folder = r'C:\Users\hardy\telecom_customer_churn_project\data\landing_layer'
    
    # Create folder if it doesn't exist
    os.makedirs(landing_folder, exist_ok=True)

    try:
        # Load raw data
        df = pd.read_csv(raw_file_path)
        
        print(f"✅ Raw data loaded successfully!")
        print(f"   Total Records : {len(df):,}")
        print(f"   Columns       : {list(df.columns)}")
        
        # Add metadata
        df['ingestion_timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df['source_file'] = 'telecomdata.csv'
        
        # Save to Landing Layer
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        landing_file_name = f"telecomdata_landing_{timestamp}.csv"
        landing_file_path = os.path.join(landing_folder, landing_file_name)
        
        df.to_csv(landing_file_path, index=False)
        
        print(f"\n✅ SUCCESS: Data saved to Landing Layer!")
        print(f"   File Name : {landing_file_name}")
        print(f"   Location  : {landing_file_path}")
        
        return df
        
    except FileNotFoundError:
        print("❌ Error: Raw file not found! Please check the path.")
        return None
    except Exception as e:
        print(f"❌ Error during ingestion: {e}")
        return None


# Run the script
if __name__ == "__main__":
    ingest_customer_data()