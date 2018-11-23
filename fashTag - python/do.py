import model_func

#C드라이브에 tmp폴더 안에 계절과 룩에 대한 모델이 준비되어있어야합니다.
#웹에 올라간 사진이 Project3/images 안으로 저장된 이후의 상황입니다.

#웹에 올라간 이후 랜덤으로 설정된 이미지 경로를 image_path에 저장하기

image_path = 'C:/Users/user\PycharmProjects/fashTag\images/bcea63f4f8a04b9a94bb4853c98c089a.jpg'  #추론을 진행할 이미지 경로

hash_tags = model_func.model(image_path)

for hash in hash_tags:
    print('#{}'.format(hash))