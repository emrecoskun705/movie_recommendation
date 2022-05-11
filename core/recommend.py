import os
from django.conf import settings
import pandas as pd

cos_sim_data = pd.read_csv(os.path.join(settings.BASE_DIR, 'cos_sim_data.csv'))


def give_recommendations(index):
    index_recomm = cos_sim_data.loc[index].sort_values(
        ascending=False).index.tolist()[1:6]

    return index_recomm
