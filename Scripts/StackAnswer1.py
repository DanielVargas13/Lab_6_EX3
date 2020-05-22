from stackapi import StackAPI
import time
import csv
import datetime

issue_answers = [
  '61856260',
  '61675950',
  '11088732',
  '61377378',
  '42365940',
  '527644',
  '55324599',
  '8506768',
  '61058876',
  '5360217',
  '60950291',
  '60891088',
  '60794140',
  '60652475',
  '60604836',
  '60531795',
  '60289757',
  '37200775',
  '60161663',
  '14266144',
  '6765570',
  '25731143',
  '51071387',
  '61614152',
  '55558845',
  '60548451',
  '54119290',
  '54832978',
  '59161072',
  '60297435',
  '59466828',
  '59200926',
  '58856418',
  '54946761',
  '55598091',
  '55870848',
  '52040818',
  '51853483',
  '53794326',
  '52348155',
  '57873192',
  '57789422',
  '57754748',
  '57612471',
  '57507027',
  '57330410',
  '56936398',
  '55818219',
  '55175869',
  '51153166',
  '54243337',
  '54227620',
  '54038487',
  '44283075',
  '46415576',
  '43805923',
  '58477684',
  '36894736',
  '44202615',
  '37396916',
  '36233809',
  '34747613',
  '8400525',
  '43521478',
  '61818301',
  '17157016',
  '32780433',
  '58154438',
  '27848656',
  '33095466',
  '21317676',
  '61270919',
  '61061131',
  '45327611',
  '60697328',
  '45721479',
  '53196970',
  '49306025',
  '59950331',
  '59755002',
  '59669570',
  '59505617',
  '47697996',
  '23543883',
  '48991513',
  '59346089',
  '59296307',
  '42471339',
  '37553697',
  '5920818',
  '18270091',
  '61746365',
  '61688049',
  '61701034',
  '32638302',
  '26661203',
  '61447950',
  '56283802',
  '61376654',
  '9481752',
  '57749046',
  '45971356',
  '54076480',
  '61130719',
  '60867367',
  '39169364',
  '60673297',
  '41200218',
  '52424032',
  '42957944',
  '23062229',
  '55537175',
  '32205064',
  '12948193',
  '9919473',
  '60561032',
  '32086329',
  '60290870',
  '60189594',
  '60076881',
  '60055772',
  '59979678',
  '25545312',
  '13956656',
  '59702704',
  '24092073',
  '37285121',
  '8704020',
  '29369819',
  '25701659',
  '22177716',
  '10612973',
  '10188168',
  '9558989',
  '60410161',
  '60248056',
  '60149619',
  '59938968',
  '59640492',
  '59270816',
  '59216216',
  '59190429',
  '43519078',
  '57709337',
  '57661070',
  '57333141',
  '57000064',
  '51613947',
  '40117848',
  '17520371'
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
  with open("/Lab_6_EX3/RespostasStack1.csv", 'w', encoding='utf-8', newline='') as n_file:
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