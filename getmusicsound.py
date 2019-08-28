# Misha Kaday
# Test SoundCloud downloader
import requests
from bs4 import BeautifulSoup


def down_load(url):

    # Session
    session_requests = requests.session()
    answer = session_requests.get('https://sclouddownloader.com/')

    # Get token
    token = str(answer.headers['set-cookie']).split(';')[0].split('=')[1]
    # print(token)
    # headers
    payload = {
        "Host": "sclouddownloader.com",
        "Origin": "https: // sclouddownloader.com",

        "Connection": "keep-alive",
        "Sec - Fetch - Mode": "navigate",
        "Sec - Fetch - Site": "same - origin",
        "Sec - Fetch - User": "?1",
        "Upgrade - Insecure - Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Referer": "https://sclouddownloader.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Cache-Control": "max-age=0",
        "Content-Length": "135",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Language": "en-US,en;q=0.9,ru;q=0.8",
        "Upgrade-Insecure-Requests": "1",
        "Cookie": "csrftoken="+token+"; _ga=GA1.2.340591236.1566226433; _gid=GA1.2.148257081.1566226433; __gads=ID=6eb7df6f17125e13:T=1566226432:S=ALNI_MbHiZ_UPIBk2TEbWyXO9EZ6UF92fQ; _gat_gtag_UA_43670572_24=1_ga=GA1.2.340591236.1566226433; _gid=GA1.2.148257081.1566226433; __gads=ID=6eb7df6f17125e13:T=1566226432:S=ALNI_MbHiZ_UPIBk2TEbWyXO9EZ6UF92fQ; _gat_gtag_UA_43670572_24=1"
    }
    # Data to post
    data = {
        "csrfmiddlewaretoken": token,
        "sound-url": url
    }

    # Get answer from site
    source_page = session_requests.post('https://sclouddownloader.com/download-sound-track', headers=payload, data=data)

    # BS4 parse answer
    soup = BeautifulSoup(source_page.text, "html.parser")

    # Parse source page
    a = soup.find('a', {'class': 'expanded button'})
    url_mus = str(a.get('onclick')).split("('")[1].split("'")[0]

    # return music bytes
    return session_requests.get(url_mus).content


#  Test
if __name__ == '__main__':
    media_file = down_load('https://soundcloud.com/garba9/you-are-the-only-one-feat-shiloh')
    open('test.mp3', "wb").write(media_file)
