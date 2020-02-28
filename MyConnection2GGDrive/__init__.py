from .googleDriveAPI import *
import os
scopeForTest = "https://www.googleapis.com/auth/drive"
credentialForTest = os.path.dirname(os.path.abspath(__file__)) + "\\" + "credential.json"