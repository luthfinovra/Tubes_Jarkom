from handler.getHandler import *
from handler.postHandler import *

def handleRequest(request) :
    response_line = "HTTP/1.1 200 OK\r\n"
    content_type = "Content-Type: text/html\r\n\r\n"
    message_body = handleMethod(request)
    
    response = response_line+content_type+message_body
    return response

def handleMethod(request) :
    method = request.split()[0]
    path = request.split()[1]

    if method == "GET":
        return handleGET(path)
    elif method == "POST":
        return handlePOST(request)

    return "Method Not Allowed"
