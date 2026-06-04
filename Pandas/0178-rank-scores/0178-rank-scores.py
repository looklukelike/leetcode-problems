import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.sort_values('score', ascending=False)[['score']]
    podium = scores['score'].drop_duplicates().reset_index(drop=True)
    podium = pd.DataFrame({'rank': podium.index + 1, 'score': podium.values})
    scores= scores.merge(podium, how='left', on='score')
    return scores