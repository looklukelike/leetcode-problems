import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.groupby('customer_number')['order_number'].count().reset_index().sort_values('order_number', ascending=False)
    return pd.DataFrame(orders.head(1)['customer_number'])