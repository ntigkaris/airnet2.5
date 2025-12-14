import torch

class AirnetLoss(torch.nn.Module):
    '''Huber Loss'''
    def __init__(self,delta):
        super(AirnetLoss,self).__init__()
        self.delta = delta
    def forward(self,X,y):
        z = torch.abs(X-y)
        return torch.where(z <= self.delta,
                           .5*z**2,
                           self.delta*(z - .5* self.delta))\
                    .mean()
