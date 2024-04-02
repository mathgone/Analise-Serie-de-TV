### PACKAGES

import requests
from bs4 import BeautifulSoup
import pandas as pd
from imdb import IMDb
import matplotlib.pyplot as plt
import seaborn as sns
import os

try:
    ### PARAMETERS
    
    # episode number count
    ep_counter = 1
    
    # IMDb package to search for the series attributes
    ia = IMDb()
    print('- TV Series Analyser! -\n')
    research = input('Enter the series name or series ID: ')
    print('...Gathering data...')
    if research.isdigit():
        series = ia.get_movie(research)
    else:
        series = ia.search_movie(research)[0]
        
    ia.update(series)
    
    # series id
    if research.isdigit():
        id = research
    else:
        id = series.movieID
    
    # series title
    title = series['title']
    
    # number of seasons
    season = range(0, series['seasons']+1)
    
    # temporary list to group all the data
    all_data = []
    
    # headers for accessing the url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    
    ### FUNCTIONS
    
    # get the season number
    def season_split(data):
        data = data.split(' ∙ ')[0].split('.')[0].strip()
        return data
    
    # get the episode number
    def episode_split(data):
        data = data.split(' ∙ ')[0].split('.')[1].strip()
        return data
    
    # get the episode name
    def name_split(data):
        data = data.split(' ∙ ')[1].strip()
        return data
    
    # get the episode rating
    def rating_split(data):
        data = data.split('/')[0]
        return data
    
    # clean the Season column
    def clean_S(string):
        string = string.replace('S', '')
        return int(string)
        
    ### SCRIPT
    
    # iterate trought the shows's seasons and gather the data
    for s in season:
        url = f'https://www.imdb.com/title/tt{id}/episodes/?season={s}'
        response = requests.get(url, headers=headers)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Episodes DATA html container: div, class: ipc-title_text
        episode_names = soup.find_all('div', class_='ipc-title__text')
        # Episodes RATING html container: span, class: ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating
        episode_ratings = soup.find_all('span', class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating')
    
        for en, er in zip(episode_names, episode_ratings):
    
            season = season_split(en.text)
            episode = episode_split(en.text)
            episode_name = name_split(en.text)
            rating = rating_split(er.text)
            
            all_data.append({'Season': season, 'Episode': episode, 'Episode Number': ep_counter,'Episode Name': episode_name, 'Rating': rating})
    
            ep_counter += 1
    
    # create the dataframe and adjust the ratings column
    df = pd.DataFrame(all_data)
    df['Rating'] = pd.to_numeric(df['Rating'])
    
    # creating a dictionary for later usage in a for loop plot
    season_dataframes = {}
    
    # iterate over unique seasons in the dataframe
    for season_num in df['Season'].unique():
        # filter the dataframe for each season
        season_df = df[df['Season'] == season_num]
        # store the season dataframe in the dictionary
        season_dataframes[f'{season_num}'] = season_df
    
    ### PLOT
    print('...Plotting a graph...')
    # figure size
    plt.figure(figsize=(20, 8))
    
    # parameters
    #custom_palette = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    markers = ['o', 'v', 's', '^', 'D', '<', 'P', '>']
    sns.set_palette('tab10', len(markers))
    counter = 0
    size = 100
    if len(df) < 50:
        size = 150
    
    # iterating throught the dictionary and plotting a scatterplot graph
    for i in season_dataframes:    
        
        # average season rating
        avg_rating = season_dataframes[i]['Rating'].mean()
        
        # scatterplot
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
    
        # for every len(markers) number of plots, rearrange the markers list so the label doesn't repeat itsefl
        if clean_S(i) % len(markers) == 0:
            
            counter = 0
            rotated_markers = markers[start_index:] + markers[:start_index]
            markers = rotated_markers
    
    # regression line plot
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
    
    # graph customization
    
    # grid
    plt.grid(True, zorder=0)
    
    # title
    plt.title(f'{title} Rating Analysis', fontsize=24, fontweight='bold')
    
    # x axis
    plt.xlabel('Episode Number', fontweight='bold', fontsize=16, labelpad=20)
    
    # y axis
    plt.ylabel('Rating', fontweight='bold', fontsize=16, labelpad=20)
    plt.ylim(0, 11)
    plt.yticks(range(1, 11))
    
    # legend
    plt.legend(bbox_to_anchor=(0.5, -0.2), loc='upper center', ncol=7, frameon=False)
    
    # remove outlines
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    
    # save plot as png
    os.chdir(os.getcwd())
    plt.savefig(f'{title}.png', bbox_inches='tight')
    
    input('\nFinished! Press Enter to exit')

except Exception as e:
    input('ERROR: No series found. Try using the series ID or certify you wrote it correctly')
