import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    top_managers = employee.groupby('managerId').count()
    top_managers = top_managers.loc[top_managers.values >= 5]

    return pd.DataFrame(employee.loc[employee['id'].isin(top_managers.index), 'name'])