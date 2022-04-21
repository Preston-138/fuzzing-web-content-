import requests 

def update_db():
  """создаем текстовый файл-словарь с гитхаба"""
  r = requests.get('https://raw.githubusercontent.com/daviddias/node-dirbuster/master/lists/directory-list-2.3-medium.txt')
  wordlist = r.text
  with open('dirbuster_wordlist.txt', 'w') as f:
    print(wordlist, file=f)

#update_db()

def start_fuzzing():
  target = input('Введи url: ') # http://pascher.world/
  with open('dirbuster_wordlist.txt', 'r') as f:
    for fuzz in f:
      target_url = target + fuzz
      r = requests.get(target_url)
      if r.status_code == 200:
        print(target_url, r.status_code)
      if r.status_code != 200 and r.status_code != 404:
        print('interesting ', target_url, r.status_code)
  print('OK')

start_fuzzing()