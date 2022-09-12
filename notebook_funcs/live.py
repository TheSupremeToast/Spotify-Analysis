import json, os
import pandas as pd
from src.utils import get_project_root


def read_logs():
    print(f'{get_project_root()}/output/history.json')
    his = pd.read_json(f'{get_project_root()}/output/history.json')
    # print('Unique Values:')
    # print(his.apply(lambda x: x.nunique()))

    return his
