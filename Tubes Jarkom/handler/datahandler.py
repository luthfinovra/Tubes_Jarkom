def handleData(path) :
    path = ''.join(path[1:])
    data = open(path.replace("%20", " "), "rb")

    return data.read()
