import pandas as pd
import numpy as np
np.random.seed(42)
import random
random.seed(42)

import os
import glob

from src.data import utils

if __name__ == '__main__':
    # preprocess training sets and gold standards
    print('BUILDING PREPROCESSED TRAINING SETS AND GOLD STANDARDS...')
    os.makedirs(os.path.dirname('../../../data/interim/wdc-lspc/training-sets/'), exist_ok=True)
    os.makedirs(os.path.dirname('../../../data/interim/wdc-lspc/gold-standards/'), exist_ok=True)

    for file in glob.glob('../../../data/raw/wdc-lspc/training-sets/*'):
        df = pd.read_json(file, lines=True)
        df['title_left'] = df['title_left'].apply(utils.clean_string_wdcv2)
        df['description_left'] = df['description_left'].apply(utils.clean_string_wdcv2)
        df['brand_left'] = df['brand_left'].apply(utils.clean_string_wdcv2)
        df['price_left'] = df['price_left'].apply(utils.clean_string_wdcv2)
        df['specTableContent_left'] = df['specTableContent_left'].apply(utils.clean_specTableContent_wdcv2)
        df['title_right'] = df['title_right'].apply(utils.clean_string_wdcv2)
        df['description_right'] = df['description_right'].apply(utils.clean_string_wdcv2)
        df['brand_right'] = df['brand_right'].apply(utils.clean_string_wdcv2)
        df['price_right'] = df['price_right'].apply(utils.clean_string_wdcv2)
        df['specTableContent_right'] = df['specTableContent_right'].apply(utils.clean_specTableContent_wdcv2)
        file = os.path.basename(file)
        file = file.replace('.json.gz', '.pkl.gz')
        file = f'preprocessed_{file}'
        df.to_pickle(f'../../../data/interim/wdc-lspc/training-sets/{file}')

    for file in glob.glob('../../../data/raw/wdc-lspc/gold-standards/*'):
        df = pd.read_json(file, lines=True)
        df['title_left'] = df['title_left'].apply(utils.clean_string_wdcv2)
        df['description_left'] = df['description_left'].apply(utils.clean_string_wdcv2)
        df['brand_left'] = df['brand_left'].apply(utils.clean_string_wdcv2)
        df['price_left'] = df['price_left'].apply(utils.clean_string_wdcv2)
        df['specTableContent_left'] = df['specTableContent_left'].apply(utils.clean_specTableContent_wdcv2)
        df['title_right'] = df['title_right'].apply(utils.clean_string_wdcv2)
        df['description_right'] = df['description_right'].apply(utils.clean_string_wdcv2)
        df['brand_right'] = df['brand_right'].apply(utils.clean_string_wdcv2)
        df['price_right'] = df['price_right'].apply(utils.clean_string_wdcv2)
        df['specTableContent_right'] = df['specTableContent_right'].apply(utils.clean_specTableContent_wdcv2)
        try:
            df = df.drop(columns='sampling')
        except KeyError:
            pass
        file = os.path.basename(file)
        file = file.replace('.json.gz', '.pkl.gz')
        file = f'preprocessed_{file}'
        df.to_pickle(f'../../../data/interim/wdc-lspc/gold-standards/{file}')

    print('FINISHED BUILDING PREPROCESSED TRAINING SETS AND GOLD STANDARDS...')
