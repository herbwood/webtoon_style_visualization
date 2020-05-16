# Webtoon Drawing Style Visualization

웹툰의 그림체를 Style Transfer와 t-SNE를 통해 시각화한 프로젝트입니다. 

## About The Project

![webtoon_thumnails](https://user-images.githubusercontent.com/35513025/82119422-67890b80-97b9-11ea-9cb6-ecc203b93217.jpg)

현재 NAVER에서 연재되고 있는 웹툰의 그림체의 분포를 시각화함으로써 그림체 간의 유사도를 직관적으로 파악할 수 있습니다. 또한 K-Means Clustering와 같은 비지도 학습을 통해 웹툰의 그림체에 label을 매기는 것이 가능해집니다. 이는 추후 웹툰의 선호도를 분석하는데 유의미한 속성으로 활용될 수 있을 것입니다(ex) 성별 선호하는 그림체 분석).

- 총 20개의 웹툰을 프로젝트에 사용했습니다.
- bs4를 활용한 이미지 크롤링을 통해 데이터셋을 수집했습니다.
- pytorch 패키지의 pretrained된 ResNet을 사용하여 이미지의 style을 추출했습니다.
- sklearn 패키지의 t-SNE를 활용하여 결과를 시각화했습니다. 


## Prerequisites

아래 명령어를 통해 프로젝트에 사용되는 패키지를 install하시길 바랍니다. 

```python
>> pip install -r requirements.txt
```

## Installing

- **데이터셋 다운로드** : 프로젝트에 필요한 데이터셋을 크롤링을 통해 다운받습니다. config.json의 "webtoon_url"을 수정하여 다운받을 웹툰을 수정할 수 있습니다. 

```python
>> cd dataloaders
>> crawler.py
```

- **데이터 전처리** : 웹툰의 컷별로 저장되도록 전처리를 진행합니다. 

```python
>> preprocess.py
```

- **모델 학습 및 시각화** : 웹툰의 그림체를 모델을 통해 학습하고 결과를 시각화합니다. 

```python
>> cd ../
>> main.py
```

## Conclusion

웹툰 그림체를 시각화한 결과는 다음과 같습니다. 

![visualization_by_images (2) (1)](https://user-images.githubusercontent.com/35513025/82119913-2dba0400-97bd-11ea-952e-e1034116f9fe.jpg)

![visualization_by_thumnail](https://user-images.githubusercontent.com/35513025/82119820-7fae5a00-97bc-11ea-9bdc-7871266662ac.jpg)

프로젝트에 대한 세부 사항은 제 [블로그](https://herbwood.github.io/)를 참고하시길 바랍니다. 
