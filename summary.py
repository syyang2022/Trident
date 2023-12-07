#--------------------------------------------#
#   该部分代码用于看网络结构
#--------------------------------------------#
import torch
from torchsummary import summary
from thop import profile
from nets.yolo import YoloBody
from nets.hr_det import HrShuffleNet

if __name__ == "__main__":
    # 需要使用device来指定网络在GPU还是CPU运行
    device  = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    #m       = YoloBody([[6, 7, 8], [3, 4, 5], [0, 1, 2]], 80).to(device)
    m       = HrShuffleNet([[6, 7, 8], [3, 4, 5], [0, 1, 2]], 6).to(device)

    #x = torch.randn(1, 3, 416, 416).to(device)

    #flops, params = profile(m, inputs=(x,))
    #print('FLOPs = ' + str(flops / 1000 ** 3) + 'G')
    #print('Params = ' + str(params / 1000 ** 2) + 'M')
    summary(m, input_size=(3, 416, 416))
