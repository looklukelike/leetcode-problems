import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    x = None
    employee = employee.sort_values('salary', ascending=False)['salary'].drop_duplicates()
    if N > 0 and employee.shape[0] >= N:
        x = employee.iloc[N - 1]
    df = pd.DataFrame({f'getNthHighestSalary({N})': [x]})
    return df
