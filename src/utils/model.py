import torch
from torch.utils.data import Dataset

from conf.config import cfg

class AirnetDataset(Dataset):
      def __init__(self,df):
            super(AirnetDataset,self).__init__()
            self.df = df
      def __len__(self):
            return len(self.df.index)
      def __getitem__(self,i):
            return torch.tensor(self.df[cfg.features].iloc[i].values,dtype=torch.float32),\
                   torch.tensor(self.df[cfg.target].iloc[i].values,dtype=torch.float32)

class Airnet(torch.nn.Module):
    def __init__(
                  self,
                  inner,
                  outer,
                  hidden
                ):
        super(Airnet,self).__init__()
        self.net = torch.nn.Sequential(torch.nn.Linear(inner,hidden,bias=True),
                                       torch.nn.ReLU(),
                                       torch.nn.Linear(hidden,outer,bias=True))
    def forward(self,x):
        return self.net(x)
