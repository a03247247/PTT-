import requests
from bs4 import BeautifulSoup
import os

article_path = './res'
if not os.path.exists(article_path):
    os.mkdir(article_path)


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36' }
page_number = 9508
while page_number >= 9507:
    url = 'https://www.ptt.cc/bbs/movie/index%s.html'%(page_number)
    resp = requests.get(url ,headers=headers)
    soup = BeautifulSoup(resp.text , 'html.parser')
    main_title = soup.findAll('div' , class_ = 'title')
    for title in main_title:
        try:
            print(title.a.text.strip() )
            print('https://www.ptt.cc/' + title.a['href'])
            # # #取得內文
            article_url = 'https://www.ptt.cc/' + title.a['href']  #文章網址
            article_title = title.a.text  #文章標題
            article_res = requests.get(article_url, headers=headers)  #對文章網址請求get
            article_soup = BeautifulSoup(article_res.text, 'html.parser')
            article_content = article_soup.select('div#main-content')[0].text.split('--')[0]
            # print(article_content)

            with open(r'%s/%s.txt'% (article_path , article_title) , 'w' ,encoding = 'utf-8' ) as w:
                w.write(article_content)
        except AttributeError as e:
            pass
        except FileNotFoundError as e:
            pass
        except OSError as e:
            pass


    # print('-------------下一頁---------------')
    page_number -= 1