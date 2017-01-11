import requests
import re

URL_EPISODE_NAME = "http://api.noovo.ca/api/v1/content/shows/"
URL_RESOLUTION = "http://c.brightcove.com/services/mobile/streaming/index/master.m3u8?videoId="
URL_ALL_SHOWS = "http://api.noovo.ca/api/v1/content/shows"
URL_ID = "http://api.noovo.ca/api/v1/pages/single-episode/"

def downloadURL( url):
    r = requests.get(url)
    if r.status_code != 200:
        raise NameError("Mauvais URL")
    return r

def cleanText(texte):
    texte = texte.lower()
    texte = re.sub("[\s'-.:!,?]", '', texte)
    texte = re.sub('[éèêë]', 'e', texte)
    texte = re.sub('[àäâ]', 'a', texte)

    return str(texte)


def getURLfromID(episodeID):
    r = downloadURL(URL_RESOLUTION + str(episodeID))
    listTempo = r.text.split('\n')
    urlBandwidth = {}
    lastBandwidth = 0
    for i in listTempo:
        if "http://" in i:
            urlBandwidth[lastBandwidth] = i
        elif 'BANDWIDTH=' in i:
            lastBandwidth = int((i.split(',')[1])[10:])
        else:
            pass
    return (urlBandwidth)