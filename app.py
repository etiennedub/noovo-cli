
import argparse
import subprocess

from gestion import Gestion

class App:
    def __init__(self, args):
        self._argparser = self._build_argparser()
        self._args = args
        self.gestion = Gestion()

    def _build_argparser(self):
        p = argparse.ArgumentParser(description='noovo-cli')

        # get emission by title command
        ##p.add_argument('-t', '--title', action="store", dest="title", type=str, help='Show Name')
        p.add_argument('title', action='store', nargs='?', type=str,
                     help="Titre de l'émision")
        p.add_argument("episode", action="store", nargs='?', type=str,
                         help="Saison et épisode (ex.: 's05e44')")
        p.add_argument("-v", "--vlc", dest="player", action='store_const', const="vlc", help="Lecture automatique avec VLC")
        p.add_argument("-sm", "--smplayer", dest="player", action='store_const', const="smplayer", help="Lecture automatique avec SMPlayer")
        p.add_argument("-q", "--quality", action='store', nargs='?', type=str, dest="quality", const="AVG",
                     help="Qualité de l'épisode (MIN, AVG, MAX, ALL)" )
        p.add_argument("-u", "--url", dest="url", action="store", nargs='?', type=str,
                         help="Sélectionner épisode à partir d'un URL Noovo.ca")
        p.add_argument("-l", "--last", action="store_true", dest="last", help="Sélectionne le dernier épisode")
        p.add_argument("-a", "--audio", action="store_true", dest="audio", help="Audio seulement")

        return p

    def menuTitle(self):
        self.gestion.addShow()
        intToTitle = []
        counter = 0;

        print("Titre d'émision")
        for i in sorted(self.gestion.getShowDict()):
            counter += 1
            intToTitle.append(i);
            if counter < 10:
                print(" " + str(counter) + "  ---  " + i)
            else:
                print(str(counter) + "  ---  " + i)
        return(intToTitle[int(input("Entrer le chiffre désiré : ")) - 1])

    def menuEpisode(self, title):
        myShow = self.gestion.getShow(title)
        myShow.addEpisode()

        print("\n" * 100)
        print("-------------------" + title + "-------------------")
        mySeason = myShow.getSeasonEmission()
        for i in sorted(mySeason):
            print("--------------- Saison : " + str(i) + " ---------------")
            for x in mySeason[i]:
                myEpisode = myShow.getEpisode(i, x)
                print(str(x) + "  ---  " + myEpisode.getTitle())

        seasonNumber = int(input("Entrer la saison : "))
        episodeNumber = int(input("Entrer l'épisode : "))
        return([seasonNumber, episodeNumber])

    def menuBandwidth(self, listeBandwidth):
        counter = 0
        urlDict = {}
        for i in sorted(listeBandwidth):
            counter += 1
            print(str(counter) + " : " + str(i))
            urlDict[counter] = listeBandwidth[i]
        return (urlDict[int(input("Entrer la qualité désiré : "))])

    def _command_default(self):
        title = self.menuTitle()
        listEpisode = self.menuEpisode(title)
        seasonNumber = listEpisode[0]
        episodeNumber = listEpisode[1]
        listeBandwidth = self.gestion.getURLfromTitle(title, seasonNumber, episodeNumber)
        print(self.menuBandwidth(listeBandwidth))


    def _command_fetch(self, argvs):
        listeBandwidth = None
        title = None
        sesonNumber = None
        episodeNumber = None

        if argvs.url:
            listeBandwidth = self.gestion.getUrlfromURL(argvs.url)
        else:
            if argvs.last:
                if argvs.title:
                    title = argvs.title
                else:
                    title = self.menuTitle()
                listEpisode = self.gestion.getShow(title).getLastEpisode()
                seasonNumber = listEpisode[0]
                episodeNumber = listEpisode[1]
            elif argvs.title and argvs.episode:
                seasonNumber = int(argvs.episode.split("e")[0][1:])
                episodeNumber = int(argvs.episode.split("e")[1])
                title = argvs.title
            elif argvs.title:
                title = argvs.title
                listEpisode = self.menuEpisode(title)
                seasonNumber = int(listEpisode[0])
                episodeNumber = int(listEpisode[1])
            else:
                title = self.menuTitle()
                listEpisode = self.menuEpisode(title)
                seasonNumber = listEpisode[0]
                episodeNumber = listEpisode[1]
            listeBandwidth = self.gestion.getURLfromTitle(title, seasonNumber, episodeNumber)

        if argvs.audio:
            url = listeBandwidth[sorted(listeBandwidth)[0]]
        elif str(argvs.quality).lower() == "all":
            url = self.menuBandwidth(listeBandwidth)
        else:
            if str(argvs.quality).lower() == "min":
                position = 1
            elif str(argvs.quality).lower() == "max":
                position = len(listeBandwidth) - 1
            else:
                position = int((len(listeBandwidth) - 1) / 2 + 1)
            url = listeBandwidth[sorted(listeBandwidth)[position]]

        if argvs.player:
            p = subprocess.Popen([argvs.player, url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            print(url)



    def run(self):
        if not self._args:
            self._command_default()
        else:
            args = self._argparser.parse_args(self._args)
            self._command_fetch(args)
        return 0




