import os
import requests
from bs4 import BeautifulSoup
from utils.util import configInfo


def crawl_naver_webtoon(episode_url, div_class ='', dir='',  thumb=False):

    html = requests.get(episode_url).text
    soup = BeautifulSoup(html, 'html.parser')

    comic_title = soup.select('.comicinfo h2')[0].text.split('\t')[0].strip()
    print(comic_title)

    for img_tag in soup.select(div_class + ' img'):
        image_file_url = img_tag['src']
        image_dir_path = os.path.join(os.getcwd(), dir, comic_title)
        image_file_path = os.path.join(image_dir_path, os.path.basename(image_file_url))
        print(image_file_path)
        if not os.path.exists(image_dir_path):
            os.makedirs(image_dir_path)

        headers = {'Referer': episode_url}
        image_file_data = requests.get(image_file_url, headers=headers).content
        open(image_file_path, 'wb').write(image_file_data)

        if thumb:
            os.rename(image_file_path, os.path.dirname(image_file_path) + '.jpg')

            os.rmdir(os.path.dirname(image_file_path))

if __name__ == '__main__':
    config = configInfo('../config.json')

    for url in list(config['webtoon_url'].values()):
        crawl_naver_webtoon(url, div_class = config['div']['images'], dir=config['path']['webtoon'])
        crawl_naver_webtoon(url, div_class=config['div']['thumnail'], dir=config['path']['thumnail'], thumb=True)
