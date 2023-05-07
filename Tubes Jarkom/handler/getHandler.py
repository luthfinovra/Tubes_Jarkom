import os

def handleGET(path):
    # Map Requested HTML Path and Path for Every File in Database
    path_dict = {
        "/": "views/index.html",
        "/index.html": "views/index.html",
        "/files.html": "views/files.html",
        **{"/database/"+file: "database/"+file for file in os.listdir("database")}
    }

    # Buka file sesuai dengan path
    try:
        file_name = path_dict[path]
        file = open(file_name, 'r')
    except (FileNotFoundError, KeyError):
        file = open("views/404.html", 'r')    

    # Baca file
    message_body = file.read()
    file.close()
    # Return File yang dibaca
    return message_body