import pandas as pd

def bonus(row):
    if row['employee_id'] % 2 == 0:
        return 0
    elif row['name'].startswith('M'):
        return 0
    else:
        return row['salary']

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(bonus, axis=1)
    return employees.loc[:, ['employee_id', 'bonus']].sort_values('employee_id')