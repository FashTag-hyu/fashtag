#-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask, redirect, url_for, request, make_response
import json
import model_func



#C드라이브에 tmp폴더 안에 계절과 룩에 대한 모델이 준비되어있어야합니다.
#웹에 올라간 사진이 Project3/images 안으로 저장된 이후의 상황입니다.

#웹에 올라간 이후 랜덤으로 설정된 이미지 경로를 image_path에 저장하기

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        json_dict = request.get_json()
        image_path = json_dict['imgDir']
        print(image_path)

        # hash_tags = model_func.model(image_path)
        hash_tags = ["겨울", "봄", "겨울", "봄"]

        for hash in hash_tags:
            hash.encode("utf-8")
            print('#{}'.format(hash))

        result = json.dumps(hash_tags)
        print("result type : ", type(result))
        response = make_response(result)
        response.headers['Content-Type'] = 'application/json;charset=UTF-8'
        print(str(response))
        return response
    return "아직 값이 넘어오지 않았습니다."

if __name__ == "__main__":
    # http://localhost:5000/querystring?test_querystring_for_test
    app.run()