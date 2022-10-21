import os
import re
os.system('cls||clear')  # clear console

open_text_from_alert = open('text_from_alert.txt', 'r', encoding='UTF-8')
open_all_hostname = open('all_hostname.txt', 'w')

for string in open_text_from_alert:
    if re.findall(r'Хост: ', string):
        hostname_current = re.findall(r'\w*\.tivoli.*', string)
        hostname_current = str(hostname_current)
        open_all_hostname.write(hostname_current)
        open_all_hostname.write('\n')
open_text_from_alert.close()
open_all_hostname.close()
