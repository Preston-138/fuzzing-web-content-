import requests 
import time


def update_db():
  """создаем текстовый файл-словарь с гитхаба"""
  r = requests.get('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/namelist.txt')
  wordlist = r.text
  with open('namelist.txt', 'w') as f:
    print(wordlist, file=f)

# update_db()

def start_fuzzing():
  """Фаззинг веб-контента"""
  target = input('Введи url: ') # http://pascher.world/
  with open('dirbuster_wordlist.txt', 'r') as f:
    for fuzz in f:
      target_url = target + fuzz
      print(target_url)
      r = requests.get(target_url)
      if r.status_code == 200:
        print(target_url, r.status_code)
      if r.status_code != 200 and r.status_code != 404:
        print('interesting ', target_url, r.status_code)
  print('OK')


def subdomains_fuzzing():
  """Фаззинг поддоменов"""
  with open('namelist.txt', 'r') as f:
    for fuzz in f:
      target_url = f'http://{fuzz}.pascher.world'
      r = requests.get(target_url)
      if r.status_code == 200:
        print(target_url, r.status_code)
      if r.status_code != 200 and r.status_code != 404:
        print('interesting ', target_url, r.status_code)
        time.sleep(0.3)
      
  print('OK')

# start_fuzzing()
subdomains_fuzzing()