import pandas as pd
import numpy as np

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses = courses.groupby('class')['student'].size().reset_index()
    courses = courses[courses['student'].astype('float64') >= 5]['class']
    return pd.DataFrame(courses)