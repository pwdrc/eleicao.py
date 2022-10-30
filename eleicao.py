"""

based on https://colab.research.google.com/drive/1n4XAEyNBrBzWQBQC8KJcnE-WOI42LeS9?usp=sharing

"""

import requests 
import json
import pandas as pd

data = requests.get("https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json")
json_data = json.loads(data.content)

candidato = []
partido = []
votos = []
porcentagem = []

for infos in json_data['cand']:
    if infos['seq'] in '1 2 3 4'.split(' '):
        candidato.append(infos['nm'])
        votos.append(infos['vap'])
        porcentagem.append(infos['pvap'])

df_eleicao = pd.DataFrame(
        list(zip(candidato, votos, porcentagem)),
        columns=['Candidato', 'Nº votos', '%']
)

print(df_eleicao)
