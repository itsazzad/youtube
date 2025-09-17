import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import argparse

# This variable specifies the name of a file that contains the OAuth 2.0
# client secret. You can find more information on creating this file at
# https://developers.google.com/youtube/v3/guides/authentication
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account.
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"

def get_authenticated_service():
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server()
    return googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials)

def add_video_to_playlist(youtube, playlist_id, video_id):
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id
                }
            }
        }
    )
    response = request.execute()
    print(f"Video {video_id} added to playlist {playlist_id}.")
    print(response)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add a video to a YouTube playlist.")
    parser.add_argument("playlist_id", help="ID of the playlist to add the video to.")
    parser.add_argument("video_id", help="ID of the video to add.")
    args = parser.parse_args()

    # When running locally, disable OAuthlib's HTTPs verification.
    # ACTION ITEM: For production use, you should remove this line.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    youtube = get_authenticated_service()
    add_video_to_playlist(youtube, args.playlist_id, args.video_id)
