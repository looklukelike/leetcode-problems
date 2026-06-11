import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.merge(company, how='left', on='com_id')
    orders = orders.loc[orders['name'] == 'RED', 'sales_id']
    sales_person = sales_person.loc[~sales_person['sales_id'].isin(orders.values), ['name']]
    return sales_person