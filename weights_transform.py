import torch

my_weight = torch.load(r'D:\DLmode\yolo3-pytorch\model_data\ep300-loss0.113-val_loss0.100.pth')

yolo_weight = torch.load(r'D:\DLmode\yolo3-pytorch\model_data\yolo_weights.pth')

for item in yolo_weight.keys():
    if item in my_weight.keys():
        #print(item)
        my_weight[item] = yolo_weight[item]


torch.save(my_weight, 'D:\DLmode\yolo3-pytorch\model_data\my_weights.pth')
