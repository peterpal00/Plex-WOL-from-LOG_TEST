from pygtail import Pygtail

filename = 'com.plexapp.system.log'

while(true):
    for line in Pygtail(filename):
        print(line)
