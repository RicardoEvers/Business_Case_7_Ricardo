#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Analises"""
    
"""

[1] - Os usuários gostam mais de vídeos de qual categoria?
[2] - Os usuários gostam menos de vídeos de qual categoria?
[3] - Top 5 vídeos que são tendência no país à qual a base de dados foi coletada?
[4] - Esses vídeos têm algo em comum?
[5] - O vídeo mais curtido também é o vídeo mais popular?
[6] - Número máximo de dias até o status de tendência de um vídeo?
[7] - Os usuários comentam em qual categoria mais?








[1] - Os usuários gostam mais de vídeos de qual categoria?

É possível observar que as maiores porcentagens de likes por views são
de vídeos de musica. (id_category: 10)



        # Código a ser executado para esta analise:

df['most_liked']=df['likes']/df['views']

df=df.sort_values(by=['most_liked'], ascending=False).groupby('video_id')

df.head(1) 








[2] - Os usuários gostam menos de vídeos de qual categoria?

É possível observar que as maiores porcentagens de dislikes por views são
de vídeos de notícias. (id_category: 22 principalmente)



        # Código a ser executado para esta analise:

df['most_disliked']=df['dislikes']/df['views']

df=df.sort_values(by=['most_disliked'], ascending=False).groupby('video_id')

df.head(1)








[3] - Top 5 vídeos que são tendência no país à qual a base de dados foi coletada?

1 - Cardi B, Bad Bunny & J Balvin - I Like It [Off...

2 - Daddy Yankee - Hielo (Video Oficial)

3 - Sanju | Official Trailer | Ranbir Kapoor | Raj...

4 - Diplo, French Montana & Lil Pump ft. Zhavia - ...

5 - Selena Gomez - Back To You



        # Código a ser executado para esta analise:

df=df.sort_values(by=['trend_date','views'], ascending=False).groupby('video_id')

df.head(1)








[4] - Esses vídeos têm algo em comum?

Os vídeos são da mesma categoria em sua maioria.








[5] - O vídeo mais curtido também é o vídeo mais popular?

Não, o mais popular é: Childish Gambino - This Is America (Official V...
e o com mais likes é: BTS (방탄소년단) 'FAKE LOVE' Official MV.



        # Código a ser executado para esta analise:
 
 (Atenção, para essa analise é necessário utilizar
  os códigos separadamente, por exemplo:
  1 e Check, ou 2 e Check)

#1
df=df.sort_values(by=['views'], ascending=False).groupby('video_id')
#Check
df['title'].head(1)

#2
df=df.sort_values(by=['likes'], ascending=False).groupby('video_id')
#Check
df['title'].head(1)








[6] - Número máximo de dias até o status de tendência de um vídeo?

O máximo de dias foi um total de 4215 dias , mas não deve ser levado
como regra pois a média é de 16 dias para tendencia.



        # Código a ser executado para esta analise:

df['days_until_trend'] = df['trend_date'] - df['published']

#df['days_until_trend'].describe()

df=df.sort_values(by=['days_until_trend'], ascending=False).groupby('video_id')

df.head(1)








[7] - Os usuários comentam em qual categoria mais?

Vídeos de tutoriais de maquiagem sao os mais comentados.



        # Código a ser executado para esta analise:

df['most_commented']=df['comment_qty']/df['views']

df=df.sort_values(by=['most_commented'], ascending=False).groupby('video_id')

df.head(1)

""" 


# In[133]:


"""Importação de bibliotecas"""

#Importando bibliotecas
import pandas as pd
import numpy as np
import datetime


# In[201]:


"""Leitura e limpeza de dados"""

#Lendo arquivo
df = pd.read_csv('videos.csv')

#Retirando espaços dos nomes das colunas
df.columns.str.strip()

