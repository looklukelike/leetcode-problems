import pandas as pd
import numpy as np

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    conditions = [(accounts['income'] < 20000), (20000 <= accounts['income']) & ( accounts['income'] <= 50000), (accounts['income'] > 50000)]
    choices = ['Low Salary', 'Average Salary', 'High Salary']
    accounts['category'] = np.select(conditions, choices)

    accounts = accounts.groupby(by=['category'], observed=True).count().reindex(choices, fill_value = 0).reset_index().rename(columns={'income': 'accounts_count'})[['category', 'accounts_count']]

    return accounts