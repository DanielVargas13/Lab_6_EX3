from stackapi import StackAPI
import time
import csv
import datetime

issue_answers = [
  '47375706',
  '47217156',
  '12644398',
  '34141842',
  '34592341',
  '22861271',
  '34594830',
  '25450652',
  '36753964',
  '36169095',
  '22119351',
  '34375537',
  '29146049',
  '33695882',
  '33554050',
  '33311365',
  '33310574',
  '32414686',
  '31078074',
  '30569202',
  '25285592',
  '25247187',
  '25150697',
  '24779585',
  '19746618',
  '21370338',
  '21363309',
  '20789285',
  '20377501',
  '17908249',
  '17774344',
  '13150957',
  '35300034',
  '59530570',
  '25172328',
  '22573124',
  '58909314',
  '57776565',
  '19945154',
  '55803720',
  '33143865',
  '55484974',
  '54507174',
  '42151979',
  '23308404',
  '54003184',
  '53799214',
  '53694227',
  '36950789',
  '52710083',
  '45688459',
  '24563800',
  '59527863',
  '59471092',
  '59329119',
  '56876197',
  '55155460',
  '55032559',
  '54466045',
  '51664341',
  '51527660',
  '48183590',
  '34315270',
  '34640849',
  '39854592',
  '28860405',
  '37700721',
  '37583771',
  '36474288',
  '31363439',
  '29453349',
  '26852100',
  '61634788',
  '52768033',
  '41524338',
  '57870033',
  '48685072',
  '58136780',
  '35306021',
  '44627356',
  '59897843',
  '48838387',
  '59672926',
  '51637101',
  '53977681',
  '41879949',
  '52431780',
  '41163741',
  '57807508',
  '53769376',
  '57615021',
  '57510877',
  '61525244',
  '60669565',
  '60246467',
  '59942034',
  '59930797',
  '45079349',
  '59748083',
  '38693107',
  '41100280',
  '59228456',
  '52400244',
  '55537502',
  '39023265',
  '26550348',
  '50521231',
  '57215704',
  '51766599',
  '57951926',
  '55752238',
  '57492352',
  '57396553',
  '45486432',
  '50505819',
  '56773066',
  '57131773',
  '47618058',
  '23823151',
  '30025231',
  '40097363',
  '35589768',
  '36136837',
  '34624217',
  '27831598',
  '39636481',
  '15735013',
  '37279742',
  '44984987',
  '60686422',
  '61787211',
  '57705878',
  '17511457',
  '60415802',
  '61019825',
  '60635918',
  '35971952',
  '32458396',
  '29508168',
  '43751933',
  '48826981',
  '19520407',
  '56475063',
  '34729960',
  '24111467',
  '55814421',
  '55808119',
  '55710570',
  '52286728',
  '55309609'
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
  with open("/Lab_6_EX3/RespostasStack3.csv", 'w', encoding='utf-8', newline='') as n_file:
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