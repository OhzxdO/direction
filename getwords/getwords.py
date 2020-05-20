import os
import requests
from bs4 import BeautifulSoup
import re

def getwords(class_id,course_id,words_checked):
    header={
        'Host': 'word.iciba.com',
        'Connection': 'keep-alive',
        'Content-Length': '483',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://word.iciba.com',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://word.iciba.com/?action=words&class=11&course=1',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    data={
        'class_id':class_id,
        'course_id':course_id,
        'no_login':0,
        'words_checked[]': words_checked,
    }

    getexample = requests.post('http://word.iciba.com/?action=card',data=data,headers=header).content

    soup = BeautifulSoup(getexample, 'html.parser', from_encoding='utf-8')
    word = soup.find('span',class_='word').text                                                      #拼写
    sound = soup.find('span',class_='sound').text.replace(' ','').replace('\r','').replace('\n','')  #发音
    dds = soup.find_all('dd')  
    plain = dds[0].text                                                                              #释义
    example = dds[2].text.replace('换一句','').replace('\n','').replace('\r','').replace('  ','')    #例句

    return word,sound,plain,example

if __name__ == "__main__":
    print(getwords(11,2,1))