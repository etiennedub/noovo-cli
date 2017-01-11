import json
from show import Show
import utils



class Gestion:
    def __init__(self):
        self.showDict = {} ## Contient show non initilisé
        self.searchDict = {}

    def addShow(self): ## Initialise show
        r = utils.downloadURL(utils.URL_ALL_SHOWS)
        json_str = json.dumps(r.json())
        id = json.loads(json_str)['data']['results']
        self.showDict = {}
        self.searchDict = {}
        for i in id:
            self.searchDict[utils.cleanText(i['title'])] = i['title']
            self.showDict[i['title']] = Show(i)
    def getShowDict(self):
        return (self.showDict)

    def getID(self, showName, episodeName):
        r = utils.downloadURL(utils.URL_ID + showName + "/" + episodeName)
        json_str = json.dumps(r.json())
        id = json.loads(json_str)['data']['contents'][0]['brightcoveId']
        return (id)

    def getShow(self, title):
        if (self.searchDict == {} or self.showDict == {}):
            self.addShow()
        try:
            return(self.showDict[self.searchDict[utils.cleanText(title)]])
        except NameError:
            print("Error ?mission non trouve")
            return(0)

    def getURLfromTitle(self, title, seasonNumber, episodeNumber):
        try:
            return(self.getShow(title).getUrlEpisode(seasonNumber, episodeNumber))
        except :
            pass
            return(0)

    def getUrlfromURL(self, URL ):
        [showName_slug, episodeName_slug] = URL.split("/")[-2:]
        return(utils.getURLfromID(self.getID(showName_slug, episodeName_slug)))


