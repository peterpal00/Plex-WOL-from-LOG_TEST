from pygtail import Pygtail
from log_analyser import LogAnalyser
from time import sleep

filename = 'Plex Media Server.log'
filepath = '/path/to/library/Library/Application Support/Plex Media Server/Logs/'
filee = filepath + filename
active_users = dict()
testfile = 'test26.txt'
analyser = LogAnalyser(active_users)

while(True):
    for line in Pygtail(filee):
        print(line)
        analyser.check_for_new_user(line)
    sleep(2)