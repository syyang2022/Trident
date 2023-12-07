import torch
from torch import nn
from torch.nn import functional as F

class Rspp(nn.Module):
    def __init__(self, rates, channel):
        super(Rspp, self).__init__()
        modules = []
        for rate in rates:
            modules.append(RsppBlock(channel, channel, rate))
        self.convs = nn.ModuleList(modules)
        self.channel_change = nn.Sequential(
            nn.Conv2d(3*channel, channel, 1, bias=False),
            nn.BatchNorm2d(channel),
            nn.ReLU()
        )
    def forward(self, x):
        _res = []
        for conv in self.convs:
            _res.append(conv(x))
        res = torch.cat(_res, dim=1)
        res = self.channel_change(res)
        res += x
        return res

class RsppBlock(nn.Sequential):
    def __init__(self, in_channels, out_channels, rate):
        super(RsppBlock, self).__init__(
            nn.Conv2d(in_channels, out_channels, 3, padding=rate, dilation=rate, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU()
        )
