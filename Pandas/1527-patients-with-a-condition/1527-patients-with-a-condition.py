import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    m = patients['conditions'].str.startswith('DIAB1') | patients['conditions'].str.contains(' DIAB1')
    return patients.loc[m]