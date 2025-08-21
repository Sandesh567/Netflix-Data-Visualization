#import library

import pandas as pd
import matplotlib.pyplot as plt


#load the data
df = pd.read_csv('netflix_titles.csv')

#clean the data

df = df.dropna(subset=['type','release_year','rating','country','duration'])

type_counts = df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index, type_counts.values , color=['skyblue', 'orange'])
plt.title('Number of Movies as compared to Web Series')
plt.xlabel('Type')
plt.ylabel('Numbers')
plt.tight_layout()
plt.savefig('movie_vs_shows.png')



rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts, labels=rating_counts.index,autopct='%1.1f%%',startangle=90)
plt.title('Percentage of Content Rating')
plt.tight_layout()
plt.savefig('content_rating.png')
plt.legend()




movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace('min', '').astype(int)

plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'], bins= 30 , color='purple', edgecolor='black')
plt.title('Distribution of Movie Duration')
plt.xlabel('Duration')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('duration_distribution.png')


release_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index , release_counts.values, color='red', marker='o')
plt.title('Release year VS Number of Shows')
plt.xlabel('Release Year')
plt.ylabel('Number of Shows')
plt.tight_layout()
plt.savefig('release year.png')


country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index, country_counts.values, color='teal')
plt.title('Top 10 Countries by number of Shows')
plt.xlabel('Number of Shows')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('top_10_country.png')


content_by_year = df.groupby(['release_year','type']).size().unstack().fillna(0)

fig, ax = plt.subplots(1,2, figsize=(12,5))

#first movie subplot

ax[0].plot(content_by_year.index , content_by_year['Movie'], color='red')
ax[0].set_title('Movies Released Per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')


#Second TV shows
ax[0].plot(content_by_year.index , content_by_year['TV Show'], color='red')
ax[0].set_title('TV Shows Released Per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of TV Shows')

fig.suptitle('Comparison of Movie and TV shows Released Per Year')

plt.tight_layout()
plt.savefig('comparison_tv_movie.png')
plt.show()

