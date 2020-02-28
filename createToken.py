from __future__ import print_function
import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def mainConnection(scope, credentialFile='credential.json'):
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    pathToken = os.path.dirname(os.path.abspath(__file__))
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(f'{pathToken}/ChanonToken.pickle'):
        with open(f'{pathToken}/ChanonToken.pickle', 'rb') as token:
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
        with open('MyConnection2GGDrive/ChanonToken.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds