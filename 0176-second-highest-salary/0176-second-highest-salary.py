import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    x = None
    salaries = employee['salary'].sort_values(ascending=False).drop_duplicates()
    if salaries.shape[0] >= 2:
        x = salaries.iloc[1]
    df = pd.DataFrame({f'SecondHighestSalary': [x]})
    return df
