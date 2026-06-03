import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    x = None
    salaries = employee['salary'].sort_values(ascending=False).drop_duplicates()
    if N > 0 and salaries.shape[0] >= N:
        x = salaries.iloc[N - 1]
    df = pd.DataFrame({f'getNthHighestSalary({N})': [x]})
    return df