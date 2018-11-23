import demo
import retrain_run_inference
import os
import shutil
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request


# Anaconda package install
# pip install bs4
# pip install selenium
# pip install lxml

def model(imagePath):

    #demo모듈이 디텍팅하고 사람 박스 잘라줍니다.
    #결과는 Project3/results 에 들어갑니다.
    demo.runDemo()

    #먼저 season내에서 예측결과
    season_list = retrain_run_inference.run_inference_on_image_season(imagePath=imagePath)
    hash_list = []

    for x in season_list:
        x = x[:-3]
        x = x.replace("b","")
        x = x.replace("'","")
        x = x.replace("\n","")
        x = x.split(' ')
        for y in x:
            hash_list.append(y)

    #look내에서 예측결과
    look_list = retrain_run_inference.run_inference_on_image_look(imagePath=imagePath)
    for x in look_list:
        x = x[:-3]
        x = x.replace("b","")
        x = x.replace("'", "")
        x = x.replace("\n","")
        x = x.split(' ')
        for y in x:
            hash_list.append(y)

    #hash_list에 결과태그가 모두 담겨있습니다.




    #images폴더 안에 있던 파일들을 train_images폴더로 이동시킵니다.
    src_files = os.listdir('./images')
    for file_name in src_files:
        full_file_name = os.path.join('./images', file_name)
        if (os.path.isfile(full_file_name)):
            shutil.move(full_file_name, './train_images')


    ##########여기부터 크롤링
    #웹드라이브로 크롬브라우즈 띄운다.
    driver_path = "C:/driver/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)

    url_page = 'http://bloglab.xyz/ciboard/console/keywordtool/keywordsearch'
    driver.get(url_page)

    login_page = 'http://bloglab.xyz/ciboard/login?url=http%3A%2F%2Fbloglab.xyz%2Fciboard%2Fconsole%2Fkeywordtool%2Fkeywordsearch'
    driver.get(login_page)

    driver.find_element_by_name('mem_userid').send_keys('hbkim1293')
    driver.find_element_by_name('mem_password').send_keys('kim56566!')
    driver.find_element_by_xpath("//div[@class='col-sm-2 col-sm-offset-3']").click()

    hash_words = []
    hash_words.append(hash_list[0] + ' ' + hash_list[1])
    hash_words.append(hash_list[2] + ' ' + hash_list[3])

    if hash_words[0] == 'woman sf':
        keyword1 = '여성 봄 패션'
        keyword2 = '여자 가을 코디'
    elif hash_words[0] == 'woman summer':
        keyword1 = '여성 여름 코디'
    elif hash_words[0] == 'woman winter':
        keyword1 = '여성 겨울 패션'
    elif hash_words[0] == 'man sf':
        keyword1 = '남자 봄 패션'
        keyword2 = '남자 가을 패션'
    elif hash_words[0] == 'man summer':
        keyword1 = '남자 여름 패션'
    elif hash_words[0] == 'man winter':
        keyword1 = '남자 겨울 패션'

    if hash_words[1] == 'man date':
        keyword3 = '남자 데이트룩'
    elif hash_words[1] == 'woman date':
        keyword3 = '여성 데이트룩'
    elif hash_words[1] == 'man office':
        keyword3 = '남성 오피스룩'
    elif hash_words[1] == 'woman office':
        keyword3 = '여자 오피스룩'
    elif hash_words[1] == 'man sports':
        keyword3 = '남성 운동복'
    elif hash_words[1] == 'woman sports':
        keyword3 = '여자 운동복'

    search = driver.find_element_by_id('keyword')
    search.send_keys(keyword1)

    click_search = driver.find_element_by_id('search')
    click_search.click()

    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")

    ids = []
    for i in range(10):
        string = 'mixkeyword_' + str(i + 1)
        ids.append(string)

    try:
        texts1 = []
        for id in ids:
            tag = soup.find('span', id=id)
            tag = tag.find('a')
            texts1.append(tag.string)
    except Exception:
        pass

    try:
        url_page = 'http://bloglab.xyz/ciboard/console/keywordtool/keywordsearch'
        driver.get(url_page)

        search = driver.find_element_by_id('keyword')
        search.send_keys(keyword2)

        click_search = driver.find_element_by_id('search')
        click_search.click()

        html = driver.page_source
        soup = BeautifulSoup(html, "lxml")

        ids = []
        for i in range(10):
            string = 'mixkeyword_' + str(i + 1)
            ids.append(string)

        try:
            texts2 = []
            for id in ids:
                tag = soup.find('span', id=id)
                tag = tag.find('a')
                texts2.append(tag.string)
        except Exception:
            pass
    except NameError as e:
        texts2 = []

    url_page = 'http://bloglab.xyz/ciboard/console/keywordtool/keywordsearch'
    driver.get(url_page)

    search = driver.find_element_by_id('keyword')
    search.send_keys(keyword3)

    click_search = driver.find_element_by_id('search')
    click_search.click()

    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")

    ids = []
    for i in range(10):
        string = 'mixkeyword_' + str(i + 1)
        ids.append(string)

    try:
        texts3 = []
        for id in ids:
            tag = soup.find('span', id=id)
            tag = tag.find('a').get_text()
            texts3.append(tag)
    except Exception:
        pass

    driver.close()
    texts = texts1 + texts3 + texts2

    must = ['패션', '옷', '코디', '쇼핑몰', '신상', '룩', '복장', '캐주얼', '의류', '복']

    def hasNumbers(inputString):
        return any(char.isdigit() for char in inputString)

    result = []
    for text in texts:
        flag = []
        for item in must:
            if item in text:
                flag.append(True)
            else:
                flag.append(False)
        if sum(flag) > 0 and not '중년' in text and not hasNumbers(text):
            result.append(text)
    hash_list.append(result)

    return hash_list