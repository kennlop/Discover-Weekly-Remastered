# Spotify Playlist Generator Based on your Discover Weekly Playlist

## Overview

This application allows users to select their favorite songs from the automated discover weekly playlist and creates a brand new playlist based on the artists and the tracks they input. It can be easily modified to draw from any other playlist and suggest songs from those by changing the url value in the file "spotifyclient.py" found in the getUserDiscoverWeekly() function. 

## Install
Install the necessary Python packages by running:

`$ pip install -r requirements.txt`

## Run
Export the environment variables:

In the file "createplaylist.py", please add your spotify username in the spotifyUserID value. Likewise, follow the provided link to the sptoify developer pages to create an authorization token and add it to the spotifyAuthToken value.

Run the entry-point script and follow the console instructions:

`$ python createplaylist.py`
