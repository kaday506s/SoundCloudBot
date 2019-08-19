# Misha Kaday
# Test SoundCloud
from bs4 import BeautifulSoup
import requests


def search_music(text):

    # find music in SC
    res = requests.get('https://soundcloud.com/search?q='+text)
    # source page bs4
    soup = BeautifulSoup(res.content, "html.parser")

    # all_list music from SC
    all_list = soup.find_all('li')

    data, id = [], 1
    for i in all_list:
        # ToDo Refactor
        try:
            url = i.find('a').get('href')

            if len(url) > 64:
                continue

            if str(url).count('/') <= 1:
                continue

            if "/sets/" in url or '/search/' in url:
                continue

            name = i.a.get_text()
            # create data list
            data.append({'id': str(id), 'url': url, "name": name})
            id += 1

        except:
            continue

    return data


#  Test
if __name__ == '__main__':
    data = search_music('lofi')
    print(data)
