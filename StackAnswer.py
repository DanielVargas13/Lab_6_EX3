from stackapi import StackAPI
import time
import csv
import datetime

issue_answers = ['123123']
answers = []
comments = []

def getAnswers():
  SITE = StackAPI('stackoverflow')
  SITE.max_pages = 1
  SITE.page_size = 100
  for id in issue_answers:
     try:
       answers.append(SITE.fetch('answers/{}'.format(id)))
       comments.append(SITE.fetch('answers/{}/comments'.format(id)))
     except:
       time.sleep(5)
       answers.append(SITE.fetch('answers/{}'.format(id)))
       comments.append(SITE.fetch('answers/{}/comments'.format(id)))
     time.sleep(15)

def getCommentsNumber(index):
  comment = comments[index]
  return len(comment['items'])

def createCsv(nodes):
  with open("/Lab_6_EX3/RespostasStack.csv", 'w', encoding='utf-8', newline='') as n_file:
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
                    'ID do Autor;': "{};".format(item['owner']['user_id']),
                    'Nome do Autor;': "{};".format(item['owner']['display_name']),
                    'Reputacao do Autor;': "{};".format(item['owner']['user_id'])
                  })

getAnswers()
createCsv(answers)
print("Terminou")                        