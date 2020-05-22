from stackapi import StackAPI
import time
import csv
import datetime

users = []

def getUsers():
  SITE = StackAPI('stackoverflow')
  SITE.max_pages = 1
  SITE.page_size = 100
  try:
    users.append(SITE.fetch('users', sort='reputation'))
  except:
    time.sleep(5)
    users.append(SITE.fetch('users', sort='reputation'))

def createCsv(nodes):
  with open("/Lab_6_EX3/UsuariosStack.csv", 'w', encoding='utf-8', newline='') as n_file:
    fnames = [
            'ID do Usuario;',
            'Nome do Usuario;',
            'Reputacao;',
            'Taxa de Aceitacao;'
            ]
    csv_writer = csv.DictWriter(n_file, fieldnames=fnames, dialect="excel-tab")
    #Escrevendo o cabeçalho
    csv_writer.writeheader()
    for users in nodes:
      for item in users['items']:
        csv_writer.writerow(
                  {
                    'ID do Usuario;': "{};".format(item['user_id']),
                    'Nome do Usuario;': "{};".format(item['display_name']),
                    'Reputacao;': "{};".format(item['reputation']),
                    'Taxa de Aceitacao;': "{};".format(item['accept_rate'] if 'accept_rate' in item else 'null')
                  })

getUsers()
createCsv(users)
print("Terminou")                        