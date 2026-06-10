import pandas as pd
import numpy as np

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses = courses.groupby('class')['student'].size().reset_index()
    return courses.loc[courses['student'] >= 5, ['class']]