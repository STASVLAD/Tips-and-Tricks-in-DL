import torch
from torchvision.models.segmentation import deeplabv3_resnet50 as resnet50
from torchvision.models.detection import fasterrcnn_resnet50_fpn as fasterrcnn

FasterRCNN = fasterrcnn()