from pygtail import Pygtail

filename = 'com.plexapp.system.log'

while(True):
    for line in Pygtail(filename):
        print(line)
        