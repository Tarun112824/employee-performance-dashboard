# Inserts data into SQL
import pandas as pd
from sqlalchemy import create_engine

def load_data_to_db(csv_path, db_url):
    # Read CSV
    df = pd.read_csv(csv_path)
    
    # Clean data (example: fill missing departments)
    df['department'].fillna('Unassigned', inplace=True)
    
    # Connect to DB and insert
    engine = create_engine(db_url)
    df.to_sql('Employees', engine, if_exists='append', index=False)
    print(f"Loaded {len(df)} records to database.")

# Example usage
if __name__ == "__main__":
    load_data_to_db(
        csv_path="database/sample_data/employees.csv",
        db_url="postgresql://user:password@localhost:5432/employee_db"
    )