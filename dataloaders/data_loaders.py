import torch
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from utils.util import configInfo

class WebtoonLoader(DataLoader):

        def __init__(self):

                config = configInfo("config.json")
                self.data_dir = config["path"]["cropped"]
                self.image_size = config["image_size"]

                self.data = datasets.ImageFolder(self.data_dir,transform= transforms.Compose([
                        transforms.Resize(self.image_size),
                        transforms.CenterCrop(self.image_size),
                        transforms.ToTensor()]))