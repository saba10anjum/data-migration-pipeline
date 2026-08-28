import pandas as pd
from migrations.02_transform import transform_cities, transform_states, transform_zones

def run_validations():
    cities = transform_cities()
    states = transform_states()
    zones = transform_zones()

    # 1. Primary Key Uniqueness
    assert not cities['id'].duplicated().any(), "Error: Duplicate IDs found in City primary keys"
    assert not states['id'].duplicated().any(), "Error: Duplicate IDs found in State primary keys"
    assert not zones['id'].duplicated().any(), "Error: Duplicate IDs found in Zone primary keys"

    # 2. Non-Null Checks
    assert cities['city_name'].notnull().all(), "Error: Null values found in City city_name"
    assert states['state_name'].notnull().all(), "Error: Null values found in State state_name"

    print("All data integrity checks passed without errors!")

if __name__ == "__main__":
    run_validations()
