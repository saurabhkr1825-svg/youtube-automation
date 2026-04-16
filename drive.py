from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

def connect_drive():
    gauth = GoogleAuth()
    gauth.LoadClientConfigFile("credentials/drive.json")
    gauth.CommandLineAuth()
    return GoogleDrive(gauth)

def list_files(drive, folder_id):
    return drive.ListFile({
        'q': f"'{folder_id}' in parents and trashed=false"
    }).GetList()

def download_file(file, save_path):
    file.GetContentFile(save_path)

import os

def download_secrets(drive, folder_id):
    os.makedirs("credentials", exist_ok=True)
    os.makedirs("tokens", exist_ok=True)

    files = drive.ListFile({
        'q': f"'{folder_id}' in parents and trashed=false"
    }).GetList()

    for file in files:
        name = file['title']

        if name.endswith(".json"):
            path = f"credentials/{name}"
        elif name.endswith(".pickle"):
            path = f"tokens/{name}"
        else:
            continue

        print("Downloading secret:", name)
        file.GetContentFile(path)