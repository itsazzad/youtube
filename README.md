# Add Video to YouTube Playlist

This Python script uses the YouTube Data API to add a video to a specified YouTube playlist. This can be useful for programmatically managing your playlists, or for re-populating a playlist that has been cleared.

## Prerequisites

Before you can run this script, you will need:

*   Python 3.6+
*   A Google Cloud Platform project with the YouTube Data API v3 enabled.
*   OAuth 2.0 credentials for a desktop application. This will be a `client_secret.json` file.

## Setup

1.  **Clone or download this repository.**

2.  **Install the required Python libraries:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your Google Cloud Project and get credentials:**
    1.  Go to the [Google Cloud Console](https://console.cloud.google.com/).
    2.  Create a new project (or select an existing one).
    3.  Enable the **YouTube Data API v3**. You can find it in the **APIs & Services > Library**.
    4.  Create OAuth 2.0 credentials. Go to **APIs & Services > Credentials**, click **Create Credentials > OAuth client ID**.
    5.  Choose **Desktop app** as the application type.
    6.  Download the JSON file and rename it to `client_secret.json`.
    7.  Place the `client_secret.json` file in the same directory as the `add_to_playlist.py` script.

## Usage

Run the script from your terminal, passing the playlist ID and video ID as command-line arguments:

```bash
python add_to_playlist.py <YOUR_PLAYLIST_ID> <YOUTUBE_VIDEO_ID>
```

For example:
```bash
python add_to_playlist.py PL-ff_YGw4cDnk18Ni-waI7wM5isCPMqmp tDnK9UzyRwo
```

### Authorize the application
The script will open a new tab in your browser. You will be asked to authorize the application to access your YouTube account. You may see a warning that "Google hasn't verified this app". You can proceed by clicking "Advanced" and then "Go to (your app name)". Grant the requested permissions.

After successful authorization, the script will add the video to your playlist, and you will see a confirmation message in the terminal.
