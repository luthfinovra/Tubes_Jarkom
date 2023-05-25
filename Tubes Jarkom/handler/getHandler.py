import os
from handler.messageHandler import *

def handleGET(path):
    # Map semua path file HTML dan file di database
    extensions = {
        "pdf": ["pdf"],
        "txt": ["txt"],
        "mp3": ["mp3"],
        "mp4": ["mp4"],
        "image": ["jpg", "png", "jpeg"],
        "document": ["docx", "pptx", "xlsx", "doc", "ppt", "xls"],
        "archive": ["zip", "rar"],
        "code": ["html", "css", "js", "py"]
    }

    path_dict = {
        "/": "views/index.html",
        "/index.html": "views/index.html",
        "/files.html": "views/files.html",
        "/listDatabase" : os.listdir("database"),
        **{"/database/"+file: "database/"+file for file in os.listdir("database")}
    }

    # Buka file yang dicari
    try:
        # Render Semua list data yang ada di database dengan htmlRenderer
        if path == "/files.html" :
            result = [name for name in os.listdir('./database')]
            return htmlRenderer("", result)
        elif path == "/listDatabase" :
            return path_dict[path]

        file_name = path_dict[path]
        file = open(file_name, 'r')
    except (FileNotFoundError, KeyError):
        file = open("views/404.html", 'r')

    # Baca file
    print()
    message_body = file.read()
    file.close()
    # Return File yang dibaca
    return message_body