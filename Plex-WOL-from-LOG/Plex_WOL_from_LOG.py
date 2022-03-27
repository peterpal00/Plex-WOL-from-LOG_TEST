from pygtail import Pygtail

filename = 'com.plexapp.system.log'

for line in Pygtail(filename):
    print(line)