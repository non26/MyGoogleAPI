import unittest
target = __import__("MyConnection2GGDrive")
ggDrive = target.GoogleAPI
scope = target.scopeForTest
credential = target.credentialForTest

class TestGoogleDrive(unittest.TestCase):
    def test_createFolder(self):
        creds = ggDrive(scope, credential)
        creds.createFolder("FromPythonApp")
    def test_insertFileIntoFolder(self):
        creds = ggDrive(scope, credential)
        creds.insertFileIntoFolder("test_insertIntoFolder.doc"
                , r"C:\Users\EiCh9001\PycharmProjects\PyNielsen\googleAPI\MyConnection2GGDrive\test_insertIntoFolder.docx"
                , "10dc2fg3nM0W4GtGPd-T85jCTyiCalgjq"
                , "application/msword")
if __name__ == "__main__":
    unittest.main()



