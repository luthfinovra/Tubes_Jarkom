def handleData(path) :
    # Parsing path data
    path = ''.join(path[1:])

    # Read data dalam tipe data biner
    data = open(path.replace("%20", " "), "rb")

    # return data yang dibaca
    return data.read()
