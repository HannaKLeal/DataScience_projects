import requests
from bs4 import BeautifulSoup as bp
import csv

# request the web-page
response = requests.get('https://open.spotify.com/playlist/37i9dQZF1DX4Umko6nOmN7')
# html parsing
page = bp(response.text, "html.parser")
# title
playlist_name = page.find('div', {'class': 'media-bd'})

list_title = playlist_name.h1.string
media_name = playlist_name.h2.get_text()
sub_title = playlist_name.p.get_text()

with open('spotify_data.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file)
    # headers of csv.file
    csv_writer.writerow(
        ['ID', 'track_name', 'artist', 'artist_link', 'album_name', 'album_link', 'total_time', 'preview_time'])

    container = page.find('div', {'class': 'tracklist-container'})
    track_list = container.find_all('li')
    for track in track_list:
        position = track.find_all(class_='tracklist-col__track-number position top-align')
        track_num = position[0].text.strip()

        tracklist_name = track.find(attrs={'top-align track-name-wrapper'})
        track_name = tracklist_name.find(class_='track-name').text.strip()

        artist = tracklist_name.find('a').string
        artist_url = tracklist_name.find('a')['href']
        # attend an URL
        artist_link = f'https://open.spotify.com{artist_url}'

        album_name = tracklist_name.find('a').find_next_sibling().get_text().strip()
        album_url = tracklist_name.find('a').find_next_sibling()['href']
        album_link = f'https://open.spotify.com{album_url}'

        duration = track.find(class_='tracklist-col duration')
        total_time = duration.select('.total-duration')[0].get_text()
        preview_time = duration.select('.preview-duration')[0].text

        csv_writer.writerow(
            [track_num, track_name, artist, artist_link, album_name, album_link, total_time, preview_time])
