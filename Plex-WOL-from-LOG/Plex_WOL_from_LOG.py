from pygtail import Pygtail
from log_analyser import LogAnalyser
from time import sleep
import os

filename = os.environ['LOG_FILE_NAME']
plex_path = os.environ['PLEX_PATH']
filepath_part = os.environ['PART_OF_LOG_PATH']
filee = plex_path + filepath_part + filename
print('FILEPATH HERE')
print(filee)
active_users = dict()
testfile = 'test26.txt'
analyser = LogAnalyser(active_users)

while(True):
    for line in Pygtail(filee):
        try:
            analyser.check_for_new_user(line)
        except:
            print('LOG READING ERROR')
    sleep(2)