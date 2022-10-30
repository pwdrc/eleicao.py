"""

based on https://colab.research.google.com/drive/1n4XAEyNBrBzWQBQC8KJcnE-WOI42LeS9?usp=sharing

"""

import requests 
import json
import pandas as pd

data = requests.get(".......")
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
        list(zip(candidato, votos, porcent)),
        columns=['Candidato', 'Nº votos', 'Porcentagem']
)

print(df_eleicao)
