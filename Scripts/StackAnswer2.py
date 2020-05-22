from stackapi import StackAPI
import time
import csv
import datetime

issue_answers = [
  '60956684',
  '574395',
  '27741086',
  '60340443',
  '37351698',
  '9422640',
  '59600806',
  '59383584',
  '59383340',
  '12149659',
  '6437832',
  '58863439',
  '16136019',
  '57783145',
  '35123511',
  '5327728',
  '21294288',
  '13000071',
  '53553693',
  '51761372',
  '44442504',
  '44316050',
  '59310787',
  '58754958',
  '44948904',
  '45540340',
  '45072363',
  '44794831',
  '35722738',
  '61875509',
  '8066242',
  '61821152',
  '58405665',
  '50659164',
  '26426401',
  '34586903',
  '14468471',
  '46906849',
  '44553288',
  '61100659',
  '34694774',
  '22207631',
  '61015731',
  '60994265',
  '60948642',
  '60602355',
  '61805775',
  '13840064',
  '55503527',
  '26442017',
  '30220811',
  '54073894',
  '38715898',
  '60295278',
  '43651048',
  '59344272',
  '19379608',
  '47882417',
  '57970547',
  '32493007',
  '57655815',
  '57530218',
  '47489490',
  '32794295',
  '51306302',
  '56509349',
  '56487366',
  '56385748',
  '56192291',
  '55975523',
  '30977104',
  '61556657',
  '59955343',
  '58440522',
  '58867055',
  '57714778',
  '56992133',
  '56779628',
  '40749237',
  '55736882',
  '55489876',
  '55306422',
  '54873211',
  '43016211',
  '44079217',
  '54047578',
  '53976044',
  '53959068',
  '53906150',
  '53696255',
  '52605969',
  '51326064',
  '50844695',
  '50826551',
  '50626352',
  '48769806',
  '47671713',
  '47356386',
  '46788803',
  '44639814',
  '44467225',
  '44429420',
  '46945038',
  '47753329',
  '57442790',
  '52405248',
  '37065971',
  '16530226',
  '46584483',
  '26905521',
  '29349753',
  '21779724',
  '49187403',
  '59371955',
  '17931400',
  '38572088',
  '61739500',
  '31754133',
  '61383382',
  '54538105',
  '33983508',
  '47206074',
  '37862584',
  '43947731',
  '16592802',
  '39866768',
  '34288826',
  '61006783',
  '45769447',
  '60985079',
  '60891425',
  '60847224',
  '21413828',
  '57611156',
  '56757526',
  '33043503',
  '56506715',
  '7610088',
  '9534377',
  '24970608',
  '17329321',
  '52547680',
  '49285288',
  '40870619',
  '50145307',
  '48810351',
  '47792936',
  '47756216',
  '45046722',
  '47666202'
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
  with open("/Lab_6_EX3/RespostasStack2.csv", 'w', encoding='utf-8', newline='') as n_file:
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