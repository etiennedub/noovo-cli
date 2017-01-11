
import json
import utils



class Show():
    def __init__(self, dataShow):
        self.title = dataShow['title']
        self.slugShow = dataShow['slug']
        self.image = dataShow['image']['url']
        self.seasonEmission = {}


    def addEpisode(self):
        r = utils.downloadURL(utils.URL_EPISODE_NAME + self.slugShow)
        json_str = json.dumps(r.json())
        jsonSeason = json.loads(json_str)['data']['seasons']
        for i in jsonSeason:
            emissionDict = {}
            for x in i['episodes']:
                emissionDict[x['episodeNumber']] = Emission(x['contents'][0], self.slugShow)
            self.seasonEmission[i['seasonNumber']] = emissionDict
    def getSeasonEmission(self):
        return self.seasonEmission

    def getEpisode(self,  seasonNumber, episodeNumber):
        if (self.seasonEmission == {}):
            self.addEpisode()
        return((self.seasonEmission[seasonNumber])[episodeNumber])

    def getLastEpisode(self):
        if self.seasonEmission == {}:
            self.addEpisode()
        lastSeason = sorted(self.seasonEmission)[-1]
        lastEpisode = sorted(self.seasonEmission[lastSeason])[-1]
        return (lastSeason, lastEpisode)

    def getUrlEpisode(self, seasonNumber, episodeNumber):
        return (self.getEpisode(seasonNumber, episodeNumber).getURL())

class Emission():
    def __init__(self, dataEmision, slugShow):
        self.title = dataEmision['title']
        self.slugEpisode = dataEmision['slug']
        self.description = dataEmision['description']
        self.slugShow = slugShow
        self.urlBandwidth = {}
        self.id = dataEmision['brightcoveId']

    def addBanwidth(self):
        self.urlBandwidth = utils.getURLfromID(self.id)

    def getURL(self):
        if (self.urlBandwidth == {}):
            self.addBanwidth()
        return(self.urlBandwidth)

    def getTitle(self):
        return self.title

