import dropbox
import datetime
import sys
class NullDevice():
    def write(self, s):
        pass
sys.stderr = NullDevice()  # redirect the real STDOUT
dbx = dropbox.Dropbox('your-api-token-here')
dbx.users_get_current_account()
file_name = sys.argv[1]
upload_name = sys.argv[1] + " " + str(datetime.datetime.now())
f = open(file_name,'r')
dbx.files_upload(f,"/your-dropbox-folder-here/" + upload_name)
