map <C-b> :execute CloudBackUp()
function! CloudBackUp()
    :w
    :r ! python /usr/bin/backup.py % | grep supercalifragilisticexpialadocious
    :q
endfunction
