import torch
import torchvision
from torchvision.transforms import functional as F
from torch.utils.data import Dataset
import os
import numpy as np
import json
from PIL import Image
import json
from pycocotools.coco import COCO


class CocoDataset(Dataset):
    def __init__(self, path: str):
        self.path = path
        self.coco = COCO(path)
        
    def __getitem__(self, idx: int):
        img = self.coco.imgs[idx]
        
        