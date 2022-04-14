import requests 
import time

r = requests.get('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/common.txt')
wordlist = r.text

# создаем текстовый файл-словарь с гитхаба
# with open('web-content.txt', 'w') as f:
#   print(wordlist, file=f)

with open('web-content.txt', 'r') as f:
  for fuzz in f:
    target_url = 'http://pascher.world/' + fuzz
    r = requests.get(target_url)
    if r.status_code == 200:
      print(target_url)
      with open('valid_urls', 'w') as f1:
        print(target_url, r.status_code, file=f1)
    else:
      print(target_url, r.status_code)
    # time.sleep(0.1)
