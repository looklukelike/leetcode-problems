import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    top_managers = employee.groupby('managerId')['id'].count()
    top_managers = top_managers.loc[top_managers.values >= 5]

    return employee.loc[employee['id'].isin(top_managers.index), ['name']]