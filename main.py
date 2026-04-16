import os
from drive import connect_drive, list_files, download_file, download_secrets
from metadata import generate_metadata
from uploader import upload_video
from database import is_uploaded, mark_uploaded

SECRETS_FOLDER = "1suyqfZ2b2ALndiGvPPz3_xccwstQYOcX"

# One credentials file
CREDS = "credentials/channel1.json"

# All channels with tokens + Drive folders
CHANNELS = {
    "channel1": {
        "token": "tokens/channel1.pickle",
        "folder_id": "1EYh2ciXrClaa6VqvTugT0svN65ioQwuP"
    },
    "channel2": {
        "token": "tokens/channel2.pickle",
        "folder_id": "1fHocToV-tG3wnJw97lY-AyiPeYv9zc41"
    },
    "channel3": {
        "token": "tokens/channel3.pickle",
        "folder_id": "1-ZmLAA8jny3NgdcQhRziebTUZERilVV1"
    },
    "channel4": {
        "token": "tokens/channela4.pickle",
        "folder_id": "1cEjHNHOOTet7NmhzOKP2OxA9Ca9sBwru"
    },
    "channel5": {
        "token": "tokens/channelme5.pickle",
        "folder_id": "1vuqz9RXbIU6puItX1xPAjx8svAWrR7Zw"
    },
    "channel6": {
        "token": "tokens/channelh6.pickle",
        "folder_id": "1zamOEWf8pszbKI8Pvx8nH7WhuppN1F7h"
    },
    "channel7": {
        "token": "tokens/channelsc7.pickle",
        "folder_id": "1EcyW3uXMPwYlECrAaHS1Rh50zat08gIJ"
    },
    "channel8": {
        "token": "tokens/channeltj8.pickle",
        "folder_id": "15076k_JTcPC_QudAU5bwf8XJxaPC40Oe"
    }
}

if __name__ == "__main__":

    drive = connect_drive()
    download_secrets(drive, SECRETS_FOLDER)

    for channel, data in CHANNELS.items():

        files = list_files(drive, data["folder_id"])

        for file in files:
            filename = file['title']

            if not filename.endswith(".mp4"):
                continue

            if not is_uploaded(channel, filename):

                print(f"[{channel}] Downloading:", filename)

                temp_path = f"temp_{filename}"
                download_file(file, temp_path)

                meta = generate_metadata(filename)

                upload_video(
                    temp_path,
                    meta["title"],
                    meta["description"],
                    meta["tags"],
                    CREDS,
                    data["token"]
                )

                mark_uploaded(channel, filename)

                os.remove(temp_path)

                print(f"[{channel}] Uploaded:", filename)

                break