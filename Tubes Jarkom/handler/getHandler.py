def handleGET(path) :
    path_dict = {
        "/" : "views/index.html",
        "/files.html" : "views/files.html"
    }

    try :
        file = open(path_dict[path], 'r')
    except (FileNotFoundError, KeyError) :
        file = open("views/404.html", 'r')

    message_body = file.read()
    file.close()

    return message_body