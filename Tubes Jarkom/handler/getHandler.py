import os
from handler.messageHandler import *

def handleGET(path):
    # Map semua path file HTML dan file di database
    path_dict = {
        "/": "views/index.html",
        "/index.html": "views/index.html",
        "/files.html": "views/files.html",
        **{"/database/"+file: "database/"+file for file in os.listdir("database")}
    }

    # Buka file yang dicari
    try:
        # Render Semua list data yang ada di database dengan htmlRenderer
        if path == "/files.html" :
            result = [name for name in os.listdir('./database')]
            return htmlRenderer("", result)

        file_name = path_dict[path]
        file = open(file_name, 'r')
    except (FileNotFoundError, KeyError):
        file = open("views/404.html", 'r')

    # Baca file
    message_body = file.read()
    file.close()
    # Return File yang dibaca
    return message_body