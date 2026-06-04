import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    highest_salaries = employee.groupby('departmentId', as_index=False).max('salary')
    employee = employee.merge(highest_salaries, how='inner', on=['departmentId', 'salary']).merge(department, how='left', left_on='departmentId', right_on='id')
    employee = employee.rename(columns={'name_y': 'Department', 'name_x': 'Employee', 'salary' : 'Salary'})[['Department', 'Employee', 'Salary']]
    return employee