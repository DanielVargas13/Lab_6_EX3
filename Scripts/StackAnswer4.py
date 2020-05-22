from stackapi import StackAPI
import time
import csv
import datetime

issue_answers = [
  '34952938',
  '53289876',
  '54936685',
  '51634844',
  '13966747',
  '45991987',
  '53848906',
  '53697731',
  '25366362',
  '51154656',
  '51084389',
  '51002182',
  '6782638',
  '26911510',
  '37860385',
  '47064583',
  '26068923',
  '57197088',
  '61740596',
  '52015945',
  '61821152',
  '7054846',
  '14955500',
  '61342904',
  '55729905',
  '61773137',
  '53332152',
  '61473730',
  '45585651',
  '36569140',
  '42108423',
  '36562548',
  '60859131',
  '30732416',
  '60461088',
  '17367984',
  '22771088',
  '58075392',
  '57810637',
  '21310109',
  '56183389',
  '9381502',
  '56005174',
  '54771264',
  '21115780',
  '17155726',
  '53787017',
  '53715472',
  '53241773',
  '53227310',
  '38736766',
  '17095870',
  '13406458',
  '59028734',
  '60005427',
  '60005250',
  '60004956',
  '58977199',
  '42492630',
  '57304109',
  '42457891',
  '41792446',
  '60001282',
  '53223348',
  '52464242',
  '59080768',
  '61506402',
  '57164156',
  '38361152',
  '55733382',
  '55013935',
  '53447566',
  '48530191',
  '46964833',
  '44973948',
  '38225722',
  '43974548',
  '38897713',
  '12605459',
  '57124512',
  '55763815',
  '55611115',
  '41953103',
  '31279075',
  '51179198',
  '51156319',
  '21253665',
  '18658122',
  '50540554',
  '25520057',
  '48039980',
  '47785573',
  '45128539',
  '44496476',
  '42554539',
  '22778358',
  '41485031',
  '35605735',
  '40278108',
  '11819654',
  '39826696',
  '22195709',
  '38713161',
  '34998529',
  '59784626',
  '60835226',
  '60641643',
  '59165229',
  '43252064',
  '59192237',
  '59089329',
  '59051306',
  '39552504',
  '55337865',
  '58525947',
  '58035106',
  '57845078',
  '42289038',
  '57762608',
  '57444537',
  '56891156',
  '56421853',
  '56092230',
  '42391262',
  '53536580',
  '50663528',
  '54153352',
  '54041414',
  '54024606',
  '53969369',
  '53966762',
  '53434794',
  '52956375',
  '48758464',
  '52081118',
  '51985482',
  '50909574',
  '47294635',
  '50125967',
  '47207339',
  '45625557',
  '44065330',
  '42314095',
  '42078196',
  '41623572',
  '38615904',
  '38080670',
  '35876727',
  '54327516',
  '51954456'
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
  with open("/Lab_6_EX3/RespostasStack4.csv", 'w', encoding='utf-8', newline='') as n_file:
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