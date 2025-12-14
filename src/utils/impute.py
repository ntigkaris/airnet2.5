from sklearn.impute import KNNImputer

class AirnetImputer(KNNImputer):
    '''KNN Imputer'''
    def __init__(self,n_neighbors):
        super(AirnetImputer,self).__init__(n_neighbors=n_neighbors)
        super().set_output(transform='pandas')
