# Misha Kaday
# Test SoundCloud
from bs4 import BeautifulSoup
from requests import get as requests_get


def search_music(text):

    # find music in SC
    res = requests_get('https://soundcloud.com/search?q='+text)
    # source page bs4
    soup = BeautifulSoup(res.content, "html.parser")

    # all_list music from SC
    data, id = [], 1
    for i in soup.find_all('li'):
        # ToDo Refactor
        try:
            url = i.find('a').get('href')

            if len(url) > 64 or str(url).count('/') <= 1 or "/sets/" in url or '/search/' in url:
                continue

            # create data list music
            data.append({'id': str(id), 'url': url, "name": i.a.get_text()})
            id += 1

        except:
            continue

    return data


#  Test
if __name__ == '__main__':
    data = search_music('lofi')
    print(data)
