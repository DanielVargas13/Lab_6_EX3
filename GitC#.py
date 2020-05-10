import requests
import time
import csv

headers = {"Authorization": "token ######"}

initial = "null"
results = [] #vetor de resultados

def run_query(query):
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    while (request.status_code == 502):
          time.sleep(2)
          request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query falhou! Codigo de retorno: {}. {}".format(request.status_code, query))

def createCsv(nodes):
  with open("/Lab_6_EX3/IssuesRepositoriosC#.csv", 'w', encoding="utf-8", newline='') as n_file:

    fnames = [
        'Nome/Dono;',
        'URL;',
        'Linguagem Primaria;',
        'Numero da Issue;',
        'Titulo da Issue;',
        'Data de Criacao da Issue;',
        'Data de Fechamento da Issue;',
        'Data de Criacao do Repositorio;']

    csv_writer = csv.DictWriter(n_file, fieldnames=fnames, dialect="excel-tab")
    csv_writer.writeheader()
    for node in nodes:
      for issue in node['issues']['nodes']:
        csv_writer.writerow(
            {
                'Nome/Dono;': "{};".format(node['nameWithOwner']),
                'URL;': "{};".format(node['url']),
                'Linguagem Primaria;': "{};".format(node['primaryLanguage']['name'] if node['primaryLanguage']!= None else 'null'),
                'Numero da Issue;': "{};".format(issue['number']),
                'Titulo da Issue;': "{};".format("{}".format(issue['title']).replace('"',"'").replace(";","")),
                'Data de Criacao da Issue;': "{};".format(issue['createdAt']),
                'Data de Fechamento da Issue;': "{};".format(issue['closedAt']),
                'Data de Criacao do Repositorio;': "{};".format(node['createdAt'])
            })

for x in range(5):   
  query = """
  {
    search(query:"stars:>100 language:C#", type:REPOSITORY, first:20, after:%s){
        nodes{
          ... on Repository
          {
            nameWithOwner
            url
            primaryLanguage
            {
              name
            }
            issues(first:10)
            {
              nodes
              {
                number
                title
                createdAt
                closedAt
              }
            }
            createdAt
          }
        }
        pageInfo
        {
          endCursor
        }
      }
  }
  """ % (initial)

  result = run_query(query)
  for y in range(20):
    results.append(result["data"]["search"]["nodes"][y])
  initial = '"{}"'.format(result["data"]["search"]["pageInfo"]["endCursor"])

print('Dados obtidos com sucesso')
createCsv(results)
print('Csv gerado com sucesso')