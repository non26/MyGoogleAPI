from __future__ import print_function
import pickle
import os.path
import io
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

def mainConnection(scope, credentialFile='credential.json'):
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('ChanonToken.pickle'):
        with open('ChanonToken.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentialFile, scope)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('ChanonToken.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

class GoogleDriveAPI:
    def __init__(self, scope, credFile='credential.json'):
        self.connCred = mainConnection(scope, credFile)
        self.drive_service = build('drive', 'v3', credentials=self.connCred)

    def createFolder(self, name):
        file_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = self.drive_service.files().create(body=file_metadata,
                                            fields='id').execute()
        # print('Folder ID: %s' % file.get('id'))

    def insertFileIntoFolder(self, fileName, filePath, folderId, mimeType):
        folder_id = folderId
        file_metadata = {
            'name': fileName,
            'parents': [folder_id]
        }
        media = MediaFileUpload(filePath,
                                mimetype=mimeType,
                                resumable=True)
        file = self.drive_service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
        print('File ID: %s' % file.get('id'))

    def uploadFile(self, fileName, filePath, mimeType):
        """Perform a simple upload"""
        file_metadata = {'name': fileName}
        media = MediaFileUpload(filePath,
                                mimetype=mimeType)
        file = self.drive_service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
        print('File ID: %s' % file.get('id'))

    def downloadFile(self, fileId):
        """Downloads of files stored in Google Drive"""
        file_id = fileId
        request = self.drive_service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()

if __name__ == "__main__":
    testGGDrive = GoogleDriveAPI(SCOPES)
    # pass
    # testGGDrive.createFolder("createFromPython")

    # fail due to "Bad request"
    # testGGDrive.insertFileIntoFolder("test_insertIntoFolder.docx"
    #        , "C:/nonContent/googleAPI/MyConnection2GGDrive/test_insertIntoFolder.docx"
    #        , "15j_lHamQTDjNdRZgCob5TuEXmDZVRl-A"
    #        , "application/vnd.openxmlformats-officedocument.wordprocessingml.document")

    # pass
    # testGGDrive.uploadFile("test_insertIntoFolder.docx"
    #        , "C:/nonContent/googleAPI/MyConnection2GGDrive/test_insertIntoFolder.docx"
    #        , "application/vnd.openxmlformats-officedocument.wordprocessingml.document")

    # fail due to "Request range not satisfiable"
    testGGDrive.downloadFile("1hZH0dspz4a07nnOOboYvd8g5mIrfmi0z")