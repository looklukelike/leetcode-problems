import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    employees = employees.merge(employee_uni, how='left', on='id')[['unique_id', 'name']]
    return employees