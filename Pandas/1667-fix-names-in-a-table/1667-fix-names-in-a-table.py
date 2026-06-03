import pandas as pd

def f(row):
    name = list(row['name'].lower())
    name[0] = name[0].upper()
    return ''.join(name)

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users.apply(f, axis=1)
    return users.sort_values('user_id')