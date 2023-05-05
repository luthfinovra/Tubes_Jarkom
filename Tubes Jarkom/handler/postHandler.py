import os
from handler.messageHandler import *

def handlePOST(request) :
    search = request.split("\n")[25].replace("\r", "")
    files = os.listdir('../database')
    
    result = [name for name in files if search in name]
    return htmlRenderer(search, result)