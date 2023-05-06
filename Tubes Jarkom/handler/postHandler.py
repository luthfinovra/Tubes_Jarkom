import os
from handler.messageHandler import *

def handlePOST(request) :
    # Index ke 25 tidak ada (karena panjangnya 24, jadi sampai index ke 23)
    search = request.split("\n")[25].replace("\r", "")
    files = os.listdir('../database')
    
    result = [name for name in files if search in name]
    return htmlRenderer(search, result)