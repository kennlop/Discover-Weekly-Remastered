import os

from spotifyclient import SpotifyClient

#ENTER YOUR SPOTIFYUSERID HERE
#ENTER YOUR SPOTIFYUSERID HERE
spotifyUserID = ""

#Link for auth token: https://developer.spotify.com/console/post-playlists/?user_id=&body=%7B%22name%22%3A%22New%20Playlist%22%2C%22description%22%3A%22New%20playlist%20description%22%2C%22public%22%3Afalse%7D
#Make sure to select playlist-modify-public and playlist-modify-private

#ENTER YOUR AUTH TOKEN USING THE LINK ABOVE
#ENTER YOUR AUTH TOKEN USING THE LINK ABOVE
spotifyAuthToken = ""

def main():
    spotify_client = SpotifyClient(spotifyAuthToken, spotifyUserID)

    #get Discover Weekly Tracks
    DWTracks = spotify_client.getUserDiscoverWeekly()

    print("Here are your current Discover Weekly tracks")
    for index, track in enumerate(DWTracks):
        print(f"{index+1}- {track}")

    # choose which tracks to use as a seed to generate a playlist
    indexes = input("\nEnter a list of up to 5 tracks you'd like to use as seeds. Use the track numbers separated by a space (ex: 1 5 13 22):")
    indexes = indexes.split()
    seed_tracks = [DWTracks[int(index)-1] for index in indexes]

    # get recommended tracks based off seed tracks
    recommended_tracks = spotify_client.get_track_recommendations(seed_tracks)
    print("\nHere are the recommended tracks which will be included in your new playlist:")
    for index, track in enumerate(recommended_tracks):
        print(f"{index+1}- {track}")

    # get playlist name from user and create playlist
    playlist_name = input("\nWhat would you like to name the playlist? ")
    playlist = spotify_client.create_playlist(playlist_name)
    print(f"\nPlaylist '{playlist.name}' was created successfully.")

    # populate playlist with recommended tracks
    spotify_client.populate_playlist(playlist, recommended_tracks)
    print(f"\nRecommended tracks successfully uploaded to playlist '{playlist.name}'.")


if __name__ == "__main__":
    main()