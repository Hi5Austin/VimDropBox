1. add the map and function from my .vimrc into your .vimrc
2. get a dropbox token from http://dropbox.github.io/dropbox-api-v2-explorer/#list_folder 
3. put the token in backup.py, put a path for a folder from your Dropbox(ie "/folder/") ,and put backup.py in /usr/bin

Now whenever you use Vim, type ESC, then CONTROL-b,and then enter,
and the file being edited will be saved, pushed to dropbox, and vim will exit
