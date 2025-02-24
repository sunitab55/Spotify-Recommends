# -*- coding: utf-8 -*-
"""Spotify rec.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vpOkjEFx5ALl7QsV_zQleJ3m-CTmJLD-
"""

from google.colab import drive

drive.mount('/content/drive')

import pandas as pd
albums = pd.read_csv('/content/drive/MyDrive/spotify-albums_data_2023.csv')
albums.drop_duplicates()
albums.rename(columns={"track_id" : "id"}, inplace = True)

albums.isnull().sum()

feature = pd.read_csv('/content/drive/MyDrive/spotify_features_data_2023.csv')
feature.columns

df = pd.merge(feature, albums[['artists', 'track_name', 'id']], on='id', how='left')
# when trying to merge use key column in the selection of columns too!

# import some important libraries
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm
sns.set()

df.head()

# some data explorations :)
df.info()
df = df[df['track_name'].notna()]
df.shape

dfn = df.select_dtypes(exclude=['object'])

# checking for some null values
dfn.isnull().sum()

dfn.corr()

# scaling the data
# both MaxAbsScaler and MinMaxScaler are good choices
from sklearn.preprocessing import MinMaxScaler
datatypes = ['int64','float64']

# select the
normarlization = dfn.select_dtypes(include=datatypes)
for col in normarlization.columns:
    MinMaxScaler(col)

normarlization.isnull().sum()

# time for some K-means clustering to group songs of similar type together
from sklearn.cluster import KMeans

normarlization.dropna(inplace=True)
kmeans = KMeans(n_clusters = 35)

features = kmeans.fit_predict(normarlization)
dfn['features'] = features
MinMaxScaler(dfn['features'])

df.info()

# recommendation system
class Spotify_rec():
  def __init__(self, dataset) -> None:
     self.dataset = dataset
  def recommend(self, songs, amount=1):
        distance = []
        song = self.dataset[(self.dataset.track_name.str.lower() == songs.lower())].head(1).values[0]
        rec = self.dataset[self.dataset.track_name.str.lower() != songs.lower()]
        for songs in tqdm(rec.values):
            d = 0
            for col in np.arange(len(rec.columns)):
                if not col in [11, 12, 13, 14, 15, 18]:
                    d = d + np.absolute(float(song[col]) - float(songs[col]))
            distance.append(d)
        rec['distance'] = distance
        rec = rec.sort_values('distance')
        columns = ['track_name']
        return rec[columns][:amount]

recommendations = Spotify_rec(df)
recommendations.recommend("Lover", 13)