import os
from handler.messageHandler import *

def handleGET(path):
    # Kategorisasi jenis file untuk icon
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

    # Map semua path file HTML dan file di database
    path_dict = {
        "/": "views/index.html",
        "/index.html": "views/index.html",
        "/files.html": "views/files.html",

        # List File yang ada di database
        "/listDatabase" : os.listdir("database"),

        # Formatting path database agar sesuai path sebenarnya
        **{"/database/"+file: "database/"+file for file in os.listdir("database")}
    }

    # Buka file yang dicari
    try:
        # Render Semua list data yang ada di database dengan htmlRenderer
        if path == "/files.html" :
            result = [name for name in os.listdir('./database')]
            return htmlRenderer("", result)
        
        # Return list file yang ada di folder database
        elif path == "/listDatabase" :
            return path_dict[path]

        # Read data untuk Get page HTML
        file_name = path_dict[path]
        file = open(file_name, 'r')

    # Return page 'Error 404' Jika file tidak ditemukan atau Key Path salah
    except (FileNotFoundError, KeyError):
        file = open("views/404.html", 'r')

    # Baca file
    message_body = file.read()
    file.close()
    
    # Return File yang dibaca
    return message_body