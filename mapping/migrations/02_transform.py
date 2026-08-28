import pandas as pd

SOURCE_FILE = 'Source_Seven_Tables_Data.xlsx'

def transform_zones():
    df = pd.read_excel(SOURCE_FILE, sheet_name='gms_zone')
    tgt = pd.DataFrame()
    tgt['id'] = df['zone_id']
    tgt['country_id'] = df['country_id'].fillna(1).astype(int)
    tgt['zone_code'] = df['zone_code'].astype(str).str.strip()
    tgt['zone_name'] = df['zone_name'].astype(str).str.strip()
    tgt['created_at'] = pd.Timestamp.now()
    tgt['updated_at'] = pd.Timestamp.now()
    tgt['deleted_at'] = None
    return tgt

def transform_states():
    df = pd.read_excel(SOURCE_FILE, sheet_name='gms_state')
    tgt = pd.DataFrame()
    tgt['id'] = df['state_id']
    tgt['zone_id'] = df['zone_id'].fillna(0).astype(int)
    tgt['state_code'] = df['state_code'].astype(str).str.strip()
    tgt['state_name'] = df['state_name'].astype(str).str.strip()
    tgt['created_at'] = pd.Timestamp.now()
    tgt['updated_at'] = pd.Timestamp.now()
    tgt['deleted_at'] = None
    return tgt

def transform_cities():
    df = pd.read_excel(SOURCE_FILE, sheet_name='gms_city')
    tgt = pd.DataFrame()
    tgt['id'] = df['city_id']
    tgt['state_id'] = df['state_id'].astype(int)
    tgt['city_code'] = df['city_code'].astype(str).str.strip()
    tgt['city_name'] = df['city_name'].astype(str).str.strip()
    tgt['is_metro'] = df['metro'].apply(lambda x: True if str(x).strip().upper() == 'Y' else False)
    tgt['created_at'] = pd.to_datetime(df['entry_date'], errors='coerce').fillna(pd.Timestamp.now())
    tgt['updated_at'] = pd.Timestamp.now()
    tgt['deleted_at'] = None
    return tgt

if __name__ == "__main__":
    cities_df = transform_cities()
    states_df = transform_states()
    zones_df = transform_zones()
    print(f"Transformed {len(zones_df)} Zones, {len(states_df)} States, {len(cities_df)} Cities successfully.")
