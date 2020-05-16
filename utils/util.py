import json
import os
import numpy as np

def configInfo(file):
    with open(file, 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config

def imgList(data, config='config.json'):

    thumnail_path = configInfo(config)["path"]["thumnail"]
    img_list, img_list2 = [], []

    for img in data.imgs:
        img_list.append(img[0])

    for img in os.listdir(thumnail_path):
      img_list2.append(os.path.join(thumnail_path,img))
    img_list2.sort()

    return img_list, img_list2

def avgList(result, label_arr):

    avg_list = []
    scatter_x = result[:, 0]
    scatter_y = result[:, 1]
    group = np.array(label_arr)

    for g in np.unique(group):
        i = np.where(group == g)
        x_avg = np.mean(scatter_x[i])
        y_avg = np.mean(scatter_y[i])
        avg_list.append((x_avg, y_avg))

    return avg_list