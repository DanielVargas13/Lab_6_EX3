from stackapi import StackAPI
import time
import csv
import datetime

issue_answers = [
  '40349307',
  '61717847',
  '61592230',
  '59038842',
  '61714973',
  '20352745',
  '61609991',
  '61394260',
  '50533462',
  '45999671',
  '39269711',
  '32069524',
  '61033574',
  '61033465',
  '60235506',
  '36789394',
  '60722399',
  '58844775',
  '60647380',
  '60342744',
  '7890611',
  '60326703',
  '46582862',
  '60233005',
  '60201345',
  '60063316',
  '59891702',
  '59828414',
  '59828340',
  '50196228',
  '61845025',
  '52556347',
  '61742656',
  '61678465',
  '61594166',
  '35044692',
  '61473854',
  '59629680',
  '61418141',
  '49024454',
  '61319437',
  '47417236',
  '37551969',
  '35929130',
  '35560532',
  '57856612',
  '57389758',
  '57338763',
  '34729960',
  '56347196',
  '55568104',
  '55293543',
  '55155460',
  '15688255',
  '54393150',
  '4063414',
  '15900752',
  '53193641',
  '53106274',
  '14460634',
  '50177619',
  '6527795',
  '33253738',
  '48925505',
  '1950381',
  '35630070',
  '48436215',
  '24844934',
  '46896132',
  '46633755',
  '11646029',
  '46080529',
  '46046161',
  '45979673',
  '45882911',
  '45788381',
  '45471067',
  '48357178',
  '54037418',
  '18585491',
  '36050008',
  '23269114',
  '30661333',
  '24568979',
  '30493091',
  '29506992',
  '27342839',
  '23121258',
  '23121205',
  '21602096',
  '19780618',
  '17666453',
  '16888457',
  '12846225',
  '13773282',
  '39832441',
  '61109160',
  '9605107',
  '56157957',
  '59384422',
  '61515171',
  '7264756',
  '61242064',
  '55423204',
  '23496825',
  '8495650',
  '60076121',
  '60105488',
  '55378636',
  '60088629',
  '49446304',
  '59958285',
  '54670990',
  '59484305',
  '37309065',
  '59112189',
  '58987087',
  '58850341',
  '30912888',
  '25594148',
  '60721963',
  '35453125',
  '57312996',
  '57271897',
  '56922769',
  '55973862',
  '32525593',
  '54828863',
  '43054448',
  '23181085',
  '52382754',
  '28326983',
  '51522256',
  '25537609',
  '26790308',
  '48989981',
  '48747910',
  '25749819',
  '46508075',
  '46473699',
  '45951744',
  '45450627',
  '25344261',
  '44499302',
  '44043087',
  '29076631',
  '43390248',
  '29602711',
  '32889870',
  '41696149'
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
  with open("/Lab_6_EX3/RespostasStack5.csv", 'w', encoding='utf-8', newline='') as n_file:
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