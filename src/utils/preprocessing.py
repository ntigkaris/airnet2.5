import os

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split,KFold

from conf.config import cfg
from utils.impute import AirnetImputer

def do_preprocessing():
    pros = [pd.read_csv(f'{cfg.prodir}/{f}') for f in os.listdir(cfg.prodir) if f.startswith('poll')]
    df = pd.concat(pros,axis=0)
    df = AirnetImputer(n_neighbors=cfg.knn).fit_transform(df)
    df['pm10_l1'] = df.pm10.shift(periods=1)
    trn,tst = train_test_split(df,train_size=cfg.trnsize,shuffle=True,random_state=cfg.seed)
    trn = trn.reset_index(drop=True)
    Fold = KFold(n_splits=cfg.nfolds,shuffle=True,random_state=cfg.seed)
    for i,(trn_idx,evl_idx) in enumerate(Fold.split(trn)):
        trn.loc[evl_idx,'fold'] = i
    trn['fold'] = trn['fold'].astype(np.uint8)
    return trn,tst
