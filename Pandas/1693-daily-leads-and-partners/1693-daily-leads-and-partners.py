import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    daily_sales = daily_sales.groupby(by=['date_id', 'make_name'])[['lead_id', 'partner_id']].agg({'lead_id' : lambda x: x.nunique(), 'partner_id' : lambda x: x.nunique()}).reset_index().rename(columns={'lead_id': 'unique_leads', 'partner_id': 'unique_partners'})
    return daily_sales
