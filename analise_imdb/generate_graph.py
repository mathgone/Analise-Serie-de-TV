import sys
import os
from tkinter import messagebox
from time import sleep

try:
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    from imdb import IMDb
    import matplotlib.pyplot as plt
    import seaborn as sns
except ImportError:
    messagebox.showinfo('Módulos não encontrados', "Clique no botão 'VERIFICAR BIBLIOTECAS' para instalar os módulos necessários", icon='warning')
folder = 'Gráficos'
folder_path = os.getcwd() + f'\\{folder}'

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f'Pasta {folder} criada em: {folder_path}')
else:
    print(f'Pasta {folder} já existe em: {folder_path}')

### PARÂMETROS

# CONTADOR DE EPISÓDIOS
ep_counter = 1

# CRIANDO OBJETO DA BIBLIOTECA IMDbPY PARA PESQUISAR DADOS DA SÉRIE
ia = IMDb()

research = sys.argv[1]
if research == None:
    messagebox.showinfo('ERRO', 'Digite o nome da série ou seu ID', icon='error')
print(f'Pesquisa: {research}')

# RETORNA TÍTULO OU ID DA SÉRIE
if research.isdigit():
    series = ia.get_movie(research)
else:
    series = ia.search_movie(research)[0]
    
ia.update(series)

# ID DA SÉRIE
if research.isdigit():
    id = research
else:
    id = series.movieID

# TÍTULO DA SÉRIE
title = series['title']
print(f'Nome original: {title}')

# NÚMERO DE TEMPORADAS
season = range(0, series['seasons']+1)

# LISTA TEMPORÁRIA PARA AGRUPAR TODOS OS DADOS
all_data = []

# HEADEERS PARA ACESSAR A URL
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

### FUNÇÕES

# OBTER O NÚMERO DA SEASON
def season_split(data):
    data = data.split(' ∙ ')[0].split('.')[0].strip()
    return data

# OBTER O NÚMERO DO EPISÓDIO
def episode_split(data):
    data = data.split(' ∙ ')[0].split('.')[1].strip()
    return data

# OBTER O NOME DO EPISÓDIO
def name_split(data):
    data = data.split(' ∙ ')[1].strip()
    return data

# OBTER O RATING DO EPISÓDIO
def rating_split(data):
    data = data.split('/')[0]
    return data

# LIMPAR A COLUNA Season
def clean_S(string):
    string = string.replace('S', '')
    return int(string)
    
### SCRIPT

# ITERAR PELAS TEMPORADAS DA SÉRIE E COLETAR DADOS
print('Coletando dados...')
for s in season:
    url = f'https://www.imdb.com/title/tt{id}/episodes/?season={s}'
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # CONTAINER DOS DADOS DOS EPISÓDIOS: div, class: ipc-title_text
    episode_names = soup.find_all('div', class_='ipc-title__text')
    # CONTAINER DAS AVALIAÇÕES DOS EPISÓDIOS: span, class: ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating
    episode_ratings = soup.find_all('span', class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating')

    for en, er in zip(episode_names, episode_ratings):

        season = season_split(en.text)
        episode = episode_split(en.text)
        episode_name = name_split(en.text)
        rating = rating_split(er.text)
        
        all_data.append({'Season': season, 'Episode': episode, 'Episode Number': ep_counter,'Episode Name': episode_name, 'Rating': rating})

        print(f'Season {season} | Episódio {episode} {episode_name} | Rating {rating}')
        sleep(0.1)
        ep_counter += 1

# CRIANDO O DATAFRAME E AJUSTANDO A COLUNA Rating
print('Gerando gráfico...')
df = pd.DataFrame(all_data)
df['Rating'] = pd.to_numeric(df['Rating'])

# DICIONÁRIO PARA SALVAR DADOS IMPORTANTES
season_dataframes = {}

# ITERAR POR TEMPORADAS DO DATAFRAME
for season_num in df['Season'].unique():
    # FILTRAR O DATAFRAME POR TEMPORADA
    season_df = df[df['Season'] == season_num]
    # GUARDAR O DATAFRAME DE TEMPORADAS NO DICIONÁRIO CRIADO NA LINHA 122
    season_dataframes[f'{season_num}'] = season_df

### GRÁFICO
# TAMANHO DA FIGURA
plt.figure(figsize=(20, 8))

# PARÂMETROS
markers = ['o', 'v', 's', '^', 'D', '<', 'P', '>']
sns.set_palette('tab10', len(markers))
counter = 0
size = 80
if len(df) < 50:
    size = 120

# ITERANDO PELO DICIONÁRIO DE DADOS E PLOTANDO UM GRÁFICO DE DISPERSÃO
for i in season_dataframes:    
    
    # AVALIAÇÃO MÉDIA DA SEASON
    avg_rating = season_dataframes[i]['Rating'].mean()
    
    # GRÁFICO DE DISPERSÃO
    sns.scatterplot(
        data=season_dataframes[i], 
        x='Episode Number', 
        y='Rating', 
        marker=markers[counter], 
        label=f'{i} (Avg. Score: {avg_rating:.2f})', 
        s=size,
        zorder=3
    )
    
    counter += 1
    start_index = (clean_S(i)+1) % len(markers)

    # fPARA CADA 'len(markers)' NÚMERO DE PLOTS, MUDAR O TIPO DE MARCADOR PARA QUE A LEGENDA NÃO SE REPITA
    if clean_S(i) % len(markers) == 0:
        
        counter = 0
        rotated_markers = markers[start_index:] + markers[:start_index]
        markers = rotated_markers

# REGRESSÃO LINEAR
sns.regplot(
            data=df, 
            x='Episode Number', 
            y='Rating', 
            scatter=False,
            ci=None,
            label='Reg Line',
            line_kws={
                'color':'red', 
                'linestyle':'--', 
                'linewidth':4, 
                'alpha':0.7,
                'zorder':4
            } 
                
)

# CUSTOMIZAÇÕES DO GRÁFICO

# GRADE
plt.grid(True, zorder=0)

# TÍTULO
plt.title(f'{title} Rating Analysis', fontsize=24, fontweight='bold')

# EIXO X
plt.xlabel('Episode Number', fontweight='bold', fontsize=16, labelpad=20)

# EIXO Y
plt.ylabel('Rating', fontweight='bold', fontsize=16, labelpad=20)
plt.ylim(0, 11)
plt.yticks(range(1, 11))

# LEGENDA
plt.legend(bbox_to_anchor=(0.5, -0.2), loc='upper center', ncol=7, frameon=False)

# REMOVER O CONTORNO
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.gca().spines['left'].set_visible(False)

# SALVANDO O GRÁFICO COMO ARQUIVO .png
os.chdir(folder_path)
plt.savefig(f'{title}.png', bbox_inches='tight')

messagebox.showinfo('Gráfico gerado', f'Gráfico salvo na pasta {folder} como: {title}.png\n\n{folder_path}')