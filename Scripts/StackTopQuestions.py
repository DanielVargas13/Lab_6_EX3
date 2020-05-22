from stackapi import StackAPI
import time
import csv
import datetime

questions = []

def buildTags(tags):
  total = 0
  newtag = ""
  for tag in tags:
    total += total + 1
    if(total == len(tags)):
      newtag += tag
    else:
      newtag += "{}/".format(tag)
  return newtag

def getQuestions():
  SITE = StackAPI('stackoverflow')
  SITE.max_pages = 10
  SITE.page_size = 100
  try:
   questions.append(SITE.fetch('questions', tagged='C#', sort='votes'))
  except:
   time.sleep(5)
   questions.append(SITE.fetch('questions', tagged='C#', sort='votes'))
  time.sleep(15) 

def createCsv(nodes):
  with open("/Lab_6_EX3/TopQuestoesStack.csv", 'w', encoding='utf-8', newline='') as n_file:
    fnames = [
            'ID da Pergunta;',
            'Quantidade de Views;',
            'Quantidade de Respostas;',
            'Score;',
            'Titulo da Questao;',
            'ID da Resposta Aceita;',
            'Tags;',
            'Link da Questao;'
            ]
    csv_writer = csv.DictWriter(n_file, fieldnames=fnames, dialect="excel-tab")
    #Escrevendo o cabeçalho
    csv_writer.writeheader()
    for question in nodes:
      for item in question['items']:
        csv_writer.writerow(
                  {
                    'ID da Pergunta;': "{};".format(item['question_id']),
                    'Quantidade de Views;': "{};".format(item['view_count']),
                    'Quantidade de Respostas;': "{};".format(item['answer_count']),
                    'Score;': "{};".format(item['score']),
                    'Titulo da Questao;': "{};".format(item['title'].replace('"',"'").replace(";","")),
                    'ID da Resposta Aceita;': "{};".format(item['accepted_answer_id'] if 'accepted_answer_id' in item else 'null'),
                    'Tags;': "{};".format(buildTags(item['tags'])),
                    'Link da Questao;': "{};".format(item['link'])
                  })

getQuestions()
createCsv(questions)
print("Terminou")                        