#Renomeando colunas
df.rename(columns={'Unnamed: 0':'id','data_tendencia':'trend_date',
                   'titulo':'title', 'titulo_canal':'channel_title',
                   'id_categoria':'category_id','publicado_em':'published',
                   'visualizacoes':'views','qtd_comentarios':'comment_qty',
                   'link_miniatura':'img_link','contearios_desabilitados':'disabled_comments',
                   'classificacoes_desativadas':'disabled_classifications','video_removido': 'removed_video',
                   'descricao':'description'}, inplace=True)


#Criando lista das listas numericas
numerical_cols = ['category_id','views','likes','dislikes','comment_qty']

#Transformando listas escolhidas em Int64
df[numerical_cols]=df[numerical_cols].astype('Int64')

#Transformando colunas de tempo para formato desejado
df['published'] = pd.to_datetime(df['published'], format='%Y-%m-%d %H:%M:%S').dt.strftime('%Y/%m/%d')
df['trend_date']=pd.to_datetime(df['trend_date'], format='%y.%d.%m').dt.strftime('%Y/%m/%d')

#Transformando tipo de dados das colunas para datetime64
df['published']=df['published'].astype('datetime64')
df['trend_date']=df['trend_date'].astype('datetime64')

#Excluindo linhas vazias com base na coluna views
df = df.drop(df[df['views'].isna()].index)

#Deletando coluna id
del df['id']

#Resetando os indices
df.reset_index()

#Criando nova coluna id 
df['id'] = df.index

#Definindo coluna id como indice
df.set_index('id',inplace=True)

#Colocando nomes das colunas em uma lista para posterior ordenação
df_columns=df.columns.to_list()

#Dando nova ordem às colunas
df = df.reindex(columns=['video_id','category_id','channel_title',
                         'title','views','likes','dislikes','comment_qty',
                         'published','trend_date','tags','disabled_classifications',
                         'disabled_comments','removed_video','img_link','description'])





"""Analises"""


#[1] Criando uma nova coluna 'most_liked' e atribuindo os valores de 'likes'/'views',
#então ordenando pela coluna 'most_liked' de forma descendente e agrupando
#pelo 'video_id'.

#df['most_liked']=df['likes']/df['views']
#df=df.sort_values(by=['most_liked'], ascending=False).groupby('video_id')
#df.head(1)



#[2]  Criando uma nova coluna 'most_disliked' e atribuindo os valores de 'dislikes'/'views',
#então ordenando pela coluna 'most_disliked' de forma descendente e agrupando
#pelo 'video_id'.

#df['most_disliked']=df['dislikes']/df['views']
#df=df.sort_values(by=['most_disliked'], ascending=False).groupby('video_id')
#df.head(1)



#[3] Ordenando valores do Data Frame pelas colunas 'trend_date' e 'views' de forma
#descendente e agrupando pelo 'video_id'.

#df=df.sort_values(by=['trend_date','views'], ascending=False).groupby('video_id')
#df.head(1)



#[5] Ordenando o Data Frame pela coluna 'views' e 'likes' de forma alternada,
#sendo as duas agrupadas pelo 'video_id' e com ordem descendente.

#A
#df=df.sort_values(by=['views'], ascending=False).groupby('video_id')

#Check
#df['title'].head(1)


#B
#df=df.sort_values(by=['likes'], ascending=False).groupby('video_id')

#Check
#df['title'].head(1)



#[6] Criando nova coluna 'days_until_trend' atribuindo valores de 'trend_date' - 'published',
#então ordenando pela coluna 'days_until_trend' de forma descendente, agrupada
#pelo 'video_id'.

#df['days_until_trend'] = df['trend_date'] - df['published']
#df['days_until_trend'].describe()
#df=df.sort_values(by=['days_until_trend'], ascending=False).groupby('video_id')
#df.head(1)



#[7] Criando nova coluna 'most_commented' atribuindo valores de 'comment_qty'/'views',
#então ordenando pela coluna 'most_commented' de forma descendente, agrupada
#pelo 'video_id'.


#df['most_commented']=df['comment_qty']/df['views']
#df=df.sort_values(by=['most_commented'], ascending=False).groupby('video_id')
#df.head(1)

