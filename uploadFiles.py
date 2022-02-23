import dropbox

class TransferData:
    def __init__(self,access_token ):
        self.access_token = access_token
    #defining the upload file function
    def upload_file(self, file_from , file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f  = open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)


def main():
    access_token = 'sl.AbKQY7cwlr949HZB7JxLOMrnYKuY39PSkiEnMjmzkLJ8mukldzSQjT8oLVfn_A-kB4yn6O0erRD07aV-9JeaGvvRPoLFEVvwg3_p2AufnKjhGlCgTVtpR4YV0SKhk6nbU2-ztZAB'
    transferData = TransferData(access_token)

    file_from = input("Enter the file to be tranfered: ")
    file_to = input("Enter the full path to upload to dropbox: ")
    
    #transferring the data
    transferData.upload_file(file_from , file_to)
    print("File has been moved: ")

main()