import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    df = students.merge(subjects, how='cross')
    examinations = examinations.groupby(['student_id', 'subject_name']).size().reset_index().rename(columns={0: 'attended_exams'})
    df = df.merge(examinations, how='left', on=['student_id', 'subject_name']).sort_values(['student_id', 'subject_name'])
    df['attended_exams'] = df['attended_exams'].fillna(0)
    return df