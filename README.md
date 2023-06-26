# Spotify Downloader

This repository contains a Python script that allows you to download tracks, playlists, and albums from Spotify using the Savify library.

## Prerequisites

- Python 3.6 or above
- Savify library: Install it using `pip install savify`

## Setup
```
git clone https://github.com/your-username/spotify-downloader.git
cd spotify-downloader
pip install -r requirements.txt
```

## Obtain Spotify API credentials

To use the Spotify API for downloading tracks, playlists, and albums, you need to obtain API credentials from the Spotify Developer Dashboard. Follow the steps below to obtain the required credentials:

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in to your Spotify account. If you don't have an account, create one.

2. Create a new application:

   - Click on the "Create an App" button.
   - Provide a name and description for your application.
   - Accept the terms and conditions, and click on the "Create" button.

3. Note down the **Client ID** and **Client Secret**:

   - Once your application is created, you will see the client details page.
   - On this page, you will find the **Client ID** and **Client Secret**.
   - Make sure to keep these credentials secure, as they grant access to your Spotify account.

4. Update the credentials in the script:

   - Open the Python script (e.g., `spotify_downloader.py`) in a text editor.
   - Locate the `CLIENT_ID` and `CLIENT_SECRET` variables.
   - Replace the empty strings with your obtained credentials.
   - Save the changes.

With the updated credentials, you will be able to authenticate your application and use the Spotify API for downloading music from Spotify.

## Contributing 
Contributions are welcome! If you find any issues or want to enhance the application, feel free to open an issue or submit a pull request.

## Disclaimer 
Please note that downloading copyrighted content from Spotify may violate the terms of service and/or the rights of the content owners. Use this script responsibly and at your own risk.

## License 
---
```

Made with Python3
(C)itz-harshit 
Copyright permission under MIT License
License -> https://github.com/itz-harshit/translator//blob/main/LICENSE

```

---
## Credits

- [Harshit Shrivastav](https://github.com/itz-harshit)
