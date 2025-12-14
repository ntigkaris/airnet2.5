import sys
import logging

import numpy as np

from conf.config import cfg
from utils.etl import do_etl
from utils.preprocessing import do_preprocessing
from utils.training import do_training
from utils.testing import do_testing

logging.basicConfig(force=True,level=logging.INFO,format='%(asctime)s %(levelname)-8s %(message)s',datefmt='%Y-%m-%d %H:%M:%S')

if __name__=='__main__':
    do_etl()
    trn,tst = do_preprocessing()
    trn_score =  np.mean([do_training(trn,fold) for fold in range(cfg.nfolds)])
    logging.info(f'Airnet/train/fold=all/score: {trn_score:.2f}')
    tst_score =  np.mean([do_testing(tst,fold) for fold in range(cfg.nfolds)])
    logging.info(f'Airnet/test/fold=all/score: {tst_score}')
    sys.exit(0)
