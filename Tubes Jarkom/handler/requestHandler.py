from handler.getHandler import *
from handler.postHandler import *

def handleRequest(request) :
    # OK Response and Type of Content
    response_line = "HTTP/1.1 200 OK\r\n"
    content_type = "Content-Type: text/html\r\n\r\n"

    # Data yang direquest
    message_body = handleMethod(request)
    
    # Concate OK response with Data
    response = response_line+content_type+message_body
    return response

def handleMethod(request) :
    # Slice to Get Method and Path from the Request
    method = request.split()[0]
    path = request.split()[1]

    if method == "GET":
        # Return Data from the Path
        return handleGET(path)
    elif method == "POST":
        # Handle POST to Server
        return handlePOST(request)

    return "Method Not Allowed"

