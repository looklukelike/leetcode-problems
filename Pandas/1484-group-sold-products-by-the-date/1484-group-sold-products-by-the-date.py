import pandas as pd

def list_products(x):
    return ','.join(sorted(set(x.values)))
def count_products(x):
    return len(x.split(','))

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.groupby('sell_date').agg({'product': list_products}).reset_index().rename(columns={'product': 'products'})
    activities['num_sold'] = activities['products'].apply(count_products)
    return activities.loc[:, ['sell_date', 'num_sold', 'products']]