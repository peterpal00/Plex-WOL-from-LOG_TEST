from pygtail import Pygtail

filename = 'Plex Media Server.log'

while(True):
    for line in Pygtail(filename):
        print(line)
        