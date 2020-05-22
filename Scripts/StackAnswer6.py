from stackapi import StackAPI
import time
import csv
import datetime

issue_answers = [
  '40849257',
  '40636911',
  '40613928',
  '58509652',
  '53863585',
  '59138338',
  '44005712',
  '42113163',
  '51209222',
  '47984342',
  '40909737',
  '60186417',
  '59169613',
  '58612187',
  '56623494',
  '55208150',
  '43320250',
  '61895797',
  '45380277',
  '30675715',
  '41257827',
  '61857077',
  '61848407',
  '49739171',
  '12789660',
  '29053891',
  '61841263',
  '61826344',
  '61826112',
  '61822947',
  '2058982',
  '42596737',
  '61342904',
  '61781044',
  '61776141',
  '58488140',
  '58304247',
  '45056305',
  '61727791',
  '61703156'
  ]
answers = []
comments = []

def getAnswers():
  SITE = StackAPI('stackoverflow')
  SITE.max_pages = 1
  for id in issue_answers:
    try:
      answers.append(SITE.fetch('answers/{}'.format(id)))
      comments.append(SITE.fetch('answers/{}/comments'.format(id)))
    except:
      time.sleep(5)
      answers.append(SITE.fetch('answers/{}'.format(id)))
      comments.append(SITE.fetch('answers/{}/comments'.format(id)))
    time.sleep(10)

def getCommentsNumber(index):
  comment = comments[index]
  return len(comment['items'])

def createCsv(nodes):
  with open("/Lab_6_EX3/RespostasStack6.csv", 'w', encoding='utf-8', newline='') as n_file:
    fnames = [
            'ID da Pergunta;',
            'ID da Resposta;',
            'Quantidade de Comentarios;',
            'Score;',
            'ID do Autor;',
            'Nome do Autor;',
            'Reputacao do Autor;'
            ]
    csv_writer = csv.DictWriter(n_file, fieldnames=fnames, dialect="excel-tab")
    #Escrevendo o cabeçalho
    csv_writer.writeheader()
    for question in nodes:
      for item in question['items']:
        csv_writer.writerow(
                  {
                    'ID da Pergunta;': "{};".format(item['question_id']),
                    'ID da Resposta;': "{};".format(item['answer_id']),
                    'Quantidade de Comentarios;': "{};".format(getCommentsNumber(nodes.index(question))),
                    'Score;': "{};".format(item['score']),
                    'ID do Autor;': "{};".format(item['owner']['user_id'] if 'user_id' in item['owner'] else 'null'),
                    'Nome do Autor;': "{};".format(item['owner']['display_name'] if 'display_name' in item['owner'] else 'null'),
                    'Reputacao do Autor;': "{};".format(item['owner']['reputation'] if 'reputation' in item['owner'] else 'null')
                  })

getAnswers()
createCsv(answers)
print("Terminou")                        