import os
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

def connect_drive():
    credentials_path = "credentials/drive.json"
    
    if not os.path.exists(credentials_path):
        env_creds = os.environ.get("DRIVE_CREDENTIALS")
        if env_creds:
            os.makedirs("credentials", exist_ok=True)
            with open(credentials_path, "w") as f:
                f.write(env_creds)
        else:
            print("Warning: credentials/drive.json not found and DRIVE_CREDENTIALS env var is not set.")

    gauth = GoogleAuth()
    gauth.LoadClientConfigFile(credentials_path)
    gauth.CommandLineAuth()
    return GoogleDrive(gauth)

def list_files(drive, folder_id):
    return drive.ListFile({
        'q': f"'{folder_id}' in parents and trashed=false"
    }).GetList()

def download_file(file, save_path):
    file.GetContentFile(save_path)

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