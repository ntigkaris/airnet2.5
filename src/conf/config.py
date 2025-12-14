class cfg(object):
    '''Basic setup'''
    rawdir = 'data/raw'
    prodir = 'data/processed'
    pthdir = 'data/model'
    outdir = 'data/output'
    logdir = 'data/logs'
    features = ['pm10_l1','temp','rh']
    target = ['pm25']
    knn = 2
    trnsize = .9
    nfolds = 2
    seed = 42
    dim = {'inner':len(features),
           'outer':len(target),
           'hidden':5}
    batchsize = 128
    trnloader = {'batch_size':batchsize,
                 'shuffle':True,
                 'pin_memory':True,
                 'drop_last':True}
    evlloader = {'batch_size':batchsize*2,
                 'shuffle':False,
                 'pin_memory':True,
                 'drop_last':False}
    delta = 1.0
    lr = 5e-3
    momentum = .0
    epochs = 10
