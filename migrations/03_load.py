import os
from sqlalchemy import create_engine
from migrations.02_transform import transform_cities, transform_states, transform_zones

# Database credentials (injected via Environment Variables / GitHub Secrets)
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "qa_gms_db")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def load_data():
    engine = create_engine(DATABASE_URL)
    
    zones = transform_zones()
    states = transform_states()
    cities = transform_cities()

    # Load into target PostgreSQL tables
    zones.to_sql('Zone', engine, if_exists='append', index=False)
    states.to_sql('State', engine, if_exists='append', index=False)
    cities.to_sql('City', engine, if_exists='append', index=False)
    
    print(" Successfully ingested Zone, State, and City data into target database.")

if __name__ == "__main__":
    load_data()
