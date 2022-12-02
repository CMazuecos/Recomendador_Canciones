import pandas as pd
import re
import random
import sys
def extract(): #We extract the data from the csv file
    songs=pd.read_csv('top10s.csv',sep=',')
    return songs

def transform(songs): #We ask the user what he wants to search
    option = int(input('Introduce 1 if you want to be recommended a song from the artist you searched for, or 2 if you want to be recommended by genre: '))
    songs.drop(columns=["number","title","artist","top genre","year","bpm","nrgy","dnce","dB","live","val","dur","acous","spch","pop"])

    if option == 1: #We recommend the most popular song from the artist and another song from the artist
        searched_artist, max_pop, another_song, artist_one, artist_two = by_artist(songs)
        return option, searched_artist, max_pop, another_song, artist_one, artist_two
    elif option == 2: #We recommend a song from the year the user inputs
        genre, max_pop, another_song, artist_one, artist_two = by_genre(songs)
        return option, genre, max_pop, another_song, artist_one, artist_two

def by_genre(songs): 
    #We recommend the most popular song from the genre and another song    
    #Print all genres in the dataset
    genres = songs['top genre'].unique()
    print('These are the genres you can choose from: ')
    for i in range(len(genres)):
        print(genres[i])

    #We recommend a song from the genre the user inputs
    genre_input = input('Enter the genre you want to search: ')
    list_songs, list_artist, popularity = [], [], []
    genre = genre_input
    salir = False
    while not salir:   
        try:
            searched_genre = re.compile(genre, re.IGNORECASE)
            #find all songs related to the input
            for i in range(len(songs)):
                if re.search(searched_genre, songs['top genre'][i]):
                    list_songs.append(songs['title'][i])
                    list_artist.append(songs['artist'][i])
                    popularity.append(songs['pop'][i])
            #find the most popular song related to the input
            max_pop = max(popularity)
            index = popularity.index(max_pop)
            max_pop = list_songs[index]
            artist_one = list_artist[index]
            #find another random song related to the input
            another_song = random.choice(list_songs)
            artist_two = list_artist[list_songs.index(another_song)]
            salir = True
        except:
            #We delete the last letter of the input if we can't find any genre with that letters
            genre = genre [:-1]
            if genre == '':
                print('You have not entered any genre.')
                sys.exit()
    
    return genre, max_pop, another_song, artist_one, artist_two



def by_artist(songs):
    #We recommend the most popular song from the artist and another song from the artist
    input_artist = input('Enter the name of the artist: ')
    salir = False
    artist = input_artist
    while not salir:
        try:
            searched_artist = re.compile(artist, re.IGNORECASE)
            list_songs, popularity, list_artist = [], [], []
            #find all songs related to the artist
            for i in range(len(songs)):
                if re.search(searched_artist, songs['artist'][i]):
                    list_songs.append(songs['title'][i])
                    list_artist.append(songs['artist'][i])
                    popularity.append(songs['pop'][i])
            #find the most popular song related to the artist
            max_pop = max(popularity)
            index = popularity.index(max_pop)
            max_pop = list_songs[index]
            artist_one = list_artist[index]
            #find another random song related to the artist
            another_song = random.choice(list_songs)
            artist_two = list_artist[list_songs.index(another_song)]
            salir = True
        except:
            artist = artist [:-1] #We delete the last letter of the input if we can't find any artist with that letters
            if artist == '':
                print('You have not entered any artist')
                sys.exit()
    return input_artist, max_pop, another_song, artist_one, artist_two
    
    

def load(option, searched, max_pop, another_song, artist_one, artist_two):
    if option == 1:
        #We print the recommendation related to the input
        print('Songs related to the input made for the artist: ', searched)
        print('The most popular song related to this search is: ', max_pop, 'from', artist_one)
        #In case we recommend two songs from the same artist
        if max_pop != another_song:
            print('Another song related song to this search is: ', another_song, 'from', artist_two)
    
    elif option == 2:
        #We print the recommendation related to the input
        print('Songs related to the input made for the genre: ', searched)
        print('The most popular song related to this search is: ', max_pop, 'from', artist_one)
        #In case we recommend two songs from the same genre
        if max_pop != another_song:
            print('Another song related song to this search is: ', another_song, 'from', artist_two)


if __name__ == '__main__':
    songs = extract()
    option, searched, max_pop, another_song, artist_one, artist_two = transform(songs)
    load(option, searched, max_pop, another_song, artist_one, artist_two)