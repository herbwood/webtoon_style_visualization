import torch
import matplotlib.pyplot as plt
import numpy as np
from dataloaders.data_loaders import WebtoonLoader
from model.loss import GramMSELoss, GramMatrix
from model.model import Resnet
from trainer.train import style_extract, tsne
from utils.util import configInfo, imgList, avgList
from visualization.plot import imscatter, show_thumnail


def main():
    config = configInfo('config.json')

    data = WebtoonLoader().data
    img_list, img_list2 = imgList(data)
    resnet = Resnet().cuda()
    for param in resnet.parameters():
        param.requires_grad = False
    total_arr, label_arr = style_extract(data)
    result = tsne(total_arr, 2, 100)
    avg_list = avgList(result, label_arr)

    for i in range(len(result)):
        img_path = img_list[i]
        imscatter(result[i, 0], result[i, 1], image=img_path, zoom=0.2)
    plt.savefig(config["visualization"]["title1"])

    for i in range(len(avg_list)):
        img_path = img_list2[i]
        imscatter(avg_list[i][0], avg_list[i][1], image=img_path, zoom=0.6, show_by_thumnail=True,
                  title=config["idx_to_class"][i])
    plt.savefig(config["visualization"]["title2"])

if __name__ == '__main__':
    main()