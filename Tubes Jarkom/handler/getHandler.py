def handleGET(path) :
    # Map Requested Path
    path_dict = {
        "/" : "views/index.html",
        "/files.html" : "views/files.html"
    }

    # Membuka file sesuai path
    try :
        file = open(path_dict[path], 'r')
    except (FileNotFoundError, KeyError) :
        file = open("views/404.html", 'r')

    # Read File
    message_body = file.read()
    file.close()

    # Return Read File
    return message_body