import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(customers, orders, how='left',left_on='id', right_on='customerId')
    df = df[df['customerId'].isnull()]
    df = pd.DataFrame(df['name'].rename('Customers'))
    return df