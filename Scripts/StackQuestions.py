from stackapi import StackAPI
import time
import csv
import datetime

issue_results = []
questions = []

def getRepoName(repo):
  name = repo.split("/")
  return name[1]

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
  SITE.max_pages = 1
  SITE.page_size = 100
  lastrepo = ""
  for issue in issue_results:
    if(len(issue) >= 6 and lastrepo != getRepoName(issue[0])):
      print(issue)
      try:
        questions.append(SITE.fetch('search/advanced', tagged='C#', title='{}'.format(getRepoName(issue[0]))))
      except:
        time.sleep(5)
        questions.append(SITE.fetch('search/advanced', tagged='C#', title='{}'.format(getRepoName(issue[0]))))
      lastrepo = getRepoName(issue[0])
      time.sleep(15)
    
def openIssuesCsv():
  with open('/Lab_6_EX3/IssuesRepositoriosC#.csv', 'r', newline='', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      try:
        issue_results.append(row['Nome/Dono;\tURL;\tLinguagem Primaria;\tNumero da Issue;\tTitulo da Issue;\tData de Criacao da Issue;\tData de Fechamento da Issue;\tData de Criacao do Repositorio;\tNumero de Estrelas;'].replace("\t","").split(';'))
      except:
        issue_results.append(u"{}".format(row['Nome/Dono;\tURL;\tLinguagem Primaria;\tNumero da Issue;\tTitulo da Issue;\tData de Criacao da Issue;\tData de Fechamento da Issue;\tData de Criacao do Repositorio;\tNumero de Estrelas;'].replace("\t","")).encode('utf-8').decode('utf-8').split(';'))

def createCsv(nodes):
  with open("/Lab_6_EX3/QuestoesStack.csv", 'w', encoding='utf-8', newline='') as n_file:
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

openIssuesCsv()
getQuestions()
createCsv(questions)
print("Terminou")                        