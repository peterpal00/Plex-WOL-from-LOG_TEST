from pygtail import Pygtail
from log_analyser import LogAnalyser
from time import sleep
import os

plex_path = os.environ['PLEX_PATH']
filepath_part = os.environ['PART_OF_LOG_PATH']
filename = os.environ['LOG_FILE_NAME']
filee = plex_path + filepath_part + filename
log_file_path = '/logfile/'
print(f"we are here: {os.getcwd()}")
print(f'FILEPATH HERE: {log_file_path}')
print(filee)
active_users = dict()
testfile = 'test26.txt'
analyser = LogAnalyser(active_users)

while(True):
    for line in Pygtail(log_file_path + filepath_part + filename, offset_file = 'offset_file.offset'):
        try:
            analyser.check_for_new_user(line)
        except:
            print('LOG READING ERROR')
    sleep(2)
