from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

def connect_drive():
    gauth = GoogleAuth()
    gauth.LoadClientConfigFile("credentials/drive.json")
    gauth.LocalWebserverAuth()
    return GoogleDrive(gauth)

def list_files(drive, folder_id):
    return drive.ListFile({
        'q': f"'{folder_id}' in parents and trashed=false"
    }).GetList()

def download_file(file, save_path):
    file.GetContentFile(save_path)