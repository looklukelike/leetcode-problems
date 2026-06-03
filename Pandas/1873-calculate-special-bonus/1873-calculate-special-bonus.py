import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    mask = (employees['employee_id'] % 2 != 0) & (~employees['name'].str.startswith('M'))
    employees['bonus'] = np.where(mask, employees['salary'], 0)
    return employees[['employee_id', 'bonus']].sort_values('employee_id')