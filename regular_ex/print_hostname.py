import os
import re
os.system('cls||clear')  # очистка консоли перед запуском

temp_var_for_open_txt_file = open('text_from_alert.txt', 'r', encoding='UTF-8')

all_hostname = []
for string in temp_var_for_open_txt_file:
    if re.findall(r'Хост: ', string):
        hostname_current = re.findall(r'\w*\.tivoli.*', string)
        all_hostname.append(hostname_current)
temp_var_for_open_txt_file.close()

print(all_hostname)
