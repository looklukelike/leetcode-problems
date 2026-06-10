import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.groupby('sell_date')['product'].agg(num_sold=lambda x: x.nunique(), products=lambda x: ','.join(x.sort_values().unique())).reset_index()
    return activities.loc[:, ['sell_date', 'num_sold', 'products']]