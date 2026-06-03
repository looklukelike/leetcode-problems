import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    m = users['mail'].str.fullmatch(r"^[a-zA-Z][a-zA-Z\_\.\-0-9]*\@leetcode\.com")
    return users.loc[m]