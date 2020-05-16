import os
import numpy as np
import glob
from PIL import Image
from utils.util import configInfo


def getCoord(image, height, width, std):

    mid = width // 2
    coor = []
    final = []
    cnt = 0

    for i in range(height):
        if image[i, mid, 0] == 255 and image[i, mid, 1] == 255 and image[i, mid, 2] == 255:
            continue
        if coor:
            if abs(coor[-1] - i) > std:
                final.append((coor[0], coor[-1]))
                cnt += 1
                coor = []
            else:
                coor.append(i)
        else:
            coor.append(i)

        if i == height-1:
            start, end = coor[0], coor[-1]
            final.append((start, end))
            cnt += 1

    return cnt, final


def Croptoon(path, save_dir, std=150):
    hap = 0
    i = 0

    for file in glob.glob(path + '/*'):
        image = np.asarray(Image.open(file))
        cnt, final = getCoord(image, image.shape[0], image.shape[1], std)
        hap += cnt
        for (start, end) in final:
            cropped = image[start:end, :]
            if cropped.shape[0] < 250:
                hap -= 1
                continue
            cropped = Image.fromarray(cropped)
            cropped.save(save_dir + '/' + str(i) + ".jpg")
            i += 1
        print(f'{file} cropped => {cnt} images')

    print(f'Total {hap} images cropped')

if __name__ == '__main__':

    config =configInfo('../config.json')
    webtoon_path = config['path']['webtoon']
    cropped_path = config['path']['cropped']

    if 'cropped' not in os.listdir('../dataset'):
        os.mkdir(cropped_path)

    for dir in os.listdir(webtoon_path):
        os.makedirs(os.path.join(os.getcwd(), cropped_path, dir))

    for toon in os.listdir(webtoon_path):
        Croptoon(webtoon_path + toon, cropped_path + toon)
