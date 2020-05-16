import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox, TextArea
from PIL import Image
import unicodedata
from utils.util import configInfo

def imscatter(x, y, image, ax=None, zoom=1, show_by_thumnail=False, title='webtoon', filename='thumnail.jpg'):
    if ax is None:
        ax = plt.gca()
    try:
        image = plt.imread(image)
    except TypeError:
        # Likely already an array...
        pass
    im = OffsetImage(image, zoom=zoom)

    # Convert inputs to arrays with at least one dimension.
    x, y = np.atleast_1d(x, y)

    artists = []
    for x0, y0 in zip(x, y):
        ab = AnnotationBbox(im, (x0, y0), xycoords='data', frameon=False)

        if show_by_thumnail:
            offsetbox = TextArea(title, minimumdescent=False)
            ac = AnnotationBbox(offsetbox, (x0, y0),
                                xybox=(20, -40),
                                xycoords='data',
                                boxcoords="offset points")
            artists.append(ax.add_artist(ac))
        artists.append(ax.add_artist(ab))

    ax.update_datalim(np.column_stack([x, y]))
    ax.autoscale()

    return artists

def show_thumnail(img_list2, config='config.json', filename='webtoons.jpg'):

    config = configInfo(config)
    idx_to_class = config["idx_to_class"]

    plt.figure(figsize=(55, 10))
    plt.suptitle('Webtoons used for drawing style classification', fontsize=50, position=(0.5, 1.0 + 0.05))
    for n in range(20):
        ax = plt.subplot(2, 10, n + 1)
        img = Image.open(img_list2[n])
        plt.imshow(img)
        title = unicodedata.normalize('NFC', idx_to_class[str(n)])
        plt.title(title, fontsize=27)
        plt.axis('off')
    plt.savefig(filename, bbox_inches='tight')

