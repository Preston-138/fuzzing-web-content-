import requests 

def update_db():
  """создаем текстовый файл-словарь с гитхаба"""
  r = requests.get('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/SVNDigger/all.txt')
  wordlist = r.text
  with open('web-content2.txt', 'w') as f:
    print(wordlist, file=f)

def start_fuzzing():
  target = input('Введи url: ') # http://pascher.world/
  with open('web-content2.txt', 'r') as f:
    for fuzz in f:
      target_url = target + fuzz
      r = requests.get(target_url)
      if r.status_code == 200:
        print(target_url, r.status_code)
      if r.status_code != 200 and r.status_code != 404:
        print('interesting ', target_url, r.status_code)
  print('OK')

start_fuzzing()